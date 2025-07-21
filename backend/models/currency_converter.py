# models/currency_converter.py

class CurrencyConverter:
    """
    A model representing a currency conversion request.

    This class encapsulates the amount to convert, the base currency,
    and the target currency. It provides a method to perform the conversion
    using a supplied exchange rate, along with methods to access internal state.
    """

    def __init__(self, amount: float, base: str, target: str):
        """
        Initialize the CurrencyConverter instance.

        Args:
            amount (float): The amount of money to convert.
            base (str): The base currency code (e.g., 'USD').
            target (str): The target currency code (e.g., 'EUR').

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.__amount = amount
        self.__base = base.upper()
        self.__target = target.upper()

    def convert(self, rate: float) -> float:
        """
        Perform the currency conversion.

        Args:
            rate (float): The conversion rate from base to target.

        Returns:
            float: The converted amount in the target currency.

        Raises:
            ValueError: If the conversion rate is not positive.
        """
        if rate <= 0:
            raise ValueError("Conversion rate must be positive.")
        return self.__amount * rate

    def get_amount(self) -> float:
        """
        Get the amount to be converted.

        Returns:
            float: The base amount.
        """
        return self.__amount

    def get_base_currency(self) -> str:
        """
        Get the base currency code.

        Returns:
            str: The base currency code in uppercase.
        """
        return self.__base

    def get_target_currency(self) -> str:
        """
        Get the target currency code.

        Returns:
            str: The target currency code in uppercase.
        """
        return self.__target

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Returns:
            str: Debug string with internal state details.
        """
        return (
            f"<CurrencyConverter(amount={self.__amount}, "
            f"base='{self.__base}', target='{self.__target}')>"
        )

    def __str__(self) -> str:
        """
        User-friendly string representation.

        Returns:
            str: Description of the currency conversion.
        """
        return f"Convert {self.__amount} {self.__base} to {self.__target}"
