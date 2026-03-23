import os

PHONE = "+66994147913"
CONTACT_BTNS = """
<div class="cta-contact">
  <h3>ဆက်သွယ်ရန် / Contact Us</h3>
  <span class="my">မေးမြန်းချင်သည်များ Viber / WhatsApp / Phone မှ ဆက်သွယ်နိုင်ပါသည်</span>
  <div class="contact-btns">
    <a href="viber://chat?number={p}" class="cbtn cbtn-line">📲 Viber</a>
    <a href="https://wa.me/{wp}" class="cbtn cbtn-wa">💬 WhatsApp</a>
    <a href="tel:{p}" class="cbtn cbtn-phone">📞 {p}</a>
  </div>
</div>""".format(p=PHONE, wp=PHONE.replace("+",""))

NAV = """<nav id="navbar">
  <a href="index.html" class="nav-logo">
    <div class="logo-icon">🏠</div>
    <div class="logo-text"><strong>True Nest BKK</strong><span>Service · Bangkok</span></div>
  </a>
  <ul class="nav-links" id="navLinks">
    <li><a href="index.html#services">Services</a></li>
    <li><a href="index.html#about">About Us</a></li>
    <li><a href="index.html#contact">Contact</a></li>
    <li><a href="tel:{p}" class="nav-cta">📞 ဆက်သွယ်ရန်</a></li>
  </ul>
  <button class="nav-toggle" id="navToggle"><span></span><span></span><span></span></button>
</nav>""".format(p=PHONE)

FOOTER = """<footer>
  <p>© 2024–2026 True Nest BKK Service · Bangkok, Thailand &nbsp;|&nbsp; <span class="my">မြန်မာနိုင်ငံသားများအတွက် ဝန်ဆောင်မှု</span></p>
</footer>"""

JS = """<script>
const nb=document.getElementById('navbar');
window.addEventListener('scroll',()=>nb.classList.toggle('scrolled',scrollY>20));
document.getElementById('navToggle').addEventListener('click',()=>document.getElementById('navLinks').classList.toggle('open'));
document.querySelectorAll('.nav-links a').forEach(a=>a.addEventListener('click',()=>document.getElementById('navLinks').classList.remove('open')));
document.querySelectorAll('.reveal').forEach(el=>new IntersectionObserver((e)=>e.forEach(x=>x.isIntersecting&&x.target.classList.add('visible')),{threshold:0.08}).observe(el));
</script>"""

def page(title, my_title, body, filename):
    html = f"""<!DOCTYPE html>
<html lang="my">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} | True Nest BKK Service</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
{NAV}
{body}
{FOOTER}
{JS}
</body>
</html>"""
    with open(f"/home/claude/truenest/{filename}", "w") as f:
        f.write(html)
    print(f"✓ {filename}")

