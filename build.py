# 바로가기 페이지: python build.py → jamsil/ · car/ (index.html · manifest.json · sw.js) + 맨 위 index.html(① 로 보냄)
# 주소 하나(맨 위)로 ① 나에안식 → ② 차량일지 를 이어서 설치 (휴대폰은 설치 버튼 한 번에 앱 하나만 허락)
import json
BASE = 'https://jamsilmb01-ship-it.github.io/jamsil-shortcuts/'
APPS = {
  'jamsil': {'TITLE': '나에안식 잠실 통합업무시스템', 'SHORT': '나에안식', 'COLOR': '#1f4e79', 'S1': 'on', 'S2': '',
             'NEXT': BASE + 'car/', 'NEXTLABEL': '다음 ② 차량일지 설치 →', 'AFTER': "setTimeout(function () { location.href = '" + BASE + "car/'; }, 1500);",
             'URL': 'https://jamsil-integrated.pages.dev/'},
  'car':    {'TITLE': '나에안식 차량 운행일지', 'SHORT': '차량일지', 'COLOR': '#257a4a', 'S1': 'done', 'S2': 'on',
             'NEXT': BASE + 'jamsil/', 'NEXTLABEL': '← ① 나에안식으로 돌아가기', 'AFTER': "document.querySelector('.steps span.on').className = 'done';",
             'URL': 'https://script.google.com/a/macros/gscsupport.org/s/AKfycbyWBPOMTDsHJAvTrzyhhL7ucnZKRUTfi-W0Df4ViefqFMfe-RC5YSUxYCw4vDWI7NHUTw/exec'},
}
tpl = open('page.tpl', encoding='utf-8').read()
for k, c in APPS.items():
  h = tpl
  for n, v in c.items(): h = h.replace('{{' + n + '}}', v)
  open(f'{k}/index.html', 'w', encoding='utf-8').write(h)
  json.dump({'id': './', 'name': c['TITLE'], 'short_name': c['SHORT'], 'start_url': './?open', 'scope': './', 'display': 'standalone',
             'background_color': '#ffffff', 'theme_color': c['COLOR'],
             'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'},
                       {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'}]},
            open(f'{k}/manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
  # 설치 조건용 서비스 워커 (저장 · 오프라인 없음, 받은 요청을 그대로 넘김)
  open(f'{k}/sw.js', 'w', encoding='utf-8').write("self.addEventListener('install', function () { self.skipWaiting(); });\n"
    "self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });\n"
    "self.addEventListener('fetch', function (e) { e.respondWith(fetch(e.request)); });\n")
open('index.html', 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><title>나에안식 바로가기</title>'
  '<script>location.replace("' + BASE + 'jamsil/");</script><a href="jamsil/">나에안식 바로가기 설치 →</a>')
print('ok')
