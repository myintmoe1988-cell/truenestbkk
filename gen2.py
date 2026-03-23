PHONE = "+66994147913"

CONTACT_BTNS = """
<div class="cta-contact">
  <h3>ဆက်သွယ်ရန် / Contact Us</h3>
  <span class="my">မေးမြန်းချင်သည်များ Viber / WhatsApp / Phone မှ ဆက်သွယ်နိုင်ပါသည်</span>
  <div class="contact-btns">
    <a href="viber://chat?number={wp}" class="cbtn cbtn-line">📲 Viber</a>
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

FOOTER = """<footer><p>© 2024–2026 True Nest BKK Service · Bangkok, Thailand &nbsp;|&nbsp; <span class="my">မြန်မာနိုင်ငံသားများအတွက် ဝန်ဆောင်မှု</span></p></footer>"""

JS = """<script>
const nb=document.getElementById('navbar');
window.addEventListener('scroll',()=>nb.classList.toggle('scrolled',scrollY>20));
document.getElementById('navToggle').addEventListener('click',()=>document.getElementById('navLinks').classList.toggle('open'));
document.querySelectorAll('.nav-links a').forEach(a=>a.addEventListener('click',()=>document.getElementById('navLinks').classList.remove('open')));
document.querySelectorAll('.reveal').forEach(el=>new IntersectionObserver((e)=>e.forEach(x=>x.isIntersecting&&x.target.classList.add('visible')),{threshold:0.08}).observe(el));
</script>"""

def make_page(title, my_title, label, back_url, back_label, body_html, filename):
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
<div class="page-hero">
  <div class="page-hero-inner">
    <a href="{back_url}" class="back-btn">← {back_label}</a>
    <div class="page-hero-label">{label}</div>
    <h1>{title}</h1>
    <p class="page-hero-my">{my_title}</p>
  </div>
</div>
<div class="page-content">
{body_html}
{CONTACT_BTNS}
</div>
{FOOTER}
{JS}
</body>
</html>"""
    with open(f"/home/claude/truenest/{filename}", "w") as f:
        f.write(html)
    print(f"✓ {filename}")

def docs(*items):
    li = "".join(f'<li><div class="doc-icon">📄</div><div><strong>{i[0]}</strong><div class="my">{i[1]}</div></div></li>' for i in items)
    return f'<ul class="docs-list">{li}</ul>'

def steps(*items):
    s = "".join(f'<div class="step"><div class="step-left"><div class="step-num">{i+1}</div><div class="step-line"></div></div><div class="step-body"><div class="step-title">{t}</div><div class="step-desc my">{d}</div></div></div>' for i,(t,d) in enumerate(items))
    return f'<div class="steps">{s}</div>'

def info(title, content):
    return f'<div class="info-section reveal"><div class="info-title">{title}</div>{content}</div>'

def alert_warn(txt):
    return f'<div class="alert alert-warn reveal"><div class="al-icon">⚠️</div><div class="al-body"><span class="my">{txt}</span></div></div>'

def alert_info(txt):
    return f'<div class="alert alert-info reveal"><div class="al-icon">ℹ️</div><div class="al-body"><span class="my">{txt}</span></div></div>'

# =================== TR VISA ===================
make_page("TR Visa (Tourist Visa)", "ခရီးသွားဗီဇာ", "Visa Service",
"visa-service.html", "Visa Service သို့ ပြန်သွားရန်", 
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","သက်တမ်း ၆ လ ကျန်ရှိရမည်"),
  ("Passport Copy","ဓာတ်ပုံစာမျက်နှာ Copy"),
  ("ဓာတ်ပုံ 2 ပုံ","ဖြူသော နောက်ခံ၊ 1.5 inch"),
  ("ဘဏ်Statement / ငွေကြေးအထောက်အထား","Bank Statement သို့မဟုတ် Cash ပြနိုင်ရမည်"),
  ("Hotel Booking / တည်းခိုမည့်လိပ်စာ","ထိုင်းမှာ တည်းနေမည့် နေရာ"),
  ("Return Ticket","ပြန်လာမည့် လေကြောင်းလက်မှတ်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပြင်ဆင်ပါ","လိုအပ်သော Documents အားလုံး ဓာတ်ပုံ / Scan ရိုက်ပြီး ပေးပို့ပါ"),
  ("Application ဖြည့်သွင်းပေး","ကျွန်ုပ်တို့မှ TR Visa Application ဖြည့်သွင်းပေးပါမည်"),
  ("Thailand Embassy / Consulate တင်ပေး","သင်နေထိုင်ရာ နိုင်ငံ Thailand Embassy တွင် တင်ပေးပါမည်"),
  ("Visa ထုတ်ပေး","Visa အတည်ဖြစ်ပါက Passport ပြန်ထုတ်ပေးပါမည်")
)) +
alert_info("TR Visa ဖြင့် ထိုင်းသို့ ရောက်ပါက 60 ရက် နေထိုင်ခွင့်ရပြီး ထိုင်းတွင်း Immigration တွင် 30 ရက်ထပ်တိုး (TR Visa Extension) လျှောက်နိုင်ပါသည်။"),
"tr-visa.html")

