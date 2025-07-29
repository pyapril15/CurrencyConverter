import requests


class CurrencyAPIService:
    BASE_URL = "http://api.currencylayer.com/"
    ACCESS_KEY = "8e94aaf91fcf03463376934065298cbf"

    def get_conversion_rate(self, base: str, target: str) -> float:
        url = self.BASE_URL + "live"
        params = {'access_key': self.ACCESS_KEY, 'source': base, 'currencies': target, 'format': 1}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        key = base + target
        if key in data['quotes']:
            return data['quotes'][key]
        else:
            raise ValueError(f"Conversion rate for {base} to {target} not found.")