# ===================== INDEX =====================
index_body = """
<section style="min-height:100vh;background:var(--navy);position:relative;overflow:hidden;display:flex;align-items:center;padding:100px 40px 60px;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 75% 30%,rgba(200,151,58,0.11) 0%,transparent 60%),radial-gradient(circle,rgba(200,151,58,0.04) 1px,transparent 1px);background-size:auto,30px 30px;"></div>
  <div style="max-width:1100px;margin:0 auto;width:100%;position:relative;z-index:1;">
    <div style="display:inline-flex;align-items:center;gap:8px;background:rgba(200,151,58,0.12);border:1px solid rgba(200,151,58,0.3);color:#E8B860;padding:6px 16px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-bottom:24px;animation:fadeUp 0.5s both;">
      <span style="width:6px;height:6px;background:var(--gold);border-radius:50%;display:inline-block;"></span>Bangkok · Thailand · Est. 2024
    </div>
    <h1 style="font-family:'Playfair Display',serif;font-size:clamp(30px,4.5vw,54px);color:#fff;line-height:1.18;margin-bottom:10px;animation:fadeUp 0.5s 0.08s both;">Your Trusted <em style="font-style:normal;color:#E8B860;">Service Partner</em><br>in Bangkok</h1>
    <p style="font-family:'Noto Sans Myanmar',sans-serif;font-size:16px;color:rgba(255,255,255,0.5);margin-bottom:20px;animation:fadeUp 0.5s 0.14s both;">ဘန်ကောက်မှာ သင်လိုအပ်တာအားလုံး ကျွန်ုပ်တို့ကို အပ်နှံပါ</p>
    <p style="color:rgba(255,255,255,0.6);font-size:14px;max-width:520px;margin-bottom:36px;line-height:1.8;animation:fadeUp 0.5s 0.2s both;"><span style="font-family:'Noto Sans Myanmar',sans-serif;">Visa, Immigration, Driving License, Airport VIP Pass နှင့် Bank Account ဝန်ဆောင်မှုများကို မြန်မာ Expert Team မှ ကူညီဆောင်ရွက်ပေးပါသည်</span></p>
    <div style="display:flex;gap:14px;flex-wrap:wrap;animation:fadeUp 0.5s 0.26s both;">
      <a href="#services" style="display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,var(--gold),#a07030);color:#fff;padding:13px 26px;border-radius:8px;font-weight:600;font-size:14px;text-decoration:none;box-shadow:0 4px 16px rgba(200,151,58,0.35);">🔍 ဝန်ဆောင်မှုများ ကြည့်ရန်</a>
      <a href="tel:""" + PHONE + """" style="display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(255,255,255,0.25);color:rgba(255,255,255,0.85);padding:13px 26px;border-radius:8px;font-weight:500;font-size:14px;text-decoration:none;">📞 """ + PHONE + """</a>
    </div>
  </div>
</section>

<section id="services" style="padding:80px 40px;background:var(--off-white);">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:52px;" class="reveal">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;">Our Services</div>
      <div style="font-family:'Playfair Display',serif;font-size:clamp(24px,3vw,36px);color:var(--navy);margin-bottom:6px;">ဝန်ဆောင်မှု အမျိုးအစားများ</div>
      <p style="font-family:'Noto Sans Myanmar',sans-serif;font-size:14px;color:var(--text-light);max-width:500px;margin:0 auto;">ထိုင်းနိုင်ငံတွင် လိုအပ်သော ဝန်ဆောင်မှုအားလုံးကို တစ်နေရာထဲမှ ဆောင်ရွက်ပေးပါသည်</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;">

      <a href="visa-service.html" class="svc-card reveal">
        <div class="svc-card-icon">🛂</div>
        <div class="svc-card-body">
          <div class="svc-card-title">Visa Service</div>
          <div class="svc-card-my">ဗီဇာ ဝန်ဆောင်မှု</div>
          <div class="svc-card-desc"><span class="my">TR · DTV · ED · Retirement · Non-O · Visa Extension</span></div>
        </div>
        <div class="svc-card-arrow">→</div>
      </a>

      <a href="immigration-service.html" class="svc-card reveal">
        <div class="svc-card-icon">📋</div>
        <div class="svc-card-body">
          <div class="svc-card-title">Immigration Service</div>
          <div class="svc-card-my">Immigration ဝန်ဆောင်မှု</div>
          <div class="svc-card-desc"><span class="my">90-Day · Re-Entry · TM30 · Overstay · Resident Certificate</span></div>
        </div>
        <div class="svc-card-arrow">→</div>
      </a>

      <a href="driving-license-service.html" class="svc-card reveal">
        <div class="svc-card-icon">🚗</div>
        <div class="svc-card-body">
          <div class="svc-card-title">Driving License Service</div>
          <div class="svc-card-my">ယာဉ်မောင်းလိုင်စင် ဝန်ဆောင်မှု</div>
          <div class="svc-card-desc"><span class="my">Convert · New · Renew · Wheel Tax Renew</span></div>
        </div>
        <div class="svc-card-arrow">→</div>
      </a>

      <a href="airport-service.html" class="svc-card reveal">
        <div class="svc-card-icon">✈️</div>
        <div class="svc-card-body">
          <div class="svc-card-title">Airport Service</div>
          <div class="svc-card-my">လေဆိပ် VIP ဝန်ဆောင်မှု</div>
          <div class="svc-card-desc"><span class="my">Fast Track · Buggy · BKK · Yangon · KL Airport VIP</span></div>
        </div>
        <div class="svc-card-arrow">→</div>
      </a>

      <a href="bank-account-service.html" class="svc-card reveal">
        <div class="svc-card-icon">🏦</div>
        <div class="svc-card-body">
          <div class="svc-card-title">Bank Account Service</div>
          <div class="svc-card-my">ဘဏ်အကောင့် ဝန်ဆောင်မှု</div>
          <div class="svc-card-desc"><span class="my">Non-B · Retirement · Non-O · Non-LA · ပန်းရောင်ကဒ် / CI</span></div>
        </div>
        <div class="svc-card-arrow">→</div>
      </a>

    </div>
  </div>
</section>

<section id="about" style="padding:80px 40px;background:var(--white);">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;" class="reveal">
    <div style="background:linear-gradient(135deg,var(--navy),var(--navy3));border-radius:20px;padding:36px;">
      <div style="display:flex;flex-direction:column;gap:18px;">
        <div style="display:flex;gap:14px;align-items:flex-start;"><div style="width:38px;height:38px;background:rgba(200,151,58,0.15);border:1px solid rgba(200,151,58,0.25);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;">🇲🇲</div><div><div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:2px;">မြန်မာနိုင်ငံသားများ ကိုင်တွယ်</div><div style="font-family:'Noto Sans Myanmar',sans-serif;font-size:11px;color:rgba(255,255,255,0.4);">Managed by Burmese Team</div></div></div>
        <div style="display:flex;gap:14px;align-items:flex-start;"><div style="width:38px;height:38px;background:rgba(200,151,58,0.15);border:1px solid rgba(200,151,58,0.25);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;">📍</div><div><div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:2px;">Bangkok အခြေစိုက်</div><div style="font-family:'Noto Sans Myanmar',sans-serif;font-size:11px;color:rgba(255,255,255,0.4);">Based in Bangkok, Thailand</div></div></div>
        <div style="display:flex;gap:14px;align-items:flex-start;"><div style="width:38px;height:38px;background:rgba(200,151,58,0.15);border:1px solid rgba(200,151,58,0.25);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;">📱</div><div><div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:2px;">Viber · WhatsApp · Phone</div><div style="font-family:'Noto Sans Myanmar',sans-serif;font-size:11px;color:rgba(255,255,255,0.4);">24/7 ဆက်သွယ်နိုင်</div></div></div>
        <div style="display:flex;gap:14px;align-items:flex-start;"><div style="width:38px;height:38px;background:rgba(200,151,58,0.15);border:1px solid rgba(200,151,58,0.25);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;">🔒</div><div><div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:2px;">ယုံကြည်မှုနှင့် လုံခြုံမှု</div><div style="font-family:'Noto Sans Myanmar',sans-serif;font-size:11px;color:rgba(255,255,255,0.4);">Trusted & Secure Service</div></div></div>
      </div>
    </div>
    <div>
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;">About Us</div>
      <div style="font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,34px);color:var(--navy);margin-bottom:8px;">ကျွန်ုပ်တို့အကြောင်း</div>
      <p style="font-family:'Noto Sans Myanmar',sans-serif;font-size:14px;color:var(--text-light);line-height:1.9;margin-bottom:14px;">True Nest BKK Service သည် ထိုင်းနိုင်ငံ ဘန်ကောက်တွင် နေထိုင်သော မြန်မာနိုင်ငံသားများအတွက် Visa, Immigration, Driving License, Airport VIP Pass နှင့် Bank Account ဝန်ဆောင်မှုများ ဆောင်ရွက်ပေးနေသော ဝန်ဆောင်မှုအဖွဲ့ ဖြစ်ပါသည်။</p>
      <p style="font-family:'Noto Sans Myanmar',sans-serif;font-size:14px;color:var(--text-light);line-height:1.9;">ထိုင်းနိုင်ငံ၏ ဥပဒေ၊ ဆောင်ရွက်နည်းများနှင့် မြန်မာ Customer များ၏ လိုအပ်ချက်ကို နားလည်ကာ တိကျမြန်ဆန်သော ဝန်ဆောင်မှု ပေးနေပါသည်။</p>
    </div>
  </div>
</section>

<section id="contact" style="padding:80px 40px;background:var(--off-white);">
  <div style="max-width:700px;margin:0 auto;text-align:center;" class="reveal">
    <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:10px;">Contact</div>
    <div style="font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,34px);color:var(--navy);margin-bottom:8px;">ဆက်သွယ်ရန်</div>
    """ + CONTACT_BTNS + """
  </div>
</section>
"""