# =================== DTV VISA ===================
make_page("DTV Visa (Destination Thailand Visa)", "ဒစ်ဂျစ်တယ် ဗီဇာ", "Visa Service",
"visa-service.html", "Visa Service သို့ ပြန်သွားရန်",
alert_info("DTV Visa သည် Remote Worker, Freelancer, Digital Nomad များအတွက် ထိုင်းနိုင်ငံတွင် 180 ရက် (6 လ) နေထိုင်ခွင့်ပေးသော Visa အမျိုးအစားဖြစ်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","သက်တမ်း ၆ လ ကျန်ရှိရမည်"),
  ("ဓာတ်ပုံ","4x6 cm, White background"),
  ("Remote Work အထောက်အထား","Freelance Contract / Employment Letter / Portfolio"),
  ("ဘဏ် Statement","နောက်ဆုံး 3 လ Bank Statement"),
  ("Travel Insurance","180 ရက်အတွက် Insurance"),
  ("ငွေကြေး အထောက်အထား","အနည်းဆုံး 500,000 THB ညီမျှသော ငွေ")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Eligibility စစ်ဆေးပါ","DTV အတွက် သင့်တော်မမတော် ဦးစွာ စစ်ဆေးပေးပါမည်"),
  ("Documents ပြင်ဆင်ပါ","လိုအပ်သော Documents အားလုံး ပြင်ဆင်ပေးပါမည်"),
  ("Online Application တင်ပေး","Thailand e-Visa system မှ တင်ပေးပါမည်"),
  ("DTV Visa ရရှိ","Approval ရပါက e-Visa ထုတ်ပေးပါမည်")
)),
"dtv-visa.html")

# =================== ED VISA ===================
make_page("ED Visa (Education Visa)", "ပညာသင်ဗီဇာ", "Visa Service",
"visa-service.html", "Visa Service သို့ ပြန်သွားရန်",
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","သက်တမ်း ၆ လ ကျန်ရှိရမည်"),
  ("ဓာတ်ပုံ 2 ပုံ","White background"),
  ("ကျောင်းတက်ရောက်ကြောင်း Letter","Thai Language School / Institute မှ Enrollment Letter"),
  ("ကျောင်းတက်ကြောင်း Schedule","Study Schedule / Timetable"),
  ("ကျောင်းလခ ပေးဆောင်မှု အထောက်အထား","Receipt of Tuition Fee")
)) +
alert_warn("ED Visa ဖြင့် ထိုင်းတွင် တရားဝင် ဘာသာစကားသင်ကြားမှသာ ရပါသည်။ အလုပ်လုပ်ကိုင်ရန် Work Permit ထပ်မံ လိုအပ်ပါသည်။") +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကျောင်းရှာပေးပါ","ကိုယ်သင့်တော်သော Thai Language School ရှာပေးပါမည်"),
  ("Documents ပြင်ဆင်","Enrollment Letter နှင့် Documents ပြင်ဆင်ပေးပါမည်"),
  ("Embassy တင်ပေး","ED Visa Application Embassy တင်ပေးပါမည်"),
  ("Visa ရရှိ + ကျောင်းတက်","Visa ရပြီးနောက် 90 ရက် Extension ဆက်ရနိုင်")
)),
"ed-visa.html")

# =================== RETIREMENT VISA ===================
make_page("Retirement Visa", "သက်ကြီးဗီဇာ", "Visa Service",
"visa-service.html", "Visa Service သို့ ပြန်သွားရန်",
alert_info("Retirement Visa သည် အသက် 50 နှင့်အထက် နိုင်ငံခြားသားများ ထိုင်းတွင် တရားဝင် အငြိမ်းစား နေထိုင်ခွင့်ပေးသော Visa ဖြစ်ပါသည်။") +
info("လိုအပ်ချက်များ", docs(
  ("အသက် 50 နှစ်နှင့်အထက်","Passport DOB ဖြင့် သက်သေပြရမည်"),
  ("Passport မူရင်း","သက်တမ်း ၆ လ ကျန်ရှိရမည်"),
  ("ဘဏ် Statement","ထိုင်းဘဏ်တွင် 800,000 THB ရှိရမည် (သို့) တစ်လ 65,000 THB ဝင်ငွေ"),
  ("ကျန်းမာရေး Insurance","Minimum 40,000 THB Outpatient / 400,000 THB Inpatient"),
  ("ဓာတ်ပုံ","4x6 cm, White background"),
  ("Criminal Record","ပြစ်မှုကင်းသော လက်မှတ်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Eligibility စစ်ဆေးပါ","အသက်နှင့် ငွေကြေးစည်းကမ်းများ စစ်ဆေးပေးပါမည်"),
  ("ဘဏ်အကောင့် ဖွင့်ပြီး ငွေသွင်းပါ","800,000 THB ထိုင်းဘဏ်တွင် သိမ်းဆည်းထားရမည်"),
  ("Documents ပြင်ဆင် + Embassy တင်","ကိုယ်စားလှယ် ဆောင်ရွက်ပေးပါမည်"),
  ("Visa ရပြီး နှစ်တိုင်း Extend","တစ်နှစ်တိုင်း Extension လျှောက်နိုင်")
)),
"retirement-visa.html")

