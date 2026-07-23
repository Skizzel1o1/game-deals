import requests

# Zoek naar top-deals over alle winkels
url = "https://www.cheapshark.com/api/1.0/deals?upperPrice=15&pageSize=5&sortBy=Savings"

# Unieke User-Agent vereist door CheapShark
headers = {
    "User-Agent": "MyGameDealBot/1.0 (mydealapp@example.com)"
}

try:
    response = requests.get(url, headers=headers)
    deals = response.json()

    print("\n--- TOP GAME DEALS GEVONDEN ---\n")

    if isinstance(deals, list) and len(deals) > 0:
        for deal in deals:
            title = deal.get('title', 'Onbekende titel')
            price = deal.get('salePrice', '0.00')
            savings = round(float(deal.get('savings', 0)), 1)
            
            print(f"🎮 {title}")
            print(f"💰 Actieprijs: €{price} ({savings}% korting)")
            print("-" * 35)
    else:
        print("Geen deals ontvangen. Respons:")
        print(deals)

except Exception as e:
    print(f"Er is iets misgegaan: {e}")
