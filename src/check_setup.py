import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def try_import(module_name):
    try:
        __import__(module_name)
        print(f"[OK] {module_name} imported.")
    except ImportError as e:
        print(f"[FAIL] Missing dependency: {module_name} - {e}")
    except OSError as e:
        print(f"[FAIL] System error loading {module_name} (likely missing DLLs): {e}")


required_modules = [
    "pyautogui",
    "pytesseract",
    "customtkinter",
    "PIL",
    "pygetwindow",
    "pyperclip",
    "cairosvg",
    "pynput",
]

print("Checking dependencies...")
for mod in required_modules:
    try_import(mod)

from src.core.automation import Automation
from src.core.settings import Settings


def check():
    print("Checking AutoRewardsPC Setup...")

    settings = Settings()
    if settings.validate():
        print("[OK] Settings validated.")
    else:
        print("[WARN] Settings validation failed (likely Tesseract missing).")

    automation = Automation()
    if automation.check_environment():
        print("[OK] Automation environment ready.")
    else:
        print("[WARN] Automation environment not ready.")

    print("\nSetup verification finished.")


if __name__ == "__main__":
    check()