# =================== NON-O VISA ===================
make_page("Non-O Visa (Family / Marriage)", "မိသားစု / အိမ်ထောင်ဗီဇာ", "Visa Service",
"visa-service.html", "Visa Service သို့ ပြန်သွားရန်",
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","သက်တမ်း ၆ လ ကျန်ရှိရမည်"),
  ("ဓာတ်ပုံ 2 ပုံ","White background"),
  ("မိသားစု / အိမ်ထောင်ဆက်ဆံမှု အထောက်အထား","Marriage Certificate / Family Book"),
  ("ထိုင်းနိုင်ငံသား Sponsor ၏ Documents","Thai ID / House Registration"),
  ("ဘဏ် Statement","20,000 THB ရှိရမည်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents စစ်ဆေးပေးပါ","ဦးစွာ Documents ပြည့်စုံမှုစစ်ဆေးပေးပါမည်"),
  ("Application ဖြည့်သွင်းပေး","Non-O Visa Application ပြင်ဆင်ပေးပါမည်"),
  ("Embassy / Immigration တင်ပေး","သတ်မှတ်နေရာ တင်ပေးပါမည်"),
  ("Visa ရရှိ + တစ်နှစ် Extension","Non-O ရပြီး 1 Year Extension ဆက်ရနိုင်")
)),
"non-o-visa.html")

# =================== ARRIVAL VISA EXTENSION ===================
make_page("Arrival Visa Extension", "၁၄ ရက်ဗီဇာ သက်တမ်းတိုး", "Immigration / Visa Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_info("Visa Free (14 ရက်) ဖြင့် ဝင်ရောက်ထားသော မြန်မာနိုင်ငံသားများ ၇ ရက် ထပ်တိုး (Extend) ဆောင်ရွက်ပေးနိုင်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","ကုန်မည့်ရက်မတိုင်မီ တင်ရမည်"),
  ("TM6 / Entry Stamp","ဝင်ရောက်ချိန် Immigration Stamp"),
  ("ဓာတ်ပုံ 1 ပုံ","4x6 cm, White background"),
  ("Extension ကြေး","1,900 THB")
)) +
alert_warn("Arrival Extension ကို ၁ ကြိမ်သာ ဆောင်ရွက်နိုင်ပါသည်။ ထပ်မံ နေချင်ပါက TR Visa သို့မဟုတ် အခြား Visa လျှောက်ထားပါ။") +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Passport နှင့် Documents ပေးပို့ပါ","ကုန်မည့်ရက်မတိုင်မီ 2-3 ရက်ကြိုတင် ဆက်သွယ်ပါ"),
  ("ကျွန်ုပ်တို့ Immigration သွားဆောင်ရွက်","Local Immigration Office မှ ကိုယ်စားလှယ် ဆောင်ရွက်ပေးပါမည်"),
  ("Extension Stamp ရရှိ","Passport တွင် 7 ရက်ထပ်တိုး Stamp ထိုးပေးပါမည်")
)),
"arrival-visa-extension.html")

# =================== TR VISA EXTENSION ===================
make_page("TR Visa Extension", "ရက် ၆၀ ဗီဇာ သက်တမ်းတိုး", "Immigration / Visa Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_info("TR Visa ဖြင့် ထိုင်းသို့ ဝင်ရောက်ပြီး 60 ရက်ကုန်မည့်အချိန် ထိုင်းတွင်း Immigration တွင် 30 ရက် ထပ်တိုးနိုင်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","TR Visa Entry Stamp ပါရှိသော Passport"),
  ("TM7 Form","Extension Application Form"),
  ("ဓာတ်ပုံ 1 ပုံ","4x6 cm, White background"),
  ("Extension ကြေး","1,900 THB"),
  ("တည်းနေမည့် လိပ်စာ","Hotel Booking / TM30 Copy")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကုန်မည့်ရက်မတိုင်မီ ဆက်သွယ်ပါ","TR Visa ကုန်မည့် 3-5 ရက်ကြိုတင် ဆက်သွယ်ပါ"),
  ("Documents ပေးပို့ပါ","Passport နှင့် Documents ကြိုတင်ပေးပို့ပါ"),
  ("Immigration ကိုယ်စားလှယ် ဆောင်ရွက်","ကျွန်ုပ်တို့မှ Immigration တွင် ကိုယ်စားဆောင်ရွက်ပေးပါမည်"),
  ("30 ရက် Extension ရရှိ","Passport ပြန်ပေးပို့ပါမည်")
)),
"tr-visa-extension.html")

# =================== OVERSTAY ===================
make_page("Over Stay Assistance", "Overstay ကိုင်တွယ်မှု", "Immigration Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_warn("Overstay ဖြစ်နေပါက ချက်ချင်း ဆောင်ရွက်ရပါမည်။ နောက်ကျလေ ဒဏ်ကြေး ပိုများလေဖြစ်ပါသည်။") +
info("Overstay ဒဏ်ကြေး", docs(
  ("1 ရက်မှ 90 ရက်","တစ်ရက်လျှင် 500 THB"),
  ("90 ရက်ကျော်","တစ်ရက်လျှင် 500 THB + အပိုဆောင်း ဒဏ်"),
  ("အများဆုံး ဒဏ်ကြေး","30,000 THB"),
  ("ပြင်းထန်သော Overstay","ထိုင်းနိုင်ငံ ပြန်ဝင်ပိတ်ပင်ခြင်း ဖြစ်နိုင်")
)) +
info("ကျွန်ုပ်တို့ ဆောင်ရွက်ပေးနိုင်သည်များ", docs(
  ("Overstay ကြေး တွက်ချက်ပေး","ကျသင့်သောကြေး တိကျစွာ တွက်ချက်ပေးပါမည်"),
  ("Immigration ကိုယ်စားဆောင်ရွက်","ဒဏ်ကြေးပေးဆောင်ပြီး ထွက်ခွင့် ဆောင်ရွက်ပေး"),
  ("Voluntary Departure ကူညီ","ပြဿနာမဖြစ်အောင် Voluntary Departure ကူညီပေး"),
  ("နောင်ဗီဇာ စီစဉ်ပေး","Overstay ဖြေရှင်းပြီး နောင်ဗီဇာ ကူညီပေး")
)),
"overstay-assistance.html")

