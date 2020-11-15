 
# smarthome
대림사의 smarthome 2.0 분석

# Analysis
- Webview 기반이며, 내장된 javascript에 '모든 것' 이 들어 있음.
- logcat에 id/pw가 노출되고 있음.
- apk decompile 후 packet 구조만 파악하면 됨.
- 별다른 encryption이나 hash는 사용하지 않고 있음.
- 다행스럽게도 https 이긴 하나, ...

## Packet

### Packet 구조
| Length | Header | Body |
|--------|--------|--------|
| 4 byte 고정 | 24 byte 고정 | 가변 |


### Packet Length
Length에는 Length자체 4byte를 포함한 Header 24byte 와 body 길이를 모두 더한 값이 들어 있음.

### Packet Header
Header에는 총 24 byte로 구성되어 있음.

|Pin| Type | SubType | Src | Dst | Error | reserved|
|--------|--------|--------|--------|--------|--------|--------|
| 8 byte | 4 byte | 4 byte | 2 byte | 2 byte | 1 byte | 3 byte | 
| STR | INT | INT | INT | INT | INT | INT (0x000000) | 
|로그인시<br/>얻는<br/>문자열|constraints.py|constraints.py|보내는측<br/>고정인듯?|받는측<br/>고정인듯?|에러유무<br/>flag|0x000000|


## Tools

App
- Android Device
- [APK Download](https://www.apkfollow.com/app/zh/epyeonhansesang-seumateuhom-2-0/kr.co.daelimcorp.smarthome/)

Reverse / Analysis
- [Frida](https://frida.re/) + Proxy Server
- WireShark

Develop
- [Visual Studio Code](https://code.visualstudio.com/)
- [Ubuntu 18.04](https://releases.ubuntu.com/18.04/) / Python 3.9.0