page("True Nest BKK Service", "ဝန်ဆောင်မှုများ", index_body, "index.html")

# ===================== VISA SERVICE =====================
visa_body = """
<div class="page-hero">
  <div class="page-hero-inner">
    <a href="index.html" class="back-btn">← ပြန်သွားရန်</a>
    <div class="page-hero-label">Visa Service</div>
    <h1>Visa Service</h1>
    <p class="page-hero-my">ဗီဇာ ဝန်ဆောင်မှု</p>
    <p class="page-hero-desc my">ထိုင်းနိုင်ငံတွင် တရားဝင် ဆက်လက်နေထိုင်နိုင်ရေးအတွက် Visa အမျိုးအစားအားလုံး ကူညီဆောင်ရွက်ပေးပါသည်</p>
  </div>
</div>
<div class="page-content">
  <div class="service-list">
    <a href="tr-visa.html" class="svc-card reveal"><div class="svc-card-icon">🛂</div><div class="svc-card-body"><div class="svc-card-title">TR Visa (Tourist Visa)</div><div class="svc-card-my">ခရီးသွားဗီဇာ</div><div class="svc-card-desc my">60 ရက် + 30 ရက် Extension ရနိုင်သော Tourist Visa</div></div><div class="svc-card-arrow">→</div></a>
    <a href="dtv-visa.html" class="svc-card reveal"><div class="svc-card-icon">💻</div><div class="svc-card-body"><div class="svc-card-title">DTV Visa (Destination Thailand)</div><div class="svc-card-my">ဒစ်ဂျစ်တယ် ဗီဇာ</div><div class="svc-card-desc my">180 ရက် နေထိုင်ခွင့် Remote Worker / Digital Nomad အတွက်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="ed-visa.html" class="svc-card reveal"><div class="svc-card-icon">🎓</div><div class="svc-card-body"><div class="svc-card-title">ED Visa (Education Visa)</div><div class="svc-card-my">ပညာသင်ဗီဇာ</div><div class="svc-card-desc my">ဘာသာစကား သို့မဟုတ် ကျောင်းတက်ရောက်မှုအတွက် ဗီဇာ</div></div><div class="svc-card-arrow">→</div></a>
    <a href="retirement-visa.html" class="svc-card reveal"><div class="svc-card-icon">🧓</div><div class="svc-card-body"><div class="svc-card-title">Retirement Visa</div><div class="svc-card-my">သက်ကြီးဗီဇာ</div><div class="svc-card-desc my">အသက် ၅၀ နှင့်အထက် တရားဝင် ထိုင်းတွင် နေထိုင်ရန်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="non-o-visa.html" class="svc-card reveal"><div class="svc-card-icon">👨‍👩‍👧</div><div class="svc-card-body"><div class="svc-card-title">Non-O Visa (Family / Marriage)</div><div class="svc-card-my">မိသားစု / အိမ်ထောင်ဗီဇာ</div><div class="svc-card-desc my">ထိုင်းနိုင်ငံသားနှင့် အိမ်ထောင်ပြုသူ သို့မဟုတ် မိသားစု ပေါင်းစည်းရန်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="arrival-visa-extension.html" class="svc-card reveal"><div class="svc-card-icon">📅</div><div class="svc-card-body"><div class="svc-card-title">Arrival Visa Extension</div><div class="svc-card-my">၁၄ ရက်ဗီဇာ သက်တမ်းတိုး</div><div class="svc-card-desc my">Visa Free ဖြင့် ဝင်ရောက်သူများ ၇ ရက် ထပ်တိုးနိုင်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="tr-visa-extension.html" class="svc-card reveal"><div class="svc-card-icon">🔄</div><div class="svc-card-body"><div class="svc-card-title">TR Visa Extension</div><div class="svc-card-my">ရက် ၆၀ ဗီဇာ သက်တမ်းတိုး</div><div class="svc-card-desc my">TR Visa ကုန်ဆုံးမည့်အချိန် 30 ရက် ထပ်တိုးနိုင်</div></div><div class="svc-card-arrow">→</div></a>
  </div>
  """ + CONTACT_BTNS + """
</div>
"""
page("Visa Service", "ဗီဇာ ဝန်ဆောင်မှု", visa_body, "visa-service.html")