# =================== 90 DAY REPORT ===================
make_page("90-Day Report", "၉၀ ရက် Report", "Immigration Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_info("Long Stay Visa (Non-O, ED, Retirement etc.) ကိုင်ဆောင်သော နိုင်ငံခြားသားများသည် 90 ရက်တစ်ကြိမ် Immigration သို့ Report တင်ရမည်ဖြစ်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","ပြောင်းလဲမှုမရှိသော Passport"),
  ("TM47 Form","90-Day Report Form"),
  ("နောက်ဆုံး Report Slip","ယခင် Report တင်ဖူးပါက Slip"),
  ("TM30 Copy","နေထိုင်ရာ လိပ်စာ ကြေငြာချက်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Report ရက်ကြိုတင် သတိပြုပါ","ကုန်မည့်ရက် 7 ရက်ကြိုတင် ဆောင်ရွက်ပါ"),
  ("Documents ပေးပို့ပါ","Passport နှင့် Documents ကြိုတင်ပေးပို့ပါ"),
  ("Online / Onsite ဆောင်ရွက်","Online Report (ဖြစ်နိုင်သည့်အခါ) သို့မဟုတ် Immigration သွားဆောင်ရွက်ပေးပါမည်"),
  ("Next Report Date ရရှိ","နောင် 90 ရက် Report ရက်ကို အကြောင်းကြားပေးပါမည်")
)),
"90-day-report.html")

# =================== RE-ENTRY ===================
make_page("Re-Entry Permit", "ပြန်ဝင်ခွင့်", "Immigration Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_warn("Long Stay Visa ကိုင်ဆောင်သူများ Re-Entry Permit မထုတ်ဘဲ ထိုင်းမှ ထွက်ပါက Visa ကုန်ဆုံးသွားမည်ဖြစ်ပါသည်။") +
info("Re-Entry Permit အမျိုးအစားများ", docs(
  ("Single Re-Entry","တစ်ကြိမ်သာ ပြန်ဝင်နိုင် · 1,000 THB"),
  ("Multiple Re-Entry","Visa သက်တမ်းအတွင်း အကြိမ်မကန့်သတ် ပြန်ဝင်နိုင် · 3,800 THB")
)) +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","Visa ပါဝင်သော Passport"),
  ("TM8 Form","Re-Entry Permit Form"),
  ("ဓာတ်ပုံ 1 ပုံ","4x6 cm, White background"),
  ("ကြေး 1,000 / 3,800 THB","Single / Multiple")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ခရီးမတက်မီ ဆောင်ရွက်ပါ","ထိုင်းမထွက်ခင် Re-Entry ဦးစွာ ထုတ်ပါ"),
  ("Documents ပေးပို့ပါ","Passport နှင့် ကြေး ပေးပို့ပါ"),
  ("Immigration ဆောင်ရွက်","Immigration Office မှ Re-Entry Stamp ထိုးပေးပါမည်"),
  ("ခရီးထွက်ရန် အဆင်သင့်","Passport ပြန်ပေးပို့ပြီး ချက်ချင်း ထွက်ခွာနိုင်")
)),
"re-entry-permit.html")

# =================== TM30 ===================
make_page("TM30 Notification", "TM30 အိမ်ရှင်ကြေငြာချက်", "Immigration Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_info("နိုင်ငံခြားသားကို တည်းနေခိုင်ကသူ (House Owner / Hotel) သည် ဝင်ရောက်ပြီး 24 နာရီအတွင်း TM30 Immigration သို့ ကြေငြာရမည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("TM30 Form","ကြေငြာချက် Form"),
  ("နိုင်ငံခြားသား Passport Copy","ဝင်ရောက်သူ၏ Passport ဓာတ်ပုံစာမျက်နှာနှင့် Entry Stamp"),
  ("အိမ်ရှင် ID / House Registration","Thailand ID နှင့် Tabien Baan"),
  ("နေထိုင်ရာ လိပ်စာ","တည်နေရာ ပြည့်စုံသော လိပ်စာ")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပေးပို့ပါ","Passport Copy နှင့် အိမ်ရှင် Documents ပေးပို့ပါ"),
  ("Online / Immigration ဆောင်ရွက်","Online TM30 System မှ တင်ပေးပါမည်"),
  ("TM30 Receipt ရရှိ","ကြေငြာပြီးကြောင်း Receipt ပေးပို့ပါမည်")
)),
"tm30-notification.html")

