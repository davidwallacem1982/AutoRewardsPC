import os
import sys

# Ensure src is in path if run from root
sys.path.append(os.path.dirname(__file__))

import customtkinter as ctk

from ui.app import App


def main():
    # Single Instance Check
    import ctypes

    mutex_name = "Global\\AutoRewardsPC_Instance_Mutex"
    # CreateMutexW returns a handle, but we don't need to keep it explicitly as long as the process is alive
    # However, garbage collection might close it if we don't assign it, though CreateMutex handle usually persists with process.
    # To be safe, we assign it to a variable that lives as long as main().
    mutex = ctypes.windll.kernel32.CreateMutexW(None, True, mutex_name)
    if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
        ctypes.windll.user32.MessageBoxW(
            0, "A aplicação já está em execução.", "Aviso", 0x30 | 0x1000
        )  # MB_ICONWARNING | MB_SYSTEMMODAL
        sys.exit(0)

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
