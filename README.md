
# 로스트아크 웹 이벤트 매크로

이 프로젝트는 Selenium을 사용하여 로스트아크 웹사이트에서 진행되는 이벤트(출석 체크, 보상 받기 등)를 자동으로 수행하는 파이썬 스크립트입니다.

## 시작하기

매크로를 실행하기 위해 필요한 몇 가지 준비 과정입니다.

### 1. 필요 라이브러리 설치

이 프로젝트는 다음 라이브러리를 사용합니다. `requirements.txt` 파일을 이용해 한 번에 설치할 수 있습니다.

```bash
pip install -r requirements.txt
```

### 2. 계정 정보 설정

프로젝트에 포함된 `ids_example.yaml` 파일을 복사하여 `ids.yaml`이라는 이름으로 파일을 새로 만듭니다.

- **Windows:**
```bash
copy ids_example.yaml ids.yaml
```

- **macOS / Linux:**
```bash
cp ids_example.yaml ids.yaml
```

그 다음, `ids.yaml` 파일을 열어 `YOUR_ID`와 `YOUR_PASSWORD` 부분을 실제 계정 정보로 채워넣습니다. 여러 계정을 사용하려면 `accounts` 목록에 계정 정보를 추가할 수 있습니다.

**`ids.yaml` 파일 예시:**
```yaml
# 매크로를 실행할 계정 목록을 여기에 추가합니다.
# 각 계정은 `-` (하이픈)으로 시작해야 하며, id와 password를 한 쌍으로 갖습니다.
# 여러 계정을 추가하려면 아래 형식을 복사하여 붙여넣으세요.
accounts:
  - id: "my_id_123"         # 실제 아이디로 변경
    password: "my_password_456" # 실제 비밀번호로 변경
#  - id: "another_id_789"
#    password: "another_password_123"
```

**주의**: `ids.yaml` 파일은 개인정보를 담고 있으므로, `.gitignore`에 포함되어 GitHub에 올라가지 않습니다. 절대로 공개된 장소에 이 파일을 공유하지 마세요.

### 3. 실행할 작업 설정

`pages.yaml` 파일에서 원하는 작업과 순서를 정의할 수 있습니다. `action` 항목에는 수행할 작업의 종류("출석", "뽑기" 등)를, `url`에는 해당 이벤트 페이지의 주소를 입력합니다.

## 사용법

모든 설정이 완료되면, 터미널에서 아래 명령어를 실행하여 매크로를 시작합니다.

```bash
python main.py
```
