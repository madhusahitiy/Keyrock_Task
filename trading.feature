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
      | asset   | trigger_type | trigger_move | cancel_type | cancel_move | 
      | BTCUSDT | usd          | 0.001        | usd         | 50          | 
      | BTCUSDT | usd          | 0.001        | usd         | 3           | 
      | ETHUSDT | percent      | 0.05         | usd         | 100         | 
      | ETHUSDT | usd          | 0.05         | usd         | 2           | 
      | BTCUSDT | percent      | 0.1          | usd         | 50          | 
