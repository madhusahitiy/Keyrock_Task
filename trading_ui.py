import tkinter as tk
from datetime import datetime

class TradingUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Trading Simulator UI")
        self.root.geometry("800x600")

        # Top frame for info
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=10)

        tk.Label(info_frame, text="Symbol:").grid(row=0, column=0, sticky="e")
        self.symbol_var = tk.StringVar()
        tk.Label(info_frame, textvariable=self.symbol_var, width=15, anchor="w").grid(row=0, column=1)

        tk.Label(info_frame, text="Initial Price:").grid(row=0, column=2, sticky="e")
        self.initial_price_var = tk.StringVar()
        tk.Label(info_frame, textvariable=self.initial_price_var, width=15, anchor="w").grid(row=0, column=3)

        tk.Label(info_frame, text="Live Price:").grid(row=1, column=0, sticky="e")
        self.live_price_var = tk.StringVar()
        tk.Label(info_frame, textvariable=self.live_price_var, width=15, anchor="w").grid(row=1, column=1)

        tk.Label(info_frame, text="Last Action:").grid(row=1, column=2, sticky="e")
        self.last_action_var = tk.StringVar()
        tk.Label(info_frame, textvariable=self.last_action_var, width=15, anchor="w").grid(row=1, column=3)

        # Log area
        log_frame = tk.LabelFrame(self.root, text="Event Log", padx=5, pady=5)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_text = tk.Text(log_frame, height=20, state="disabled", wrap="word", font=("Courier", 10))
        self.log_text.pack(fill="both", expand=True)

        # Make UI appear on top
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(500, lambda: self.root.attributes('-topmost', False))

    def set_symbol(self, symbol):
        self.symbol_var.set(symbol)

    def set_initial_price(self, price):
        self.initial_price_var.set(f"{price:.2f}")

    def update_price(self, price):
        self.live_price_var.set(f"{price:.2f}")

    def set_last_action(self, action):
        self.last_action_var.set(action)

    def log_event(self, event_type, price=None):
        timestamp = datetime.now().strftime("%H:%M:%S")
        price_str = f" @ {price:.2f}" if price is not None else ""
        message = f"[{timestamp}] {event_type.upper()}{price_str}\n"
        self._append_log(message)

    def _append_log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message)
        self.log_text.config(state="disabled")
        self.log_text.see(tk.END)
        self.root.update()

def start_ui():
    return TradingUI()
