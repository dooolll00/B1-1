# 반응형 포트폴리오 미션 수행 가이드

이 가이드는 현재 저장소의 코드를 이해하고, 같은 기능을 단계별로 직접 구현하는 방법을 설명합니다. 디자인은 현재 배포본을 유지합니다. 새 프레임워크나 라이브러리는 사용하지 않습니다.

- 실제 사이트: https://dooolll00.github.io/B1-1/
- 저장소: https://github.com/dooolll00/B1-1
- 구현 설명과 검증 범위: [README](README.md)
- 기준 파일: [HTML](index.html), [CSS](css/style.css), [JavaScript](js/main.js)

## 1. 먼저 알아둘 것

미션의 핵심은 다음 흐름을 직접 설명하는 것입니다.

```text
사용자 이벤트 → 상태 변경 → 렌더링 함수 → DOM/CSS 변경 → 화면 업데이트
```

HTML은 구조, CSS는 표현, JavaScript는 동작을 담당합니다. 상태는 화면이 기억할 값이고, 렌더링은 그 값을 화면에 반영하는 과정입니다.

현재 프로젝트는 이미 완성되어 있습니다. 아래 코드 조각은 흐름을 설명하는 예시이므로 기존 `main.js`에 다시 붙여넣지 마세요. 같은 변수나 이벤트를 중복 선언하면 오류나 중복 실행이 생깁니다. 직접 처음부터 연습하려면 별도 폴더에서 시작하고, 각 단계의 완성 코드를 현재 파일과 비교하세요.

## 2. 개발 환경 준비

VS Code에서 `portfolio` 폴더를 엽니다. Live Server 확장(`ritwickdey.LiveServer`)을 설치하고 `index.html`을 우클릭해 **Open with Live Server**를 선택합니다. 현재 환경에는 설치되어 있습니다.

```text
portfolio/
├── index.html
├── css/style.css
├── js/main.js
├── images/profile.png
├── images/favicon.svg
├── images/screenshots/
├── .vscode/
├── .gitignore
├── .nojekyll
├── README.md
└── MISSION_GUIDE.md
```

Live Server 기본 설정 주소는 `http://127.0.0.1:5500`입니다. 포트가 이미 사용 중이면 기존 서버를 종료하거나 다른 포트를 사용하세요. 이미지와 CSS/JS는 상대 경로로 연결해야 GitHub Pages의 `/B1-1/` 하위 경로에서도 동작합니다.

**완료 기준:** 페이지가 열리고 개발자 도구의 Console에 JavaScript 오류, Network에 로컬 파일 404가 없습니다.

## 3. HTML: 의미 있는 구조 만들기

`index.html`의 주석을 따라 Header → Hero → About → Skills → Projects → Contact → Footer 순서로 읽습니다.

| 태그 | 현재 사용하는 이유 |
| --- | --- |
| `header` | 사이트 상단 로고와 메뉴 영역 |
| `nav` | 주요 섹션으로 이동하는 링크 묶음 |
| `main` | 페이지의 핵심 본문 |
| `section` | 제목이 있는 주제 구역 |
| `article` | 독립적으로 읽을 수 있는 기술·프로젝트 카드 |
| `footer` | 저작권과 GitHub 링크 |

`href="#about"`은 `id="about"`인 요소로 이동합니다. 폼의 `label for="email"`은 `input id="email"`과 연결됩니다. 프로필 이미지의 `alt`는 이미지 내용을 설명합니다.

외부 파일은 다음 역할로 연결합니다.

```html
<link rel="stylesheet" href="css/style.css">
<script src="js/main.js" defer></script>
```

`defer`를 사용하면 HTML 파싱이 끝난 다음 스크립트가 실행되어 DOM을 선택할 수 있습니다.

**완료 기준:** 6개 본문·하단 섹션, 앵커 링크, 이미지 설명과 폼 레이블이 존재합니다. HTML에는 `onclick`과 인라인 `style`이 없습니다.

## 4. CSS: 현재 디자인과 반응형 이해하기

`style.css`는 01~12 번호 주석으로 구분했습니다. 현재 디자인을 유지하려면 색상·크기·레이아웃 값을 바꾸기보다 먼저 각 선언의 역할을 읽어보세요.

