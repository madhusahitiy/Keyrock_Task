# environment.py
import asyncio
from playwright.async_api import async_playwright
from features.steps.ui_helpers import TradingUI


TRADING_UI_URL = "http://localhost:3000"

# Global counters (persist across scenarios)
orders_totals = {
    "placed": 0,
    "canceled": 0,
    "executed": 0
}

def before_all(context):
    print("[DEBUG] Starting Playwright for test suite.")
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)

    async def start_browser():
        context.playwright = await async_playwright().start()
        context.browser = await context.playwright.chromium.launch(headless=False)
        context.ui = TradingUI(context.browser, TRADING_UI_URL)

    context.loop.run_until_complete(start_browser())

def after_all(context):
    print("[DEBUG] Closing browser and Playwright.")
    async def close_browser():
        if hasattr(context, "browser") and context.browser:
            await context.browser.close()
        if hasattr(context, "playwright") and context.playwright:
            await context.playwright.stop()

    context.loop.run_until_complete(close_browser())