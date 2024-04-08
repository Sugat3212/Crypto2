import requests

def get_new_crypto_pairs(api_key):
    base_url = "https://public-api.birdeye.so"  # Adjust the base URL as needed
    endpoint = "/defi/tokenlist"  # Endpoint for fetching crypto pairs

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    params = {
        "sort": "newly_added",  # Sort by newly added pairs
        "liquidity": "high",  # Filter by high liquidity
        "limit": 10  # Adjust the limit as desired
    }


    try:
        response = requests.get(f"{base_url}{endpoint}", headers=headers, params=params)
        response_data = response.json()

        if "data" in response_data:
            new_pairs = response_data["data"]
            for pair in new_pairs:
                print(f"Pair: {pair['name']} ({pair['symbol']})")
                print(f"Price: {pair['price']}")
                print(f"24h Volume: {pair['volume_24h']}")
                print("-" * 30)
        else:
            print("No data found for new crypto pairs.")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    api_key = "12f5f5656e734628830b8a78f0598867"  # Replace with your actual API key
    get_new_crypto_pairs(api_key)