- `:root`: 색상·폰트·간격 등 공통 변수.
- `[data-theme="dark"]`: 같은 변수 이름에 다크 모드 값을 지정.
- `.nav`: Flexbox로 로고·메뉴·버튼을 한 축에 배치.
- `.projects-grid`: Grid로 카드의 행과 열을 구성.
- 기본 규칙: 모바일 화면에 적용.
- `@media (min-width: 768px)`: 태블릿부터 메뉴를 가로로 표시.
- `@media (min-width: 1024px)`: 넓은 화면의 간격과 카드 배치를 조정.

```css
grid-template-columns: repeat(auto-fit, minmax(min(100%, 290px), 1fr));
```

화면 너비에 맞는 수의 열을 만들고 남는 공간을 균등하게 나눕니다. 아주 좁은 화면에서는 카드 최소 너비가 부모 너비를 넘지 않도록 `min(100%, 290px)`를 사용합니다.

**완료 기준:** Chrome 개발자 도구의 기기 모드에서 320/375/768/1024/1440px을 확인합니다. 가로 스크롤이 없고, 모바일에서 햄버거가 나타나며, 버튼과 카드의 hover가 동작합니다.

## 5. JavaScript: 상태와 DOM 선택

`main.js`의 `01. 공통 설정`을 읽습니다.

```javascript
const themeButton = document.querySelector("#theme-toggle");
const fields = [...form.querySelectorAll("input, textarea")];
```

`querySelector`는 첫 요소를, `querySelectorAll`은 일치하는 요소 목록을 가져옵니다. `...`는 목록을 배열에 펼쳐 담습니다. `const`는 변수 재할당을 막지만 객체 내부 값은 바꿀 수 있습니다.

| 상태 | 의미 |
| --- | --- |
| `state.theme` | 현재 밝은/어두운 테마 |
| `state.menuOpen` | 모바일 메뉴 열림 여부 |
| `state.projects.status` | API 요청 진행 상황 |
| `state.projects.repos` | GitHub에서 받은 저장소 배열 |
| `state.projects.filter` | 선택한 언어 |
| `state.form.values` | 입력값 |
| `state.form.errors` | 필드별 오류 문구 |
| `state.form.success` | 마지막 검증 성공 여부 |

**완료 기준:** DOM 요소와 상태 값의 차이를 설명할 수 있습니다.

## 6. 다크 모드 구현과 확인

`02. [필수] 다크 모드`의 이벤트와 `renderTheme()`를 연결해서 읽습니다.

```text
theme-toggle 클릭
→ state.theme 전환
→ localStorage 저장
→ renderTheme()
→ html의 data-theme와 버튼 안내 변경
→ CSS 변수가 바뀌어 전체 색상 변경
```

처음 접속하면 저장된 테마를 우선 사용합니다. 직접 선택한 값이 없으면 시스템 테마를 따릅니다. 저장소가 차단되어도 페이지가 중단되지 않도록 도우미 함수에서 오류를 처리합니다.

**완료 기준:** 클릭하면 테마가 바뀌고, 새로고침해도 유지됩니다. 저장 키는 `portfolio-theme`입니다.

## 7. 모바일 메뉴와 스크롤

`03. [필수] 모바일 메뉴`와 `04. [필수] 앵커 이동`을 읽습니다.

```javascript
// 흐름 설명용 예시: 기존 파일에 중복 추가하지 않습니다.
menuButton.addEventListener("click", () => {
  state.menuOpen = !state.menuOpen;
  renderMenu();
});
```

`renderMenu()`는 `classList.toggle("active", state.menuOpen)`으로 클래스와 상태를 일치시킵니다. `aria-expanded`는 보조 기술에 메뉴가 열렸는지 알려줍니다.

| 기능 | 기준·처리 |
| --- | --- |
| 링크 이동 | `preventDefault()` 후 `scrollIntoView()` |
| 헤더 변경 | 스크롤 60px 이상 |
| 맨 위 버튼 | 스크롤 300px 이상 |
| 등장 애니메이션 | Observer threshold 0.2, 실제 노출 비율 20% 이상 |
| 메뉴 닫기 | 재클릭, 링크 선택, Escape, 외부 클릭, 화면 폭 전환 |

