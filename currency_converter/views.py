import requests
from typing import Dict, Any

_API_KEY = "nB8QLUu4FfhsF1YyNnuqOQrrFZLMUMP0"

def get_currency_conversion(to_currency: str, from_currency: str, amount: float) -> Dict[str, Any]:
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {
        "apikey": _API_KEY
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()

    return response_data

# Test the function
if __name__ == "__main__":
    result = get_currency_conversion("RUB", "USD", 1.0)
    print("Conversion Result:", result)