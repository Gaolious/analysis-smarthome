import struct

from src.client import DaelimHeader, DaelimPacket, DaelimClient, IntegerToBytes



def process():
    # 1. login auth (cert pin)
    # daelim_device_start.js :2213
    client = DaelimClient()

    ID = '********'
    PW = '**********'
    UUID = '27EB914E0****************E847FBD'
    client.setPins("00000000", None)

    # 1, 5
    """
        0000   00 00 00 65 30 30 30 30 30 30 30 30 00 00 00 01   ...e00000000....
        0010   00 00 00 05 00 01 00 03 00 00 00 00 7b 22 69 64   ............{"id
        0020   22 3a 22 xx xx xx xx xx xx xx xx 22 2c 22 70 77   ":"********","pw
        0030   22 3a 22 xx xx xx xx xx xx xx xx xx xx 22 2c 22   ":"**********","
        0040   55 55 49 44 22 3a 22 32 37 45 42 39 31 34 45 30   UUID":"27EB914E0
        ...
        0060   45 38 34 37 46 42 44 22 7d                        E847FBD"}
    """
    client.reqLoginAuth(ID, PW, UUID)
    # 1, 9
    """
        0000   00 00 00 50 43 33 38 34 31 32 33 36 00 00 00 01   ...PC3841236....
        0010   00 00 00 09 00 01 00 03 00 00 00 00 7b 22 69 64   ............{"id
        0020   22 3a 22 xx xx xx xx xx xx xx xx 22 2c 22 70 77   ":"********","pw
        0030   22 3a 22 xx xx xx xx xx xx xx xx xx xx 22 2c 22   ":"**********","
        0040   63 65 72 74 70 69 6e 22 3a 22 43 33 38 xx xx xx   certpin":"C38***
        0050   33 36 22 7d                                       36"}
    """
    client.reqLogin(ID, PW)

    # 1, 7
    """
        0000   00 00 00 1a 4c xx xx xx xx xx xx 32 00 00 00 01   ....L*******....
        0010   00 00 00 07 00 01 00 03 00 00 00 00 7b 7d         ............{}
    """
    client.reqMenu()

    # 1, 13
    token = "dFF043Rz6zI:APA9*************************KI26wT6vTHwu_2tn6BNoDTJI"
    """
        0000   00 00 00 ec 4c xx xx xx xx xx xx 32 00 00 00 01   ...ìL*******....
        0010   00 00 00 0d 00 01 00 03 00 00 00 00 7b 22 64 6f   ............{"do
        0020   6e 67 22 3a 22 xx xx xx 22 2c 22 68 6f 22 3a 22   ng":"***","ho":"
        0030   xx xx xx xx 22 2c 22 70 75 73 68 49 44 22 3a 22   ****","pushID":"
        0040   64 46 46 30 34 33 52 7a 36 7a 49 3a 41 50 41 39   dFF043Rz6zI:APA9
        ...
        00c0   4b 49 32 36 77 54 36 76 54 48 77 75 5f 32 74 6e   KI26wT6vTHwu_2tn
        00d0   36 42 4e 6f 44 54 4a 49 22 2c 22 70 68 6f 6e 65   6BNoDTJI","phone
        00e0   54 79 70 65 22 3a 22 61 6e 64 72 6f 69 64 22 7d   Type":"android"}
    """
    client.req_Push(token=token)

    # 2, 1
    """
        0000   00 00 00 1a 4c xx xx xx xx xx xx 32 00 00 00 02   ....L*******....
        0010   00 00 00 01 00 01 00 03 00 00 00 00 7b 7d         ............{}
    """
    client.req_guard_info()
    #
    # # 5, 57
    # client.req_service_info()
    client.req_guard_change_pw(0)

process()