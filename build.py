# 바로가기 페이지 만들기: python build.py → jamsil/ · car/ 의 index.html · manifest.json
import json
APPS = {
  'jamsil': {'TITLE': '나에안식 잠실 통합업무시스템', 'SHORT': '통합업무', 'COLOR': '#1f4e79',
             'URL': 'https://script.google.com/a/macros/gscsupport.org/s/AKfycbyXpPF1653Jcdb7gTh4Efq5zx_-NSma935vyzxfqtKJZkl9aTMh83iYis9wJRcfE9nD/exec'},
  'car':    {'TITLE': '나에안식 차량 운행일지', 'SHORT': '차량일지', 'COLOR': '#257a4a',
             'URL': 'https://script.google.com/a/macros/gscsupport.org/s/AKfycbyWBPOMTDsHJAvTrzyhhL7ucnZKRUTfi-W0Df4ViefqFMfe-RC5YSUxYCw4vDWI7NHUTw/exec'},
}
tpl = open('page.tpl', encoding='utf-8').read()
for k, c in APPS.items():
  h = tpl
  for n, v in c.items(): h = h.replace('{{' + n + '}}', v)
  open(f'{k}/index.html', 'w', encoding='utf-8').write(h)
  json.dump({'name': c['TITLE'], 'short_name': c['SHORT'], 'start_url': './?open', 'scope': './', 'display': 'browser',
             'background_color': '#ffffff', 'theme_color': c['COLOR'],
             'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]},
            open(f'{k}/manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open('index.html', 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>나에안식 잠실 바로가기</title>'
  '<body style="font-family:sans-serif;max-width:420px;margin:30px auto;padding:0 18px"><h2>나에안식 잠실 바로가기</h2>'
  + ''.join(f'<p><a href="{k}/" style="display:flex;align-items:center;gap:12px;text-decoration:none;color:#1f2933;font-size:18px;font-weight:700"><img src="{k}/icon-192.png" width="56" height="56" style="border-radius:12px">{c["TITLE"]}</a></p>' for k, c in APPS.items())
  + '<p style="color:#7b8794;font-size:13px">누른 뒤 안내대로 홈 화면에 추가하세요.</p></body>')
print('ok')
