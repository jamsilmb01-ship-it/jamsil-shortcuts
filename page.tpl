<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<meta name="apple-mobile-web-app-title" content="{{SHORT}}">
<meta name="application-name" content="{{SHORT}}">
<meta name="theme-color" content="{{COLOR}}">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="manifest" href="manifest.json">
<script>
  // 홈 화면 아이콘으로 열면(?open) 바로 앱으로. 이 안내 페이지를 처음 열면 주소에 ?open 을 붙여 두어,
  // 아이폰 「홈 화면에 추가」도 ?open 주소로 저장되게 한다 (안드로이드는 manifest 의 start_url)
  var APP = '{{URL}}';
  if (/[?&]open\b/.test(location.search)) location.replace(APP);
  else if (history.replaceState) history.replaceState(null, '', location.pathname + '?open');
</script>
<style>
  body { font-family: -apple-system, "Malgun Gothic", "Apple SD Gothic Neo", sans-serif; margin: 0; background: #f4f6f9; color: #1f2933; }
  .wrap { max-width: 460px; margin: 0 auto; padding: 28px 18px 40px; text-align: center; }
  img.ic { width: 96px; height: 96px; border-radius: 22px; box-shadow: 0 4px 14px rgba(0,0,0,.15); }
  h1 { font-size: 22px; margin: 14px 0 4px; }
  .sub { color: #5b6773; font-size: 14px; margin: 0 0 20px; }
  a.go { display: block; background: {{COLOR}}; color: #fff; text-decoration: none; font-weight: 700; font-size: 17px; padding: 14px; border-radius: 12px; }
  .how { text-align: left; background: #fff; border: 1px solid #dde3ea; border-radius: 12px; padding: 12px 16px; margin-top: 18px; font-size: 14.5px; line-height: 1.6; }
  .how h2 { font-size: 15px; margin: 6px 0 4px; }
  .how ol { margin: 0 0 6px; padding-left: 20px; }
  .note { color: #7b8794; font-size: 12.5px; margin-top: 14px; }
</style>
</head>
<body>
<div class="wrap">
  <img class="ic" src="icon-192.png" alt="">
  <h1>{{TITLE}}</h1>
  <p class="sub">휴대폰 홈 화면에 아이콘으로 저장해 두세요.</p>
  <a class="go" href="{{URL}}">지금 열기</a>
  <div class="how">
    <h2>📱 안드로이드 (크롬)</h2>
    <ol><li>오른쪽 위 <b>⋮</b> 누르기</li><li><b>「홈 화면에 추가」</b>(또는 「앱 설치」) → <b>추가</b></li></ol>
    <h2>🍎 아이폰 (사파리)</h2>
    <ol><li>아래 가운데 <b>공유 버튼(□↑)</b> 누르기</li><li><b>「홈 화면에 추가」</b> → 오른쪽 위 <b>추가</b></li></ol>
    홈 화면의 <b>「{{SHORT}}」</b> 아이콘을 누르면 바로 열립니다.
  </div>
  <p class="note">기관 계정(gscsupport.org)으로 로그인해야 열립니다. 이 페이지는 앱으로 넘겨 주기만 하고 아무것도 저장하지 않습니다.</p>
</div>
</body>
</html>
