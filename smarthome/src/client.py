import json
import time
import socket
import traceback

from src.constraints import DaelimType, DaelimSubtype
from src.log import dump


def bitShort(v:int)->int:
    return v & 0x0000ffff

def bitByte(v:int)->int:
    return v & 0x000000ff

def BytesToInteger(data:bytes, offset:int, nbytes:int)->int :
    n = 0
    for i in range(nbytes):
        n = n * 256 + data[offset+i]
    return n
BytesToInteger(bytes([0,0,2,0x93]), 0, 4)

def BytesToString(data:bytes, offset:int, nbytes:int)->str:
    b = data[offset : offset+nbytes].decode('utf-8')
    return b


def IntegerToBytes(data:int, nbytes:int)->bytes:
    ret = [0]*nbytes

    for i in range(0, nbytes):
        ret[nbytes-i-1] = (data >> (i*8) ) & ( 0xFF )
    return bytes(ret)


def StringToBytes(data:str, nbytes)->bytes:
    return data.encode('UTF-8')[0:nbytes]


class DaelimHeader(object):
    # length size = 4
    nDst:int = 0
    nError:int = None
    nReserved:int = 0
    nSrc: int = 0
    nSubType: int = 0
    nType: int = 0
    strPin: str = 0

    def __init__(self, strPin:str, nType:int, nSubType:int, nSrc:int, nDst:int, nError:int = 0):
        self.strPin = strPin
        self.nType = nType
        self.nSubType = nSubType
        self.nSrc = nSrc
        self.nDst = nDst
        self.nError = nError

    @classmethod
    def parse(cls, data:bytes, offset:int):
        pin = BytesToString(data=data, offset=offset, nbytes=8)
        offset += 8

        nType = BytesToInteger(data=data, offset=offset, nbytes=4)
        offset += 4

        nSubtype = BytesToInteger(data=data, offset=offset, nbytes=4)
        offset += 4

        nSrc = BytesToInteger(data=data, offset=offset, nbytes=2)
        offset += 2

        nDst = BytesToInteger(data=data, offset=offset, nbytes=2)
        offset += 2

        nError = BytesToInteger(data=data, offset=offset, nbytes=1)
        offset += 1

        obj = DaelimHeader(
            strPin=pin,
            nType=nType,
            nSubType=nSubtype,
            nSrc=nSrc,
            nDst=nDst,
            nError=nError,
        )
        return obj

    @property
    def length(self) -> int:
        return 8 + 4 + 4 + 2 + 2 + 1 + 3

    def getBytes(self):
        ret = StringToBytes(self.strPin, 8) + \
              IntegerToBytes(self.nType, 4) + \
              IntegerToBytes(self.nSubType, 4) + \
              IntegerToBytes(self.nSrc, 2) + \
              IntegerToBytes(self.nDst, 2) + \
              IntegerToBytes(self.nError, 1) + \
              IntegerToBytes(0, 3)
        return ret

    def dump(self):
        print("[ dump - Header ]")
        print("pin : {}".format(self.strPin))
        print("Type : {}".format(self.nType))
        print("nSubType : {}".format(self.nSubType))
        print("nSrc : {}".format(self.nSrc))
        print("nDst : {}".format(self.nDst))
        print("nError : {}".format(self.nError))

class DaelimPacket(object):
    # header size = 24
    # length size = 4
    header: DaelimHeader = None
    body: bytes = None
    length: int = 0

    def __init__(self):
        self.header = None
        self.body = None
        self.length = 0

    @classmethod
    def create(cls, body, strPin:str, nType:int, nSubType:int, nSrc:int, nDst:int, nError:int = 0):
        """
        00 00 00 33 4c 38 30 39 39 32 35 37 00 00 00 02 00 00 00 0c 00 01 00 03 00 00 00 00 
        [length]    [certPine             ] [type     ] [subtype  ] [src] [dst] e  0  0  0
        """
        packet = DaelimPacket()
        packet.header = DaelimHeader(strPin=strPin, nType=nType, nSubType=nSubType, nSrc=nSrc, nDst=nDst, nError=nError)
        packet.body = json.dumps(body).encode('UTF-8') if body else bytes([])
        packet.length = packet.header.length + len(packet.body)
        return packet

    @classmethod
    def parse(cls, data: bytes, offset = 0):
        obj = cls()
        obj.length = BytesToInteger(data=data, offset=offset, nbytes=4)
        offset += 4

        obj.header = DaelimHeader.parse(data, offset=offset)
        offset += obj.header.length

        obj.body = data[offset:offset + obj.length - 4]
        return obj

    def dump(self):
        print("-"*80)
        self.header.dump()
        print("-"*80)
        print("Body : ")
        print(self.jsonBody)
        print("-"*80)

    @property
    def jsonBody(self):
        try:
            return json.loads(self.strBody, strict=False)
        except:
            return {}

    @property
    def strBody(self):
        try:
            return self.body.decode('UTF-8')
        except:
            return ''

    def getBytes(self):
        return IntegerToBytes(self.length, 4) + self.header.getBytes() + self.body

