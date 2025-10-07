
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .action import Action
from ..utils import highlight

class ClaimRewardAction(Action):
    """'뽑기' 작업을 수행하는 클래스"""
    ACTION_NAME = "뽑기"
    def execute(self, details: dict):
        self.driver.get(self.url)
        draw_type = details.get("draw_type", 100)
        repeat_count = details.get("repeat", 1)
        button_text = f"{draw_type:,} 뽑기"
        
        print(f"  - '{button_text}'를 {repeat_count}회 반복합니다.")
        for i in range(1, repeat_count + 1):
            try:
                claim_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, f"//button[.//span[normalize-space()='{button_text}']]"))
                )
                highlight(claim_button, self.driver, duration=0.5)
                claim_button.click()
                print(f"    - 뽑기 {i}/{repeat_count}회 완료.")
                time.sleep(0.5)
            except Exception:
                print("    - 버튼을 더 이상 찾을 수 없어 뽑기를 중단합니다.")
                break
