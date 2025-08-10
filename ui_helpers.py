import requests


class TradingUI:
    def __init__(self, browser, trading_ui_url):
        self.browser = browser
        self.trading_ui_url = trading_ui_url
        self.page = None
        self.selectors = {
            "asset_input": "input[placeholder='Search asset']",
            "asset_result": ".asset-list-item >> nth=0",
        }

    async def start(self):
        print(f"[DEBUG] Navigating to: {self.trading_ui_url}")

        try:
            r = requests.get(self.trading_ui_url, timeout=2)
            r.raise_for_status()
        except Exception as e:
            raise RuntimeError(f"Trading UI not reachable at {self.trading_ui_url}: {e}")


        self.page = await self.browser.new_page()
        await self.page.goto(self.trading_ui_url)
        await self.page.wait_for_load_state("networkidle")
        print("[DEBUG] UI loaded.")

    async def select_asset(self, asset_name):
        print(f"[DEBUG] Selecting asset: {asset_name}")
        await self.page.fill(self.selectors["asset_input"], asset_name)
        await self.page.click(self.selectors["asset_result"])
        print(f"[DEBUG] Asset {asset_name} selected.")

def get_price(symbol):
    """Fetch live price from Binance API."""
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    resp = requests.get(url)
    resp.raise_for_status()
    price = float(resp.json()["price"])
    print(f"[DEBUG] Price for {symbol.upper()}: {price}")
    return price