class DaelimClient(object):
    certPin = "00000000"
    infoControl = {}
    infoDong = None 
    infoHo = None 
    loginPin = None 
    packetPinType = None 
    strPacketPin = None 

    src = 0
    sock = None

    def __init__(self):
        self.infoDong = None 
        self.infoHo = None 
        self.loginPin = None 
        self.packetPinType = None 
        self.strPacketPin = None
        self.sock = None

    @property
    def isLogged(self) -> bool:
        return isinstance(self.loginPin, str) and len(self.loginPin) == 8

    @property
    def hasCertPin(self) -> bool:
        return self.certPin and self.certPin != "00000000"

    def setPins(self, certPin, loginPin):
        self.certPin = certPin
        self.loginPin = loginPin

    def sendMMF(self, body, paramInt1, paramInt2) -> DaelimPacket:
        pin = ''
        if self.loginPin:
            pin = self.loginPin
        else:
            pin = self.certPin
        self.src += 1
        return self.sendRequest(
            body=body,
            param1=pin,
            param2=paramInt1,
            param3=paramInt2,
            param4=3,
            param5=1
        )


    def sendCenter(self, body, paramInt1, paramInt2) -> DaelimPacket:
        return self.sendRequest(
            body=body,
            param1=self.certPin,
            param2=paramInt1,
            param3=paramInt2,
            param4=1,
            param5=3
        )

    def recv(self, sock, nBytes:int):
        received = 0
        msg = b''
        while received < nBytes:
            # print("wait for {} bytes of {} bytes".format(nBytes - received, nBytes))
            d = sock.recv(nBytes - received)
            received += len(d)
            msg += d
            # print("now received {} bytes of {} bytes".format(received, nBytes))

        return msg

    def send(self, data:bytes) -> DaelimPacket:
        # IP = '211.232.143.113'
        IP = '125.132.139.56'
        PORT = 25301
        # try:
        # print("[request]")
        # dump(data)
        if self.sock is None:
            self.sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((IP, PORT))

        self.sock.sendall(data)

        msg = self.recv(self.sock, 4)
        length = BytesToInteger(msg, 0, 4)
        # print("received body length : {}".format(length))

        msg += self.recv(self.sock, length)

        # print("[resp]")
        # dump(msg)

        dp = DaelimPacket.parse(data=msg, offset=0)
        return dp

    def sendRequest(self, body, param1, param2, param3, param4, param5) -> DaelimPacket:
        """
        :param body:
        :param param1:
        :param param2:
        :param param3:
        :param param4:
        :param param5:
        :return:
        """
        packet = DaelimPacket.create(
            body=body,
            strPin=param1,
            nType=param2,
            nSubType=param3,
            nSrc=param4,
            nDst=param5
        )
        # print("request dump")
        # packet.dump()
        ret = self.send(packet.getBytes())
        # print("response dump")
        # ret.dump()
        return ret

    def reqLoginAuth(self, id, pw, uuid):
        body = {
            'id': id,
            'pw': pw,
            'UUID': uuid,
        }
        if self.hasCertPin:
            return True

        resp = self.sendMMF(
            body=body,
            paramInt1=DaelimType.TYPE_LOGIN,
            paramInt2=DaelimSubtype.Login.LOGIN_CERTPIN_REQ,
        )

        body = resp.jsonBody
        self.infoHo = body.get('ho', '')
        self.infoDong = body.get('dong', '')
        self.certPin = body.get('certpin', '00000000')

        return True

    def reqLogin(self, id, pw):

        if not self.isLogged:
            body = {
                'id': id,
                'pw': pw,
                'certpin': self.certPin,
            }

            resp = self.sendMMF(
                body=body,
                paramInt1=DaelimType.TYPE_LOGIN,
                paramInt2=DaelimSubtype.Login.LOGIN_LOGINPIN_REQ,
            )

            body = resp.jsonBody
            self.loginPin = body.get('loginpin', '')

    def reqMenu(self):
        resp = self.sendMMF(
            body={},
            paramInt1=DaelimType.TYPE_LOGIN,
            paramInt2=DaelimSubtype.Login.LOGIN_MENU_REQ,
        )

    def req_Push(self, token):
        body = {
            'dong': self.infoDong,
            'ho': self.infoHo,
            'pushID': token,
            'type': 'android'
        }
        resp = self.sendMMF(
            body=body,
            paramInt1=DaelimType.TYPE_LOGIN,
            paramInt2=DaelimSubtype.Login.LOGIN_PUSH_REQ,
        )

    def req_guard_info(self):

        body = {
        }

        resp = self.sendMMF(
            body=body,
            paramInt1=DaelimType.TYPE_GUARD,
            paramInt2=DaelimSubtype.Guard.GUARD_STATE_REQ,
        )
        body = resp.jsonBody
        resp.dump()

    def req_guard_change_pw(self, pw = 0):
        for pw in range(300, 551):
            body = {
                'type' : 'qry',
                'num' : '{0:04d}'.format(pw)
            }

            resp = self.sendMMF(
                body=body,
                paramInt1=DaelimType.TYPE_GUARD,
                paramInt2=DaelimSubtype.Guard.SEC_PWDSET_REQ,
            )

            if resp.header.nError != 0 or resp.jsonBody:
                print("pw = {}".format(pw))
                resp.dump()

        pass


    def req_service_info(self):
        body = {
        }

        resp = self.sendMMF(
            body=body,
            paramInt1=DaelimType.TYPE_INFO,
            paramInt2=DaelimSubtype.Info.SERVICE_CNT_REQ,
        )
