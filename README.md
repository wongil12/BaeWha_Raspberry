# 배화여자대학교 1학년 여름 계절학기 프로젝트

## 라즈베리파이를 사용한 Smart 쓰레기통 제작

1. 사용하는 모듈 및 센서들
    - SG90 서보모터
    - 초음파 센서 (2개)
    - 온/습도 센서 (2개)
    - 불꽃 감지 센서
    - 부저
    - 5색 LED (2개)
    - Toggle 스위치
    - 카메라 모듈 (2개)

1. 구현 기능
    1. 초음파 센서 범위에 사물이 감지되었을 때 휴지통 뚜껑이 열림 - **완료**
        * 감지 범위를 <u>50cm</u>로 했을 때 범위가 너무 크다고 판단하여 <u>20cm</u>로 축소
        * 한번 열리면 5초동안 열림 상태 유지
    1. 온/습도 센서로 휴지통 내/외부 온/습도를 파악하여 휴지통 내부의 위생상태 확인 
        * DB와 연동하여 온/습도를 일정 시간 단위로 확인 가능
    1. 불꽃 감지 센서를 이용하여 휴지통 내 화재 감지 - **완료**
        * 불꽃이 감지되었을 때 부저로 알림
    1. 휴지통 내부 상단에 초음파 센서를 장착하여 휴지통의 가득 찬 정도를 확인 가능
        * 거리별로 5색 LED 및 7색 LED를 이용하여 범위별로 다른 색을 표시
        * 휴지통이 가득 찼을 경우 불꽃 감지와는 다른 소리의 부저로 알림
    1. Toggle 스위치를 활용하여 열림 상태 유지 가능
    1. ~~카메라 모듈을 활용하여 휴지통이 가득 찼을 때 마지막에 쓰레기를 버린 사람 확인 가능~~
        * 휴지통 내/외부에 카메라를 설치하여 열리기 전에 사진을 찍게 한다