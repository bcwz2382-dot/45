from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>🌿 أذكار وأدعية - Khalifa</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        transition: background 0.5s, color 0.5s;
    }
    body.light {
        background: #f7f3f0;
        color: #333;
    }
    body.dark {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .container {
        max-width: 900px;
        margin: auto;
        padding: 20px;
        text-align: center;
    }
    h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    .box {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s;
    }
    .box:hover {
        transform: scale(1.02);
    }
    .zekr {
        margin: 12px 0;
        line-height: 1.8;
        font-size: 1.1em;
    }
    button {
        background: #ffcc00;
        border: none;
        padding: 8px 15px;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        margin: 5px;
        transition: background 0.3s;
    }
    button:hover { background: #e6b800; }
    footer {
        margin-top: 40px;
        padding: 15px;
        font-size: 14px;
        opacity: 0.9;
    }
    .toggle-theme {
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 10px 15px;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
        background: #ffcc00;
    }
</style>
</head>
<body class="light">
<div class="toggle-theme" onclick="toggleTheme()">🌙/☀️</div>
<div class="container">
<h1>🌿 أذكار وأدعية يومية</h1>
<p>صدقة جارية لكل من نشر هذا الرابط 🌟</p>

<div class="box">
<h2>☀️ أذكار الصباح</h2>
<div class="zekr">أصبحنا وأصبح الملك لله والحمد لله وهو على كل شيء قدير 
<button onclick="copyText(this)">نسخ</button></div>
<div class="zekr">اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك النشور 
<button onclick="copyText(this)">نسخ</button></div>
<div class="zekr">حسبي الله لا إله إلا هو عليه توكلت وهو رب العرش العظيم (7 مرات)
<button onclick="copyText(this)">نسخ</button></div>
</div>

<div class="box">
<h2>🌙 أذكار المساء</h2>
<div class="zekr">أمسينا وأمسى الملك لله والحمد لله وهو على كل شيء قدير
<button onclick="copyText(this)">نسخ</button></div>
<div class="zekr">اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت وإليك المصير
<button onclick="copyText(this)">نسخ</button></div>
<div class="zekr">أعوذ بكلمات الله التامات من شر ما خلق (3 مرات)
<button onclick="copyText(this)">نسخ</button></div>
</div>

<div class="box">
<h2>🤲 أدعية مختارة</h2>
<div class="zekr">اللهم ارزقني رزقًا طيبًا واسعًا مباركًا فيه
<button onclick="copyText(this)">نسخ</button></div>
<div class="zekr">اللهم اشف مرضانا ومرضى المسلمين
<button onclick="copyText(this)">نسخ</button></div>
<div class="zekr">رب اشرح لي صدري ويسر لي أمري
<button onclick="copyText(this)">نسخ</button></div>
</div>

<div class="box">
<h2>📿 عداد تسبيح</h2>
<p>عدد التسبيحات: <span id="counter">0</span></p>
<button onclick="incrementCounter()">🔄 سبح</button>
<button onclick="resetCounter()">♻️ إعادة</button>
</div>

<footer>
© جميع الحقوق محفوظة — تصميم وبرمجة: KHA.7
<br>
صدقة جارية — انشر الرابط وادخل الأجر 🌟
</footer>
</div>

<script>
function copyText(btn){
    navigator.clipboard.writeText(btn.parentElement.textContent.replace('نسخ',''));
    alert('تم نسخ الذكر ✅');
}

let counter = 0;
function incrementCounter(){
    counter++;
    document.getElementById('counter').textContent = counter;
}
function resetCounter(){
    counter = 0;
    document.getElementById('counter').textContent = counter;
}

function toggleTheme(){
    document.body.classList.toggle('dark');
    document.body.classList.toggle('light');
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)
