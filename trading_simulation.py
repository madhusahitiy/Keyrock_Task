import time
import requests
from datetime import datetime

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return float(r.json()['price'])
    except Exception as e:
        print(f"[ERROR] Failed to fetch price: {e}")
        return None

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def trading_simulation(asset, trigger_move, trigger_type, order_offset, cancel_move, cancel_type, poll_interval, duration):
    print("=== Trading Simulation Start ===")
    initial_price = get_price(asset)
    if initial_price is None:
        print("Error: Could not fetch initial price.")
        return 0, 0, 0  

    if trigger_type.lower() == "percent":
        trigger_value = initial_price * (trigger_move / 100)
    else:
        trigger_value = trigger_move

    if cancel_type.lower() == "percent":
        cancel_value = initial_price * (cancel_move / 100)
    else:
        cancel_value = cancel_move

    print(f"Asset: {asset.replace('USDT','')}")
    print(f"Initial Price: ${initial_price:,.2f}")
    print(f"Trigger: Price moves ±{trigger_move} {trigger_type} (≈ ±${trigger_value:,.2f})")
    print(f"Order Type: Limit Sell at ${initial_price - order_offset:,.2f}")
    print(f"Cancel Condition: Price moves ±{cancel_move} {cancel_type} (≈ ±${cancel_value:,.2f}) after order placement")
    print(f"Polling Interval: {poll_interval}s")
    print("----------------------------------\n")

    order_placed = False
    order_price = None
    orders_placed_count = 0
    orders_executed_count = 0
    orders_canceled_count = 0
    order_type = None
    start_time = time.time()

    while time.time() - start_time < duration:
        price = get_price(asset)
        if price is None:
            time.sleep(poll_interval)
            continue

        if not order_placed:
            diff = price - initial_price
            if abs(diff) >= trigger_value:
                # Place order
                if diff > 0:
                    order_type = "SELL"
                    order_price = price + order_offset
                else:
                    order_type = "BUY"
                    order_price = price - order_offset

                log(f"Price {'rose' if diff > 0 else 'dropped'} to ${price:,.2f} → Trigger hit ({'up' if diff > 0 else 'down'} ${abs(diff):,.2f})")
                print(f"\n{MAGENTA}Placed LIMIT {order_type}:{RESET} 0.01 {asset.replace('USDT','')} @ ${order_price:,.2f}")
                orders_placed_count += 1
                order_placed = True
            else:
                log(f"Current Price: ${price:,.2f} → Waiting for trigger...")

        else:
            # Cancel check
            if abs(price - initial_price) >= cancel_value:
                log(f"Price {'rose' if price > initial_price else 'dropped'} to ${price:,.2f} → Cancel condition met ({'up' if price > initial_price else 'down'} ${abs(price - initial_price):,.2f})")
                print(f"\n{RED}Order CANCELED:{RESET} 0.01 {asset.replace('USDT','')} @ ${order_price:,.2f}")
                orders_canceled_count += 1
                break

            # Execution check
            if order_type == "SELL" and price >= order_price:
                print(f"\n{GREEN}ORDER EXECUTED:{RESET} SELL 0.01 {asset.replace('USDT','')} @ ${price:,.2f}")
                orders_executed_count += 1
                break
            elif order_type == "BUY" and price <= order_price:
                print(f"\n{GREEN}ORDER EXECUTED:{RESET} BUY 0.01 {asset.replace('USDT','')} @ ${price:,.2f}")
                orders_executed_count += 1
                break
            else:
                log(f"Current Price: ${price:,.2f} → Monitoring after order...")

        time.sleep(poll_interval)

    return orders_placed_count, orders_canceled_count, orders_executed_count

