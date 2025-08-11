# Trading Simulation with Behave

This project simulates simple crypto trading scenarios using Python, Behave (BDD), and an interactive logging UI.  
It supports different trigger/cancel price moves and random BUY/SELL starting positions.

---

## Requirements

- Python 3.8+
- `behave`
- Any terminal that supports ANSI colors

---

## Installation

```bash
git clone <https://github.com/madhusahitiy/Keyrock_Task>
pip install -r requirements.txt
```

## 📂 Project Structure

<details>
<summary>Click to expand</summary>
  
```text
trading-simulation/
├── features/
│   ├── trading.feature
│   ├── environment.py
│   └── steps/
│       ├── trading_steps.py
│       └── ui_helper.py
├── trading_simulation.py
├── run_with_ui.py
├── requirements.txt
└── README.md


```

</details> 

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/trading-simulation.git
cd trading-simulation

2️⃣ Install Dependencies
Make sure you have Python 3.9+ installed, then:
pip install -r requirements.txt

3️⃣ Install Playwright Browsers
playwright install

▶️ Running the Tests
Run all BDD scenarios:
behave 

## 📜 Example Test Output
<details>
<summary>Click to expand</summary>
  
```text
[02:39:24] SIMULATION STARTED @ 29252.84
[02:39:24] TRIGGER MOVE SET TO 0.001 USD
[02:39:24] CANCEL MOVE SET TO 99999.0 USD
[02:39:24] PLANNED ORDER TYPE: BUY
[02:39:24] [1;94mBUY ORDER PLACED[0m @ 29252.13
[02:39:25] [1;92mSELL ORDER EXECUTED[0m @ 29253.58


```
</details>

## 📁 File Overview

| File / Folder                     | Description                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `features/trading.feature`        | BDD scenarios defining the trading simulation behavior.                                                           |
| `features/environment.py`         | Global setup & teardown hooks for Behave tests.                                                                   |
| `features/steps/trading_steps.py` | Step definitions implementing the `.feature` scenarios.                                                           |
| `features/steps/ui_helper.py`     | UI automation helpers (Playwright) + Binance price fetch.                                                         |
| `trading_simulation.py`           | Core logic for the trading simulation: triggers, cancels, executions (with ANSI-colored logging).                 |
| `run_with_ui.py`                  | Standalone script to run a single trading simulation with the UI, without Behave. Useful for debugging and demos. |
| `requirements.txt`                | Python dependencies for the project.                                                                              |
| `README.md`                       | Project documentation and instructions.                                                                           |



How It Works
*Initialization: The simulation sets an initial random price and chooses BUY or SELL for the first order.          
*Price Simulation: The price changes randomly on every tick.                                    
*Trigger Check: If price moves by at least the trigger amount, the planned order is placed.              
*Outcome:If price comes close enough to the placed order → execution (green log)                  
         If price moves beyond cancel distance → cancellation (red log)                
*End of Scenario: Once an order is executed or canceled, the simulation moves to the next scenario.

Customizing:

*Change Trigger/Cancel Values in your .feature file                     
*Tick Speed: Modify tick_delay in TradingSimulation.run() to speed up or slow down price changes                   
*Price Movement Range: Adjust the random.uniform(-5, 5) value in run() for bigger/smaller volatility
