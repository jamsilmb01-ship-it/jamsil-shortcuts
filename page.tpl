<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{SHORT}}</title>
<meta name="apple-mobile-web-app-title" content="{{SHORT}}">
<meta name="application-name" content="{{SHORT}}">
<meta name="theme-color" content="{{COLOR}}">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="manifest" href="manifest.json">
<script>
  // 홈 화면 아이콘으로 열면(?open) 바로 앱으로. 설치 안내로 열면 주소에 ?open 을 붙여 두어 아이폰 「홈 화면에 추가」도 ?open 으로 저장되게
  var APP = '{{URL}}';
  // 카카오톡 안 브라우저는 홈 화면 추가 · 설치가 없음 → 카카오톡의 「외부 브라우저로 열기」로 크롬 · 사파리에서 다시 연다
  var UA = navigator.userAgent || '';
  var KAKAO = /KAKAOTALK/i.test(UA);
  var INAPP = KAKAO || /NAVER\(inapp|Instagram|FBAN|FBAV|Line\/|DaumApps|everytimeApp/i.test(UA);
  if (KAKAO && !/[?&]open\b/.test(location.search)) location.href = 'kakaotalk://web/openExternal?url=' + encodeURIComponent(location.origin + location.pathname);
  else if (/[?&]open\b/.test(location.search)) location.replace(APP);
  else if (history.replaceState && !INAPP) history.replaceState(null, '', location.pathname + '?open');
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(function () { });
</script>
<style>
  body { font-family: -apple-system, "Malgun Gothic", "Apple SD Gothic Neo", sans-serif; margin: 0; background: #f4f6f9; color: #1f2933; }
  .wrap { max-width: 460px; margin: 0 auto; padding: 24px 18px 40px; text-align: center; }
  .steps { display: flex; justify-content: center; gap: 8px; margin-bottom: 16px; font-size: 13px; }
  .steps span { padding: 4px 12px; border-radius: 999px; background: #e3e8ee; color: #5b6773; }
  .steps span.on { background: {{COLOR}}; color: #fff; font-weight: 700; }
  .steps span.done { background: #c8ead6; color: #1c6b3d; }
  img.ic { width: 104px; height: 104px; border-radius: 24px; box-shadow: 0 4px 14px rgba(0,0,0,.15); }
  h1 { font-size: 23px; margin: 12px 0 4px; }
  .sub { color: #5b6773; font-size: 14px; margin: 0 0 18px; }
  button.go, a.go { display: block; width: 100%; box-sizing: border-box; background: {{COLOR}}; color: #fff; border: 0; text-decoration: none; font-weight: 700; font-size: 18px; padding: 15px; border-radius: 12px; cursor: pointer; }
  a.next { display: block; margin-top: 10px; padding: 13px; border-radius: 12px; border: 2px solid {{COLOR}}; color: {{COLOR}}; font-weight: 700; text-decoration: none; }
  .how { text-align: left; background: #fff; border: 1px solid #dde3ea; border-radius: 12px; padding: 12px 16px; margin-top: 16px; font-size: 14.5px; line-height: 1.6; }
  .how h2 { font-size: 15px; margin: 4px 0 2px; }
  .how ol { margin: 0 0 6px; padding-left: 20px; }
  .ok { color: #1c6b3d; font-weight: 700; margin-top: 10px; }
  .note { color: #7b8794; font-size: 12.5px; margin-top: 14px; }
  .inapp { background: #fff4d6; border: 1px solid #f0c36a; color: #6b4b00; border-radius: 12px; padding: 12px 14px; font-size: 14.5px; line-height: 1.6; margin-bottom: 16px; text-align: left; }
  [hidden] { display: none !important; }
</style>
</head>
<body>
<div class="wrap">
  <div class="steps"><span class="{{S1}}">① 나에안식</span><span class="{{S2}}">② 차량일지</span></div>
  <div class="inapp" id="inapp" hidden>⚠️ 지금은 <b>카카오톡 · 다른 앱 안</b>에서 열려 있어 설치가 안 돼요.<br>오른쪽 위(또는 아래) <b>⋮ · … 메뉴 → 「다른 브라우저로 열기」</b>를 눌러 <b>크롬(아이폰은 사파리)</b>에서 열어 주세요.</div>
  <img class="ic" src="icon-192.png" alt="">
  <h1>{{SHORT}}</h1>
  <p class="sub">{{TITLE}}</p>
  <button type="button" class="go" id="inst" hidden>📲 홈 화면에 설치</button>
  <div class="ok" id="done" hidden>✅ 설치했어요!</div>
  <a class="next" href="{{NEXT}}">{{NEXTLABEL}}</a>
  <div class="how" id="manual">
    <h2>📱 버튼이 안 보이면 (아이폰 · 다른 브라우저)</h2>
    <ol>
      <li>아이폰 사파리: 아래 가운데 <b>공유(□↑)</b> → <b>「홈 화면에 추가」</b> → <b>추가</b></li>
      <li>안드로이드: 오른쪽 위 <b>⋮</b> → <b>「홈 화면에 추가」</b>(또는 「앱 설치」)</li>
    </ol>
    그다음 위의 <b>{{NEXTLABEL}}</b>을 누르세요.
  </div>
  <p class="note">기관 계정(gscsupport.org)으로 로그인해야 열립니다. 이 페이지는 앱으로 넘겨 주기만 하고 아무것도 저장하지 않습니다.</p>
</div>
<script>
  // 안드로이드 크롬: 설치 버튼 한 번으로 홈 화면에 (브라우저가 허락할 때만 버튼이 보임). 설치되면 다음 단계로
  if (INAPP) document.getElementById('inapp').hidden = false;   // 카카오톡이 외부 브라우저로 못 넘겼거나 다른 앱 안일 때
  var ask = null;
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); ask = e; document.getElementById('inst').hidden = false; });
  document.getElementById('inst').onclick = function () {
    if (!ask) return;
    ask.prompt();
    ask.userChoice.then(function (c) { if (c && c.outcome === 'accepted') installed(); ask = null; document.getElementById('inst').hidden = true; });
  };
  window.addEventListener('appinstalled', installed);
  function installed() {
    document.getElementById('done').hidden = false;
    {{AFTER}}
  }
</script>
</body>
</html>
