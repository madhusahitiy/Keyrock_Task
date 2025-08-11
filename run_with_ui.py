# run_with_ui.py
import threading
import behave.__main__
from trading_ui import start_ui

def run_behave():
    # Pass UI to behave via builtins so environment.py can grab it
    import builtins
    builtins.global_ui = ui
    behave.__main__.main()

if __name__ == "__main__":
    # Create UI on main thread
    ui = start_ui()

    # Start behave in a background thread
    threading.Thread(target=run_behave, daemon=True).start()

    # Keep UI running
    ui.root.mainloop()
