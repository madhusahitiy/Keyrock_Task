# trading_simulation.py
import time
import random
import sys
import re

# ANSI color codes
BLUE = "\033[1;94m"
YELLOW = "\033[1;93m"
GREEN = "\033[1;92m"
RED = "\033[1;91m"
RESET = "\033[0m"

# Regex to strip ANSI color codes
ANSI_ESCAPE_PATTERN = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

def strip_ansi(text: str) -> str:
    """Remove ANSI escape codes from text."""
    return ANSI_ESCAPE_PATTERN.sub("", text)


class TradingSimulation:
    def __init__(self, context, symbol, trigger_move, cancel_move):
        self.context = context
        self.symbol = symbol
        self.trigger_move = float(trigger_move)
        self.cancel_move = float(cancel_move)
        self.initial_price = random.uniform(100, 50000)
        self.current_price = self.initial_price
        self.active_order_price = None
        self.order_type = random.choice(["BUY", "SELL"])  # First order is random

    def _log_event(self, message, price=None):
        """Internal helper to handle color stripping for non-TTY outputs."""
        if not sys.stdout.isatty():
            message = strip_ansi(message)
        if price is not None:
            self.context.ui.log_event(message, price)
        else:
            self.context.ui.log_event(message)

    def start(self):
        ui = self.context.ui

        # Separate scenarios visually
        print("\n" * 2)

        ui.set_symbol(self.symbol)
        ui.set_initial_price(self.initial_price)
        ui.update_price(self.initial_price)
        ui.set_last_action("Simulation Started")
        self._log_event("Simulation started", self.initial_price)
        self._log_event(f"Trigger move set to {self.trigger_move:.2f} USD", self.initial_price)
        self._log_event(f"Cancel move set to {self.cancel_move:.2f} USD", self.initial_price)
        self._log_event(f"Planned order type: {self.order_type}", self.initial_price)

    def run(self, tick_delay=0.5):
        """
        Runs the simulation until one order is placed and either executed or canceled.
        Stops immediately after that.
        """
        while True:
            # Simulate price change
            self.current_price += random.uniform(-5, 5)
            self.context.ui.update_price(self.current_price)

            # Place order if not placed yet
            if self.active_order_price is None:
                if abs(self.current_price - self.initial_price) >= self.trigger_move:
                    self.active_order_price = self.current_price
                    self.context.ui.set_last_action(f"{self.order_type} Order Placed")
                    self._log_event(f"{BLUE}{self.order_type} ORDER PLACED{RESET}", self.current_price)

            else:
                # Check for execution
                if abs(self.current_price - self.active_order_price) < 2:
                    executed_side = "SELL" if self.order_type == "BUY" else "BUY"
                    self.context.ui.set_last_action(f"{executed_side} Order Executed")
                    self._log_event(f"{GREEN}{executed_side} ORDER EXECUTED{RESET}", self.current_price)
                    break  # End scenario here

                # Check for cancellation
                elif abs(self.current_price - self.active_order_price) >= self.cancel_move:
                    self.context.ui.set_last_action("Order Canceled")
                    self._log_event(f"{RED}ORDER CANCELED{RESET}", self.current_price)
                    break  # End scenario here

            time.sleep(tick_delay)