# ===================== IMMIGRATION SERVICE =====================
imm_body = """
<div class="page-hero">
  <div class="page-hero-inner">
    <a href="index.html" class="back-btn">← ပြန်သွားရန်</a>
    <div class="page-hero-label">Immigration Service</div>
    <h1>Immigration Service</h1>
    <p class="page-hero-my">Immigration ဝန်ဆောင်မှု</p>
    <p class="page-hero-desc my">ထိုင်း Immigration နှင့် ပတ်သက်သော လုပ်ငန်းစဉ်များကို ကိုယ်စားလှယ် ဆောင်ရွက်ပေးပါသည်</p>
  </div>
</div>
<div class="page-content">
  <div class="service-list">
    <a href="arrival-visa-extension.html" class="svc-card reveal"><div class="svc-card-icon">📅</div><div class="svc-card-body"><div class="svc-card-title">Arrival Visa Extension</div><div class="svc-card-my">၁၄ ရက်ဗီဇာ သက်တမ်းတိုး</div><div class="svc-card-desc my">Visa Free 14 ရက်ကုန်မည့်အချိန် 7 ရက်ထပ်တိုး ဆောင်ရွက်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="tr-visa-extension.html" class="svc-card reveal"><div class="svc-card-icon">🔄</div><div class="svc-card-body"><div class="svc-card-title">TR Visa Extension</div><div class="svc-card-my">ရက် ၆၀ ဗီဇာ သက်တမ်းတိုး</div><div class="svc-card-desc my">TR Visa 30 ရက် ထပ်တိုးနိုင်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="overstay-assistance.html" class="svc-card reveal"><div class="svc-card-icon">⚠️</div><div class="svc-card-body"><div class="svc-card-title">Over Stay Assistance</div><div class="svc-card-my">Overstay ကိုင်တွယ်မှု</div><div class="svc-card-desc my">Overstay ဖြစ်နေသူများအတွက် ဒဏ်ကြေးပေးသွင်း ဆောင်ရွက်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="90-day-report.html" class="svc-card reveal"><div class="svc-card-icon">📝</div><div class="svc-card-body"><div class="svc-card-title">90-Day Report</div><div class="svc-card-my">၉၀ ရက် Report</div><div class="svc-card-desc my">တရားဝင် နေထိုင်သူများ ၉၀ ရက်တိုင်း Report တင်ရမည့် ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
    <a href="re-entry-permit.html" class="svc-card reveal"><div class="svc-card-icon">🔁</div><div class="svc-card-body"><div class="svc-card-title">Re-Entry Permit</div><div class="svc-card-my">ပြန်ဝင်ခွင့်</div><div class="svc-card-desc my">ထိုင်းမှ ထွက်ပြီး ပြန်ဝင်ရာတွင် Visa မပျက်ရန် Re-Entry ထုတ်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="tm30-notification.html" class="svc-card reveal"><div class="svc-card-icon">🏠</div><div class="svc-card-body"><div class="svc-card-title">TM30 Notification</div><div class="svc-card-my">TM30 အိမ်ရှင်ကြေငြာချက်</div><div class="svc-card-desc my">နေထိုင်ရာ လိပ်စာ Immigration သို့ တရားဝင် ကြေငြာခြင်း</div></div><div class="svc-card-arrow">→</div></a>
    <a href="resident-certificate.html" class="svc-card reveal"><div class="svc-card-icon">📜</div><div class="svc-card-body"><div class="svc-card-title">Resident Certificate</div><div class="svc-card-my">နေထိုင်ကြောင်း အထောက်အထား</div><div class="svc-card-desc my">ထိုင်းတွင် တရားဝင် နေထိုင်ကြောင်း Immigration Certificate ထုတ်ပေး</div></div><div class="svc-card-arrow">→</div></a>
  </div>
  """ + CONTACT_BTNS + """
</div>
"""
page("Immigration Service", "Immigration ဝန်ဆောင်မှု", imm_body, "immigration-service.html")

