import yaml

def load_yaml_config(filepath: str) -> dict | None:
    """YAML 파일을 읽어서 내용을 반환합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"오류: {filepath} 파일을 찾을 수 없습니다.")
        return None
    except Exception as e:
        print(f"오류: {filepath} 파일을 읽는 중 오류 발생: {e}")
        return None