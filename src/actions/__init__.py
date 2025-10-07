
import pkgutil
import importlib
import inspect
from pathlib import Path

from .action import Action

# 액션 이름과 클래스를 매핑할 딕셔너리
ACTION_MAP = {}

def _register_actions():
    """현재 패키지 내의 모든 Action 서브클래스를 찾아 ACTION_MAP에 동적으로 등록합니다."""
    package_path = Path(__file__).parent
    package_name = package_path.name

    # 현재 패키지 내의 모든 모듈을 순회합니다.
    for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):
        if module_name == 'action':
            continue

        # 모듈을 동적으로 임포트합니다.
        module = importlib.import_module(f'.{module_name}', package=f'src.{package_name}')

        # 모듈 내의 모든 멤버(클래스 등)를 확인합니다.
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # Action의 서브클래스이고, ACTION_NAME 속성이 있는지 확인합니다.
            if issubclass(obj, Action) and obj is not Action and hasattr(obj, 'ACTION_NAME'):
                ACTION_MAP[obj.ACTION_NAME] = obj

# 함수를 호출하여 액션을 등록합니다.
_register_actions()
