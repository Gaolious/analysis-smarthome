
class ServerType():
    SMART_PHONE = 1
    CENTER_SERVER = 2
    MMF_SERVER = 3
    CSF = 4


class DaelimType():
    # Packet Type
    TYPE_SYSTEM = 0  # 시스템
    TYPE_LOGIN = 1  # 로그인
    TYPE_GUARD = 2  # 방범
    TYPE_DEVICE = 3  # 제어
    TYPE_EMS = 4  # EMS
    TYPE_INFO = 5  # 조회
    TYPE_HEALTHCARE = 6  # 헬스케어
    TYPE_SETTING = 7  # 설정
    TYPE_EVCALL = 8  # 엘리베이터콜
    TYPE_ETC = 9  # etc(call)
    TYPE_APP_LOG = 100  # request not work


class DaelimSubtype():

    class System():
        # SubType (SYSTEM)
        SYSTEM_GENERAL = 0  # API호출됨
        SYSTEM_CONNECTED = 1  # 스마트홈 서버와 연결됨
        SYSTEM_CLOSED = 2  # 스마트홈 서버와 연결 종료
        SYSTEM_RESERVED = 3  # 사용되지 않음
        SYSTEM_CONN_STATUS = 4  # 스마트홈 서버 접속 상태
        SYSTEM_LOGIN_STATUS = 5  # 로그인 핀 상태
        SYSTEM_INFO = 6  # 앱 정보
        SYSTEM_OPEN = 7  # 스마트 홈 서버 연결 요청
        SYSTEM_OPEN_RES = 8  # 스마트 홈 서버 연결 요청 결과
        SYSTEM_TIMEOUT = 9  # TIME OUT
        SYSTEM_CLEARCACHE = 10  # 단말기 Cache삭제 완료시 리턴

    class Login():
        # SubType (LOGIN)
        LOGIN_DANJILIST_REQ = 1  # 단지목록요청
        LOGIN_DANJILIST_RES = 2  # 단지목록응답
        LOGIN_DANJIINFO_REQ = 3  # 단지IP요청
        LOGIN_DANJIINFO_RES = 4  # 단지IP응답
        LOGIN_CERTPIN_REQ = 5  # 인증요청
        LOGIN_CERTPIN_RES = 6  # 인증요청응답
        LOGIN_MENU_REQ = 7  # UI구성정보요청
        LOGIN_MENU_RES = 8  # UI구성정보전달
        LOGIN_LOGINPIN_REQ = 9  # 로그인요청
        LOGIN_LOGINPIN_RES = 10  # 로그인응답
        LOGIN_COMMONINFO_REQ = 11  # 알림메시지요청
        LOGIN_COMMONINFO_RES = 12  # 알림메시지응답
        LOGIN_PUSH_REQ = 13  # 푸쉬토큰등록
        LOGIN_PUSH_RES = 14  # 푸쉬토큰응답
        LOGIN_ALIVE_REQ = 15  # MMF실행
        LOGIN_ALIVE_RES = 16  # MMF실행응답
        LOGIN_DELCERT_REQ = 17  # 인증삭제요청
        LOGIN_DELCERT_RES = 18  # 인증삭제응답
        LOGIN_REGISTER_REQ = 19  # 회원가입요청
        LOGIN_REGISTER_RES = 20  # 회원가입응답
        LOGIN_CHECKID_REQ = 21  # 아이디중복확인요청
        LOGIN_CHECKID_RES = 22  # 아이디중복확인응답
        LOGIN_CHECKHH_REQ = 23  # 세대주중복확인요청
        LOGIN_CHECKHH_RES = 24  # 세대주중복확인응답
        LOGIN_FINDID_REQ = 25  # 아이디찾기요청
        LOGIN_FINDID_RES = 26  # 아이디찾기응답
        LOGIN_APPR_REQ = 27  # 인증방식요청
        LOGIN_APPR_RES = 28  # 인증방식응답
        LOGIN_WPAD_REQ = 29  # 월패드인증확인요청
        LOGIN_WPAD_RES = 30  # 월패드인증확인응답
        LOGIN_SWITCHS_REQ = 31  # 통합스위치인증시작요청
        LOGIN_SWITCHS_RES = 32  # 통합스위치인증시작응답
        LOGIN_SWITCHE_REQ = 33  # 통합스위치인증취소요청
        LOGIN_SWITCHE_RES = 34  # 통합스위치인증취소응답
        LOGIN_USERINFO_REQ = 35  # 회원정보요청
        LOGIN_USERINFO_RES = 36  # 회원정보응답
        LOGIN_USEREDIT_REQ = 37  # 회원정보수정요청
        LOGIN_USEREDIT_RES = 38  # 회원정보수정응답
        LOGIN_USERDEL_REQ = 39  # 회원탈퇴요청
        LOGIN_USERDEL_RES = 40  # 회원탈퇴응답
        LOGIN_PASSWORD_REQ = 41  # 비밀번호변경 요청
        LOGIN_PASSWORD_RES = 42  # 비밀번호변경 응답
        LOGIN_FINDPW_REQ = 43  # 비밀번호찾기 응답
        LOGIN_FINDPW_RES = 44  # 비밀번호찾기 응답
        LOGIN_REGISTER_NOT = 45  # 회원가입알림
        LOGIN_USERDEL_NOT = 46  # 회원탈퇴알림
        LOGIN_APPRCEL_REQ = 47  # 회원가입인증취소요청
        LOGIN_APPRCEL_RES = 48  # 회원가입인증취소응답
        LOGIN_HOUSEHD_NOT = 49  # 세대주변경알림
        LOGIN_FINDPWINFO_REQ = 50  # 비밀번호찾기계정미인증요청
        LOGIN_FINDPWINFO_RES = 51  # 비밀번호찾기계정미인증응답
        LOGIN_NEWPASSWORD_REQ = 52  # 신규비밀번호변경요청
        LOGIN_NEWPASSWORD_RES = 53  # 신규비밀번호변경응답

    class Guard():
        # 2.2.2    방범 – TYPE 2
        GUARD_STATE_REQ = 1  # 방범상태요청 스마트폰– 단지서버(이하)
        GUARD_STATE_RES = 2  # 방범상태응답 단지서버(이하) –스마트폰
        GUARD_NOTIFY = 3  # 방범알림 단지서버 – APNS
        EMER_LIST_REQ = 4  # 비상리스트 목록 요청
        EMER_LIST_RES = 5  # 비상리스트 목록 응답

        SEC_ACT_REQ = 6  # 방범 실행/해제요청
        SEC_ACT_RES = 7  # 방범 실행/해제응답
        SEC_QRY_REQ = 8  # 방범설정 상태요청
        SEC_QRY_RES = 9  # 방범설정 상태응답
        SEC_SET_REQ = 10  # 방범설정 설정요청
        SEC_SET_RES = 11  # 방범설정 설정응답
        SEC_PWDSET_REQ = 12  # 방범비밀번호 설정요청
        SEC_PWDSET_RES = 13  # 방범비밀번호 설정응답
        SEC_SET_NOT = 14  # 방범설정 설정 알림
        SEC_INV_NOT = 15  # 방범설정 침입감지시 알림
        SEC_INVREL_NOT = 16  # 방범설정 침입감지 미해제시 알림
        SEC_PWD_NOT = 17  # 방범비밀번호 변경 알림
        SEC_RELEASE_NOT = 18  # 방범 해제요청알림

    class DeviceControl():
        # SubType : 2.2.3  제어 – TYPE 3 (스마트폰– 단지서버(이하)
        DEVICE_QUERY_REQ = 1  # 기기상태요청   스마트폰– 단지서버(이하)
        DEVICE_QUERY_RES = 2  # 기기상태응답   단지서버(이하) –스마트폰
        DEVICE_INVOKE_REQ = 3  # 기기제어요청   스마트폰– 단지서버(이하)
        DEVICE_INVOKE_RES = 4  # 기기제어응답   단지서버(이하) –스마트폰
        DEVICE_INVOKE_NOT = 5  # 기기제어알림
        WALLSOCKET_QUERY_REQ = 6  # 대기전력 상태요청
        WALLSOCKET_QUERY_RES = 7  # 대기전력 상태응답
        WALLSOCKET_INVOKE_REQ = 8  # 대기전력 제어요청
        WALLSOCKET_INVOKE_RES = 9  # 대기전력 제어응답

    class EMS():
        # SubType, 2.2.4   EMS – TYPE 4  (스마트폰– 단지서버(이하))
        EMS_FORECAST_REQ = 1  # 에너지예측소비량요청
        EMS_FORECAST_RES = 2  # 에너지예측소비량응답
        EMS_NOW_REQ = 3  # 현재사용량요청
        EMS_NOW_RES = 4  # 현재사용량정보응답
        EMS_MONTHLYTABLE_REQ = 5  # 월간사용량표요청
        EMS_MONTHLYTABLE_RES = 6  # 월간사용량표응답
        EMS_MONTHLYGRAPH_REQ = 7  # 월간사용량그래프요청
        EMS_MONTHLYGRAPH_RES = 8  # 월간사용량그래프응답
        EMS_SAMETYPE_REQ = 9  # 연간사용량 요청
        EMS_SAMETYPE_RES = 10  # 연간사용량 응답
        EMS_CO2_REQ_CO2 = 11  # 저감량 요청
        EMS_CO2_RES_CO2 = 12  # 저감량 응답
        EMS_ENERGYALARM_NOT = 13  # 에너지 절약 알림
        EMS_YEARTABLE_REQ = 14  # 연간사용량표요청
        EMS_YEARTABLE_RES = 15  # 연간사용량표응답
        EMS_RANK_REQ = 16  # 랭킹정보요청
        EMS_RANK_RES = 17  # 랭킹정보응답
        EMS_TARGETQRY_REQ = 18  # 목표사용량조회 요청
        EMS_TARGETQRY_RES = 19  # 목표사용량조회 응답
        EMS_TARGETSET_REQ = 20  # 목표사용량설정 요청
        EMS_TARGETSET_RES = 21  # 목표사용량설정 응답
        EMS_ELECPGS_NOT = 22  # 전기누진단계 변화 알림
        EMS_NOWAMT_REQ = 23  # 당월예상요금요청
        EMS_NOWAMT_RES = 24  # 당월예상요금응답
        EMS_TIMETABLE_REQ = 25  # 당월시간별사용량요청
        EMS_TIMETABLE_RES = 26  # 당월시간별사용량응답

    class Info():
        # SubType, 2.2.5   조회 – TYPE 5
        INFO_NOTICELIST_REQ = 1  # 공지사항 목록 요청
        INFO_NOTICELIST_RES = 2  # 공지사항 목록 응답
        INFO_NOTICECHECK_REQ = 3  # 공지사항 보기 요청
        INFO_NOTICECHECK_RES = 4  # 공지사항 보기 응답
        INFO_PARCELLIST_REQ = 5  # 택배 목록 요청
        INFO_PARCELLIST_RES = 6  # 택배목록 응답
        INFO_PARCELCHECK_REQ = 7  # 택배보기 요청
        INFO_PARCELCHECK_RES = 8  # 택배보기 응답
        INFO_VISITORLIST_REQ = 9  # 부재중방문자 목록요청
        INFO_VISITORLIST_RES = 10  # 부재중방문자 목록응답
        INFO_VISITORCHECK_REQ = 11  # 부재중방문자 보기요청
        INFO_VISITORCHECK_RES = 12  # 부재중방문자 보기응답
        CCTV_ON_REQ = 13  # CCTV 화면요청
        CCTV_IMAGE_SEND = 14  # CCTV 화면전송
        CCTV_OFF_REQ = 15  # CCTV 화면종료
        CCTV_OFF_RES = 16  # CCTV 화면종료응답
        CCTV_CHCHANGE_REQ = 17  # CCTV 채널변경
        LOCATION_TAGINFO_REQ = 18  # 위치인식태그정보요청
        LOCATION_TAGINFO_RES = 19  # 위치인식태그정보응답
        LOCATION_ONMAP_REQ = 20  # 위치인식태그위치요청
        LOCATION_ONMAP_RES = 21  # 위치인식태그위치응답
        LOCATION_EMERLIST_REQ = 22  # 위치인식비상콜이력요청
        LOCATION_EMERLIST_RES = 23  # 위치인식비상콜이력응답
        LOCATION_EMERMAP_REQ = 24  # 비상콜위치요청
        LOCATION_EMERMAP_RES = 25  # 비상콜위치응답
        LOCATION_MAPIMAGE_REQ = 26  # 맵 이미지 요청
        LOCATION_MAPIMAGE_RES = 27  # 맵 이미지 응답
        SHOP_LIST_REQ = 28  # 단지주변정보요청
        SHOP_LIST_RES = 29  # 단지주변정보응답
        INFO_NOTICE_NOT = 30  # 공지 발생 알림    단지서버(이하) – APNS
        INFO_PARCEL_NOT = 31  # 택배 발생 알림     단지서버(이하) - APNS
        INFO_VISITOR_NOT = 32  # 부재중 발생 알림   단지서버(이하) - APNS
        INFO_EMERCALL_NOT = 33  # 위치확인 비상콜 발생 알림  단지서버(이하) - APNS
        INFO_NOTICEIMG_REQ = 34  # 공지사항 이미지 요청
        INFO_NOTICEIMG_RES = 35  # 공지사항 이미지 응답
        INFO_VISITORDEL_REQ = 36  # 부재중방문자 삭제 요청
        INFO_VISITORDEL_RES = 37  # 부재중방문자 삭제 응답
        INCAR_LIST_REQ = 38  # 입차목록 요청
        INCAR_LIST_RES = 39  # 입차목록 응답
        INCAR_VLIST_REQ = 40  # 방문차량목록 요청
        INCAR_VLIST_RES = 41  # 방문차량목록 응답
        INCAR_VREG_REQ = 42  # 방문차량등록 요청
        INCAR_VREG_RES = 43  # 방문차량등록 응답
        INCAR_VDEL_REQ = 44  # 방문차량삭제 요청
        INCAR_VDEL_RES = 45  # 방문차량삭제 응답
        INCAR_INFO_NOT = 46  # 입차발생 알림
        PASSNOTI_LIST_REQ = 47  # 출입관리목록 요청
        PASSNOTI_LIST_RES = 48  # 출입관리목록 응답
        MTCOSTMM_LIST_REQ = 49  # 월별관리비 요청
        MTCOSTMM_LIST_RES = 50  # 월별관리비 응답
        MTCOSTYY_LIST_REQ = 51  # 연간관리비 요청
        MTCOSTYY_LIST_RES = 52  # 연간관리비 응답
        INCAR_DEL_REQ = 53  # 입차목록삭제 요청
        INCAR_DEL_RES = 54  # 입차목록삭제 응답
        PASSNOTI_DEL_REQ = 55  # 출입관리삭제 요청
        PASSNOTI_DEL_RES = 56  # 출입관리삭제 응답
        SERVICE_CNT_REQ = 57  # 미확인메세지 요청
        SERVICE_CNT_RES = 58  # 미확인메세지 응답
        USE_HISTORY_REQ = 59  # 사용이력 요청
        USE_HISTORY_RES = 60  # 사용이력 응답
        INFO_PASSNOTI_NOT = 61  # 출입관리 알림
        USE_HISTORY_NOT = 62  # 사용이력 알림
        LOCATION_TAGINFO_NOT = 63  # 위치조회 알림
        PARKCAR_LOC_REQ = 64  # 차량주차위치목록요청
        PARKCAR_LOC_RES = 65  # 차량주차위치목록응답
        INCAR_LOC_REQ = 66  # 차량위치요청
        INCAR_LOC_RES = 67  # 차량위치응답
        INCAR_LOC_PIC_REQ = 68  # 차량위치사진요청
        INCAR_LOC_PIC_RES = 69  # 차량위치사진응답
        PARKING_STATUS_REQ = 70  # 주차가능공간정보요청
        PARKING_STATUS_RES = 71  # 주차가능공간정보응답

    class Health():
        # SubType, 2.2.6   헬스케어 – TYPE 6 (스마트폰– 단지서버)
        HEALTH_LOGIN_REQ = 1  # 헬스케어 로그인 요청
        HEALTH_LOGIN_RES = 2  # 헬스케어 로그인 응답
        HEALTH_PRESSURE_REQ = 3  # 혈압값 요청
        HEALTH_PRESSURE_RES = 4  # 혈압값 응답
        HEALTH_COMPOSITION_REQ = 5  # 체성분 요청
        HEALTH_COMPOSITION_RES = 6  # 체성분 응답
        HEALTH_COMPOSITIONLIST_REQ = 7  # 체성분 목록 요청
        HEALTH_COMPOSITIONLIST_RES = 8  # 체성분 목록 응답
        HEALTH_COMPOSITIONTEXT_REQ = 9  # 체성분 문구 요청
        HEALTH_COMPOSITIONTEXT_RES = 10  # # 체성분 문구 응답
        HEALTH_FAT_REQ = 11  # 비만 요청
        HEALTH_FAT_RES = 12  # 비만 응답
        HEALTH_FATLIST_REQ = 13  # 비만 목록 요청
        HEALTH_FATLIST_RES = 14  # 비만 목록 응답
        HEALTH_FATTEXT_REQ = 15  # 비만 문구 요청
        HEALTH_FATTEXT_RES = 16  # 비만 문구 응답
        HEALTH_ABDOMEN_REQ = 17  # 복부 요청
        HEALTH_ABDOMEN_RES = 18  # 복부 응답
        HEALTH_ABDOMENLIST_REQ = 19  # 복부 목록 요청
        HEALTH_ABDOMENLIST_RES = 20  # 복부 목록 응답
        HEALTH_ABDOMENTEXT_REQ = 21  # 복부 문구 요청
        HEALTH_ABDOMENTEXT_RES = 22  # 복부 문구 응답
        HEALTH_MUSCLE_REQ = 23  # 근육 요청
        HEALTH_MUSCLE_RES = 24  # 근육 응답
        HEALTH_MUSCLELIST_REQ = 25  # 근육 목록 요청
        HEALTH_MUSCLELIST_RES = 26  # 근육 목록 응답
        HEALTH_MUSCLETEXT_REQ = 27  # 근육 문구 요청
        HEALTH_MUSCLETEXT_RES = 28  # 근육 문구 응답    단지서버(이하) – APNS

    class Settings():
        # SubType, 2.2.7   설정 – TYPE 7
        PUSH_QUERY_REQ = 1  # 푸시상태요청
        PUSH_QUERY_RES = 2  # 푸시상태응답
        PUSH_SETTING_REQ = 3  # 푸시설정요청
        PUSH_SETTING_RES = 4  # 푸시설정응답
        SETTING_USERLIST_REQ = 5  # 세대사용자목록 요청
        SETTING_USERLIST_RES = 6  # 세대사용자목록 응답
        SETTING_USERDEL_REQ = 7  # 세대사용자탈퇴 요청
        SETTING_USERDEL_RES = 8  # 세대사용자탈퇴 응답
        SETTING_USER_NOT = 9  # 세대사용자탈퇴 알림
        SETTING_ENTPWQRY_REQ = 10  # 공동현관비밀번호상태 요청
        SETTING_ENTPWQRY_RES = 11  # 공동현관비밀번호상태 응답
        SETTING_ENTPWSET_REQ = 12  # 공동현관비밀번호설정 요청
        SETTING_ENTPWSET_RES = 13  # 공동현관비밀번호설정 응답
        SETTING_ENTPW_NOT = 14  # 공동현관비밀번호설정 알림
        SETTING_UNUSEDQRY_REQ = 15  # 장기미사용상태 요청
        SETTING_UNUSEDQRY_RES = 16  # 장기미사용상태 응답
        SETTING_UNUSEDSET_REQ = 17  # 장기미사용설정 요청
        SETTING_UNUSEDSET_RES = 18  # 장기미사용설정 응답
        SETTING_VLIGHTQRY_REQ = 19  # 방문객조명알림상태 요청
        SETTING_VLIGHTQRY_RES = 20  # 방문객조명알림상태 응답
        SETTING_VLIGHTSET_REQ = 21  # 방문객조명알림설정 요청
        SETTING_VLIGHTSET_RES = 22  # 방문객조명알림설정 응답
        SETTING_UNUSEDSET_NOT = 23  # 장기미사용알림
        SETTING_CUSTOMLIST_REQ = 24  # 맞춤설정 목록 요청
        SETTING_CUSTOMLIST_RES = 25  # 맞춤설정 목록 응답
        SETTING_CUSTOMGET_REQ = 26  # 맞춤설정 엑션 요청
        SETTING_CUSTOMGET_RES = 27  # 맞춤설정 엑션 응답
        SETTING_CUSTOMSET_REQ = 28  # 맞춤설정 설정 요청
        SETTING_CUSTOMSET_RES = 29  # 맞춤설정 설정 응답
        SETTING_CUSTOMDEL_REQ = 30  # 맞춤설정 삭제 요청
        SETTING_CUSTOMDEL_RES = 31  # 맞춤설정 삭제 응답
        SETTING_CUSTOM_NOT = 32  #

    class Elevator():
        # SubType, 2.2.8   엘리베이터콜 – TYPE 8
        EVCALL_CALL_REQ = 1  # 엘리베이터 콜 요청
        EVCALL_CALL_RES = 2  # 엘리베이터 콜 응답
        EVCALL_ARRIVE_NOT = 3  # 엘리베이터 도착 알림

    class Etc():
        ETC_SIPCALL_REQ = 1  # 통화 앱 요청
        ETC_SIPCALL_RES = 2  # 통화 앱 응답
        ETC_SIPCALL_NOT = 3  # 통화 수신 알림
        ETC_CALLLIST_REQ = 4  # 통화수신자 목록 요청
        ETC_CALLLIST_RES = 5  # 통화수신자 목록 응답
        ETC_CALLSET_REQ = 6  # 통화수신자 설정 요청
        ETC_CALLSET_RES = 7  # 통화수신자 설정 응답

"""

//TYPE_APP_LOG
var APP_WEATHER_REQ = 1;
var APP_LIVING_REQ = 2;
var APP_MAINMENU_REQ = 3;
var APP_SMARTELEC_REQ = 4;
var APP_EMS_ELEC_REQ = 5;
var APP_EMS_GAS_REQ = 6;
var APP_EMS_WATER_REQ = 7;
var APP_EMS_HOTWATER_REQ = 8;
var APP_EMS_HEATING_REQ = 9;
"""
