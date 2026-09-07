# B1-1 — 순수 웹 포트폴리오

HTML, CSS, JavaScript만으로 만든 반응형 포트폴리오입니다. **사용자 이벤트 → 상태 변경 → DOM 업데이트 → 화면 변화**를 직접 구현하는 미션이며, React 등 외부 라이브러리는 사용하지 않습니다.

- [GitHub 저장소](https://github.com/dooolll00/B1-1)
- [GitHub Pages 사이트](https://dooolll00.github.io/B1-1/)
- [단계별 구현 가이드](MISSION_GUIDE.md): 기능별 학습과 실습

## 검토 결론과 범위

2026-09-07에 구현 상태를 검토했습니다. 필수 기능을 구현했고, 아래 체크리스트에 근거를 연결했습니다. 최종 판단은 코드 확인, Chrome 동작 검증, 배포 확인을 구분합니다.

이번 보완에서는 모든 구역에 접근할 수 있도록 Footer 메뉴와 앵커를 추가했습니다. API 배열 내부의 잘못된 항목을 검사하고, 손상된 캐시는 무시한 뒤 다시 조회하도록 수정했습니다. 이전에는 `[null]` 같은 캐시가 남아 있으면 네트워크가 정상이어도 네트워크 오류로 표시됐습니다.

**배포 완료(2026-09-07):** 새 Footer 링크, 데이터 검증 보완, 블루·퍼플 디자인과 Pretendard가 공개 사이트에 반영됐습니다. 배포 커밋은 `e318a29`이며 [Pages 배포 작업](https://github.com/dooolll00/B1-1/actions/runs/34114075751)이 성공했습니다. 공개 HTML·CSS·JavaScript가 로컬 파일과 일치하고 실제 Chrome 주요 기능 검증도 통과했습니다.

## 디자인

사용자가 제안한 미니멀 블루(라이트)·미드나잇 퍼플(다크) 색상과 Pretendard 폰트를 적용했습니다. 공통 모서리 변수는 `10px`, 그림자는 밝은 테마에서 `0 10px 30px rgba(0, 0, 0, 0.05)`, 어두운 테마에서 같은 크기에 불투명도 `0.2`입니다. `--radius`와 `--shadow`를 참조하는 요소에 적용되며, 별도 값으로 지정된 Hero 그래픽의 색상·모서리는 기존 값을 사용합니다.

미션은 웹 폰트를 허용합니다. Pretendard는 UI 프레임워크가 아닌 웹 폰트이므로 이 조건에 부합하며, 스타일시트 맨 위의 `@import`로 불러옵니다. CDN에 연결할 수 없으면 뒤에 지정한 시스템 폰트로 표시합니다. 테마는 기존과 동일하게 CSS 변수와 `data-theme`로 전환합니다.

디자인 변경 후 Chrome 검증 29개 항목을 다시 통과했습니다. 별도 확인으로 Pretendard 400/600/700/800/900 굵기의 실제 로딩, CDN 차단 시 시스템 폰트 표시, 양쪽 테마의 배경색과 10px 카드 모서리, 320/375/768/1024/1440px 가로 넘침 없음을 확인했습니다.

## 실행과 사용 기술

사용 기술은 HTML5(구조), CSS3(배치·테마·반응형), JavaScript ES6+(이벤트·상태·비동기), GitHub REST API(공개 저장소), GitHub Pages(정적 배포)입니다. npm 설치나 빌드는 필요하지 않습니다.

1. VS Code에서 **B1-1** 폴더를 엽니다.
2. **Live Server (`ritwickdey.LiveServer`)** 확장을 설치합니다. 이번 작업 환경에서는 설치를 확인했습니다. 다른 컴퓨터에서는 별도 설치해야 합니다.
3. `index.html`을 우클릭해 **Open with Live Server**를 선택합니다.
4. `http://127.0.0.1:5500`으로 접속합니다.

대안은 아래 명령입니다. 같은 포트에는 서버 하나만 실행합니다.

```bash
python3 -m http.server 5500 --bind 127.0.0.1
```

## 파일 구조

```text
B1-1/
├── index.html                 # 의미 있는 구조, 폼, 기본 콘텐츠
├── css/style.css              # CSS 변수, 모바일 퍼스트, 테마, 애니메이션
├── js/main.js                 # 상태, 이벤트, 렌더링, API 요청
├── images/
│   ├── profile.png
│   ├── favicon.svg
│   └── screenshots/           # desktop / mobile / dark
├── .vscode/                   # Live Server 추천 및 5500 포트 설정
├── .nojekyll                  # 정적 Pages 배포용
├── tests/review.py            # 개발용 Chrome 검증; 사이트에서 로드하지 않음
├── MISSION_GUIDE.md           # 단계별 학습
├── WORK_LOG.md                # 이어서 작업하기 위한 기록
└── README.md
```

## 미션 요구사항 체크리스트

`[x]`는 아래 근거로 구현·설정을 확인했다는 뜻입니다. 배포 갱신과 본인의 설명 연습은 별도로 남겨 둡니다. 코드 위치는 줄 번호 대신 변경에 강한 함수명과 CSS 선택자로 표시했습니다.

### 기본 구성·HTML

- [x] `index.html`, `css/`, `js/`, `images/` 역할 분리; 외부 CSS와 JS 연결.
- [x] VS Code + Live Server 환경: `.vscode/extensions.json`, `.vscode/settings.json`; 확장 설치 확인.
- [x] `header`, `nav`, `main`, `section`, `article`, `footer` 사용 — [index.html](index.html).
- [x] Hero 인사말·CTA, About 소개·프로필, Skills 기술 목록, Projects API 카드, Contact 문의 폼, Footer 저작권·GitHub 링크.
- [x] 네비게이션에서 Hero/About/Skills/Projects/Contact/Footer로 이동하는 앵커와 대응 ID 존재.
- [x] 프로필 이미지의 의미 있는 `alt`; CSS 그래픽은 `role="img"`와 `aria-label`로 설명.
- [x] 이름·이메일·메시지의 `label for`와 입력 요소 `id` 일치.

### CSS·반응형

- [x] 외부 `css/style.css`; `:root`에 색상·폰트·간격 변수 정의.
- [x] `[data-theme="dark"]`에서 테마 변수 재정의.
- [x] `.nav`에 Flexbox: 로고 왼쪽, 메뉴와 버튼 오른쪽.
- [x] `.projects-grid`에 Grid: `repeat(auto-fit, minmax(min(100%, 290px), 1fr))`.
- [x] 기본 모바일 스타일 → `min-width: 768px` 태블릿 → `min-width: 1024px` 데스크톱.
- [x] 768px 미만 메뉴 숨김·햄버거 표시, 이상에서는 가로 메뉴 표시.
- [x] 버튼·카드 `:hover`, `transition`; 카드 `box-shadow` 적용.

### JavaScript·인터랙션

- [x] `defer` 연결; `const`/`let` 사용; `var`, 인라인 `onclick`, 인라인 `style` 사용 없음.
- [x] `querySelector`/`querySelectorAll`, `textContent`/`innerHTML`, `classList.add/remove/toggle` 사용 — [js/main.js](js/main.js).
- [x] `click`, `submit`, `scroll`, `input` 이벤트와 `addEventListener`; 앵커·폼에서 `preventDefault()`.
- [x] 햄버거 클릭으로 열기·닫기: `state.menuOpen` → `renderMenu()` → `classList.toggle("active", state.menuOpen)`.
- [x] 앵커 클릭 시 `scrollIntoView()`로 부드럽게 이동; 메뉴 닫기와 대상 포커스 처리.
- [x] 스크롤 **300px 이상**에서 맨 위 버튼 표시, 클릭 시 `scrollTo({ top: 0 })`.
- [x] 스크롤 **60px 이상**에서 헤더 배경 변경 — `renderScroll()`.
- [x] 테마 토글 → `portfolio-theme`에 저장 → 새로고침 시 복원 — `renderTheme()`, 저장소 도우미.
- [x] Intersection Observer **threshold: 0.2**, 20% 이상 보이면 한 번 등장; `unobserve()`로 관찰 종료.
- [x] `prefers-reduced-motion` 사용자에게 애니메이션과 부드러운 이동 생략(접근성 보완).

### 폼 UX·ES6+·API

- [x] 이름·이메일·메시지 필수값, `trim()`으로 공백만 입력한 경우 거부 — `validateField()`.
- [x] 이메일 정규식과 `typeMismatch` 검사, 필드 근처 오류 표시, 첫 오류로 포커스 이동.
- [x] 제출 기본 동작 방지, 검증 성공 안내 — `submit` 이벤트와 `renderForm()`.
- [x] 화살표 함수, 템플릿 리터럴, 객체 구조분해 활용.
- [x] `map()`으로 카드 문자열 생성 후 `join("")`, `forEach()`로 요소 순회, 선택 과제 `filter()` 활용.
- [x] 본인 계정 `dooolll00`의 `/users/dooolll00/repos` 호출 — `fetch`, `async/await`, `try/catch`.
- [x] 로딩 스피너, 성공 카드, 에러 안내·재시도, 빈 결과 안내 — `renderProjects()`.
- [x] `response.ok` 검사; 403/429 한도 안내, 404, 서버 오류, 네트워크 오류 처리.
- [x] 실제 한도를 소진하지 않고 모의 응답으로 403·빈 배열·실패·재시도 검증.
- [x] 최소 3개의 상태 → 렌더링 흐름: 테마, 메뉴, API, 폼, 필터(아래 표).

문의 폼은 **검증 데모**입니다. 입력 내용을 저장하거나 이메일을 보내지 않으며, 성공 문구에도 실제 미전송을 명시합니다. 실제 전송은 선택 과제입니다.

### 제출·개발 제약

- [x] 순수 HTML/CSS/JavaScript; React/Vue/jQuery/Bootstrap/Tailwind 등 런타임 라이브러리 없음.
- [x] README에 프로젝트 설명·사용 기술·저장소 URL·Pages URL·스크린샷 3종 포함.
- [x] 기존 GitHub Pages URL 존재 및 HTTP 200 응답 확인.
- [x] 변경 사항을 GitHub main에 커밋·업로드하고 Pages 배포 완료 후 최종본 재검증(2026-09-07).

### 보너스 과제(선택)

- [x] 언어별 프로젝트 필터 (`renderFilters()`, `array.filter()`).
- [x] 시스템 다크 모드 감지 (`matchMedia`, `explicitTheme`); 직접 선택한 설정을 우선 적용.
- [ ] Hero 타이핑 효과 — 선택 사항, 미구현.
- [ ] Formspree/EmailJS 실제 이메일 전송 — 선택 사항, 미구현.

## 핵심 개념과 코드 설명

HTML은 콘텐츠의 역할을 표현합니다. 사이트 전체 제목과 이동은 `header`/`nav`, 주요 내용은 `main`, 주제 단위는 `section`, 독립적인 카드는 `article`, 저작권은 `footer`로 나눴습니다. 단순 배치를 묶을 때는 `div`를 사용했습니다.

Flexbox는 한 축을 중심으로 정렬할 때 적합하므로 메뉴와 버튼 묶음에 사용했습니다. Grid는 행과 열을 함께 다루기 좋아 프로젝트 목록에 사용했습니다. `auto-fit`은 들어갈 열 수를 조절하고, `minmax`는 열 너비 범위를 정하며, `min(100%, 290px)`는 좁은 모바일에서 카드가 화면을 넘는 것을 막습니다.

| 이벤트 | 바뀌는 상태 | DOM·화면에 반영하는 방법 |
| --- | --- | --- |
| 테마 버튼 클릭 | `state.theme` | `renderTheme()` → HTML `data-theme` → CSS 변수 |
| 햄버거 클릭 | `state.menuOpen` | `renderMenu()` → `active`, `aria-expanded` |
| API 요청 시작·완료·실패 | `state.projects.status`, `repos`, `error` | `renderProjects()` → 스피너·카드·오류·빈 결과 |
| 폼 입력·제출 | `state.form.values`, `errors`, `success` | `renderForm()` → 필드 오류·글자 수·성공 안내 |
| 언어 버튼 클릭 | `state.projects.filter` | 버튼 클래스·`aria-pressed` 갱신 후 `renderProjects()`에서 필터링 |

상태는 화면이 기억할 값이고 DOM은 실제 문서 요소입니다. `querySelector`로 요소를 선택하고 `addEventListener`로 동작을 연결합니다. **상태를 바꾸는 것만으로 DOM이 자동 변경되지는 않으므로 렌더링 함수를 직접 호출**합니다. 이 점을 이해하면 다음 미션의 React 상태와 렌더링을 연결하기 쉽습니다.

화살표 함수는 콜백을 간결하게 쓰는 문법입니다. 구조분해는 객체에서 필요한 속성을 꺼내며, `map`은 배열의 각 값을 변환하고 `filter`는 조건에 맞는 값만 남기고 `forEach`는 각 항목에 작업을 수행합니다. 카드 생성에서는 템플릿 리터럴로 HTML 문자열을 만듭니다. 외부 문자열은 `escapeHTML()`을 거치고, 링크는 `safeRepoURL()`로 검사한 뒤 `innerHTML`에 넣습니다. 단순 안내는 `textContent`를 사용합니다.

`await fetch()`는 해당 비동기 함수의 다음 작업을 응답까지 기다리게 하며, 기다리는 동안 브라우저의 다른 상호작용은 계속됩니다. HTTP 403/500은 응답 자체가 도착한 것이므로 `response.ok`를 직접 검사해 오류로 처리합니다. `catch`에서 오류 상태를 저장하고 `finally`에서 타이머 정리와 최종 렌더링을 수행합니다. 빈 결과는 별도 `empty` 상태값 없이 **성공 응답의 배열 길이가 0인지**로 판단합니다.

## API 설정과 예외 처리

```text
https://api.github.com/users/dooolll00/repos?sort=updated&per_page=100&page=1
```

계정을 바꾸려면 `js/main.js`의 `GITHUB_USERNAME`과 HTML 소개·소셜 링크·프로필 이미지도 수정합니다. fork를 포함한 공개 저장소를 조회하며, 언어가 없으면 `기타`로 표시합니다.

- **5분 캐시:** `portfolio-repos-dooolll00`에 성공 응답을 저장해 요청 횟수를 줄입니다. 손상·만료 캐시는 무시하며, 재시도는 캐시를 건너뜁니다.
- **100개 단위 페이지네이션:** 100개가 오면 다음 페이지도 요청합니다.
- **15초 제한:** 전체 조회에 `AbortController`를 사용합니다. 페이지마다 15초를 새로 주는 방식이 아닙니다.
- **데이터 검사:** `isRepoList()`로 배열 및 카드 렌더링에 필요한 항목 형식을 검사합니다. 잘못된 응답은 에러 UI로 표시합니다.
- **저장소 차단:** 예외를 잡아 현재 페이지 기능은 유지합니다. 저장 자체가 불가능하면 새로고침 후 테마 유지와 캐시는 사용할 수 없습니다.

미션에서 안내한 비인증 API 제한은 시간당 60회입니다. 오류 시 한도·접근 제한 안내를 표시합니다. 발표를 위해 실제 한도를 소진하지 마세요. 캐시를 비우려면 개발자 도구 Application → Local Storage에서 **`portfolio-repos-dooolll00` 키만 삭제**합니다.

## 검증 및 재현

개발용 검증은 Python + Playwright가 설치된 환경에서 **실제 Google Chrome**을 실행합니다. 이 도구는 사이트의 의존성이 아니며 HTML에서 로드하지 않습니다.

```bash
python3 -m venv /tmp/b1-1-review-venv
/tmp/b1-1-review-venv/bin/pip install playwright
python3 -m http.server 5511 --bind 127.0.0.1
```

위 서버를 켜 둔 채 다른 터미널에서 실행합니다. Google Chrome 설치가 필요합니다.

```bash
/tmp/b1-1-review-venv/bin/python tests/review.py
# 실제 API·기존 Pages도 점검하고 로컬 스크린샷 3종을 갱신할 때:
/tmp/b1-1-review-venv/bin/python tests/review.py --live
```

일반 실행은 API를 모의 응답으로 대체하므로 GitHub 한도를 사용하지 않습니다. `--live`는 실제 API를 사용하며 기존 스크린샷을 갱신합니다. 기존 Pages와 로컬 파일이 동일한지 판정하거나 배포하는 명령은 아닙니다.

2026-09-07, 설치된 **Chrome 146.0.7680.165**에서 `tests/review.py --live` 실행 결과 **29개 검증 항목 모두 통과**했습니다. 더 최신 버전의 Chrome을 별도로 설치하거나 검증한 것은 아닙니다.

| 검증 범위 | 결과 |
| --- | --- |
| 구조·앵커·label·alt·이미지 로딩·Flex/Grid | 통과 |
| 320/375/767/768/1024/1440px, 가로 넘침·메뉴 표시·메뉴 영역 겹침 | 통과 |
| 메뉴 재클릭·Escape·외부 클릭·앵커·폭 변경, 포커스 이동 | 통과 |
| 스크롤 경계 59/60/299/300px, 맨 위 이동 | 통과 |
| 시스템 테마·직접 선택 우선·새로고침 유지 | 통과 |
| 폼 필수값·공백·이메일·성공·수정 후 초기화·글자 수 | 통과 |
| API 로딩·성공·빈 결과·403/429/404/500·재시도·네트워크 실패 | 통과(모의 응답) |
| 잘못된 응답·손상/만료/유효 캐시·저장소 차단·100+1개 페이지네이션·15초 제한 | 통과(모의 응답·가상 시간) |
| 언어 필터·키보드 포커스·HTML 이스케이프·URL 검사 | 통과 |
| 실제 Intersection Observer 등장, smooth 스크롤 CSS | 통과 |
| 로컬·기존 Pages의 실제 API | 각 7개 공개 저장소 표시 확인 |
| 로컬·기존 Pages의 테마·폼·모바일 메뉴·스크롤·반응형 | 통과 |
| JavaScript 실행 오류 | 검증 중 없음 |

추가로 Python 문법, 문서의 로컬 링크, 금지 구문·속성, CSS 필수 선언, 설정 파일과 `git diff --check`를 확인했습니다. 스크린샷은 전체 화면으로 갱신하고 육안으로 확인했습니다. 테스트는 확인한 화면 크기와 시나리오의 근거이며 모든 기기·모든 입력에 대한 무오류 보장은 아닙니다. 배포 설정 화면 자체는 변경하거나 재확인하지 않았습니다.

## 스크린샷

로컬 최종 코드와 실제 GitHub 데이터를 사용한 Chrome 캡처입니다. API 데이터가 바뀌면 카드 개수와 순서는 달라질 수 있습니다.

| 데스크톱 · 1440px | 모바일 · 375px | 다크 모드 · 1440px |
| --- | --- | --- |
| ![밝은 테마 데스크톱 전체 화면](images/screenshots/desktop.png) | ![모바일 전체 화면](images/screenshots/mobile.png) | ![다크 테마 데스크톱 전체 화면](images/screenshots/dark.png) |

## 배포 방법

Git 변경을 확인하고 필요한 파일만 커밋한 뒤 `main`으로 push합니다. GitHub 저장소 Settings → Pages에서 **Deploy from a branch → main → / (root)** 설정을 확인합니다. Actions의 Pages 배포가 성공하면 위 URL에서 반응형·메뉴·테마 저장·실제 API·폼을 다시 확인합니다. 파일 경로는 `css/style.css`처럼 상대 경로이므로 `/B1-1/` 하위 경로에서도 동작합니다.

2026-09-07 사용자 요청으로 변경 사항을 main에 커밋·업로드하고 Pages 배포를 완료했습니다. 터미널 Git 인증이 없어 GitHub 앱으로 동일한 파일 트리의 커밋을 만들고 main을 갱신했으며, 로컬 main도 원격과 동기화했습니다. 배포 설정 변경은 필요하지 않았습니다. 새 공개본에서 320/375/768/1024/1440px 반응형, Pretendard, 테마 저장·복원, Footer 메뉴·포커스, 맨 위 이동, 문의 폼, 이미지, 실제 GitHub 저장소 7개 표시를 확인했고 JavaScript 실행 오류가 없었습니다.
