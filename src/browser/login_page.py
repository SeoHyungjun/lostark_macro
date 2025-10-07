
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..utils import highlight

class LoginPage:
    """로그인 기능만을 전담하는 클래스"""
    URL = "https://accounts.onstove.com/login"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, user_id, user_password) -> bool:
        print(f"\n--- {user_id} 계정으로 로그인합니다. ---")
        try:
            self.driver.get(self.URL)

            id_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#id")))
            highlight(id_input, self.driver)
            id_input.send_keys(user_id)

            pw_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#password")))
            highlight(pw_input, self.driver)
            pw_input.send_keys(user_password)

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='로그인']]" )))
            highlight(login_button, self.driver)
            login_button.click()

            self.wait.until(EC.url_changes(self.URL))
            print("로그인 성공.")
            return True
        except Exception as e:
            print(f"로그인 중 오류 발생: {e}")
            return False
