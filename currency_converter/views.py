from django.http import JsonResponse, HttpRequest
import requests
from typing import Any, Dict

_API_KEY: str = "nB8QLUu4FfhsF1YyNnuqOQrrFZLMUMP0"


def convert_currency(request: HttpRequest) -> JsonResponse:
    from_currency: str = request.GET.get('from', 'USD')
    to_currency: str = request.GET.get('to', 'RUB')
    value: float = float(request.GET.get('value', '1'))

    url: str = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={value}"

    headers: Dict[str, str] = {
        "apikey": _API_KEY
    }

    response: requests.Response = requests.get(url, headers=headers)
    response_data: Dict[str, Any] = response.json()

    if response_data.get('success'):
        conversion_result: float = response_data.get('result', 0.0)
        return JsonResponse({"result": conversion_result})
    else:
        return JsonResponse({"error": "Failed to convert currency."}, status=400)