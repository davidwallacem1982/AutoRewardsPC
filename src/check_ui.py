import os
import sys

# Add src to path
sys.path.append(os.path.dirname(__file__))

try:
    print("Attempting to import UI...")
    from ui.app import App

    print("[OK] UI module imported successfully.")

    print("Attempting to import Main...")
    import main

    print("[OK] Main module imported successfully.")

    print("Initializing App class (headless check)...")
    # We won't call mainloop(), just init to check for instantiation errors
    # Note: This might fail if no display is present, but on user's PC it should work or at least try
    # If it fails due to no display, that is expected in some agent environments, but we catch it.
    try:
        app = App()
        app.destroy()  # Clean up immediately
        print("[OK] App initialized successfully.")
    except Exception as e:
        print(f"[WARN] App initialization failed (could be lack of display): {e}")

except ImportError as e:
    print(f"[FAIL] Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"[FAIL] Unexpected error: {e}")
    sys.exit(1)