**완료 기준:** 모바일 메뉴를 키보드와 마우스로 열고 닫을 수 있습니다. 링크 이동 시 제목이 헤더에 가려지지 않고 맨 위 버튼이 작동합니다. 운영체제에서 동작 줄이기를 선택하면 애니메이션을 생략합니다.

## 8. GitHub API: 요청과 4가지 화면 상태

`05. [필수] 프로젝트`에서 먼저 `loadProjects()`와 `renderProjects()`를 읽습니다. 캐시·페이지네이션은 이후에 읽어도 됩니다.

```text
loadProjects()
→ status = loading → 로딩 렌더링
→ await fetch(...)
→ response.ok 검사
→ await response.json()
→ repos 저장, status = success
→ renderProjects()
```

오류가 생기면 `catch`에서 `status = error`와 오류 문구를 저장합니다. `finally`는 시간 제한 타이머를 정리하고 최종 화면을 렌더링합니다.

현재 계정은 `GITHUB_USERNAME = "dooolll00"`입니다. 저장소 목록은 `/users/dooolll00/repos`에서 받습니다.

| 경우 | 화면 |
| --- | --- |
| 요청 중 | 스피너와 로딩 안내 |
| 성공, 저장소 있음 | 프로젝트 카드 |
| 성공, 저장소 0개 | 표시할 프로젝트가 없습니다 |
| HTTP 오류·네트워크 오류 | 오류 문구와 다시 시도 버튼 |

현재 구현은 `empty`라는 별도 상태값 대신 성공 응답의 배열 길이로 빈 결과를 판단합니다. 가이드 예제처럼 별도 상태값을 두는 방식과 모두 가능합니다.

`map()`은 저장소를 HTML 카드 문자열로 바꾸고, `join("")`은 하나로 합칩니다. 구조분해 할당으로 `name`, `description` 등의 값을 꺼냅니다. 외부 문자열은 `escapeHTML()`로 처리한 뒤 `innerHTML`에 넣습니다.

**완료 기준:** 실제 저장소가 표시되고 링크가 올바릅니다. 비인증 API는 호출 제한이 있으므로 403 테스트를 위해 실제 요청을 반복하지 마세요.

## 9. 문의 폼: 입력과 유효성 검사

`06. [필수] 문의 폼`을 읽습니다.

```text
input → state.form.values 변경
→ 검사할 시점이면 validateField()
→ errors 변경 → renderForm()

submit → preventDefault()
→ 모든 필드 검사 → success 변경
→ 성공 안내 또는 첫 오류 필드로 포커스 이동
```

`trim()`으로 공백만 있는 입력을 거부하고 정규식과 이메일 입력 요소의 검사 결과를 사용합니다. `touched`는 사용자가 한 번 떠난 필드를 기억하므로, 처음 접속하자마자 오류가 표시되지 않습니다.

**완료 기준:** 빈 제출·공백 입력·잘못된 이메일은 오류를 표시하고 정상 입력은 성공 안내를 표시합니다. 성공 뒤 수정하면 이전 성공 안내가 사라집니다. 이 폼은 입력값 검증 데모로, 실제 이메일을 전송하지 않습니다.

## 10. 추가 기능은 핵심 흐름 다음에 읽기

| 기능 | 목적 | 관련 코드 |
| --- | --- | --- |
| 언어 필터 | 언어별 저장소 표시 | `renderFilters()`, `filter()` |
| 시스템 테마 | 최초 사용자 설정 반영 | `systemTheme`, `explicitTheme` |
| 5분 캐시 | 불필요한 API 호출 감소 | `CACHE_TTL`, `readStorage()` |
| 페이지네이션 | 100개를 넘는 저장소 조회 | `page`, `hasMore` |
| 15초 제한 | 응답이 없는 요청 종료 | `AbortController`, `setTimeout()` |
| 접근성 | 키보드·화면 낭독기·동작 줄이기 대응 | `aria-*`, 포커스, 미디어 쿼리 |

추가 기능은 구현되어 있으므로 학습 순서만 나중으로 미룹니다. 서로 참조하는 코드를 무작정 삭제하지 않습니다.

