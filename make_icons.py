# 홈 화면 아이콘: 색 바탕(둥근 네모) + 그림(나에안식 = 집, 차량일지 = 자동차). python make_icons.py
from PIL import Image, ImageDraw
S = 1024
def base(bg):
  im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
  d.rounded_rectangle([0, 0, S, S], radius=220, fill=bg)
  return im, d
def house():
  im, d = base((31, 78, 121)); W = (255, 255, 255); Y = (255, 192, 0)
  d.polygon([(512, 170), (140, 500), (884, 500)], fill=W)                 # 지붕
  d.rectangle([640, 230, 730, 400], fill=W)                               # 굴뚝
  d.rectangle([230, 470, 794, 850], fill=W)                               # 몸통
  d.rounded_rectangle([445, 600, 579, 850], radius=24, fill=Y)            # 문
  d.rectangle([290, 560, 395, 665], fill=(31, 78, 121)); d.rectangle([629, 560, 734, 665], fill=(31, 78, 121))   # 창
  return im
def car():
  G = (37, 122, 74); im, d = base(G); W = (255, 255, 255)
  d.rounded_rectangle([130, 470, 894, 740], radius=90, fill=W)            # 몸통
  d.polygon([(285, 480), (380, 290), (650, 290), (760, 480)], fill=W)     # 지붕
  d.polygon([(330, 470), (405, 330), (505, 330), (505, 470)], fill=G)     # 앞창
  d.polygon([(545, 470), (545, 330), (630, 330), (710, 470)], fill=G)     # 뒷창
  for cx in (315, 709):                                                   # 바퀴
    d.ellipse([cx - 115, 640, cx + 115, 870], fill=(30, 40, 35)); d.ellipse([cx - 50, 705, cx + 50, 805], fill=(200, 200, 200))
  d.rounded_rectangle([150, 560, 230, 610], radius=20, fill=(255, 210, 90))  # 등
  return im
for key, im in (('jamsil', house()), ('car', car())):
  bg = im.getpixel((S // 2, 40))[:3]
  for size, name in [(512, 'icon-512.png'), (192, 'icon-192.png')]:
    im.resize((size, size), Image.LANCZOS).save(f'{key}/{name}')
  full = Image.new('RGB', (S, S), bg); full.paste(im, (0, 0), im)          # 아이폰용은 바탕을 꽉 채움
  full.resize((180, 180), Image.LANCZOS).save(f'{key}/apple-touch-icon.png')
print('ok')