# =================== RESIDENT CERT ===================
make_page("Resident Certificate", "နေထိုင်ကြောင်း အထောက်အထား", "Immigration Service",
"immigration-service.html", "Immigration Service သို့ ပြန်သွားရန်",
alert_info("Resident Certificate သည် ထိုင်းနိုင်ငံ Immigration ထုတ်ပေးသော တရားဝင် နေထိုင်ကြောင်း Certificate ဖြစ်ပြီး ဘဏ်၊ ကားဝယ်ယူခြင်း၊ ယာဉ်မောင်းလိုင်စင် လျှောက်ခြင်းတို့အတွက် လိုအပ်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","Long Stay Visa ပါဝင်ရမည်"),
  ("TM30 Copy","နေထိုင်ရာ လိပ်စာ ကြေငြာချက်"),
  ("ဓာတ်ပုံ 2 ပုံ","4x6 cm, White background"),
  ("ကြေး","200-500 THB ခန့်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပြင်ဆင်ပါ","Long Stay Visa နှင့် TM30 ရှိရမည်"),
  ("Immigration ကိုယ်စားဆောင်ရွက်","ကျွန်ုပ်တို့မှ Immigration Office တွင် ဆောင်ရွက်ပေးပါမည်"),
  ("Certificate ရရှိ","Resident Certificate ထုတ်ပေးပါမည်")
)),
"resident-certificate.html")

# =================== DL CONVERT ===================
make_page("Driving License Convert", "လိုင်စင် ပြောင်းလဲခြင်း", "Driving License Service",
"driving-license-service.html", "Driving License Service သို့ ပြန်သွားရန်",
alert_info("Myanmar Driving License (Category B ပါဝင်ရမည်) ကို Thai Driving License သို့ Convert ပြုလုပ်ပေးသည့် ဝန်ဆောင်မှု။ ဗုဒ္ဓဟူးနေ့တိုင်း DLT Office တွင် ဆောင်ရွက်နိုင်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Myanmar Driving License မူရင်း","Category B ပါဝင်ရမည်၊ သက်တမ်းမကုန်ရ"),
  ("Passport မူရင်း","Long Stay Visa ပါဝင်ရမည် (TR, ED, Non-O, DTV etc.)"),
  ("Visa / Stay သက်တမ်း","Processing ကာလ အထိ Visa ကျန်ရှိရမည်"),
  ("TM30 Copy","နေထိုင်ရာ လိပ်စာ ကြေငြာချက်"),
  ("Resident Certificate","Immigration ထုတ်ပေးသော Certificate"),
  ("ဓာတ်ပုံ 2 ပုံ","4x6 cm, White background"),
  ("Health Certificate","ဆေးဆိုင် / ဆေးရုံမှ ထုတ်ပေးသော ကျန်းမာကြောင်း ထောက်ခံစာ")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents စစ်ဆေးပေးပါ","Myanmar DL နှင့် Documents ပြည့်စုံမှု စစ်ဆေးပေးပါမည်"),
  ("Resident Certificate ထုတ်ပေး","မရှိသေးပါက Immigration မှ ကိုယ်စားထုတ်ပေးပါမည်"),
  ("Health Certificate ပြင်ဆင်ပေး","သင့်ပတ်ဝန်းကျင် ဆေးဆိုင်တွင် ထုတ်ပေးအောင် ကူညီပေးပါမည်"),
  ("DLT Office ကိုယ်စားလှယ်ဆောင်ရွက်","Department of Land Transport တွင် ကိုယ်စားဆောင်ရွက်ပေးပါမည်"),
  ("Thai Driving License ရရှိ","Driving Test (Theory / Practical) ပြီးမှ License ထုတ်ပေးပါမည်")
)),
"driving-license-convert.html")

# =================== DL NEW ===================
make_page("Driving License New", "လိုင်စင် အသစ်ထုတ်ခြင်း", "Driving License Service",
"driving-license-service.html", "Driving License Service သို့ ပြန်သွားရန်",
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Passport မူရင်း","Long Stay Visa ပါဝင်ရမည်"),
  ("Visa / Stay သက်တမ်း","Processing ကာလ ကျန်ရှိရမည်"),
  ("TM30 Copy","နေထိုင်ရာ လိပ်စာ"),
  ("Resident Certificate","Immigration Certificate"),
  ("ဓာတ်ပုံ 2 ပုံ","4x6 cm, White background"),
  ("Health Certificate","ဆေးဆိုင် ထောက်ခံစာ")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပြင်ဆင်","အစ မှ ဆောင်ရွက်ပေးပါမည်"),
  ("Theory Test ကြိုတင်လေ့ကျင့်","Thai DLT Theory Test အတွက် ကြိုတင်ပြင်ဆင်ပေးပါမည်"),
  ("DLT Office ဆောင်ရွက်","Theory Test + Practical Test ဆောင်ရွက်ပေး"),
  ("Thai DL ရရှိ","ပါရမတ်ပြည့်မှ License ထုတ်ပေးပါမည်")
)),
"driving-license-new.html")

