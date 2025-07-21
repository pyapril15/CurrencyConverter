# models/currency_manager.py

import base64
import json
import os
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Currency:
    """
    Represents a currency with its metadata.

    Attributes:
        code (str): ISO 4217 currency code (e.g., 'USD').
        name (str): Full name of the currency (e.g., 'US Dollar').
        country (str): Country using the currency.
        country_code (str): ISO 3166 country code (e.g., 'US').
        flag_base64 (str): Base64-encoded image of the flag.
    """

    code: str
    name: str
    country: str
    country_code: str
    flag_base64: str

    def get_flag_bytes(self) -> bytes:
        """
        Returns the flag image in raw bytes format.

        Returns:
            bytes: Decoded image bytes.
        """
        try:
            if self.flag_base64.startswith("data:image"):
                return base64.b64decode(self.flag_base64.split(",", 1)[1])
            return base64.b64decode(self.flag_base64)
        except Exception as e:
            raise ValueError(f"Failed to decode base64 flag for {self.code}: {e}")

    def __repr__(self) -> str:
        return (
            f"<Currency(code='{self.code}', name='{self.name}', "
            f"country='{self.country}', country_code='{self.country_code}')>"
        )


class CurrencyManager:
    """
    Manages the loading and access of currency data from a JSON file.
    """

    def __init__(
            self,
            json_path: str = os.path.join(
                os.path.dirname(__file__), "..", "data", "currencies_with_flags.json"
            )
    ):
        """
        Initialize CurrencyManager and load currencies from JSON.

        Args:
            json_path (str): Path to the currency JSON file.
        """
        self.__json_path = os.path.abspath(json_path)
        self.__currencies: List[Currency] = []
        self.__load_currencies()

    def __load_currencies(self):
        """
        Load currency data from the JSON file.

        Raises:
            FileNotFoundError: If the JSON file is not found.
            ValueError: If JSON parsing fails or format is invalid.
        """
        if not os.path.exists(self.__json_path):
            raise FileNotFoundError(f"Currency JSON file not found: {self.__json_path}")

        try:
            with open(self.__json_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.__currencies = [
                    Currency(
                        code=item["code"],
                        name=item["name"],
                        country=item["country"],
                        country_code=item["countryCode"],
                        flag_base64=item.get("flag", ""),
                    )
                    for item in data
                ]
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to parse currency JSON: {e}")

    def get_currency_list(self) -> List[tuple[str, str, str]]:
        """
        Get a simplified list of currencies for UI display.

        Returns:
            List[tuple[str, str, str]]: A list of (flag_base64, code, name).
        """
        return [(c.flag_base64, c.code, c.name) for c in self.__currencies]

    def get_all_currencies(self) -> List[Currency]:
        """
        Get the full list of Currency objects.

        Returns:
            List[Currency]: List of Currency dataclass instances.
        """
        return self.__currencies.copy()

    def find_currency_by_code(self, code: str) -> Optional[Currency]:
        """
        Find a currency by its code.

        Args:
            code (str): The currency code to search for.

        Returns:
            Currency or None: The matching Currency, or None if not found.
        """
        code = code.upper()
        return next((c for c in self.__currencies if c.code == code), None)

    def __repr__(self) -> str:
        return f"<CurrencyManager(currencies_loaded={len(self.__currencies)})>"
