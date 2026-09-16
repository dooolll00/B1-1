# B1-1 — 반응형 포트폴리오

순수 HTML, CSS, JavaScript로 만든 개인 포트폴리오입니다. 자기소개와 기술 스택을 소개하고, GitHub의 공개 저장소를 프로젝트 카드로 보여 줍니다. 모바일·태블릿·데스크톱 화면과 라이트·다크 모드를 지원합니다.

- [사이트 보기](https://dooolll00.github.io/B1-1/)
- [GitHub 저장소](https://github.com/dooolll00/B1-1)

## 주요 기능

| 기능 | 내용 |
| --- | --- |
| 페이지 구성 | Hero, About, Skills, Projects, Contact, Footer |
| 반응형 메뉴 | 모바일 햄버거 메뉴, 다시 클릭·Escape·외부 클릭으로 닫기 |
| 스크롤 | 섹션으로 부드럽게 이동, 헤더 배경 변경, 맨 위 버튼, 구역 등장 애니메이션 |
| 테마 | 다크 모드 전환·저장·복원, 직접 선택하기 전에는 시스템 테마 반영 |
| 프로젝트 | 실제 GitHub 저장소 조회, 언어별 필터, 로딩·오류·빈 결과 안내와 재시도 |
| 문의 폼 | 이름·이메일·메시지 검사, 필드별 오류 안내, 글자 수와 검증 성공 표시 |
| 접근성 | 이미지 설명, 입력 레이블, 키보드 포커스, 본문 바로가기, 동작 줄이기 설정 지원 |

문의 폼은 **입력값 검증 데모**입니다. 메시지를 서버에 저장하거나 실제 이메일로 보내지는 않습니다.

## 사용 기술

- **HTML5:** 시맨틱 구조와 폼
- **CSS3:** CSS 변수, Flexbox, Grid, 미디어 쿼리, 전환 효과
- **JavaScript ES6+:** DOM·이벤트·상태 관리, Fetch API, async/await, Intersection Observer
- **GitHub REST API / GitHub Pages:** 공개 저장소 데이터와 정적 사이트 배포
- **Pretendard:** CDN 웹 폰트. 로딩 실패 시 시스템 폰트 사용

사이트는 프레임워크나 별도의 빌드 과정 없이 실행됩니다. Python과 Playwright는 개발용 자동 검사에만 사용합니다.

## 로컬 실행

1. VS Code에서 `B1-1` 폴더를 엽니다.
2. **Live Server** 확장(`ritwickdey.LiveServer`)을 설치합니다.
3. `index.html`을 우클릭하고 **Open with Live Server**를 선택합니다.
4. `http://127.0.0.1:5500`에 접속합니다.

`.vscode`에 확장 추천과 주소·포트 설정이 들어 있습니다. 확장은 사용하는 VS Code 환경마다 설치해야 합니다.

Python이 있다면 아래 명령으로도 실행할 수 있습니다.

```bash
python3 -m http.server 5500 --bind 127.0.0.1
```

## 화면과 동작 설정

| 항목 | 현재 값 |
| --- | --- |
| 반응형 기준 | 모바일 기본, 768px 이상 태블릿, 1024px 이상 데스크톱 |
| 헤더 배경 변경 | 스크롤 60px 이상 |
| 맨 위 버튼 표시 | 스크롤 300px 이상 |
| 등장 애니메이션 | Intersection Observer `threshold: 0.2`, 한 번 실행 |
| 테마 저장 키 | `portfolio-theme` |
| 메시지 최대 길이 | 2,000자 |

라이트 모드는 블루, 다크 모드는 퍼플을 강조색으로 사용합니다. 색상·폰트·간격은 `css/style.css`의 CSS 변수로 관리합니다. 운영체제의 동작 줄이기 설정을 켜면 애니메이션과 부드러운 스크롤을 생략합니다.

## GitHub 프로젝트 조회

현재 계정은 `dooolll00`이며 다음 주소에서 최근 업데이트 순으로 공개 저장소를 가져옵니다.

```text
https://api.github.com/users/dooolll00/repos?sort=updated&per_page=100&page=1
```

- 한 번에 100개씩 조회하고, 필요한 경우 다음 페이지도 가져옵니다.
- 성공한 응답은 `portfolio-repos-dooolll00` 키에 5분간 저장합니다. 손상되거나 만료된 캐시는 사용하지 않습니다.
- 전체 조회가 15초를 넘으면 요청을 중단하고 재시도 안내를 표시합니다.
- 요청 한도·접근 제한, 계정 없음, 서버 오류, 네트워크 오류를 처리합니다.
- 재시도 버튼은 캐시를 건너뛰고 다시 요청합니다.
- 언어가 없는 저장소는 `기타`로 분류하며 fork 저장소도 포함합니다.
- 브라우저 저장소가 차단되어도 현재 페이지는 동작하지만, 테마 저장·복원과 캐시는 사용할 수 없습니다.

계정을 변경하려면 `js/main.js`의 `GITHUB_USERNAME`과 HTML의 소개·GitHub 링크, 프로필 이미지를 함께 수정합니다.

## 자동 검사

Python 3와 Google Chrome이 필요합니다. 프로젝트 루트에서 검사 환경과 로컬 서버를 준비합니다.

```bash
python3 -m venv /tmp/b1-1-review-venv
/tmp/b1-1-review-venv/bin/pip install playwright
python3 -m http.server 5511 --bind 127.0.0.1
```

서버를 켜 둔 채 다른 터미널에서 실행합니다.

```bash
# 모의 API로 기능 검사
/tmp/b1-1-review-venv/bin/python tests/review.py

# 실제 API·공개 사이트까지 검사하고 스크린샷 갱신
/tmp/b1-1-review-venv/bin/python tests/review.py --live
```

일반 실행은 GitHub API를 모의 응답으로 대체합니다. `--live`는 실제 API를 호출하고 `images/screenshots/`의 이미지 3개를 덮어씁니다. 배포는 수행하지 않습니다.

2026-09-16, Chrome **146.0.7680.165**에서 현재 코드의 기본 검사 27개와 실제 API·공개 사이트 검사 2개, **총 29개 검사가 통과**했습니다. 이후 최신 정리본의 Pages 배포를 완료하고 공개 HTML·CSS·JS와 로컬 파일의 일치, 테마 저장·폼·모바일 메뉴·스크롤·반응형·실제 API 동작을 다시 확인했습니다. 배포 이력은 `WORK_LOG.md`에 기록합니다.

검사 범위는 HTML 구조, 320/375/767/768/1024/1440px 반응형, 메뉴·스크롤·테마·폼·필터, API 상태와 재시도, 캐시·페이지네이션·시간 제한, 외부 데이터 처리입니다. 확인한 브라우저와 시나리오를 기준으로 한 결과입니다.

## 스크린샷

현재와 같은 디자인으로 2026-09-07 촬영한 화면입니다. 저장소 목록은 GitHub의 실제 데이터에 따라 개수와 순서가 달라집니다.

| 데스크톱 · 1440px | 모바일 · 375px | 다크 모드 · 1440px |
| --- | --- | --- |
| ![라이트 모드 데스크톱](images/screenshots/desktop.png) | ![모바일 화면](images/screenshots/mobile.png) | ![다크 모드 데스크톱](images/screenshots/dark.png) |

## 배포

GitHub Pages를 사용하며 별도의 빌드 명령은 없습니다.

1. 변경 파일을 검토하고 커밋하여 `main` 브랜치에 업로드합니다.
2. 저장소 **Settings → Pages**에서 배포 소스를 **Deploy from a branch**, 브랜치를 **main**, 폴더를 **/ (root)**로 설정합니다.
3. GitHub Actions의 **pages build and deployment** 완료를 확인합니다.
4. 공개 사이트에서 메뉴·테마 저장·폼·GitHub 프로젝트 조회가 정상 동작하는지 확인합니다.

CSS·JavaScript·이미지는 상대 경로로 연결되어 `/B1-1/` 하위 주소에서도 사용할 수 있습니다.
