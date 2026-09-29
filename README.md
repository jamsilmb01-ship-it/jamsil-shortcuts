# 나에안식 잠실 휴대폰 바로가기

통합업무시스템 · 차량 운행일지를 휴대폰 홈 화면에 **아이콘으로** 저장하기 위한 작은 페이지 (GitHub Pages).
Apps Script 웹앱은 구글 페이지 안에 싸여 열려서 홈 화면 아이콘을 직접 넣을 수 없어, 이 페이지가 아이콘을 들고 앱으로 넘겨 준다.

- 주소 하나: https://jamsilmb01-ship-it.github.io/jamsil-shortcuts/ → ① 나에안식(집) 설치 → ② 차량일지(자동차) 설치로 이어짐
- 안드로이드 크롬: [📲 홈 화면에 설치] 버튼 한 번(PWA, manifest · sw.js). 아이폰: 공유 → 홈 화면에 추가 안내. 설치 안내로 열면 주소에 ?open 을 붙여 두어 아이콘으로 열 때 바로 앱으로
- 개인정보 없음: 앱 주소로 넘겨 주기만 함 (앱은 기관 계정만 열림)
- 고칠 때: 아이콘 `python make_icons.py`, 페이지 `python build.py` (page.tpl · APPS) → 커밋 · push 하면 1~2분 뒤 반영
- 앱 배포ID가 바뀌면 build.py 의 URL 을 고친다 (보통 --deploymentId 로 배포해서 안 바뀜)
