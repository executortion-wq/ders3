from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# Backend API URL
API_URL = "https://ders3.onrender.com"

HTML = """
<!doctype html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Ziyaretçi Defteri</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
        h1 { color: #333; }
        form { margin-bottom: 25px; }
        input {
            padding: 10px;
            font-size: 16px;
            border-radius: 6px;
            border: 1px solid #ccc;
            margin: 5px;
        }
        button {
            padding: 10px 15px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        button:hover { background: #45a049; }
        li {
            background: white;
            margin: 5px auto;
            width: 260px;
            padding: 8px;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Mikro Hizmetli Selam!</h1>
    <p>Adını ve şehrini yaz:</p>

    <form method="POST">
        <input type="text" name="isim" placeholder="Adını yaz" required>
        <input type="text" name="sehir" placeholder="Şehrini yaz" required>
        <button type="submit">Gönder</button>
    </form>

    <h3>Ziyaretçiler:</h3>
    <ul>
    {% for ad in isimler %}
        <li>{{ ad }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
if request.method == "POST":
    isim = request.form.get("isim")
    sehir = request.form.get("sehir")
    try:
        r = requests.post(API_URL, json={"isim": isim, "sehir": sehir})
        print("POST status:", r.status_code, r.text)  # <- burası debug
    except Exception as e:
        print("POST isteğinde hata:", e)
    return redirect("/")

    try:
        resp = requests.get(API_URL)
        isimler = resp.json() if resp.status_code == 200 else []
    except Exception as e:
        print("GET isteğinde hata:", e)
        isimler = []

    return render_template_string(HTML, isimler=isimler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
