from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# De strakke HTML & CSS code voor je website
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Deals Central</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        h1 { color: #38bdf8; text-align: center; margin-bottom: 5px; }
        p.subtitle { text-align: center; color: #94a3b8; margin-bottom: 30px; font-size: 0.95rem; }
        .card { background-color: #1e293b; border-radius: 12px; padding: 20px; margin-bottom: 16px; border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .title { font-size: 1.2rem; font-weight: bold; color: #f1f5f9; margin-bottom: 10px; }
        .price-box { margin-bottom: 15px; }
        .price { color: #4ade80; font-weight: bold; font-size: 1.2rem; }
        .savings { background-color: #065f46; color: #a7f3d0; padding: 4px 8px; border-radius: 6px; font-size: 0.85rem; margin-left: 8px; font-weight: bold; }
        .btn { display: inline-block; padding: 10px 18px; background-color: #0284c7; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 0.9rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔥 Game Deals Central</h1>
        <p class="subtitle">De allerbeste game-kortingen live op een rij!</p>
        
        {% for deal in deals %}
        <div class="card">
            <div class="title">🎮 {{ deal.title }}</div>
            <div class="price-box">
                <span class="price">€{{ deal.salePrice }}</span>
                <span class="savings">{{ deal.savings }}% KORTING</span>
            </div>
            <a href="https://www.cheapshark.com/redirect?dealID={{ deal.dealID }}" target="_blank" class="btn">Bekijk Deal op Webshop ➔</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    url = "https://www.cheapshark.com/api/1.0/deals?upperPrice=15&pageSize=10&sortBy=Savings"
    headers = {"User-Agent": "MyGameDealWebApp/1.0"}
    
    try:
        response = requests.get(url, headers=headers)
        deals = response.json()
        if not isinstance(deals, list):
            deals = []
        for deal in deals:
            deal['savings'] = round(float(deal.get('savings', 0)), 1)
    except Exception:
        deals = []
        
    return render_template_string(HTML_TEMPLATE, deals=deals)

if __name__ == '__main__':
    # Start de webserver op je telefoon
    app.run(host='0.0.0.0', port=5000)
