Feature: Automated Trading Simulation
  As a trader
  I want to simulate trading based on price movements
  So that I can verify the automation works as expected

  Scenario Outline: Run trading simulation for given asset and parameters
    Given I start a trading simulation for "<asset>"
    And trigger move is <trigger_move> <trigger_type>
    And cancel move is <cancel_move> <cancel_type>
    Then I run the simulation

  Examples:
      # Test 1: BTC triggers and EXECUTES (small trigger, cancel far away)
      | asset   | trigger_type | trigger_move | cancel_type | cancel_move | 
      | BTCUSDT | usd          | 0.001        | usd         | 50          | 

      # Test 2: BTC triggers and CANCELS quickly (cancel close)
      | BTCUSDT | usd          | 0.001        | usd         | 3           | 

      # Test 3: ETH triggers and EXECUTES (small percent trigger, large cancel move)
      | ETHUSDT | percent      | 0.05         | usd         | 100         | 

      # Test 4: ETH triggers and CANCELS (cancel close in USD)
      | ETHUSDT | usd          | 0.05         | usd         | 2           | 

      # Test 5: BTC large % trigger (unlikely to hit — no trade)
      | BTCUSDT | percent      | 0.1          | usd         | 50          | 
