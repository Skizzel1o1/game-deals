from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Map van winkel-ID's van CheapShark naar winkelnamen
STORES = {
    '1': 'Steam',
    '7': 'GOG',
    '11': 'Humble Store',
    '25': 'Epic Games'
}

@app.route('/')
def index():
    # Parameters ophalen uit de zoekbalk / filters
    search_query = request.args.get('q', '').strip()
    filter_free = request.args.get('free', '0')
    store_id = request.args.get('store', '')

    url = 'https://www.cheapshark.com/api/1.0/deals'
    params = {
        'pageSize': 30,
        'sortBy': 'Savings'
    }

    if search_query:
        params['title'] = search_query

    if filter_free == '1':
        params['upperPrice'] = 0

    if store_id:
        params['storeID'] = store_id

    try:
        response = requests.get(url, params=params, timeout=5)
        raw_deals = response.json() if response.status_code == 200 else []
    except Exception:
        raw_deals = []

    deals = []
    for d in raw_deals:
        deals.append({
            'title': d.get('title', 'Onbekende game'),
            'price': d.get('salePrice', '0.00'),
            'normal_price': d.get('normalPrice'),
            'savings': float(d.get('savings', 0)),
            'thumb': d.get('thumb', ''),
            'link': f"https://www.cheapshark.com/redirect?dealID={d.get('dealID')}",
            'store': STORES.get(str(d.get('storeID')), 'Webshop')
        })

    return render_template(
        'index.html', 
        deals=deals, 
        search_query=search_query, 
        filter_free=filter_free, 
        store_id=store_id
    )

if __name__ == '__main__':
    app.run(debug=True)
    
