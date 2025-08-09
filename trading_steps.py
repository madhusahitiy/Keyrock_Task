from behave import given, when, then
from trading_simulation import trading_simulation
import features.environment as environment


@given('I start a trading simulation for "{asset}"')
def step_set_asset(context, asset):
    context.asset = asset

@given('trigger move is {trigger_move:g} {trigger_type}')
def step_set_trigger_move(context, trigger_move, trigger_type):
    context.trigger_move = trigger_move
    context.trigger_type = trigger_type  # store type for later logic

@given('cancel move is {cancel_move:g} {cancel_type}')
def step_set_cancel_move(context, cancel_move, cancel_type):
    context.cancel_move = cancel_move
    context.cancel_type = cancel_type  # store type for later logic

@then("I run the simulation")
def step_run_simulation(context):
    placed, canceled, executed = trading_simulation(
        asset=context.asset,
        trigger_move=context.trigger_move,
        trigger_type=context.trigger_type,
        order_offset=0.01,
        cancel_move=context.cancel_move,
        cancel_type=context.cancel_type,
        poll_interval=2,
        duration=30
    )

    # Update global totals in environment.py
    environment.orders_totals["placed"] += placed
    environment.orders_totals["canceled"] += canceled
    environment.orders_totals["executed"] += executed

    print(
    f"\n \033[92mPlaced={environment.orders_totals['placed']}\033[0m, "
    f"\033[91mCanceled={environment.orders_totals['canceled']}\033[0m, "
    f"\033[93mExecuted={environment.orders_totals['executed']}\033[0m"
)