# ===================== DRIVING LICENSE SERVICE =====================
dl_body = """
<div class="page-hero">
  <div class="page-hero-inner">
    <a href="index.html" class="back-btn">← ပြန်သွားရန်</a>
    <div class="page-hero-label">Driving License Service</div>
    <h1>Driving License Service</h1>
    <p class="page-hero-my">ယာဉ်မောင်းလိုင်စင် ဝန်ဆောင်မှု</p>
    <p class="page-hero-desc my">မြန်မာ Driving License မှ ထိုင်း Driving License သို့ Convert ပြုလုပ်ပေးသည့်အပြင် အသစ်ထုတ်ရန်နှင့် သက်တမ်းသစ်ရန် ဝန်ဆောင်မှုများ ဆောင်ရွက်ပေးပါသည်</p>
  </div>
</div>
<div class="page-content">
  <div class="service-list">
    <a href="driving-license-convert.html" class="svc-card reveal"><div class="svc-card-icon">🔄</div><div class="svc-card-body"><div class="svc-card-title">Driving License Convert</div><div class="svc-card-my">လိုင်စင် ပြောင်းလဲခြင်း</div><div class="svc-card-desc my">Myanmar DL မှ Thai DL သို့ Convert ပြုလုပ်ပေးသည့် ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
    <a href="driving-license-new.html" class="svc-card reveal"><div class="svc-card-icon">🆕</div><div class="svc-card-body"><div class="svc-card-title">Driving License New</div><div class="svc-card-my">လိုင်စင် အသစ်ထုတ်ခြင်း</div><div class="svc-card-desc my">ထိုင်း Driving License အသစ် လျှောက်ထားပေးသည့် ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
    <a href="thai-driving-license-renew.html" class="svc-card reveal"><div class="svc-card-icon">♻️</div><div class="svc-card-body"><div class="svc-card-title">Thai Driving License Renew</div><div class="svc-card-my">ထိုင်းလိုင်စင် သက်တမ်းသစ်</div><div class="svc-card-desc my">ထိုင်း Driving License သက်တမ်းကုန်မည့်အချိန် ပြန်သစ်ပေးသည့် ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
    <a href="myanmar-driving-license-renew.html" class="svc-card reveal"><div class="svc-card-icon">🇲🇲</div><div class="svc-card-body"><div class="svc-card-title">Myanmar Driving License Renew</div><div class="svc-card-my">မြန်မာလိုင်စင် သက်တမ်းသစ်</div><div class="svc-card-desc my">Myanmar DL သက်တမ်းကုန်မည့်အချိန် ကိုယ်စားလှယ် ပြန်သစ်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="wheel-tax-renew.html" class="svc-card reveal"><div class="svc-card-icon">🏷️</div><div class="svc-card-body"><div class="svc-card-title">Thai Vehicle Wheel Tax Renew</div><div class="svc-card-my">ထိုင်းယာဉ် နှစ်ပတ်လည်ကြေး</div><div class="svc-card-desc my">ထိုင်းနိုင်ငံ ယာဉ်များ နှစ်ပတ်လည် Wheel Tax သစ်ပေးသည့် ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
  </div>
  """ + CONTACT_BTNS + """
</div>
"""
page("Driving License Service", "ယာဉ်မောင်းလိုင်စင် ဝန်ဆောင်မှု", dl_body, "driving-license-service.html")

