# 홈 화면 아이콘 만들기: 색 바탕(둥근 네모) + 굵은 글자 두 줄. python make_icons.py
from PIL import Image, ImageDraw, ImageFont
FONT = r"C:\Windows\Fonts\malgunbd.ttf"
APPS = {
  'jamsil': {'bg': (31, 78, 121), 'lines': ['통합', '업무'], 'accent': (255, 192, 0)},
  'car':    {'bg': (37, 122, 74), 'lines': ['차량', '일지'], 'accent': (255, 255, 255)},
}
def make(key, cfg):
  S = 1024
  im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
  d = ImageDraw.Draw(im)
  d.rounded_rectangle([0, 0, S, S], radius=220, fill=cfg['bg'])   # 아이폰은 모서리를 알아서 깎지만 안드로이드용으로 둥글게
  d.rectangle([180, 870, S - 180, 900], fill=cfg['accent'])          # 아래 띠
  f = ImageFont.truetype(FONT, 330)
  for i, t in enumerate(cfg['lines']):
    w = d.textlength(t, font=f)
    d.text(((S - w) / 2, 110 + i * 360), t, font=f, fill=(255, 255, 255))
  for size, name in [(512, 'icon-512.png'), (192, 'icon-192.png'), (180, 'apple-touch-icon.png')]:
    im.resize((size, size), Image.LANCZOS).save(f'{key}/{name}')
  # 아이폰 apple-touch-icon 은 투명을 검게 채우므로 바탕을 꽉 채운 판도 따로
  full = Image.new('RGB', (S, S), cfg['bg']); full.paste(im, (0, 0), im)
  full.resize((180, 180), Image.LANCZOS).save(f'{key}/apple-touch-icon.png')
for k, c in APPS.items(): make(k, c)
print('ok')
