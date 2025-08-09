# Keyrock_Task  
**Automated Trading Simulation (BDD Tests)**  

This project simulates crypto trading scenarios using **Binance live prices**, automated UI checks with **Playwright**, and BDD tests via **Behave**.

---

## 📂 Project Structure

features/
│── trading.feature # BDD scenarios for trading simulations  
│── environment.py # Global setup/teardown for Behave tests   
│── steps/    
│ ├── trading_steps.py # Step definitions for trading.feature    
│ ├── ui_helpers.py # UI automation helpers & Binance price fetch    
trading_simulation.py # Core simulation logic        
requirements.txt # Python dependencies            
README.md # This file

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/trading-simulation.git
cd trading-simulation

2️⃣ Install Dependencies
Make sure you have Python 3.9+ installed, then:
pip install -r requirements.txt

3️⃣ Install Playwright Browsers
playwright install

▶️ Running the Tests
Run all BDD scenarios:
behave -f plain --no-capture

📜 Example Test Output

<details><summary>Click to expand</summary>
Example output from one test scenario:
keyrock-project % behave -f plain --no-capture
USING RUNNER: behave.runner:Runner
[DEBUG] Starting Playwright for test suite.
Feature: Automated Trading Simulation

  Scenario Outline: Run trading simulation for given asset and parameters -- @1.1 
    Given I start a trading simulation for "BTCUSDT" ... passed in 0.000s
    And trigger move is 0.001 usd ... passed in 0.000s
    And cancel move is 50 usd ... passed in 0.000s
=== Trading Simulation Start ===
Asset: BTC
Initial Price: $116,580.01
Trigger: Price moves ±0.001 usd (≈ ±$0.00)
Order Type: Limit Sell at $116,580.00
Cancel Condition: Price moves ±50.0 usd (≈ ±$50.00) after order placement
Polling Interval: 2s
----------------------------------

[00:04:30] Current Price: $116,580.01 → Waiting for trigger...
[00:04:33] Price dropped to $116,568.68 → Trigger hit (down $11.33)

Placed LIMIT BUY: 0.01 BTC @ $116,568.67
[00:04:35] Current Price: $116,568.69 → Monitoring after order...
[00:04:37] Current Price: $116,568.68 → Monitoring after order...
[00:04:40] Current Price: $116,568.68 → Monitoring after order...
[00:04:42] Current Price: $116,568.68 → Monitoring after order...
[00:04:44] Current Price: $116,568.69 → Monitoring after order...
[00:04:46] Current Price: $116,568.68 → Monitoring after order...

ORDER EXECUTED: BUY 0.01 BTC @ $116,568.49

Placed=1, Canceled=0, Executed=1
</details>

🧩 How It Works
Price Fetching – Binance API is queried in real-time to get current asset prices.

Trigger Conditions – When the price moves by a configured USD or % value, an order is "placed".

Cancel Conditions – If price moves further in an opposite direction before execution, the order is canceled.

Execution – If the price reaches the target order price, it is marked executed.

Global Totals – Summary of placed, executed, and canceled orders is tracked across all scenarios.

⚠️ Notes
Requires internet access for Binance API.

The trading simulation is mocked — no real orders are sent.

The Playwright UI URL in environment.py must be reachable, otherwise tests will raise an error.

Default order_offset is 0.01 if not specified in feature files.
