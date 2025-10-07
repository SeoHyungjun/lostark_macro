
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

        if repeat_count < 1:
            print("  - 반복 횟수가 1보다 작아 뽑기를 실행하지 않습니다.")
            return

        # 1. 첫 번째 뽑기
        initial_button_text = f"{draw_type:,} 뽑기"
        try:
            print(f"  - '{initial_button_text}' 버튼을 찾습니다.")
            initial_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[.//span[normalize-space()='{initial_button_text}']]"))
            )
            highlight(initial_button, self.driver)
            initial_button.click()
            time.sleep(2) # 팝업이 뜰 시간을 줍니다.
        except Exception:
            print(f"    - '{initial_button_text}' 버튼을 찾을 수 없어 뽑기를 중단합니다.")
            return

        # 2. 두 번째 이후의 반복 뽑기
        if repeat_count > 1:
            repeat_button_text = f"{draw_type:,} 뽑기 한번 더!"
            print(f"  - '{repeat_button_text}' 버튼으로 나머지 {repeat_count - 1}회를 반복합니다.")
            for i in range(2, repeat_count + 1):
                try:
                    repeat_button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, f"//button[.//span[normalize-space()='{repeat_button_text}']]"))
                    )
                    highlight(repeat_button, self.driver, duration=0.5)
                    repeat_button.click()
                    time.sleep(0.1)
                except Exception:
                    print(f"    - '{repeat_button_text}' 버튼을 더 이상 찾을 수 없어 뽑기를 중단합니다.")
                    break
