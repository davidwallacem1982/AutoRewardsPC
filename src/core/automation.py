import json
import os
import random
import re
import subprocess
import time

import pyautogui
import pygetwindow as gw
import pyperclip
import pytesseract

from .settings import Settings

try:
    from src.domain.items import gerar_lista_itens
except ImportError:
    from domain.items import gerar_lista_itens


class Automation:
    def __init__(self):
        self.settings = Settings()
        self.running = False
        # Explicitly set the tesseract executable path for pytesseract
        if self.settings.validate():
            pytesseract.pytesseract.tesseract_cmd = self.settings.tesseract_path

    def check_environment(self):
        """
        Verifies if the environment is ready for automation.
        """
        if not self.settings.validate():
            return False
        return True

    def open_browser(self, logger):
        """Opens the browser specified in settings and maximizes it."""
        try:
            subprocess.Popen(self.settings.chrome_path)
            logger(f"Launching Chrome from {self.settings.chrome_path}...")
            # Wait for browser to open
            time.sleep(3)

            # Find and maximize window
            windows = gw.getWindowsWithTitle("Google Chrome")
            if not windows:
                # Fallback search if title is different (e.g. active tab name)
                windows = gw.getWindowsWithTitle("Chrome")

            if windows:
                window = windows[0]
                if not window.isMaximized:
                    logger("Maximizing browser window...")
                    window.maximize()
            else:
                logger("Could not find Chrome window to maximize.")

        except Exception as e:
            logger(f"Error opening/maximizing browser: {e}")
            raise

    def load_config(self):
        """Loads the calibration configuration from JSON."""
        config_path = "calibration_config.json"
        if not os.path.exists(config_path):
            return None

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def _click_element(self, logger, config, key, description):
        """Helper to click an element based on configuration."""
        if not self.running:
            return

        if "coordinates" in config and key in config["coordinates"]:
            coords = config["coordinates"][key]
            x, y = coords["x"], coords["y"]
            # logger(f"Clicando em '{description}' ({x}, {y})...") # Reduced verbosity
            pyautogui.click(x, y)
            time.sleep(1)  # Default wait
        else:
            logger(f"Aviso: Coordenada para '{description}' não encontrada.")

    def _get_coords(self, config, key):
        if "coordinates" in config and key in config["coordinates"]:
            return config["coordinates"][key]["x"], config["coordinates"][key]["y"]
        return None, None

    def check_score(self, logger, config):
        """Checks if the score reached the target (e.g. 90/90, 60/60) using OCR and Regex."""
        try:
            # Target near "PC Search" text, slightly below
            base_x, base_y = self._get_coords(config, "abrir_pc_search")
            if base_x is None:
                logger(
                    "Erro: Coordenada 'abrir_pc_search' necessária para verificar pontuação."
                )
                return False

            # Capture region below the "PC Search" click point
            region_x = base_x - 100
            region_y = base_y
            region_w = 200
            region_h = 100

            logger(
                f"Verificando pontuação na região: ({region_x}, {region_y}, {region_w}, {region_h})..."
            )

            screenshot = pyautogui.screenshot(
                region=(region_x, region_y, region_w, region_h)
            )

            # Use Tesseract
            text = pytesseract.image_to_string(screenshot)
            text = text.strip()

            # Common OCR corrections for "PC Search"
            # Fix "FC searcn", "FC Search", "PC Searcn", etc.
            text = re.sub(r"(?i)fc\s*searc[hn]", "PC Search", text)
            text = re.sub(r"(?i)pc\s*searc[hn]", "PC Search", text)  # Normalize casing
            text = re.sub(
                r"(?i)me\s*sealCr", "em PC Search", text
            )  # Fix specific OCR error

            logger(f"Texto detectado: {text}")

            # Regex to find pattern "Number / Number" (e.g. 90/90, 60 / 60, 12/90)
            match = re.search(r"(\d+)\s*/\s*(\d+)", text)

            if match:
                current_score = int(match.group(1))
                total_score = int(match.group(2))

                logger(f"Pontuação identificada: {current_score} / {total_score}")

                if current_score >= total_score:
                    return True
            else:
                logger("Nenhuma pontuação no formato 'X / Y' encontrada.")

            return False
        except Exception as e:
            logger(f"Erro ao verificar pontuação: {e}")
            return False

    def stop(self):
        """Stops the running automation."""
        self.running = False

    def run_safe(self, logger=print):
        """
        Executes automation logic safely.
        """
        if not self.check_environment():
            logger("Environment check failed. Aborting.")
            # Continue anyway if just Tesseract is missing, as we only need Chrome for now
            # But check_environment calls validate which returns False if Chrome missing.
            if not self.settings.validate():
                return

        logger("")
        self.running = True

        try:
            # Load Calibration
            config = self.load_config()
            if not config:
                logger(
                    "Erro: Arquivo de calibração 'calibration_config.json' não encontrado. Por favor, calibre antes."
                )
                return

            self.open_browser(logger)
            logger("Navegador aberto e maximizado..")
            time.sleep(2)

            # 1. Setup Phase - Go to Search Bar
            setup_steps = [
                ("botao_microsoft_rewards", "Botão Rewards"),
                ("detalhamentos_pontos", "Detalhamento de Pontos"),
                ("abrir_pc_search", "PC Search"),
                ("barra_pesquisa", "Barra de Pesquisa"),
            ]

            for key, desc in setup_steps:
                if not self.running:
                    break
                self._click_element(logger, config, key, desc)
                time.sleep(1)

                # Verificação antecipada de pontos
                if key == "detalhamentos_pontos":
                    logger("Verificando status da pontuação...")
                    time.sleep(2)  # Aguarda a interface atualizar
                    if self.check_score(logger, config):
                        logger(
                            "META DIÁRIA JÁ ATINGIDA! Volte amanhã\nseu fominha por pontos🖕"
                        )
                        pyautogui.hotkey("ctrl", "shift", "w")  # Fecha o navegador
                        self.stop()
                        return

            # 2. Search Loop
            items = gerar_lista_itens(500)
            logger(f"Iniciando ciclo de pesquisas com {len(items)} itens...")

            for i, item in enumerate(items):
                if not self.running:
                    break

                # Check Score every 10 searches
                if i > 0 and i % 10 == 0:
                    logger(f"Verificação de pontuação ({i}/500)...")
                    # Go to Main Tab
                    self._click_element(
                        logger, config, "aba_principal", "Aba Principal"
                    )
                    time.sleep(3)  # Wait for page load

                    # Check Score
                    if self.check_score(logger, config):
                        logger("META DE PONTOS ATINGIDA!")
                        logger("Fechando navegador e encerrando automação...")
                        # Close the entire Chrome window (all tabs)
                        pyautogui.hotkey("ctrl", "shift", "w")
                        if self.running:
                            self.running = False
                        break

                    # Return to Search
                    logger("Meta não atingida. Retornando para pesquisas...")
                    self._click_element(logger, config, "aba_pesquisa", "Aba Pesquisa")
                    time.sleep(1)
                    self._click_element(
                        logger, config, "barra_pesquisa", "Barra de Pesquisa"
                    )
                    time.sleep(1)

                # Perform Search
                logger(f"Pesquisando: {item}")

                # Clear field (Ctrl+A, Del) ensures we don't append
                pyautogui.hotkey("ctrl", "a")
                time.sleep(0.1)
                pyautogui.press("delete")
                time.sleep(0.1)

                # Type and Enter - Using Clipboard for Accents
                # pyautogui.write(item, interval=0.05) # Fails with accents on some systems
                pyperclip.copy(item)
                time.sleep(0.1)
                pyautogui.hotkey("ctrl", "v")
                time.sleep(0.1)
                pyautogui.press("enter")

                # Wait random interval
                sleep_time = random.uniform(2, 4)
                time.sleep(sleep_time)

                # Re-focus search bar for next iteration?
                # Usually bing search results page keeps bar accessible or we might need to click it again.
                # The prompt says: "continue os clicks em aba principal e depois aba pesquisa e novamente em barra pesquisa"
                # ONLY for the 10th item check.
                # For normal loop, we just need to be in the bar.
                # "quando ela chegar em barra pesquisa... continue as pesquisas" implies we are in the bar.
                # But after pressing enter, focus might be lost or page reloads.
                # Safest is to click "barra_pesquisa" again between every search?
                # Or assumes the page layout has the bar in the same place.
                # Let's ensure focus by clicking bar every time?
                # The user didn't explicitly ask to click bar every time, but "os clicks parem lá, com o cursor focado".
                # For the loop, we probably need to click the bar to type again.
                self._click_element(
                    logger, config, "barra_pesquisa", "Barra de Pesquisa (Refocus)"
                )

            if self.running:
                logger("Automação finalizada.")

        except Exception as e:
            logger(f"Critical Error: {e}")
        finally:
            self.running = False
