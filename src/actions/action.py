
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Action(ABC):
    """모든 작업 클래스의 기반이 되는 추상 베이스 클래스"""
    def __init__(self, driver: webdriver.Chrome, url: str):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.url = url

    @abstractmethod
    def execute(self, details: dict):
        """작업의 실제 로직을 구현합니다."""
        pass