## 11. 상태별 검증하기

실제 사이트 확인과 실패 상황 검증을 구분합니다. 아래 테스트는 로컬 개발 서버에서 수행합니다.

1. 정상 접속: 프로젝트 카드와 모든 이미지 확인.
2. 로딩: Chrome Network에서 느린 네트워크를 선택하고 API 캐시를 삭제한 뒤 새로고침.
3. 네트워크 오류: Network의 Offline 설정 후 API 캐시를 삭제하고 새로고침. 오류 화면을 확인한 뒤 Online으로 되돌려 재시도.
4. 빈 결과·403: 개발용 요청 모킹으로 각각 `[]`, HTTP 403을 반환해 검증. 실제 API 한도를 소진하지 않기.
5. 테마: 다크 모드를 켜고 새로고침.
6. 폼: 빈 값 → 잘못된 이메일 → 정상 값 순서로 제출.
7. 반응형: 320/375/768/1024/1440px에서 가로 넘침과 메뉴 확인.

캐시는 개발자 도구 Application → Local Storage에서 `portfolio-repos-dooolll00` 키만 삭제합니다. 개인정보나 다른 사이트의 저장소를 지울 필요는 없습니다. 테스트를 마치면 네트워크 설정을 원래대로 돌립니다.

현재 제출본은 별도 개발 환경에서 로딩·빈 결과·403·404·500·네트워크 실패·잘못된 응답·재시도·캐시·페이지네이션·저장소 차단을 자동 검증했습니다. 테스트용 Python과 라이브러리는 사이트에 포함하지 않습니다.

## 12. GitHub 업로드와 Pages 배포

현재 결과물은 GitHub 도구로 업로드했으므로 기존 로컬 `portfolio` 폴더에는 `.git`이 없을 수 있습니다. 직접 Git을 연습하려면 별도 폴더에 복제합니다.

```bash
git clone https://github.com/dooolll00/B1-1.git portfolio-git-practice
cd portfolio-git-practice
git status
```

파일을 수정한 뒤 아래 순서로 변경을 확인하고 올립니다. GitHub 쓰기 권한과 로컬 Git 인증이 필요합니다.

```bash
git diff
git add index.html css/style.css js/main.js images README.md MISSION_GUIDE.md
git commit -m "Improve portfolio learning guide"
git push origin main
```

`add`는 올릴 변경을 선택하고, `commit`은 기록을 만들며, `push`는 GitHub로 전송합니다. 커밋할 변경이 없는 상태에서는 새 커밋이 만들어지지 않습니다.

Pages 설정: 저장소 Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save. 이 저장소는 이미 배포되어 있으므로 설정을 다시 만들 필요는 없습니다.

업로드 후 Actions의 `pages build and deployment`가 성공했는지 확인하고 실제 URL을 엽니다. 배포 완료 전에는 이전 화면이 보일 수 있습니다. CSS/JS/이미지는 상대 경로로 연결하며 `.nojekyll`은 정적 파일 배포용으로 유지합니다.

## 13. 제출 전 최종 점검

- [ ] 사이트 URL과 GitHub 저장소 URL이 README에 있다.
- [ ] 시맨틱 태그, 6개 섹션, 이미지 alt, 폼 label이 있다.
- [ ] 순수 HTML/CSS/JavaScript이며 외부 UI 라이브러리가 없다.
- [ ] Flexbox/Grid, 768/1024px, 다크 모드 변수가 있다.
- [ ] 메뉴·스크롤·다크 모드 저장·등장 애니메이션이 동작한다.
- [ ] 폼의 필수값·이메일·오류·성공 안내가 동작한다.
- [ ] API 로딩·성공·오류·빈 상태와 재시도를 검증했다.
- [ ] 데스크톱·모바일·다크 모드 스크린샷을 갱신했다.
- [ ] 최소 3개 기능의 이벤트 → 상태 → 렌더링을 직접 설명할 수 있다.
- [ ] API를 쓰는 이유, map/filter/forEach의 차이, async/await와 try/catch의 역할을 설명할 수 있다.

기능이 많다는 것보다 필수 동작이 정확하고 그 동작을 설명할 수 있는지가 이 미션의 중요한 완료 기준입니다.
