import os

class Settings:
    def __init__(self):
        self.tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.screen_resolution = (1920, 1080)
        self.search_count = 30
        self.search_url = "https://www.bing.com"
        self.min_delay = 2
        self.max_delay = 5
        
    def validate(self):
        if not os.path.exists(self.tesseract_path):
            print(f"WARNING: Tesseract not found at {self.tesseract_path}. OCR features will fail.")
            # return False # Non-blocking for now if only doing search
        
        if not os.path.exists(self.chrome_path):
            print(f"WARNING: Chrome not found at {self.chrome_path}.")
            return False
            
        return True
