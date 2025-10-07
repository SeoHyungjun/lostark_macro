
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .action import Action
from ..utils import highlight

class CheckInAction(Action):
    """'출석' 작업을 수행하는 클래스"""
    ACTION_NAME = "출석"
    def execute(self, details: dict):
        try:
            self.driver.get(self.url)
            try:
                popup_close_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.dialog-close"))
                )
                highlight(popup_close_button, self.driver)
                popup_close_button.click()
                print("  - 팝업을 닫았습니다.")
            except Exception:
                pass

            check_in_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='오늘의 아이템 받기']]"))
            )
            highlight(check_in_button, self.driver)
            check_in_button.click()
            print("  - '오늘의 아이템 받기' 완료.")
        except Exception:
            print("  - 이미 처리했거나, 출석 체크 버튼을 찾을 수 없습니다.")
