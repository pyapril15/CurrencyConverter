# widget.py
import tkinter as tk
from tkinter import ttk


class ModernLabel(tk.Label):
    def __init__(self, parent, text="", **kwargs):
        super().__init__(
            parent,
            text=text,
            font=("Arial", 13, "bold"),  # larger font
            bg=kwargs.get("bg", "#ffffff"),
            fg=kwargs.get("fg", "#333"),
            anchor="w",
            padx=2,  # add padding
            pady=4
        )


class ModernEntry(tk.Entry):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            font=("Arial", 14),
            justify="right",
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#ccc",
            **kwargs
        )


class ModernCombobox(ttk.Combobox):
    def __init__(self, parent, variable, values, **kwargs):
        style = ttk.Style()
        custom_style_name = "Modern.TCombobox"

        style.configure(
            custom_style_name,
            font=("Arial", 14),
            padding=6,
            relief="flat",
            foreground="#000",
            fieldbackground="#fff",
            background="#fff"
        )
        style.map(
            custom_style_name,
            fieldbackground=[('readonly', '#fff')],
            background=[('readonly', '#fff')],
            foreground=[('readonly', '#000')]
        )

        super().__init__(
            parent,
            textvariable=variable,
            values=values,
            state="readonly",
            width=kwargs.get("width", 30),
            style=custom_style_name
        )


class ModernButton(tk.Button):
    def __init__(self, parent, text="", command=None, bg="#4CAF50", fg="white", hover_bg="#45A049", **kwargs):
        self.default_bg = bg
        self.hover_bg = hover_bg
        self.active_bg = self._darken_color(bg, 0.9)

        super().__init__(
            parent,
            text=text,
            font=("Arial", 13, "bold"),
            bg=self.default_bg,
            fg=fg,
            activebackground=self.active_bg,
            activeforeground=fg,
            bd=0,
            relief="flat",
            padx=10,
            pady=6,
            cursor="hand2",
            command=command,
            **kwargs
        )

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_enter(self, event):
        self.configure(bg=self.hover_bg)

    def _on_leave(self, event):
        self.configure(bg=self.default_bg)

    def _on_press(self, event):
        self.configure(bg=self.active_bg)

    def _on_release(self, event):
        self.configure(bg=self.hover_bg)

    def _darken_color(self, color, factor):
        """Darken a hex color by a given factor (0.0 - 1.0)."""
        color = color.lstrip("#")
        r, g, b = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        return f"#{r:02x}{g:02x}{b:02x}"


class KeyButton(tk.Button):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(
            master,
            text=text,
            font=("Arial", 14),
            bg="#ffffff",
            relief="flat",
            cursor="hand2",
            command=lambda: command(text) if command else None,
            **kwargs
        )
        self.bind("<Enter>", lambda e: self.config(bg="#e6f0ff"))
        self.bind("<Leave>", lambda e: self.config(bg="#ffffff"))
