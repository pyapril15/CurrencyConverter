import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

from backend.models.currency_manager import CurrencyManager
from frontend.components.menubar import MainMenuBar
from frontend.components.modern_combobox import ModernCombobox
from frontend.components.tooltip import ToolTip
from frontend.components.widget import (
    ModernLabel,
    ModernEntry,
    ModernButton,
    KeyButton,
)


class MainWindow(tk.Tk):
    """
    Main application window for the Currency Converter.
    """

    def __init__(self, controller=None):
        super().__init__()
        self._controller = controller
        self.title("Currency Converter")
        self.geometry("360x620")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        # Set icon if available
        try:
            self.iconbitmap("assets/icon/currency-converter.ico")
        except:
            pass  # Icon not found, continue without it

        self.amount_entry = None
        self.result_entry = None
        self.base_currency_combo = None
        self.target_currency_combo = None

        cm = CurrencyManager()
        self.currency_list = cm.get_currency_list()  # [(flag, code, name), ...]

        self._build_ui()
        self._bind_keyboard_events()

    def set_controller(self, value):
        """Sets the controller for this window."""
        self._controller = value

    def _build_ui(self):
        """Builds all UI components."""
        MainMenuBar(self, controller=self._controller)

        header_frame = tk.Frame(self, bg="#f0f0f0")
        header_frame.pack(fill="x")

        try:
            logo_img = Image.open("assets/images/currency.png").resize((80, 80))
            logo = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(header_frame, image=logo, bg="#f0f0f0")
            logo_label.image = logo
            logo_label.pack()
        except Exception:
            tk.Label(header_frame, text="[Logo Missing]", bg="#f0f0f0").pack()

        tk.Label(
            header_frame,
            text="Currency Converter",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        ).pack(pady=(5, 10))

        converter_frame = tk.Frame(self, bd=2, relief="flat")
        converter_frame.pack(fill="both", expand=True, padx=20, pady=5)

        for i in range(4):
            converter_frame.rowconfigure(i, weight=1, uniform="row")
        converter_frame.columnconfigure(0, weight=1, uniform="col")
        converter_frame.columnconfigure(1, weight=2, uniform="col")
        converter_frame.columnconfigure(2, weight=0)

        self._currency_row(converter_frame, "From", 0)
        self._currency_row(converter_frame, "To", 2)

        try:
            swap_img = Image.open("assets/images/switch.png").resize((32, 32))
            swap_icon = ImageTk.PhotoImage(swap_img)
        except Exception:
            swap_icon = None

        swap_btn = tk.Button(
            converter_frame,
            image=swap_icon,
            bg="#f0f0f0",
            bd=0,
            command=self._swap_currencies,
            cursor="hand2"
        )
        swap_btn.image = swap_icon
        swap_btn.grid(row=1, column=2, rowspan=2, padx=(5, 10), pady=5, sticky="ns")
        ToolTip(swap_btn, text="Swap currencies")

        keypad_border = tk.Frame(self, bg="#fff", bd=0)
        keypad_border.pack(fill="both", expand=True, padx=10, pady=(5, 0))

        keypad_frame = tk.Frame(keypad_border, bg="#f0f0f0")
        keypad_frame.pack(fill="both", expand=True, padx=2, pady=2)

        btn_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0', 'Clear']

        for r in range(4):
            keypad_frame.rowconfigure(r, weight=1, uniform="row")
        for c in range(3):
            keypad_frame.columnconfigure(c, weight=1, uniform="col")

        for idx, val in enumerate(btn_values):
            action = self._insert_digit if val != 'Clear' else self._clear_fields
            btn = KeyButton(keypad_frame, text=val, command=lambda v=val: action(v))
            btn.grid(row=idx // 3, column=idx % 3, sticky="nsew", padx=3, pady=3)
            ToolTip(btn, text=f"Insert '{val}'" if val != "Clear" else "Clear the fields")

        footer_frame = tk.Frame(self, bg="#f0f0f0")
        footer_frame.pack(fill="x", pady=10)

        convert_btn = ModernButton(
            footer_frame,
            text="Convert",
            command=self._on_convert_click,
            bg="#4CAF50",
            hover_bg="#45A049"
        )
        convert_btn.pack(ipady=2, ipadx=20, padx=80)
        ToolTip(convert_btn, text="Click to convert currency")

    def _currency_row(self, parent, label_text, row):
        """Creates one row of combobox and entry for currency selection and amount."""
        label = ModernLabel(parent, text=label_text, bg="#f0f0f0")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=(5, 2), columnspan=2)

        combo = ModernCombobox(parent, currencies=self.currency_list)
        combo.grid(row=row, column=1, sticky="ew", padx=10, pady=(10, 10))
        ToolTip(combo, text=f"Select {label_text.lower()} currency")

        entry = ModernEntry(parent)
        entry.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), ipadx=10, ipady=2)

        if label_text == "From":
            self.base_currency_combo = combo
            validate_cmd = self.register(self._validate_amount)
            entry.configure(validate="key", validatecommand=(validate_cmd, "%P"))
            self.amount_entry = entry
            ToolTip(entry, text="Enter amount to convert")
        else:
            self.target_currency_combo = combo
            self.result_entry = entry
            self.result_entry.configure(state='readonly')
            ToolTip(entry, text="Converted amount will appear here")

    def _insert_digit(self, digit):
        """Inserts a digit into the amount entry."""
        self.amount_entry.insert(tk.END, digit)

    @staticmethod
    def _validate_amount(new_value: str) -> bool:
        """Validates if the input is a valid number."""
        if new_value == "":
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    def _clear_fields(self, _=None):
        """Clears both input and result fields."""
        self.amount_entry.delete(0, tk.END)
        self.result_entry.configure(state='normal')
        self.result_entry.delete(0, tk.END)
        self.result_entry.configure(state='readonly')

    def _swap_currencies(self):
        """Swaps base and target currencies using the controller."""
        if self._controller:
            self._controller.swap_currencies()

    def _on_convert_click(self):
        """Handles the convert button click."""
        try:
            amount = self.amount_entry.get()
            if not amount:
                raise ValueError("Please enter an amount to convert.")

            base_currency = self.base_currency_combo.get()
            target_currency = self.target_currency_combo.get()

            if not base_currency or not target_currency:
                raise ValueError("Both currencies must be selected.")

            if base_currency == target_currency:
                raise ValueError("Please select different currencies for conversion.")

            self._controller.convert_currency(amount, base_currency, target_currency)

        except ValueError as ve:
            self.show_error(str(ve))
        except Exception as e:
            self.show_error(f"Unexpected error: {str(e)}")

    def update_result(self, result: float):
        """Displays the conversion result in the result entry."""
        self.result_entry.configure(state='normal')
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, f"{result:,.2f}")
        self.result_entry.configure(state='readonly')
        messagebox.showinfo("Conversion Successful", "Currency has been converted.")

    def _bind_keyboard_events(self):
        """Binds keyboard input events."""
        self.bind("<Key>", self._handle_keypress)
        self.bind("<Return>", lambda e: self._on_convert_click())

    def _handle_keypress(self, event):
        """Handles keyboard input when not focused on entry."""
        widget = self.focus_get()
        if widget == self.amount_entry:
            return
        key = event.char
        if key.isdigit() or key == ".":
            self._insert_digit(key)
        elif event.keysym == "BackSpace":
            current = self.amount_entry.get()
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, current[:-1])

    @staticmethod
    def show_error(message: str):
        """Displays an error message dialog."""
        messagebox.showerror("Error", message)

    def get_base_currency(self) -> str:
        """Returns the current base currency code."""
        return self.base_currency_combo.get()

    def get_target_currency(self) -> str:
        """Returns the current target currency code."""
        return self.target_currency_combo.get()

    def set_base_currency(self, currency: tuple[str, str, str], icon):
        """Sets the base currency combobox selection."""
        self.base_currency_combo._select_currency(currency, icon)

    def set_target_currency(self, currency: tuple[str, str, str], icon):
        """Sets the target currency combobox selection."""
        self.target_currency_combo._select_currency(currency, icon)

    def get_amount(self) -> str:
        """Returns the current value from the amount entry."""
        return self.amount_entry.get()

    def set_amount(self, value: str):
        """Sets the amount entry with a new value."""
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, value)

    def get_result(self) -> str:
        """Returns the result from the result entry."""
        return self.result_entry.get()

    def set_result(self, value: str):
        """Sets the result entry with a new value."""
        self.result_entry.configure(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, value)
        self.result_entry.configure(state="readonly")

    def swap_currencies(self):
        """
        Swaps the selected currencies and their associated flag icons safely.
        Called by the controller.
        """
        try:
            base_text = self.get_base_currency()
            target_text = self.get_target_currency()

            base_tuple = next(item for item in self.currency_list if item[1] == base_text)
            target_tuple = next(item for item in self.currency_list if item[1] == target_text)

            # Get the icons from the comboboxes
            base_icon = self.base_currency_combo.get_icon(base_text)
            target_icon = self.target_currency_combo.get_icon(target_text)

            self.set_base_currency(target_tuple, target_icon)
            self.set_target_currency(base_tuple, base_icon)

            # Optionally swap the values too
            amount = self.get_amount()
            result = self.get_result()
            if result:
                self.set_amount(result)
                self.set_result(amount)

        except Exception as e:
            self.show_error(f"Swap failed: {e}")
