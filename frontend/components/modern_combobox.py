import base64
import io
import tkinter as tk
from tkinter import ttk
from typing import Callable

from PIL import Image, ImageTk


class ModernCombobox(tk.Frame):
    """
    A modern dropdown-style combobox widget for selecting a currency.

    Displays a flag icon, currency code, and name in both the dropdown and the
    selected area. Supports smooth mouse scrolling and professional styling.

    Attributes:
        currencies: A list of tuples (base64_flag, currency_code, currency_name).
        on_select: Optional callback when an item is selected.
        width: Width of the dropdown in pixels.
        height: Height of the dropdown in pixels.
    """

    def __init__(
            self,
            master,
            currencies: list[tuple[str, str, str]],
            on_select: Callable[[tuple[str, str, str]], None] = None,
            width: int = 300,
            height: int = 300,
            *args,
            **kwargs
    ):
        super().__init__(master, *args, **kwargs)
        self._currencies = currencies
        self._on_select = on_select
        self._width = width
        self._height = height
        self._flag_images: list[ImageTk.PhotoImage] = []  # Prevent GC

        self._selected_currency = tk.StringVar()
        self._dropdown_frame = None
        self._is_dropdown_open = False
        self._selected_icon = None

        self._create_main_button()

    def _create_main_button(self):
        """Create the main area that displays the selected item."""
        self._button_frame = tk.Frame(self, bg="white", bd=1, relief="solid")
        self._button_frame.pack(fill="x")

        self._icon_label = tk.Label(self._button_frame, bg="white")
        self._icon_label.pack(side="left", padx=6, pady=4)

        self._text_label = tk.Label(
            self._button_frame,
            text="Select Currency",
            bg="white",
            font=("Segoe UI", 10)
        )
        self._text_label.pack(side="left", fill="x", expand=True, padx=4)

        self._button_frame.bind("<Button-1>", lambda e: self._toggle_dropdown())
        self._text_label.bind("<Button-1>", lambda e: self._toggle_dropdown())
        self._icon_label.bind("<Button-1>", lambda e: self._toggle_dropdown())

    def _toggle_dropdown(self):
        """Toggle the dropdown menu open/closed."""
        if self._is_dropdown_open:
            self._close_dropdown()
        else:
            self._open_dropdown()

    def _open_dropdown(self):
        """Open the dropdown menu."""
        if self._dropdown_frame:
            return

        self._dropdown_frame = tk.Toplevel(self)
        self._dropdown_frame.wm_overrideredirect(True)
        self._dropdown_frame.configure(bg="white")

        self.update_idletasks()
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        self._dropdown_frame.geometry(f"{self._width}x{self._height}+{x}+{y}")

        self._build_dropdown_content()

        self._is_dropdown_open = True
        self._dropdown_frame.lift()
        self._dropdown_frame.focus_force()
        self._dropdown_frame.bind("<FocusOut>", lambda e: self._close_dropdown())

    def _build_dropdown_content(self):
        """Build the scrollable dropdown content."""
        outer_frame = tk.Frame(self._dropdown_frame, bg="white")
        outer_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(outer_frame, bg="white", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        self._inner_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=self._inner_frame, anchor="nw")
        self._inner_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)
        canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

        for currency in self._currencies:
            self._add_currency_row(currency)

    def _close_dropdown(self):
        """Close the dropdown menu."""
        if self._dropdown_frame:
            self._dropdown_frame.destroy()
            self._dropdown_frame = None
            self._is_dropdown_open = False

    def _add_currency_row(self, currency: tuple[str, str, str]):
        """Add a row in the dropdown for a single currency."""
        flag_img = self._decode_flag(currency[0])
        if flag_img is None:
            return

        row = tk.Frame(self._inner_frame, bg="white")
        row.pack(fill="x", padx=6, pady=4)

        icon_label = tk.Label(row, image=flag_img, bg="white")
        icon_label.pack(side="left", padx=5)

        text_label = tk.Label(
            row,
            text=f"{currency[1]} - {currency[2]}",
            bg="white",
            font=("Segoe UI", 10),
            anchor="w"
        )
        text_label.pack(side="left", fill="x", expand=True)

        self._flag_images.append(flag_img)

        for widget in (row, icon_label, text_label):
            widget.bind("<Button-1>", lambda e, cur=currency, img=flag_img: self._select_currency(cur, img))

    def _decode_flag(self, base64_str: str) -> ImageTk.PhotoImage | None:
        """
        Decode a base64 string into a resized flag image (24x16).

        Args:
            base64_str: The base64 image data.

        Returns:
            ImageTk.PhotoImage or None if decoding fails.
        """
        try:
            if not base64_str:
                return None
            if "," in base64_str:
                base64_str = base64_str.split(",", 1)[1]
            image_data = base64.b64decode(base64_str)
            image = Image.open(io.BytesIO(image_data)).resize((24, 16), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"[ERROR] Failed to decode flag: {e}")
            return None

    def _select_currency(self, currency: tuple[str, str, str], icon: ImageTk.PhotoImage):
        """
        Handle selection of a currency.

        Updates the main display and calls the on_select callback if provided.

        Args:
            currency: Tuple containing (flag_base64, code, name).
            icon: ImageTk.PhotoImage for the flag icon.
        """
        self._selected_currency.set(currency[1])
        self._icon_label.config(image=icon)
        self._text_label.config(text=f"{currency[1]}")
        self._selected_icon = icon
        self._close_dropdown()
        if self._on_select:
            self._on_select(currency)

    def get(self) -> str:
        """
        Get the currently selected currency code.

        Returns:
            str: The selected currency code.
        """
        return self._selected_currency.get()

    def get_icon(self, currency_code: str) -> ImageTk.PhotoImage | None:
        """
        Returns the icon for the given currency code if it is currently selected.

        Args:
            currency_code: Currency code string (e.g., 'USD').

        Returns:
            ImageTk.PhotoImage or None
        """
        if self.get() == currency_code:
            return self._selected_icon
        return None
