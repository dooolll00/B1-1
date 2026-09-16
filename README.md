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

## 미션 요구사항 체크리스트

2026-09-16 미션 전문과 현재 코드, Chrome 검사 및 배포 확인 결과를 기준으로 작성했습니다. `[x]`는 구현·확인 완료, `[ ]`는 추가 확인 필요 또는 선택 과제 미구현을 뜻합니다. 발표 준비 여부를 표시하는 표가 아닙니다.

### 기본 구성·개발 환경

- [x] `index.html`, `css/`, `js/`, `images/`로 역할 분리
- [x] 외부 CSS 연결 및 JavaScript의 `defer` 적용
- [x] VS Code와 Live Server 설치·설정 확인 — `127.0.0.1:5500`
- [x] 순수 HTML/CSS/JavaScript 사용 — React, Vue, jQuery, Bootstrap, Tailwind 등 사용하지 않음
- [x] 허용된 웹 폰트 사용 — Pretendard, 검사 도구는 사이트에 로드하지 않음

### HTML 구조

- [x] `header`, `nav`, `main`, `section`, `article`, `footer` 사용
- [x] Hero: 인사말과 CTA 버튼
- [x] About: 자기소개와 프로필 이미지
- [x] Skills: 기술 스택 목록
- [x] Projects: GitHub API 프로젝트 카드
- [x] Contact: 문의 폼
- [x] Footer: 저작권과 소셜 링크
- [x] 네비게이션에 각 구역으로 이동하는 앵커 링크 제공
- [x] 이미지에 의미 있는 `alt` 지정
- [x] 폼의 `label for`와 입력 요소 `id` 연결

구현 위치: [index.html](index.html), 동적 프로젝트 카드는 [js/main.js](js/main.js)의 `createProjectCard`.

### CSS·반응형

- [x] 외부 `css/style.css` 사용
- [x] `:root`에 색상·폰트·간격 변수 정의
- [x] `[data-theme="dark"]`에 다크 모드 변수 정의
- [x] 네비게이션에 Flexbox 적용 — 로고 왼쪽, 메뉴 오른쪽
- [x] 프로젝트 카드에 Grid의 `auto-fit`과 `minmax` 적용
- [x] 모바일 퍼스트와 768px·1024px 브레이크포인트 적용
- [x] 모바일에서 기본 메뉴 숨김·햄버거 버튼 표시
- [x] 버튼·카드에 `hover`와 `transition`, 카드에 `box-shadow` 적용
- [x] 320/375/767/768/1024/1440px에서 반응형 및 가로 넘침 검사 통과

구현 위치: [css/style.css](css/style.css)의 `.nav`, `.projects-grid`, 미디어 쿼리.

### JavaScript·DOM·이벤트

- [x] `var` 대신 `const`·`let` 사용
- [x] HTML의 `onclick` 대신 `addEventListener` 사용
- [x] 인라인 `style` 속성 사용하지 않음
- [x] `querySelector`·`querySelectorAll`로 요소 선택
- [x] `textContent`·`innerHTML`로 화면 내용 갱신
- [x] `classList.add`·`remove`·`toggle` 사용
- [x] `click`·`submit`·`scroll`·`input` 이벤트 처리
- [x] `event.preventDefault()`로 앵커·폼 기본 동작 제어
- [x] 화살표 함수·템플릿 리터럴·구조분해 할당 사용
- [x] `map`으로 저장소를 카드 HTML로 변환하고 `forEach`로 순회

### 인터랙션

- [x] 햄버거 버튼 재클릭으로 메뉴 열기·닫기 — `active` 클래스 토글
- [x] 네비게이션 클릭 시 해당 구역으로 부드럽게 이동
- [x] 스크롤 300px 이상에서 맨 위 버튼 표시, 클릭 시 최상단 이동
- [x] 스크롤 60px 이상에서 헤더 배경 변경
- [x] 다크 모드 전환·localStorage 저장·새로고침 후 복원
- [x] Intersection Observer 등장 효과 — `threshold: 0.2`
- [x] 스크롤 기준값과 Observer 설정을 README에 명시

구현 위치: `renderMenu`, `renderScroll`, `renderTheme`, `IntersectionObserver`. 동작 줄이기 설정에서는 부드러운 이동과 애니메이션을 생략합니다.

### 문의 폼

- [x] 이름·이메일·메시지 필드 제공
- [x] 필수값과 공백만 있는 입력 검사
- [x] 이메일 형식 검사
- [x] 오류 메시지를 해당 입력칸 근처에 표시
- [x] 제출 시 `preventDefault()` 적용
- [x] 검증 성공 메시지 표시

구현 위치: `validateField`, `renderForm`, `contact-form`의 제출 이벤트. 실제 이메일 전송은 선택 과제입니다.

### GitHub API·상태 관리

- [x] 본인 계정의 `/users/dooolll00/repos` 호출
- [x] `fetch`·`async/await`·`try/catch` 사용
- [x] 로딩 상태: 스피너와 안내 표시
- [x] 성공 상태: 저장소 카드 목록 표시
- [x] 오류 상태: 불러올 수 없다는 안내와 재시도 버튼 표시
- [x] 빈 결과: 표시할 프로젝트가 없다는 안내 표시
- [x] HTTP 403 응답을 오류 UI로 처리
- [x] 최소 3개의 상태 → 화면 갱신 흐름 구현 — 테마·API·폼, 추가로 메뉴·필터
- [x] 반복 API 호출을 줄이도록 5분 캐시 적용 — 미션 원문의 비인증 시간당 60회 제한 안내 고려

구현 위치: `fetchAllRepos`, `checkRepoResponse`, `loadProjects`, `renderProjects`, `state`. 실제 요청을 반복하기보다 모의 응답으로 오류를 검사합니다.

### 배포·제출 자료·브라우저

- [x] GitHub Pages 공개 URL 제공 및 최신 코드 배포 확인
- [x] 배포본 반응형·메뉴·테마·스크롤·API·폼 동작 확인
- [x] 공개 HTML·CSS·JS와 로컬 파일 일치 확인
- [x] README에 프로젝트 설명·사용 기술·배포 URL·스크린샷 포함
- [x] GitHub 저장소 URL·Pages URL 준비 — 문서 상단 링크
- [x] 데스크톱·모바일·다크 모드 스크린샷 준비 — `images/screenshots/`
- [x] 설치된 Chrome 146.0.7680.165에서 검사 통과
- [ ] 제출 시점의 최신 Chrome 버전 여부와 해당 버전 동작 확인

제출 자료를 준비한 상태이며 제출처에 실제 제출했는지는 별개입니다. 스크린샷은 같은 디자인의 2026-09-07 촬영본이며 API 목록은 현재와 다를 수 있습니다.

### 선택 과제

- [x] 언어별 프로젝트 필터 — `array.filter()`와 필터 버튼
- [x] 시스템 다크 모드 감지 — `prefers-color-scheme`
- [ ] Hero 타이핑 효과 — 미구현, 선택 사항
- [ ] Formspree/EmailJS 실제 이메일 전송 — 미구현, 선택 사항

### 학습 목표 확인 범위

시맨틱 구조 설계, Flexbox/Grid 선택, DOM 선택·이벤트 연결, ES6+와 map/filter, 비동기 API 상태, 이벤트 → 상태 → 화면 갱신을 설명할 구현은 갖추었습니다. **본인이 이 여섯 가지를 스스로 설명할 수 있는지는 자동 검사로 판정하지 않았습니다.** 발표자료의 별도 체크리스트에서 직접 확인합니다.
