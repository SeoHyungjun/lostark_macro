
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

def highlight(element: WebElement, driver: webdriver.Chrome, duration: float = 1):
    """요소를 시각적으로 강조 표시합니다 (반투명 빨간색 배경)."""
    try:
        original_style = driver.execute_script("return arguments[0].getAttribute('style');", element)
        style = f"outline: 2px solid red; background-color: rgba(255, 0, 0, 0.2);"
        driver.execute_script(f"arguments[0].setAttribute('style', '{style}');", element)
        time.sleep(duration)
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)
    except Exception as e:
        print(f"하이라이트 중 오류: {e}")
