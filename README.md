# gps-of-gps
사용자가 지도에서 선택한 위치를 기준으로, 약 3억 건의 GPS 데이터를 분석하여 반경 내 패턴을 시각화하는 웹 애플리케이션입니다.
<img src="https://github.com/user-attachments/assets/2b9a1573-7338-460e-9f3d-773304dc1f14">
<img src="https://github.com/user-attachments/assets/ef0028dc-afa3-4916-805f-e8690f1d8d95">

## Overvies
- 약 3억 건 GPS 데이터 기반 분석
- 사용자 지정 좌표 기준 반경(5~25km) 데이터 조회
- Google Maps API 기반 위치 선택 및 시각화
- Uber H3 인덱스를 활용한 공간 데이터 파티셔닝

## 애플리케이션 구조
<img src="https://github.com/user-attachments/assets/c379b7b4-de4a-49a7-809b-96f91a2e3e99">

## 개발 의의
- 약 3억 건의 GPS 데이터를 효율적으로 조회하기 위해 Uber H3 인덱스를 활용한 공간 파티셔닝 구조 설계
- 사용자가 선택한 좌표 기준으로 5~25km 반경 데이터를 실시간 필터링 및 시각화 기능 구현
- 지도 클릭 이벤트를 통해 직관적인 위치 선택 UI 구성

## 기술 스택
|Category|Stack|
| --- | --- |
|Frontend|React, JavaScript|
|Backend|Python|
|Database|MariaDB|
|API|Google Maps API|

## 주요 특징
- 지도 클릭을 통한 GPS 좌표 획득
- 선택 위치 마커 표시
- 반경 기반 데이터 필터링 (5~25km)
- GPS 데이터 시각화
- 기본 위치: 서울
