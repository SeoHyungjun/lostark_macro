import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from src.config import load_yaml_config
from src.browser.login_page import LoginPage
from src.actions import ACTION_MAP

def main():
    """메인 실행 함수"""
    # 1. 설정 로드
    ids_config = load_yaml_config("ids.yaml")
    steps_config = load_yaml_config("pages.yaml")

    if not ids_config or not steps_config:
        return

    accounts = ids_config.get("accounts", [])
    steps = steps_config if isinstance(steps_config, list) else []

    if not accounts or not steps:
        print("설정 파일에 계정 정보 또는 매크로 단계가 없습니다.")
        return

    # 2. 웹 드라이버 초기화
    options = Options()
    options.page_load_strategy = 'eager'
    # options.add_argument("--headless")  # 백그라운드 실행을 원할 경우 주석 해제
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(ChromeDriverManager().install())
    
    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=options)
        login_page = LoginPage(driver)

        # 3. 계정 루프 시작
        for account in accounts:
            user_id = account.get("id")
            user_password = account.get("password")

            if not all([user_id, user_password]):
                print("ID 또는 비밀번호가 없는 계정이 있어 건너뜁니다.")
                continue

            # 3-1. 로그인
            if not login_page.login(user_id, user_password):
                print(f"{user_id} 계정 로그인에 실패하여 다음으로 넘어갑니다.")
                continue
            
            # 3-2. 작업 루프 시작
            print(f"\n--- {user_id} 계정의 매크로 단계를 시작합니다. ---")
            for step in steps:
                action_name = step.get("action")
                action_class = ACTION_MAP.get(action_name)
                
                if not action_class:
                    print(f"- 알 수 없는 액션({action_name})입니다. 건너뜁니다.")
                    continue

                print(f"- 작업: {step.get('name', action_name)}")
                try:
                    action_instance = action_class(driver, step.get("url"))
                    action_instance.execute(step.get("details", {}))
                except Exception:
                    print(f"  - 작업 실행 중 오류 발생:")
                    traceback.print_exc() # 상세 오류 내용 출력

            print(f"\n--- {user_id} 계정의 모든 작업이 완료되었습니다. ---")

    except Exception:
        print(f"스크립트 실행 중 예기치 않은 오류가 발생했습니다:")
        traceback.print_exc() # 상세 오류 내용 출력
    finally:
        # 4. 드라이버 종료
        if driver:
            print("\n모든 작업이 종료되었습니다. 3초 후 브라우저를 닫습니다.")
            time.sleep(3)
            driver.quit()

if __name__ == "__main__":
    main()