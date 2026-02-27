import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Ensure src is in the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.automation import Automation

class TestOCRIntegration(unittest.TestCase):
    def setUp(self):
        # Mock Settings to avoid validation errors during initialization
        with patch('src.core.automation.Settings') as MockSettings:
            instance = MockSettings.return_value
            instance.validate.return_value = True
            instance.tesseract_path = "dummy_path"
            self.automation = Automation()

    @patch('pytesseract.image_to_string')
    @patch('pyautogui.screenshot')
    def test_check_score_success_90_90(self, mock_screenshot, mock_ocr):
        """Testa se a pontuação 90/90 é reconhecida corretamente (Meta Atingida)."""
        mock_ocr.return_value = "PC Search 90 / 90"
        config = {"coordinates": {"abrir_pc_search": {"x": 100, "y": 100}}}
        
        logger = MagicMock()
        result = self.automation.check_score(logger, config)
        
        self.assertTrue(result)
        logger.assert_any_call("Pontuação identificada: 90 / 90")

    @patch('pytesseract.image_to_string')
    @patch('pyautogui.screenshot')
    def test_check_score_partial_30_90(self, mock_screenshot, mock_ocr):
        """Testa se a pontuação 30/90 não dispara o fim da automação."""
        mock_ocr.return_value = "PC Search 30/90"
        config = {"coordinates": {"abrir_pc_search": {"x": 100, "y": 100}}}
        
        logger = MagicMock()
        result = self.automation.check_score(logger, config)
        
        self.assertFalse(result)
        logger.assert_any_call("Pontuação identificada: 30 / 90")

    @patch('pytesseract.image_to_string')
    @patch('pyautogui.screenshot')
    def test_check_score_ocr_correction_fc_searcn(self, mock_screenshot, mock_ocr):
        """Testa a correção de erros comuns de OCR (FC Searcn -> PC Search)."""
        mock_ocr.return_value = "FC Searcn 90/90"
        config = {"coordinates": {"abrir_pc_search": {"x": 100, "y": 100}}}
        
        logger = MagicMock()
        result = self.automation.check_score(logger, config)
        
        self.assertTrue(result)
        logger.assert_any_call("Texto detectado: PC Search 90/90")

    @patch('pytesseract.image_to_string')
    @patch('pyautogui.screenshot')
    def test_check_score_ocr_correction_me_sealcr(self, mock_screenshot, mock_ocr):
        """Testa a correção de erro específico 'me sealCr'."""
        mock_ocr.return_value = "me sealCr 60/60"
        config = {"coordinates": {"abrir_pc_search": {"x": 100, "y": 100}}}
        
        logger = MagicMock()
        result = self.automation.check_score(logger, config)
        
        self.assertTrue(result)
        logger.assert_any_call("Texto detectado: em PC Search 60/60")

    @patch('pytesseract.image_to_string')
    @patch('pyautogui.screenshot')
    def test_check_score_no_pattern_found(self, mock_screenshot, mock_ocr):
        """Testa quando nenhum padrão de pontuação é encontrado."""
        mock_ocr.return_value = "Texto aleatório sem números"
        config = {"coordinates": {"abrir_pc_search": {"x": 100, "y": 100}}}
        
        logger = MagicMock()
        result = self.automation.check_score(logger, config)
        
        self.assertFalse(result)
        logger.assert_any_call("Nenhuma pontuação no formato 'X / Y' encontrada.")

    @patch('pytesseract.image_to_string')
    @patch('pyautogui.screenshot')
    def test_check_score_invalid_coordinates(self, mock_screenshot, mock_ocr):
        """Testa se a função lida corretamente com coordenadas ausentes."""
        config = {"coordinates": {}} # Sem 'abrir_pc_search'
        
        logger = MagicMock()
        result = self.automation.check_score(logger, config)
        
        self.assertFalse(result)
        logger.assert_any_call("Erro: Coordenada 'abrir_pc_search' necessária para verificar pontuação.")

if __name__ == '__main__':
    unittest.main()
