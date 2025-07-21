from backend.models.currency_converter import CurrencyConverter
from backend.services.api_service import CurrencyAPIService


class MainController:
    """
    Controller class that handles the interaction between the UI and backend services.
    """

    def __init__(self, ui):
        """
        Initializes the MainController.

        Args:
            ui: The UI object responsible for rendering and user interaction.
        """
        self.ui = ui
        self.api_service = CurrencyAPIService()

    def convert_currency(self, amount: str, base: str, target: str):
        """
        Handles the currency conversion logic.

        Args:
            amount: The amount to convert (as a string, from user input).
            base: The base currency code.
            target: The target currency code.
        """
        try:
            if not amount.strip():
                raise ValueError("Please enter an amount to convert.")

            if base == target:
                raise ValueError("Please select different currencies for conversion.")

            amount_float = float(amount)
            if amount_float <= 0:
                raise ValueError("Amount must be greater than zero.")

            # Get conversion rate
            rate = self.api_service.get_conversion_rate(base, target)

            # Perform conversion
            converter = CurrencyConverter(amount_float, base, target)
            result = converter.convert(rate)

            # Update result in UI
            self.ui.update_result(result)

        except ValueError as ve:
            self.ui.show_error(str(ve))
        except Exception as e:
            self.ui.show_error(f"Conversion failed: {str(e)}")

    def swap_currencies(self):
        """
        Delegates the swap logic to the UI layer, which manages combobox selection and icon updates.
        """
        try:
            self.ui.swap_currencies()
        except Exception as e:
            self.ui.show_error(f"Swap failed: {e}")
