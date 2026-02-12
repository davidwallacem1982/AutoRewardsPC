import ctypes
import json
import threading

import customtkinter as ctk
import pyautogui

try:
    from src.core.automation import Automation
except ImportError:
    from core.automation import Automation
import logging
import logging.handlers
import os
import shutil
import sys
import tkinter.filedialog
import tkinter.messagebox
from datetime import datetime, timedelta

import pystray
from PIL import Image, ImageDraw, ImageTk

from .theme import Theme


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Windows Taskbar Icon Fix
        try:
            myappid = "antigravity.autorewardspc.1.0"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass

        # Window Setup
        self.title("Automação Microsoft de Rewards PC")
        self._center_window(self, 800, 380)
        self.resizable(False, False)
        self.configure(fg_color=Theme.BACKGROUND)

        # Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Clean up old logs (retention policy: 9 days)
        self.cleanup_old_logs()

        # Setup initial logger for app startup
        self.setup_logger()

        # Prevent adding multiple handlers if re-initialized
        # Load Icon
        self.icon_image = None
        self.icon_path = None

        # Try to resolve icon path using resource_path
        icon_ico = resource_path(os.path.join("assets", "icon.ico"))
        icon_png = resource_path(os.path.join("assets", "icon.png"))

        if os.path.exists(icon_ico):
            self.icon_path = icon_ico
        elif os.path.exists(icon_png):
            self.icon_path = icon_png

        if self.icon_path:
            try:
                # Set Window Icon
                if self.icon_path.endswith(".ico"):
                    self.iconbitmap(self.icon_path)
                else:
                    self.icon_image = Image.open(self.icon_path)
                    self.iconphoto(False, ImageTk.PhotoImage(self.icon_image))

                # Load image for Tray/Other uses if not already loaded
                if not self.icon_image:
                    self.icon_image = Image.open(self.icon_path)

            except Exception as e:
                logging.error(f"Failed to load icon: {e}")

        # --- Load Button Icons ---
        self.icons = {}
        icon_files = {
            "play": "play.png",
            "stop": "stop.png",
            "target": "target.png",
            "import": "import.png",
            "export": "export.png",
            "logs": "logs.png",
            "save": "save.png",
            "cancel": "cancel.png",
            "capture": "capture.png",
        }

        for name, filename in icon_files.items():
            try:
                path = resource_path(os.path.join("assets", "icons", filename))
                if os.path.exists(path):
                    # Resize to 20x20 for buttons
                    self.icons[name] = ctk.CTkImage(
                        # packet_image=None, # Deprecated/Internal in some versions, but light/dark is standard
                        light_image=Image.open(path),
                        dark_image=Image.open(path),
                        size=(20, 20),
                    )
                else:
                    logging.warning(f"Icon not found: {path}")
            except Exception as e:
                logging.error(f"Failed to load button icon {name}: {e}")

        # Handle window closing (Exit)
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        # Handle minimize to tray
        self.bind("<Unmap>", self.check_minimize)

        self.automation = Automation()

        # Header
        self.automation = Automation()

        # Header Frame
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, padx=40, pady=(40, 20), sticky="ew")

        # Header Label (Gradient-like effect using bright color)
        self.header_label = ctk.CTkLabel(
            self,
            text="Automação Microsoft de Rewards PC",
            font=(Theme.FONT_FAMILY, 22, "bold"),
            text_color=Theme.TEXT_MAIN,
        )
        self.header_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.subheader_label = ctk.CTkLabel(
            self,
            text="Maximize seus pontos com automação inteligente.",
            font=(Theme.FONT_FAMILY, 14),
            text_color=Theme.TEXT_SUB,
        )
        self.subheader_label.grid(
            row=0, column=0, padx=20, pady=(20, 5), sticky="e"
        )  # Right aligned subtile

        # Main Content Area (Card)
        self.main_card = ctk.CTkFrame(
            self,
            fg_color=Theme.SURFACE,
            corner_radius=Theme.CORNER_RADIUS,
            border_width=1,
            border_color=Theme.BORDER,
        )
        # sticky="ew" to prevent vertical stretching (centers vertically due to row weight)
        self.main_card.grid(row=1, column=0, padx=20, pady=(5, 20), sticky="ew")

        # Configure Main Card Layout (Left Sidebar, Right Log)
        self.main_card.grid_columnconfigure(0, weight=1)  # Buttons (Sidebar)
        self.main_card.grid_columnconfigure(1, weight=2)  # Logs (Main Area)
        self.main_card.grid_rowconfigure(0, weight=0)  # Shrink to fit content height

        # --- LEFT SIDEBAR (Buttons) ---
        self.sidebar_frame = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.sidebar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.sidebar_frame.grid_columnconfigure((0, 1), weight=1)
        self.sidebar_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)  # Compact rows

        btn_font = (Theme.FONT_FAMILY, Theme.FONT_BUTTON_SIZE, "bold")
        small_btn_font = (Theme.FONT_FAMILY, 12, "bold")

        # Row 0: Iniciar | Calibrar
        self.start_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" INICIAR",
            command=self.start_automation_thread,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.PRIMARY_HOVER,
            corner_radius=Theme.CORNER_RADIUS,
            height=Theme.BUTTON_HEIGHT,
            font=btn_font,
            image=self.icons.get("play"),
            compound="left",
        )
        self.start_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.calibrate_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" Calibrar",
            command=self.open_calibration_window,
            fg_color="transparent",
            border_width=1,
            border_color=Theme.SECONDARY,
            text_color=Theme.SECONDARY,
            hover_color=Theme.SURFACE_HOVER,
            corner_radius=Theme.CORNER_RADIUS,
            height=Theme.BUTTON_HEIGHT,
            font=small_btn_font,
            image=self.icons.get("target"),
            compound="left",
        )
        self.calibrate_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Row 1: Importar | Exportar (Swapped)
        self.import_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" Importar",
            command=self.import_calibration,
            fg_color=Theme.BTN_RESTORE,
            hover_color="#002171",
            text_color="white",
            height=Theme.BUTTON_HEIGHT,
            corner_radius=Theme.CORNER_RADIUS,
            font=small_btn_font,
            image=self.icons.get("import"),
            compound="left",
        )
        self.import_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.export_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" Exportar",
            command=self.export_calibration,
            fg_color=Theme.BTN_BACKUP,
            hover_color="#039BE5",
            text_color="black",
            height=Theme.BUTTON_HEIGHT,
            corner_radius=Theme.CORNER_RADIUS,
            font=small_btn_font,
            image=self.icons.get("export"),
            compound="left",
        )
        self.export_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Row 2: Ver Logs (Full Width)
        self.logs_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" Ver Logs",
            command=self.open_logs,
            fg_color=Theme.BTN_LOGS,
            hover_color="#455A64",
            text_color="white",
            height=Theme.BUTTON_HEIGHT,
            corner_radius=Theme.CORNER_RADIUS,
            font=small_btn_font,
            image=self.icons.get("logs"),
            compound="left",
        )
        self.logs_button.grid(
            row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew"
        )

        # Row 3: Parar (Full Width)
        self.stop_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" PARAR",
            command=self.stop_automation,
            state="disabled",
            fg_color=Theme.DANGER,
            hover_color=Theme.DANGER_HOVER,
            corner_radius=Theme.CORNER_RADIUS,
            height=Theme.BUTTON_HEIGHT,
            font=btn_font,
            image=self.icons.get("stop"),
            compound="left",
        )
        self.stop_button.grid(
            row=3, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="ew"
        )

        # --- RIGHT AREA (Logs) ---
        self.log_textbox = ctk.CTkTextbox(
            self.main_card,
            width=500,  # Initial width
            height=100,  # Small min-height, lettings buttons dictate actual height
            fg_color=Theme.BACKGROUND,
            text_color=Theme.TEXT_MAIN,
            font=("Consolas", 12),
            corner_radius=10,
            border_width=0,
        )
        self.log_textbox.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.log("Inicialização do sistema...")

    def log(self, message):
        self.log_textbox.insert("end", message + "\n")
        self.log_textbox.see("end")
        logging.info(message)

    def cleanup_old_logs(self):
        """Removes log files older than 9 days to satisfy weekly purge requirement + buffer."""
        try:
            log_dir = "logs"
            if not os.path.exists(log_dir):
                return

            retention_days = 9
            cutoff = datetime.now() - timedelta(days=retention_days)

            for filename in os.listdir(log_dir):
                if filename.startswith("automation_") and filename.endswith(".log"):
                    file_path = os.path.join(log_dir, filename)
                    try:
                        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                        if file_time < cutoff:
                            os.remove(file_path)
                            logging.info(f"Log antigo removido: {filename}")
                    except Exception as e:
                        logging.error(
                            f"Erro ao verificar/remover log antigo {filename}: {e}"
                        )
        except Exception as e:
            logging.error(f"Erro no processo de limpeza de logs: {e}")

    def setup_logger(self):
        """Configures a new log file for the current session/execution."""
        if not os.path.exists("logs"):
            os.makedirs("logs")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f"logs/automation_{timestamp}.log"

        root_logger = logging.getLogger()
        # Remove existing handlers to switch to new file
        if root_logger.handlers:
            for handler in root_logger.handlers[:]:
                if isinstance(handler, logging.FileHandler):
                    handler.close()
                    root_logger.removeHandler(handler)

        handler = logging.FileHandler(log_filename, encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        handler.setFormatter(formatter)

        root_logger.setLevel(logging.INFO)
        root_logger.addHandler(handler)
        # Force a log entry to confirm file creation
        logging.info(f"Log iniciado: {log_filename}")

    def start_automation_thread(self):
        """Runs automation in a separate thread to keep UI responsive."""
        # Create a new log file for this execution run
        self.setup_logger()

        # Clear previous UI logs
        self.log_textbox.delete("1.0", "end")

        self.log("Iniciando thread de automação...")
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.stop_button.configure(state="normal")
        self.calibrate_button.configure(state="disabled")
        self.export_button.configure(state="disabled")
        self.import_button.configure(state="disabled")

        thread = threading.Thread(target=self.run_automation)
        thread.daemon = True
        thread.start()

    def stop_automation(self):
        """Signals automation to stop."""
        self.log("Parando...")
        self.stop_button.configure(state="disabled")  # Prevent double clicks
        self.automation.stop()

    def open_calibration_window(self):
        """Opens the calibration window."""
        self.log("Abrindo janela de calibração...")
        self.calibration_window = ctk.CTkToplevel(self)
        self.calibration_window.title("Calibragem de Coordenadas")
        self._center_window(self.calibration_window, 700, 500)
        self.calibration_window.resizable(False, False)
        self.calibration_window.configure(fg_color=Theme.BACKGROUND)

        # Force Dark Title Bar
        self._force_dark_title_bar(self.calibration_window)

        # Apply icon with delay to ensure it persists on Toplevel
        self.after(200, lambda: self._apply_calibration_icon())

        # Hide Main Window
        self.withdraw()

        # Make modal-like (without transient, so it stays visible while parent is hidden)
        self.calibration_window.grab_set()
        self.calibration_window.focus_force()

        # Calibration State

        self.calibration_steps = [
            {
                "key": "botao_microsoft_rewards",
                "desc": "botão favoritos do Microsoft Rewards",
            },
            {"key": "detalhamentos_pontos", "desc": "Detalhamento dos pontos"},
            {"key": "abrir_pc_search", "desc": "PC Search"},
            {
                "key": "barra_pesquisa",
                "desc": "Barra de Pesquisa do https://www.bing.com",
            },
            {
                "key": "aba_pesquisa",
                "desc": "Aba da Página de Pesquisa do https://www.bing.com",
            },
            {
                "key": "aba_principal",
                "desc": "Aba da Página do https://rewards.bing.com",
            },
        ]
        self.current_step_index = 0
        self.captured_coords = {}

        # Main Container (Card)
        main_frame = ctk.CTkFrame(
            self.calibration_window,
            fg_color=Theme.SURFACE,
            corner_radius=Theme.CORNER_RADIUS,
            border_width=1,
            border_color=Theme.BORDER,
        )
        main_frame.pack(fill="both", expand=True, padx=40, pady=40)

        # Instructions
        instruction_label = ctk.CTkLabel(
            main_frame,
            text="Siga as instruções abaixo e pressione Enter para capturar cada item.",
            font=(Theme.FONT_FAMILY, 16, "bold"),
            text_color=Theme.TEXT_MAIN,
            wraplength=600,
        )
        instruction_label.pack(pady=(30, 10), padx=30, anchor="w")

        # Tip
        tip_label = ctk.CTkLabel(
            main_frame,
            text="💡 Dica: para evitar mover o mouse ao clicar, apenas posicione o cursor\nsobre o local desejado e pressione Enter.",
            font=(Theme.FONT_FAMILY, 13),
            text_color=Theme.TEXT_SUB,
            wraplength=600,
            justify="left",
        )
        tip_label.pack(pady=(0, 30), padx=30, anchor="w")

        # Step Display Area (Dark Frame)
        self.step_frame = ctk.CTkFrame(
            main_frame,
            fg_color=Theme.BACKGROUND,
            corner_radius=Theme.CORNER_RADIUS,
            border_width=1,
            border_color=Theme.PRIMARY,
        )
        self.step_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))

        current_desc = self.calibration_steps[self.current_step_index]["desc"]
        self.step_label = ctk.CTkLabel(
            self.step_frame,
            text=f"🔍 Posicione o mouse sobre: {current_desc} e pressione Enter.",
            font=(Theme.FONT_FAMILY, 18),
            text_color=Theme.TEXT_MAIN,
            wraplength=550,
        )
        self.step_label.place(relx=0.5, rely=0.5, anchor="center")

        # Buttons Frame
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=30, pady=(0, 30))

        btn_font = (Theme.FONT_FAMILY, Theme.FONT_BUTTON_SIZE, "bold")

        self.btn_capture = ctk.CTkButton(
            button_frame,
            text="Capturar Próximo",
            command=self.capture_step,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.PRIMARY_HOVER,
            corner_radius=Theme.CORNER_RADIUS,
            height=Theme.BUTTON_HEIGHT,
            font=btn_font,
            image=self.icons.get("capture"),
            compound="left",
        )
        self.btn_capture.pack(side="left", expand=True, padx=5)

        self.btn_save = ctk.CTkButton(
            button_frame,
            text="Salvar Calibração",
            command=self.save_calibration,
            state="disabled",
            fg_color=Theme.SECONDARY,
            hover_color=Theme.SECONDARY_HOVER,
            text_color="black",  # Contrast on Cyan
            corner_radius=Theme.CORNER_RADIUS,
            height=Theme.BUTTON_HEIGHT,
            font=btn_font,
            image=self.icons.get("save"),
            compound="left",
        )
        self.btn_save.pack(side="left", expand=True, padx=5)

        self.btn_cancel = ctk.CTkButton(
            button_frame,
            text="Cancelar",
            command=self.calibration_window.destroy,
            fg_color="transparent",
            border_width=1,
            border_color=Theme.DANGER,
            text_color=Theme.DANGER,
            hover_color=Theme.SURFACE_HOVER,
            corner_radius=Theme.CORNER_RADIUS,
            height=Theme.BUTTON_HEIGHT,
            font=btn_font,
            image=self.icons.get("cancel"),
            compound="left",
        )
        self.btn_cancel.pack(side="left", expand=True, padx=5)

        # Bind Enter Key
        self.calibration_window.bind("<Return>", lambda event: self.capture_step())

        # Restore Main Window on Close
        self.calibration_window.protocol("WM_DELETE_WINDOW", self._on_calibration_close)
        self.btn_cancel.configure(command=self._on_calibration_close)

    def _on_calibration_close(self):
        """Restores main window when calibration is closed."""
        self.calibration_window.destroy()
        self.deiconify()

    def _apply_calibration_icon(self):
        """Helper to apply icon to calibration window."""
        try:
            if self.icon_image:
                # Create a CTkImage for the icon
                icon = ImageTk.PhotoImage(self.icon_image)
                self.calibration_window.iconphoto(False, icon)
            elif self.icon_path and self.icon_path.endswith(".ico"):
                self.calibration_window.iconbitmap(self.icon_path)
        except Exception as e:
            logging.error(f"Failed to set calibration icon delayed: {e}")

    def capture_step(self):
        """Captures the current mouse position for the active step."""
        if self.current_step_index < len(self.calibration_steps):
            # Capture
            x, y = pyautogui.position()
            step_data = self.calibration_steps[self.current_step_index]
            step_key = step_data["key"]
            step_desc = step_data["desc"]

            self.captured_coords[step_key] = {"x": x, "y": y}
            self.log(f"Capturado '{step_desc}' em: ({x}, {y})")

            # Advance
            self.current_step_index += 1

            # Update UI for next step
            if self.current_step_index < len(self.calibration_steps):
                next_desc = self.calibration_steps[self.current_step_index]["desc"]
                self.step_label.configure(
                    text=f"🔍 Posicione o mouse sobre: {next_desc} e pressione Enter."
                )
            else:
                # Finished
                self.step_label.configure(
                    text="✅ Calibração concluída! Clique em Salvar."
                )
                self.btn_capture.configure(state="disabled")
                self.btn_save.configure(state="normal")
                # Unbind Enter to prevent accidental triggers, or rebind to save
                self.calibration_window.unbind("<Return>")
                self.calibration_window.bind(
                    "<Return>", lambda event: self.save_calibration()
                )

    def save_calibration(self):
        """Saves the captured coordinates and resolution to a JSON file."""
        try:
            # Capture current screen resolution
            screen_width, screen_height = pyautogui.size()

            data = {
                "resolution": {"width": screen_width, "height": screen_height},
                "coordinates": self.captured_coords,
            }

            with open("calibration_config.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            self.log(
                f"Calibração salva em 'calibration_config.json' (Resolução: {screen_width}x{screen_height})."
            )
            tkinter.messagebox.showinfo(
                "Sucesso", "Calibração e resolução salvas com sucesso!"
            )
            self._on_calibration_close()
        except Exception as e:
            self.log(f"Erro ao salvar calibração: {e}")
            logging.error(f"Failed to save calibration: {e}")
            tkinter.messagebox.showerror("Erro", f"Falha ao salvar: {e}")

    def _center_window(self, window, width, height):
        """Centers the window on the screen."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (int(screen_width) - int(width)) // 2
        y = (int(screen_height) - int(height)) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def _force_dark_title_bar(self, window):
        """Forces the title bar to be dark using Windows API."""
        try:
            window.update()
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
            get_parent = ctypes.windll.user32.GetParent
            hwnd = get_parent(window.winfo_id())
            rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
            value = 2
            value = ctypes.c_int(value)
            set_window_attribute(
                hwnd, rendering_policy, ctypes.byref(value), ctypes.sizeof(value)
            )
        except Exception as e:
            logging.error(f"Failed to force dark title bar: {e}")

    def open_logs(self):
        """Opens the logs directory."""
        log_dir = os.path.abspath("logs")
        if os.path.exists(log_dir):
            os.startfile(log_dir)
        else:
            self.log("Diretório de logs não encontrado.")

    def run_automation(self):
        try:
            # Pass the log method to the automation core
            self.automation.run_safe(
                logger=lambda msg: self.after(0, lambda: self.log(msg))
            )
        except Exception:
            self.after(0, lambda: self.log(f"Erro: {e}"))
        finally:
            self.after(0, lambda: self.start_button.configure(state="normal"))
            self.after(0, lambda: self.stop_button.configure(state="disabled"))
            self.after(0, lambda: self.calibrate_button.configure(state="normal"))
            self.after(0, lambda: self.export_button.configure(state="normal"))
            self.after(0, lambda: self.import_button.configure(state="normal"))

    def import_calibration(self):
        """Imports a calibration file from the filesystem."""
        file_path = tkinter.filedialog.askopenfilename(
            title="Selecione o arquivo de calibração",
            filetypes=[("Arquivos JSON", "*.json"), ("Todos os arquivos", "*.*")],
            initialdir="backups" if os.path.exists("backups") else ".",
        )

        if not file_path:
            return  # User cancelled

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Simple validation
            if "coordinates" not in data or "resolution" not in data:
                tkinter.messagebox.showerror(
                    "Erro de Validação",
                    "O arquivo selecionado não parece ser um arquivo de calibração válido.",
                )
                return

            # Check if source and destination are the same to avoid shutil error
            dest_path = os.path.abspath("calibration_config.json")
            if os.path.abspath(file_path) == dest_path:
                self.log("O arquivo selecionado já é a configuração atual.")
                tkinter.messagebox.showinfo(
                    "Informação", "O arquivo selecionado já é a configuração atual."
                )
                return

            # Overwrite current config
            shutil.copy2(file_path, "calibration_config.json")

            self.log(
                f"Calibração importada com sucesso de: {os.path.basename(file_path)}"
            )
            tkinter.messagebox.showinfo(
                "Sucesso", "Calibração importada e aplicada com sucesso!"
            )

        except json.JSONDecodeError:
            tkinter.messagebox.showerror(
                "Erro", "O arquivo selecionado não é um JSON válido."
            )
        except Exception as e:
            self.log(f"Erro ao importar calibração: {e}")
            logging.error(f"Failed to import calibration: {e}")
            tkinter.messagebox.showerror("Erro", f"Falha ao importar: {e}")

    def export_calibration(self):
        """Exports the current calibration file to the backups folder."""
        config_path = "calibration_config.json"
        if not os.path.exists(config_path):
            self.log("Erro: Arquivo de calibração não encontrado para exportar.")
            tkinter.messagebox.showwarning(
                "Aviso",
                "Arquivo de calibração não encontrado.\nFaça a calibração primeiro.",
            )
            return

        backup_dir = "backups"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"calibration_backup_{timestamp}.json"
        backup_path = os.path.join(backup_dir, backup_filename)

        try:
            shutil.copy2(config_path, backup_path)
            self.log(f"Backup criado com sucesso: {backup_filename}")
            tkinter.messagebox.showinfo("Sucesso", f"Backup salvo em:\n{backup_path}")
        except Exception as e:
            self.log(f"Erro ao criar backup: {e}")
            logging.error(f"Failed to backup calibration: {e}")
            tkinter.messagebox.showerror("Erro", f"Falha ao criar backup: {e}")

    # System Tray Logic
    # (on_closing replaced by on_exit and check_minimize)

    def setup_tray_icon(self):
        """Creates and runs the system tray icon."""
        if self.icon_image:
            image = self.icon_image
        else:
            # Fallback
            image = Image.new("RGB", (64, 64), color=(73, 109, 137))
            d = ImageDraw.Draw(image)
            d.rectangle([16, 16, 48, 48], fill=(255, 255, 255))

        menu = pystray.Menu(
            pystray.MenuItem("Abrir", self.show_window, default=True, visible=False),
            pystray.MenuItem("Iniciar Automação", self.start_from_tray),
            pystray.MenuItem("Sair", self.quit_application),
        )

        self.tray_icon = pystray.Icon(
            "Automação Microsoft Rewards", image, "Automação Microsoft Rewards", menu
        )
        self.tray_icon.run()

    def start_from_tray(self, icon, item):
        """Starts automation from tray menu."""
        self.show_window(icon, item)
        self.start_automation_thread()

    def show_window(self, icon, item):
        """Restores the window from tray."""
        self.tray_icon.stop()
        self.after(0, self.deiconify)

    def quit_application(self, icon, item):
        """Confirms exit and closes application from tray."""
        icon.stop()
        self.after(0, self.on_exit)

    def on_exit(self):
        """Exits the application directly."""
        self.deiconify()  # Ensure window is visible for the dialog
        if tkinter.messagebox.askyesno("Sair", "Deseja realmente sair da aplicação?"):
            self.quit()
            self.destroy()
            try:
                os._exit(0)
            except:
                pass
        else:
            # If user cancelled exit from tray, window is already restored by deiconify
            pass

    def check_minimize(self, event):
        """Checks if window was minimized to hide it to tray."""
        # Only trigger if the event is for the main window and state is iconic
        if event.widget == self and self.state() == "iconic":
            self.withdraw()
            threading.Thread(target=self.setup_tray_icon, daemon=True).start()