# =================== THAI DL RENEW ===================
make_page("Thai Driving License Renew", "ထိုင်းလိုင်စင် သက်တမ်းသစ်", "Driving License Service",
"driving-license-service.html", "Driving License Service သို့ ပြန်သွားရန်",
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Thai Driving License မူရင်း","ကုန်မည့် License"),
  ("Passport မူရင်း","Valid Visa ပါဝင်ရမည်"),
  ("TM30 Copy","နေထိုင်ရာ လိပ်စာ"),
  ("Health Certificate","ဆေးဆိုင် ထောက်ခံစာ"),
  ("ဓာတ်ပုံ 1 ပုံ","4x6 cm, White background")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပေးပို့ပါ","License ကုန်မည့် 1 လကြိုတင် ဆက်သွယ်ပါ"),
  ("DLT Office ဆောင်ရွက်","ကိုယ်စားလှယ် DLT Office တွင် ဆောင်ရွက်ပေးပါမည်"),
  ("Renewed License ရရှိ","License ပြန်ရပြီး ပေးပို့ပါမည်")
)),
"thai-driving-license-renew.html")

# =================== MM DL RENEW ===================
make_page("Myanmar Driving License Renew", "မြန်မာလိုင်စင် သက်တမ်းသစ်", "Driving License Service",
"driving-license-service.html", "Driving License Service သို့ ပြန်သွားရန်",
alert_info("မြန်မာနိုင်ငံ Driving License သက်တမ်းကုန်တော့မည်ဆိုပါက ထိုင်းမှ မြန်မာနိုင်ငံ ပြန်သွားစရာမလိုဘဲ ကိုယ်စားလှယ် ဆောင်ရွက်ပေးနိုင်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("Myanmar DL မူရင်း (Scan/Photo)","ပေးပို့ပါ"),
  ("Passport Copy","NRC နှင့် Passport ဓာတ်ပုံစာမျက်နှာ"),
  ("NRC Card Copy","မြန်မာ မှတ်ပုံတင်"),
  ("မြန်မာ ဆက်သွယ်ရမည့် လိပ်စာ","ရွေးချယ်ပြီး ထိုနေရာ DRD Office ဆောင်ရွက်ပေး")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပေးပို့ပါ","Scan/Photo ဖြင့် ပေးပို့ပါ"),
  ("မြန်မာ Agent မှ ဆောင်ရွက်","မြန်မာနိုင်ငံ DRD Office တွင် ကိုယ်စားဆောင်ရွက်ပေးပါမည်"),
  ("Renewed DL ပေးပို့","မြန်မာ Courier / ပြန်လာသောအခါ ထုတ်ယူနိုင်")
)),
"myanmar-driving-license-renew.html")

# =================== WHEEL TAX ===================
make_page("Thai Vehicle Wheel Tax Renew", "ထိုင်းယာဉ် နှစ်ပတ်လည်ကြေး", "Driving License Service",
"driving-license-service.html", "Driving License Service သို့ ပြန်သွားရန်",
alert_info("ထိုင်းနိုင်ငံ ယာဉ်များ (Car / Motorcycle) တိုင်းသည် နှစ်တစ်နှစ်တစ်ကြိမ် Wheel Tax ပေးဆောင်ရမည်ဖြစ်ပါသည်။") +
info("လိုအပ်သော စာရွက်စာတမ်းများ", docs(
  ("ယာဉ်မှတ်ပုံတင် (Green Book)","Vehicle Registration Book"),
  ("ယာဉ် Insurance Certificate","Compulsory Insurance (CTPL) ရှိရမည်"),
  ("ယာဉ်စစ်ဆေးမှု Certificate (ဖြစ်နိုင်သည့်ယာဉ်)","7 နှစ်ကျော်ယာဉ်များ စစ်ဆေးမှု ဦးစွာ လုပ်ရမည်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("Documents ပေးပို့ပါ","Green Book နှင့် Insurance ပေးပို့ပါ"),
  ("ကြေးတွက်ချက်ပေး","ယာဉ် CC အပေါ်မူတည်၍ ကြေး တိကျစွာ တွက်ချက်ပေးပါမည်"),
  ("DLT / Land Transport ဆောင်ရွက်","ကိုယ်စားလှယ် ကြေးဆောင်ပေးပြီး Sticker ရယူပေးပါမည်"),
  ("Sticker ပေးပို့","ယာဉ်ဇာတ်ထိုးသော Sticker ပေးပို့ပါမည်")
)),
"wheel-tax-renew.html")

# =================== FAST TRACK ===================
make_page("Fast Track Immigration", "Fast Track Immigration", "Airport Service",
"airport-service.html", "Airport Service သို့ ပြန်သွားရန်",
alert_info("Fast Track Immigration ဝန်ဆောင်မှုဖြင့် Immigration လိုင်းတန်းစောင့်ဆိုင်းစရာမလိုဘဲ မြန်ဆန်စွာ ဖြတ်သန်းနိုင်ပါသည်။") +
info("ဝန်ဆောင်မှု ပါဝင်သောအချက်များ", docs(
  ("Immigration Counter Priority","VIP Counter မှ မြန်ဆန်စွာ ဖြတ်သန်းနိုင်"),
  ("Ground Staff လိုက်ပါကူညီ","Airport Staff မှ ဂရုတစိုက် လိုက်ပါကူညီ"),
  ("Arrival နှင့် Departure နှစ်မျိုးစလုံး","Inbound နှင့် Outbound ရနိုင်")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကြိုတင် Book ပါ","ခရီးထွက်မည့် ၂-၃ ရက်ကြိုတင် Book ပါ"),
  ("Flight Details ပေးပို့ပါ","Flight No., Date, Time, Passport Name ပေးပို့ပါ"),
  ("Airport တွင် Staff ကြိုဆိုပေး","ကျွန်ုပ်တို့ Staff သည် Airport တွင် ကြိုဆိုပါမည်"),
  ("Fast Track ဖြင့် ဖြတ်သန်းပြီးပါ","မြန်ဆန်စွာ Immigration ဖြတ်သန်းပြီး Lounge/Gate သွားနိုင်")
)),
"fast-track-immigration.html")

# =================== BUGGY ===================
make_page("Buggy Service (BKK)", "Buggy ဝန်ဆောင်မှု", "Airport Service",
"airport-service.html", "Airport Service သို့ ပြန်သွားရန်",
alert_info("Suvarnabhumi (BKK) လေဆိပ်တွင်း Buggy Cart ဖြင့် Departure / Arrival Gate မှ Immigration / Lounge / Connecting Gate ထိ လိုက်ပို့ပေးသည့် ဝန်ဆောင်မှု၊ သက်ကြီးရွယ်အိုများ၊ မသန်စွမ်းသူများ၊ ကလေးငယ်ပါသော မိသားစုများ အထူး အဆင်ပြေပါသည်။") +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကြိုတင် Book ပါ","ခရီးထွက်မည့် ၂-၃ ရက်ကြိုတင် Book ပါ"),
  ("Flight Details ပေးပို့ပါ","Flight No., Date, Time, Arrival/Departure, Passport Name"),
  ("Buggy Staff ကြိုဆိုပေး","Gate / Arrival Hall တွင် Buggy Staff ကြိုဆိုပေးပါမည်"),
  ("လိုချင်သောနေရာ ရောက်ပါ","Gate မှ Immigration / Lounge / Connecting Gate ထိ ပို့ပေးပါမည်")
)),
"buggy-service.html")