# ===================== AIRPORT SERVICE =====================
airport_body = """
<div class="page-hero">
  <div class="page-hero-inner">
    <a href="index.html" class="back-btn">← ပြန်သွားရန်</a>
    <div class="page-hero-label">Airport Service</div>
    <h1>Airport Service</h1>
    <p class="page-hero-my">လေဆိပ် VIP ဝန်ဆောင်မှု</p>
    <p class="page-hero-desc my">Bangkok, Yangon, Kuala Lumpur လေဆိပ်များတွင် VIP Fast Track ဝန်ဆောင်မှုများ ကြိုတင်စီစဉ်ပေးပါသည်</p>
  </div>
</div>
<div class="page-content">
  <div class="service-list">
    <a href="fast-track-immigration.html" class="svc-card reveal"><div class="svc-card-icon">⚡</div><div class="svc-card-body"><div class="svc-card-title">Fast Track Immigration</div><div class="svc-card-my">Fast Track Immigration</div><div class="svc-card-desc my">Immigration လိုင်းတန်းမနေဘဲ မြန်ဆန်စွာ ဖြတ်သန်းနိုင်သော ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
    <a href="buggy-service.html" class="svc-card reveal"><div class="svc-card-icon">🛺</div><div class="svc-card-body"><div class="svc-card-title">Buggy Service (BKK)</div><div class="svc-card-my">Buggy ဝန်ဆောင်မှု (ဘန်ကောက်)</div><div class="svc-card-desc my">Suvarnabhumi လေဆိပ်တွင်း Buggy Cart ဖြင့် လိုက်ပို့ပေးသည့် ဝန်ဆောင်မှု</div></div><div class="svc-card-arrow">→</div></a>
    <a href="bangkok-airport-vip.html" class="svc-card reveal"><div class="svc-card-icon">🇹🇭</div><div class="svc-card-body"><div class="svc-card-title">Bangkok Airport VIP Pass</div><div class="svc-card-my">ဘန်ကောက်လေဆိပ် VIP Pass</div><div class="svc-card-desc my">Suvarnabhumi နှင့် Don Mueang လေဆိပ် VIP Lounge ဝင်ခွင့်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="yangon-airport-vip.html" class="svc-card reveal"><div class="svc-card-icon">🇲🇲</div><div class="svc-card-body"><div class="svc-card-title">Yangon Airport VIP Pass</div><div class="svc-card-my">ရန်ကုန်လေဆိပ် VIP Pass</div><div class="svc-card-desc my">ရန်ကုန် International Airport VIP Lounge ဝင်ခွင့်</div></div><div class="svc-card-arrow">→</div></a>
    <a href="kl-airport-vip.html" class="svc-card reveal"><div class="svc-card-icon">🇲🇾</div><div class="svc-card-body"><div class="svc-card-title">Kuala Lumpur Airport VIP Pass</div><div class="svc-card-my">ကွာလာလမ်ပူ လေဆိပ် VIP Pass</div><div class="svc-card-desc my">KLIA / KLIA2 VIP Lounge ဝင်ခွင့် ကြိုတင်စီစဉ်</div></div><div class="svc-card-arrow">→</div></a>
  </div>
  """ + CONTACT_BTNS + """
</div>
"""
page("Airport Service", "လေဆိပ် VIP ဝန်ဆောင်မှု", airport_body, "airport-service.html")

