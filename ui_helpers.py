# features/steps/ui_helpers.py
class TradingUI:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.page = None

    async def open(self):
        if not self.page:
            self.page = await self.browser.new_page()
            await self.page.goto(self.base_url)

    async def place_order(self):
        await self.open()
        print("[DEBUG] Clicking Place Order button in UI...")
        await self.page.click("text=Place Order")

    async def cancel_order(self):
        await self.open()
        print("[DEBUG] Clicking Cancel Order button in UI...")
        await self.page.click("text=Cancel Order")

    async def execute_order(self):
        await self.open()
        print("[DEBUG] Clicking Execute Order button in UI...")
        await self.page.click("text=Execute Order")

    async def start_simulation(self):
        await self.open()
        print("[DEBUG] Clicking Start Simulation button in UI...")
        await self.page.click("text=Start Simulation")

    async def log_to_ui(self, message: str):
        """
        Adds a log message to the UI if your UI supports
        an input field or some JS-based logging mechanism.
        This is a placeholder — adapt it to your UI.
        """
        try:
            await self.open()
            # Example: If your UI has a textarea with id="log"
            # and JS function to append logs
            await self.page.evaluate(f"""
                let logBox = document.getElementById('log');
                if (logBox) {{
                    logBox.value += "\\n{message}";
                }}
            """)
        except Exception as e:
            print(f"[WARN] Could not log to UI: {e}")