# =================== BKK VIP ===================
make_page("Bangkok Airport VIP Pass", "ဘန်ကောက်လေဆိပ် VIP Pass", "Airport Service",
"airport-service.html", "Airport Service သို့ ပြန်သွားရန်",
info("ဝန်ဆောင်မှု ပါဝင်သောအချက်များ", docs(
  ("Suvarnabhumi (BKK) VIP Lounge","Premium Lounge ဝင်ခွင့် · အစားအသောက် Free"),
  ("Don Mueang (DMK) VIP Lounge","DMK Lounge ဝင်ခွင့်"),
  ("Fast Track Immigration","VIP Counter ဖြင့် မြန်ဆန်စွာ ဖြတ်သန်း"),
  ("Baggage Assistance","Baggage Cart / Porter ဝန်ဆောင်မှု")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကြိုတင် Book ပါ","ခရီးထွက်မည့် ၃ ရက်ကြိုတင် Book ပါ"),
  ("Flight Details ပေးပို့ပါ","Flight No., Date, Departure/Arrival, Passport Name, Pax Count"),
  ("Confirmation ရပြီး Airport သွားပါ","e-Voucher / Confirmation ထုတ်ပေးပါမည်"),
  ("VIP Service ခံစားပါ","Lounge နှင့် Fast Track ဝန်ဆောင်မှု ခံစားနိုင်")
)),
"bangkok-airport-vip.html")

# =================== YANGON VIP ===================
make_page("Yangon Airport VIP Pass", "ရန်ကုန်လေဆိပ် VIP Pass", "Airport Service",
"airport-service.html", "Airport Service သို့ ပြန်သွားရန်",
info("ဝန်ဆောင်မှု ပါဝင်သောအချက်များ", docs(
  ("Yangon International Airport VIP Lounge","Premium Lounge ဝင်ခွင့်"),
  ("Fast Track Immigration (Arrival/Departure)","VIP Lane ဖြင့် မြန်ဆန်စွာ ဖြတ်သန်း"),
  ("Meet & Greet","Airport Staff ကြိုဆိုပေး"),
  ("Baggage Assistance","Luggage ကိုင်ဆောင်ပေးသည့် ဝန်ဆောင်မှု")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကြိုတင် Book ပါ","ခရီးမတက်မီ ၃-၅ ရက်ကြိုတင် Book ပါ"),
  ("Flight Details ပေးပို့ပါ","Flight No., Date, Arrival/Departure, Passport Name"),
  ("Confirmation ရပြီး ခရီးထွက်ပါ","e-Voucher ထုတ်ပေးပါမည်"),
  ("Airport တွင် VIP Service ခံစားပါ","Meet & Greet + Lounge + Fast Track ဝန်ဆောင်မှု")
)),
"yangon-airport-vip.html")

# =================== KL VIP ===================
make_page("Kuala Lumpur Airport VIP Pass", "ကွာလာလမ်ပူ လေဆိပ် VIP Pass", "Airport Service",
"airport-service.html", "Airport Service သို့ ပြန်သွားရန်",
info("ဝန်ဆောင်မှု ပါဝင်သောအချက်များ", docs(
  ("KLIA / KLIA2 VIP Lounge","Kuala Lumpur International Airport Lounge ဝင်ခွင့်"),
  ("Fast Track Immigration","VIP Lane ဖြင့် Immigration မြန်ဆန်စွာ ဖြတ်သန်း"),
  ("Transit Assistance","KL Transit ဖြင့် ဆက်လက်ခရီးသွားသူများ ကူညီ")
)) +
info("ဝန်ဆောင်မှု အဆင့်များ", steps(
  ("ကြိုတင် Book ပါ","ခရီးမတက်မီ ၃-၅ ရက်ကြိုတင် Book ပါ"),
  ("Flight Details ပေးပို့ပါ","Flight No., Date, KLIA or KLIA2, Passport Name"),
  ("Confirmation ရပြီး ခရီးထွက်ပါ","e-Voucher ထုတ်ပေးပါမည်")
)),
"kl-airport-vip.html")

