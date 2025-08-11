Feature: Trading Simulation Scenarios

  Scenario Outline: Run trading simulation with different triggers
    Given I start a trading simulation for "<symbol>"
    And trigger move is <trigger> usd
    And cancel move is <cancel> usd
    Then I run the simulation

    Examples:
      | symbol  | trigger | cancel |
      | BTCUSDT | 0.001   | 99999  |
      | ETHUSDT | 0.001   | 0.0005 |
      | BNBUSDT | 0.001   | 99999  |
      | XRPUSDT | 99999   | 99999  |
