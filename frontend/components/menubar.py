# frontend/components/menubar.py

import tkinter as tk
from tkinter import messagebox

# Define consistent style
MENU_BG = "#f0f0f0"
MENU_FG = "#000000"
ACTIVE_BG = "#d9d9d9"
ACTIVE_FG = "#000000"
FONT = ("Segoe UI", 10)


class MainMenuBar(tk.Menu):
    def __init__(self, parent, controller=None):
        super().__init__(parent,
                         bg=MENU_BG, fg=MENU_FG,
                         activebackground=ACTIVE_BG, activeforeground=ACTIVE_FG,
                         font=FONT)
        self.controller = controller
        self._build_menus(parent)

    def _build_menus(self, parent):
        # Settings Menu
        settings_menu = tk.Menu(self, tearoff=0,
                                bg=MENU_BG, fg=MENU_FG,
                                activebackground=ACTIVE_BG, activeforeground=ACTIVE_FG,
                                font=FONT)
        settings_menu.add_command(label="Control", command=self._show_control)
        settings_menu.add_command(label="Check for Update", command=self._check_update)
        self.add_cascade(label="Settings", menu=settings_menu)

        # Info Menu
        info_menu = tk.Menu(self, tearoff=0,
                            bg=MENU_BG, fg=MENU_FG,
                            activebackground=ACTIVE_BG, activeforeground=ACTIVE_FG,
                            font=FONT)
        info_menu.add_command(label="About", command=self._show_about)
        info_menu.add_command(label="Manual", command=self._show_manual)
        self.add_cascade(label="Info", menu=info_menu)

        # Attach to window
        parent.config(menu=self)

    @staticmethod
    def _show_about():
        messagebox.showinfo("About", "Currency Converter v1.0\nCreated by You")

    @staticmethod
    def _show_manual():
        manual_text = (
            "1. Select base and target currencies.\n"
            "2. Enter amount using keypad or keyboard.\n"
            "3. Press Convert to see result.\n"
            "4. Use 'Swap' button to reverse currencies."
        )
        messagebox.showinfo("Manual", manual_text)

    @staticmethod
    def _show_control():
        messagebox.showinfo("Control", "Control settings can be added here.")

    def _check_update(self):
        if self.controller:
            self.controller.check_for_update()
        else:
            messagebox.showinfo("Update", "Update controller not connected.")