# =================== BANK PAGES ===================
bank_types = [
  ("bank-non-b.html","Non-B Visa ကိုင်ဆာင်သူ ဘဏ်အကောင့်","Non-B Visa (Work Permit) Holder","Work Permit ကိုင်ဆောင်သောကြောင့် ထိုင်းဘဏ်တွင် အကောင့် ဖွင့်ရန် အဆင်ပြေဆုံး Visa အမျိုးအစားဖြစ်ပါသည်",
    [("Passport မူရင်း","Non-B Visa ပါဝင်ရမည်"),("Work Permit မူရင်း","တရားဝင် Work Permit"),("Employer Letter","ကုမ္ပဏီထောက်ခံစာ"),("ဓာတ်ပုံ","4x6 cm"),("ကနဦး ငွေသွင်းငွေ","ဘဏ်အပေါ်မူတည်")]),
  ("bank-retirement.html","Retirement Visa ကိုင်ဆာင်သူ ဘဏ်အကောင့်","Retirement Visa Holder","Retirement Visa ကိုင်ဆောင်သူများ ထိုင်းဘဏ်တွင် အကောင့်ဖွင့်ရာ၌ 800,000 THB ငွေသွင်းလိုအပ်ပါသည်",
    [("Passport မူရင်း","Retirement Visa ပါဝင်ရမည်"),("ဓာတ်ပုံ","4x6 cm"),("ကနဦး ငွေသွင်းငွေ","800,000 THB (Retirement Visa အတည်ဖြစ်ရန်)")]),
  ("bank-non-o.html","Non-O Visa ကိုင်ဆာင်သူ ဘဏ်အကောင့်","Non-O (Marriage/Family) Visa Holder","Non-O Visa ကိုင်ဆောင်သောကြောင့် ထိုင်းဘဏ်တွင် အကောင့် ဖွင့်နိုင်ပါသည်",
    [("Passport မူရင်း","Non-O Visa ပါဝင်ရမည်"),("Marriage Certificate / Family Document","Thai Sponsor Documents"),("TM30 Copy","နေထိုင်ရာ လိပ်စာ"),("ဓာတ်ပုံ","4x6 cm")]),
  ("bank-non-la.html","Non-LA Visa ကိုင်ဆာင်သူ ဘဏ်အကောင့်","Non-LA Visa Holder","Non-LA Visa ကိုင်ဆောင်သောကြောင့် ထိုင်းဘဏ်တွင် အကောင့် ဖွင့်နိုင်ပါသည်",
    [("Passport မူရင်း","Non-LA Visa ပါဝင်ရမည်"),("TM30 Copy","နေထိုင်ရာ လိပ်စာ"),("ဓာတ်ပုံ","4x6 cm"),("Resident Certificate","Immigration Certificate")]),
  ("bank-pink-card.html","ပန်းရောင်ကဒ် / CI ကိုင်ဆာင်သူ ဘဏ်အကောင့်","Pink Card / CI Card Holder","ထိုင်းပန်းရောင်ကဒ် (Thailand Alien Registration Card) သို့မဟုတ် CI ကိုင်ဆောင်သူများ ထိုင်းဘဏ်တွင် အကောင့် ဖွင့်နိုင်ပါသည်",
    [("Pink Card မူရင်း / CI မူရင်း","Alien Registration Card"),("Passport (ရှိပါက)","မြန်မာ Passport သို့မဟုတ် ခရီးသွားစာအုပ်"),("TM30 Copy","နေထိုင်ရာ လိပ်စာ"),("ဓာတ်ပုံ","4x6 cm")]),
]

for fname, title, my_title, description, doc_items in bank_types:
    bdocs = docs(*doc_items)
    bsteps = steps(
      ("Documents စစ်ဆေးပေးပါ","Visa / Card နှင့် Documents ပြည့်စုံမှု စစ်ဆေးပေးပါမည်"),
      ("ဘဏ် ရွေးချယ်ပေးပါ","KBank, Bangkok Bank, SCB စသည် သင့်တော်သော ဘဏ် ညှိပေးပါမည်"),
      ("ဘဏ် ကိုယ်စားလှယ်ဆောင်ရွက်","ဘဏ်သွားပြီး Account ဖွင့်ပေးပါမည်"),
      ("Bank Account ရရှိ","Account Number, ATM Card ရရှိပြီး သုံးနိုင်")
    )
    make_page(title, my_title, "Bank Account Service",
      "bank-account-service.html", "Bank Account Service သို့ ပြန်သွားရန်",
      alert_info(description) + info("လိုအပ်သော စာရွက်စာတမ်းများ", bdocs) + info("ဝန်ဆောင်မှု အဆင့်များ", bsteps),
      fname)

print("\n✅ All detail pages generated!")
