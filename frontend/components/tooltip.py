# frontend/components/tooltip.py

import tkinter as tk


class ToolTip:
    def __init__(self, widget, text="", delay=500):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip_window = None
        self.id = None

        self.widget.bind("<Enter>", self._schedule_show)
        self.widget.bind("<Leave>", self._hide_tooltip)
        self.widget.bind("<ButtonPress>", self._hide_tooltip)

    def _schedule_show(self, event=None):
        self._cancel_scheduled()
        self.id = self.widget.after(self.delay, self._show_tooltip)

    def _cancel_scheduled(self):
        if self.id:
            self.widget.after_cancel(self.id)
            self.id = None

    def _show_tooltip(self):
        if self.tip_window or not self.text:
            return

        x, y, cx, cy = self.widget.bbox("insert") if self.widget.winfo_class() != "Frame" else (0, 0, 0, 0)
        x += self.widget.winfo_rootx() + 20
        y += self.widget.winfo_rooty() + 20

        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(tw, text=self.text, justify="left",
                         background="#ffffe0", relief="solid", borderwidth=1,
                         font=("Arial", 9))
        label.pack(ipadx=5, ipady=3)

    def _hide_tooltip(self, event=None):
        self._cancel_scheduled()
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None
