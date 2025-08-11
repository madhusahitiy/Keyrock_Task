# steps/trading_steps.py
from behave import given, then
from trading_simulation import TradingSimulation

@given('I start a trading simulation for "{symbol}"')
def step_start_simulation(context, symbol):
    context.symbol = symbol

@given('trigger move is {trigger_move} usd')
def step_trigger_move(context, trigger_move):
    context.trigger_move = float(trigger_move)

@given('cancel move is {cancel_move} usd')
def step_cancel_move(context, cancel_move):
    context.cancel_move = float(cancel_move)

@then('I run the simulation')
def step_run_simulation(context):
    sim = TradingSimulation(
        context,
        symbol=context.symbol,
        trigger_move=context.trigger_move,
        cancel_move=context.cancel_move
    )
    sim.start()
    sim.run()