# ===================== BANK ACCOUNT SERVICE =====================
bank_body = """
<div class="page-hero">
  <div class="page-hero-inner">
    <a href="index.html" class="back-btn">← ပြန်သွားရန်</a>
    <div class="page-hero-label">Bank Account Service</div>
    <h1>Bank Account Service</h1>
    <p class="page-hero-my">ဘဏ်အကောင့် ဝန်ဆောင်မှု</p>
    <p class="page-hero-desc my">ထိုင်းနိုင်ငံတွင် ဘဏ်အကောင့် ဖွင့်ရာတွင် လိုအပ်သော Documents ပြင်ဆင်မှုနှင့် လိုက်ပါဆောင်ရွက်ပေးသည့် ဝန်ဆောင်မှု</p>
  </div>
</div>
<div class="page-content">
  <div class="alert alert-info reveal"><div class="al-icon">ℹ️</div><div class="al-body"><strong>မှတ်ချက် :</strong> <span class="my">ထိုင်းဘဏ်များသည် Visa အမျိုးအစားအပေါ် မူတည်၍ Bank Account ဖွင့်ခွင့် ကွဲပြားပါသည်။ သင့် Visa အမျိုးအစားနှင့် ကိုက်ညီသော ဝန်ဆောင်မှုကို ရွေးချယ်ပါ။</span></div></div>
  <div class="service-list">
    <a href="bank-non-b.html" class="svc-card reveal"><div class="svc-card-icon">💼</div><div class="svc-card-body"><div class="svc-card-title">Non-B Visa ကိုင်ဆောင်သူ</div><div class="svc-card-my">Work Permit / Non-B Visa Holder</div><div class="svc-card-desc my">Non-B Visa နှင့် Work Permit ကိုင်ဆောင်သူများ ဘဏ်အကောင့် ဖွင့်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="bank-retirement.html" class="svc-card reveal"><div class="svc-card-icon">🧓</div><div class="svc-card-body"><div class="svc-card-title">Retirement Visa ကိုင်ဆောင်သူ</div><div class="svc-card-my">Retirement Visa Holder</div><div class="svc-card-desc my">Retirement Visa ကိုင်ဆောင်သူများ ဘဏ်အကောင့် ဖွင့်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="bank-non-o.html" class="svc-card reveal"><div class="svc-card-icon">👨‍👩‍👧</div><div class="svc-card-body"><div class="svc-card-title">Non-O Visa ကိုင်ဆောင်သူ</div><div class="svc-card-my">Non-O Visa Holder</div><div class="svc-card-desc my">Non-O (Marriage / Family) Visa ကိုင်ဆောင်သူများ ဘဏ်အကောင့် ဖွင့်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="bank-non-la.html" class="svc-card reveal"><div class="svc-card-icon">📋</div><div class="svc-card-body"><div class="svc-card-title">Non-LA Visa ကိုင်ဆောင်သူ</div><div class="svc-card-my">Non-LA Visa Holder</div><div class="svc-card-desc my">Non-LA Visa ကိုင်ဆောင်သူများ ဘဏ်အကောင့် ဖွင့်ပေး</div></div><div class="svc-card-arrow">→</div></a>
    <a href="bank-pink-card.html" class="svc-card reveal"><div class="svc-card-icon">🪪</div><div class="svc-card-body"><div class="svc-card-title">ပန်းရောင်ကဒ် / CI ကိုင်ဆောင်သူ</div><div class="svc-card-my">Pink Card / CI Card Holder</div><div class="svc-card-desc my">ထိုင်း ပန်းရောင်ကဒ် (Pink Card) သို့မဟုတ် CI ကိုင်ဆောင်သူများ ဘဏ်အကောင့် ဖွင့်ပေး</div></div><div class="svc-card-arrow">→</div></a>
  </div>
  """ + CONTACT_BTNS + """
</div>
"""
page("Bank Account Service", "ဘဏ်အကောင့် ဝန်ဆောင်မှု", bank_body, "bank-account-service.html")

print("\nAll category pages done!")
