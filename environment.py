def before_all(context):
    import builtins
    context.ui = getattr(builtins, "global_ui", None)
    if context.ui is None:
        print("[ERROR] UI not found in context — logging will be disabled.")

def before_scenario(context, scenario):
    if context.ui:
        context.ui.log_event(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    if context.ui:
        context.ui.log_event(f"Finished scenario: {scenario.name}")
