# B1-1 비전공자를 위한 발표·학습 가이드

발표의 중심은 **“버튼이나 입력이 어떤 상태를 바꾸고, 그 상태가 어떻게 화면에 반영되는가”**입니다. 아래 대본을 본인 말투로 바꾸어 연습하세요. 실제로 수행한 작업과 이해한 범위만 설명하고, 자동 검증 결과와 본인의 설명 능력은 구분합니다.

이 문서는 2026-09-10에 다시 제공한 미션 원문의 요구사항과 현재 로컬 코드를 기준으로 작성했습니다. **2장은 5~7분 요약 발표**, **7~10장은 자세한 설명과 요구사항 전체 확인용**입니다. 짧은 대본만 읽으면 모든 세부 항목을 다룰 수 없으므로 질의응답 준비에는 전체 확인표도 사용하세요.

- 먼저 7장의 용어와 설명을 읽고, 2장의 대본을 자기 말로 연습합니다.
- 8장의 상태 흐름을 실제 코드에서 따라가고, 9장의 시연을 연습합니다.
- 마지막으로 10장의 모든 항목에 대해 코드 위치를 찾고 설명할 수 있는지 확인합니다.
- 코드 링크: [HTML](index.html), [CSS](css/style.css), [JavaScript](js/main.js), [README](README.md), [미션 요약·작업 이력](WORK_LOG.md).

## 1. 시작 전 준비

- 로컬 최종본을 Live Server로 실행하고 Chrome 개발자 도구를 엽니다.
- `index.html`, `css/style.css`, `js/main.js`를 열어 둡니다.
- GitHub API 카드가 표시되는지 확인합니다. 5분 캐시가 있으므로 새로고침해도 로딩이 아주 짧거나 보이지 않을 수 있습니다.
- 저장소는 [B1-1](https://github.com/dooolll00/B1-1), 제출 URL은 [Pages](https://dooolll00.github.io/B1-1/)입니다. 기존 배포 확인일은 2026-09-07입니다. 2026-09-10 코드 구조 정리는 로컬에만 반영되어 있으므로 현재 코드 설명은 로컬 사이트에서 시연합니다.
- 실제 문의 메일은 전송되지 않습니다. 시연에는 예시 이름과 `hello@example.com`을 사용합니다.

## 2. 5~7분 발표 순서와 대본

### 0:00~0:40 — 무엇을 만들었나

> HTML, CSS, JavaScript만으로 반응형 포트폴리오를 만들었습니다. HTML은 콘텐츠의 구조, CSS는 디자인과 화면 크기 대응, JavaScript는 사용자 동작과 데이터 처리를 담당합니다. Hero, About, Skills, Projects, Contact, Footer를 구성했고, 프로젝트 목록은 GitHub API의 실제 공개 저장소를 보여 줍니다.

화면에서 여섯 구역을 짧게 보여 줍니다. 프로필·소개 문구는 학습용 포트폴리오임을 설명하고, 문구에 없는 실제 경력을 덧붙이지 않습니다.

### 0:40~1:30 — 구조와 반응형을 어떻게 설계했나

> 태그만 봐도 역할을 알 수 있도록 상단은 header, 이동 링크는 nav, 주요 내용은 main으로 나눴습니다. 주제별 영역은 section, 독립적인 기술 카드와 프로젝트 카드는 article, 저작권은 footer입니다. 이미지에는 alt를 넣고 폼의 label과 입력 id를 연결했습니다.
>
> 메뉴처럼 한 방향의 정렬은 Flexbox를, 프로젝트처럼 행과 열을 구성하는 목록은 Grid를 선택했습니다. 모바일을 기본으로 작성하고 768px부터 태블릿, 1024px부터 데스크톱 배치를 적용합니다. 프로젝트 카드는 auto-fit과 minmax로 화면에 맞는 열 수와 너비를 정합니다.

Chrome 기기 모드에서 375 → 768 → 1440px로 전환합니다. 메뉴의 표시 방식과 카드 열 수 변화를 보여 줍니다.

### 1:30~2:30 — 테마와 메뉴로 상태 흐름 설명

> querySelector로 테마 버튼을 찾고 addEventListener로 클릭 이벤트를 연결했습니다. 클릭하면 state.theme을 바꾸고 localStorage에 저장한 다음 renderTheme을 호출합니다. 이 함수가 HTML의 data-theme을 바꾸면 CSS에서 같은 변수 이름의 다크 모드 값이 적용됩니다. 새로고침 때 저장된 값을 읽으므로 선택이 유지됩니다.
>
> 모바일 메뉴도 같은 구조입니다. 클릭하면 setMenuOpen으로 state.menuOpen이라는 참·거짓 값을 바꾸고 renderMenu가 active 클래스와 aria-expanded를 맞춥니다. 상태는 기억하는 값이고 렌더링은 그 값을 실제 화면에 반영하는 작업입니다.

다크 모드 전환 → 새로고침 → 모바일 메뉴 열기·닫기를 시연합니다. `const state`여도 객체 내부 속성은 변경할 수 있다는 점을 설명할 준비를 합니다.

### 2:30~3:50 — GitHub API와 네 가지 화면

> loadProjects는 요청 전에 상태를 loading으로 바꾸고 스피너를 먼저 보여 줍니다. fetchAllRepos에서 fetch와 async/await로 GitHub 응답을 기다린 뒤 checkRepoResponse에서 response.ok를 확인합니다. 정상 데이터는 repos에 저장하고 success로 바꿉니다. renderProjects는 map(createProjectCard)로 저장소 객체를 카드 문자열로 변환하고 join으로 합쳐 화면에 넣습니다.
>
> 실패하면 catch에서 error 상태와 오류 문구를 저장합니다. finally는 타이머를 정리하고 마지막 상태를 화면에 반영합니다. HTTP 403은 fetch가 자동으로 예외를 던지는 상황이 아니므로 직접 응답 상태를 검사합니다. 오류 화면에는 재시도 버튼이 있고, 성공했어도 배열이 비어 있으면 ‘표시할 프로젝트가 없습니다’라고 안내합니다.
>
> 추가로 5분 캐시를 두어 API 호출을 줄이고, 언어 필터는 filter로 조건에 맞는 저장소만 남깁니다. 잘못된 캐시 항목은 다시 조회하고, 잘못된 API 응답은 오류로 표시하도록 보완했습니다.

언어 필터를 선택했다가 전체로 복원합니다. 시간이 있으면 아래 안전한 모의 시연으로 빈 결과·403을 보여 줍니다.

### 3:50~4:50 — 문의 폼과 세 번째 상태 흐름

> 입력 이벤트가 발생하면 값을 state.form.values에 저장합니다. validateField는 trim으로 공백만 있는 값을 거르고 이메일 형식도 확인합니다. 오류 문구는 errors에 저장하고 renderForm이 각 필드 근처에 표시합니다. 처음부터 오류를 띄우지 않도록 해당 필드를 떠났는지도 기억합니다.
>
> 제출할 때 preventDefault로 기본 이동을 막고 모든 필드를 검사합니다. 오류가 있으면 첫 오류로 포커스를 옮기고, 없으면 검증 성공을 표시합니다. 이 미션의 실제 이메일 전송은 선택 과제라서 현재는 전송하지 않습니다.

빈 제출 → 잘못된 이메일 → 정상 입력 → 성공 후 메시지 수정 순서로 보여 줍니다. 이전 성공 안내가 사라지는 것도 상태 반영 사례입니다.

### 4:50~6:00 — 검증과 배운 점

> 스크롤이 60px 이상이면 헤더 배경을 바꾸고 300px 이상이면 맨 위 버튼을 표시합니다. 등장 애니메이션은 Intersection Observer로 요소가 20% 이상 보일 때 한 번 실행합니다. 동작 줄이기를 설정한 사용자에게는 애니메이션을 생략합니다.
>
> 정상 화면뿐 아니라 빈 배열, 403, 네트워크 실패, 재시도, 손상된 캐시도 Chrome 자동 검증으로 확인했습니다. 미션의 핵심은 상태를 바꾸는 것과 화면을 갱신하는 것을 연결하는 것이었습니다. 이 프로젝트에서는 렌더링 함수를 직접 호출하며, 다음 React 미션에서는 상태 업데이트를 통해 UI를 선언적으로 표현하는 방식으로 이어집니다.

맨 위 버튼과 README 체크리스트를 보여 줍니다. 현재 상태는 다음처럼 설명합니다.

> 기존 사이트는 GitHub Pages에 배포했습니다. 9월 10일에는 디자인과 기능을 보존하면서 로컬 코드 구조를 정리했고 Chrome에서 모의 API를 사용하는 27개 검증 항목을 통과했습니다. 이 구조 정리는 아직 공개 사이트에 반영하지 않았습니다.

배포 이후에는 실제 확인한 결과에 맞게 이 설명을 갱신합니다. “최신 Chrome에서 무조건 정상”이라고 말하지 않고 실제 검증한 Chrome 버전과 범위를 설명합니다.

## 3. 설명할 코드 위치

검색(Cmd+F)으로 아래 이름을 찾으면 됩니다. 설명용으로 상태 값을 직접 변경할 때는 로컬에서만 연습하세요.

| 질문 | 파일·검색어 | 설명해야 할 연결 |
| --- | --- | --- |
| 시맨틱 구조 | `index.html`: `header`, `main`, `article`, `footer` | 역할 기준으로 나눈 이유 |
| Flexbox와 Grid | `css/style.css`: `.nav`, `.projects-grid` | 한 축 정렬과 행·열 구성 |
| 모바일 퍼스트 | `css/style.css`: `min-width: 768px`, `min-width: 1024px` | 기본 모바일 규칙에 넓은 화면 규칙을 추가 |
| DOM 선택·이벤트 | `js/main.js`: `themeButton`, `addEventListener` | 버튼 선택 → 클릭 감지 |
| 상태와 렌더링 | `state`, `renderTheme`, `renderMenu`, `renderForm` | 값 변경만으로 DOM은 자동 변경되지 않음 |
| 비동기 API | `loadProjects`, `fetchAllRepos`, `checkRepoResponse`, `finally` | 요청 전 로딩, 응답 검사, 성공·오류, 렌더링 |
| 배열·ES6+ | `renderProjects`, `createProjectCard`, `.map`, `.join` | 구조분해로 속성 추출, filter로 선택, map으로 변환 |
| 재시도·이벤트 위임 | `projectList.addEventListener` | 부모에 이벤트를 연결해 나중에 생성된 재시도 버튼도 처리 |
| 입력 검증 | `validateField`, `renderForm`, `form.addEventListener` | 값 → 오류 상태 → 필드별 안내 |
| 방어적 데이터 처리 | `isRepoList`, `escapeHTML`, `safeRepoURL` | 형식 검사, 문자 출력, 링크 검사 각각의 역할 |

이벤트 콜백은 ‘이벤트가 발생했을 때 실행할 함수’입니다. DOM은 ‘브라우저가 HTML을 읽어 만든 문서 요소 구조’, API는 ‘다른 서비스의 데이터를 요청하는 창구’라고 풀어 설명하면 됩니다.

## 4. 로컬에서 API 상태를 안전하게 시연하기

아래 코드는 발표 연습용이며 **프로젝트 소스에 붙여 넣지 않습니다.** 로컬 사이트의 Chrome 개발자 도구 Console에서 한 번씩 실행합니다. 현재 페이지에서만 `fetch`를 바꾸며 새로고침하면 원래 함수로 복원됩니다. 실제 GitHub 한도를 소진하지 않습니다.

페이지의 최초 로딩이 끝난 다음 다음 코드를 실행합니다.

```javascript
// 원래 함수를 보관하고, GitHub 저장소 요청만 모의 응답으로 바꿉니다.
window.demoOriginalFetch ??= window.fetch;
window.demoAPI = async (status, data, delay = 600) => {
  window.fetch = async (...args) => {
    if (!String(args[0]).startsWith("https://api.github.com/users/dooolll00/repos")) {
      return window.demoOriginalFetch(...args);
    }
    await new Promise((resolve) => setTimeout(resolve, delay));
    return new Response(JSON.stringify(data), {
      status,
      headers: { "Content-Type": "application/json" },
    });
  };
  await loadProjects(true); // 캐시를 건너뛰고 실제 렌더링 함수를 사용
};
```

순서대로 실행해 각 화면을 확인합니다.

```javascript
await demoAPI(200, [], 2000); // 2초 로딩 → 빈 결과
await demoAPI(403, {});      // 한도/접근 제한 오류 → 다시 시도 버튼
```

재시도 성공을 보여 주려면 모의 응답을 정상 카드 데이터로 교체한 뒤 화면의 **다시 시도** 버튼을 누릅니다.

```javascript
window.fetch = async (...args) => {
  if (!String(args[0]).startsWith("https://api.github.com/users/dooolll00/repos")) {
    return window.demoOriginalFetch(...args);
  }
  return new Response(JSON.stringify([{
    name: "demo-project", description: "발표용 모의 데이터", language: "JavaScript",
    html_url: "https://github.com/dooolll00/B1-1",
    updated_at: "2026-09-07T00:00:00Z", stargazers_count: 0, forks_count: 0
  }]), { status: 200, headers: { "Content-Type": "application/json" } });
};
```

모의 성공 데이터도 앱의 캐시에 저장되므로 시연이 끝나면 반드시 복원합니다.

```javascript
window.fetch = window.demoOriginalFetch;
localStorage.removeItem("portfolio-repos-dooolll00");
await loadProjects(true); // 실제 API로 복구; 실제 요청이 발생함
```

또는 해당 캐시 키를 삭제하고 새로고침합니다. 이 시연은 빈 상태와 오류 상태를 보여 주기 위한 것이며 실제 데이터 검증 결과라고 설명하지 않습니다. 자동 재현은 `tests/review.py`를 사용합니다.

## 5. 예상 질문과 답변

| 질문 | 답변 요점 |
| --- | --- |
| 왜 전부 div로 만들지 않았나요? | 역할이 있는 태그로 문서 구조를 전달해 개발자와 보조 기술이 이해하기 쉽게 했습니다. |
| Flexbox로도 카드를 만들 수 있지 않나요? | 가능합니다. 이 목록에서는 열 너비와 개수를 함께 다루기 쉬운 Grid를 선택했습니다. |
| defer가 없으면 무슨 문제가 생기나요? | head에서 스크립트가 먼저 실행되면 아래 버튼이 아직 만들어지지 않아 DOM 선택 결과가 null일 수 있습니다. |
| const인데 state.theme을 바꿔도 되나요? | const는 state 변수 자체의 재할당을 막습니다. 객체 속성 변경은 가능합니다. |
| 화살표 함수가 반드시 필요한가요? | 일반 함수로도 구현할 수 있습니다. 여기서는 짧은 콜백 표현에 사용했고, 화살표 함수는 자체 this를 만들지 않는 차이도 있습니다. |
| map/filter/forEach는 어떻게 다른가요? | map은 각 값을 변환한 새 배열, filter는 조건을 통과한 새 배열을 만듭니다. forEach는 순회하며 작업하고 배열을 반환하지 않습니다. |
| async/await면 브라우저가 멈추나요? | 해당 비동기 함수의 다음 작업을 기다리는 동안 다른 이벤트는 처리할 수 있습니다. 무거운 동기 계산까지 자동으로 분리되는 것은 아닙니다. |
| fetch를 try/catch로만 감싸면 충분한가요? | 네트워크 오류는 잡히지만 HTTP 403/500은 response.ok를 검사해 직접 오류를 발생시켜야 합니다. |
| 빈 상태도 실패인가요? | 정상 응답이지만 표시할 항목이 없는 상태입니다. 오류와 다른 메시지를 보여 줍니다. |
| novalidate인데 왜 required를 쓰나요? | 자동 제출 차단 팝업 대신 직접 오류 UI를 만들되 필수 필드의 의미를 HTML에 남깁니다. JS에서 필수값을 검사합니다. |
| 이메일 검사를 통과하면 실재 주소인가요? | 형식이 맞는지만 확인합니다. 실제 존재하거나 메일이 전달된다는 뜻은 아닙니다. |
| 상태를 저장하면 화면도 바뀌나요? | 여기서는 아닙니다. 상태 변경 후 render 함수를 직접 호출해야 DOM이 갱신됩니다. |
| 저장소 접근이 막히면 어떻게 되나요? | 오류를 잡아 현재 페이지는 계속 동작합니다. 저장이 불가능하므로 새로고침 후 설정 유지는 보장할 수 없습니다. |
| innerHTML은 안전한가요? | 외부 문자열을 그대로 넣으면 위험합니다. 텍스트를 이스케이프하고 URL을 검사하며 단순 안내는 textContent로 처리합니다. |
| 캐시와 상태는 무엇이 다른가요? | state는 현재 페이지의 메모리 값이고, localStorage 캐시는 새로고침 이후에도 일정 시간 데이터를 재사용하려고 저장한 값입니다. |
| 왜 모든 보너스를 구현하지 않았나요? | 언어 필터와 시스템 테마를 구현했습니다. 타이핑과 실제 이메일 전송은 선택 사항이며 필수 흐름 이해에 집중했습니다. |

## 6. 발표자가 직접 확인할 학습 목표

- [ ] 시맨틱 태그를 고른 기준을 코드와 함께 설명한다.
- [ ] Flexbox와 Grid의 차이, 이 프로젝트에서의 선택 이유를 설명한다.
- [ ] querySelector → addEventListener → DOM 변경을 설명한다.
- [ ] 화살표 함수·구조분해·map/filter의 역할을 설명한다.
- [ ] fetch/async/await와 로딩·성공·실패·빈 결과를 설명한다.
- [ ] 테마·API·폼 중 최소 세 기능의 이벤트 → 상태 → 렌더링을 스스로 따라간다.

대본을 외우기보다 실제 버튼을 누른 뒤 “어떤 값이 바뀌었고 어떤 함수가 어떤 요소를 바꿨는가”를 말해 보는 것이 좋습니다.


## 7. 비전공자를 위한 개념 설명과 추가 발표 대본

### 7-1. 파일 구조와 실행 환경

HTML은 내용의 구조, CSS는 표현, JavaScript는 동작을 담당합니다. 한 파일에 모두 넣지 않고 역할을 나누면 수정할 곳을 쉽게 찾을 수 있습니다.

| 파일·폴더 | 쉬운 설명 | 발표할 문장 |
| --- | --- | --- |
| index.html | 사이트의 내용과 요소 배치 순서 | “제목·소개·버튼·폼처럼 어떤 내용이 있는지를 정했습니다.” |
| css/style.css | 색상·글꼴·간격·화면 크기에 따른 배치 | “같은 내용을 화면 크기에 맞게 보여 줍니다.” |
| js/main.js | 클릭·입력·데이터 요청 처리 | “사용자의 행동에 따라 상태를 바꾸고 화면에 반영합니다.” |
| images/ | 프로필·아이콘·스크린샷 파일 | “사이트에서 사용하는 이미지와 제출용 화면을 보관합니다.” |
| .vscode/ | 편집기의 개발 환경 설정 | “Live Server를 추천하고 로컬 주소와 포트를 설정했습니다.” |

**실제 위치:** index.html의 `stylesheet`, `script`, `defer`; `.vscode/settings.json`, `.vscode/extensions.json`.

> “VS Code는 코드를 편집하는 도구이고, Live Server는 내 컴퓨터에서 사이트를 실행하고 저장한 변경을 확인하게 해 주는 도구입니다. 현재 설정은 127.0.0.1의 5500번 포트입니다. HTML에 CSS와 JS 파일 경로를 연결했고, defer로 HTML을 읽은 뒤 JS가 실행되게 했습니다.”

`127.0.0.1`은 내 컴퓨터를 뜻하며 공개 배포 주소가 아닙니다. `css/style.css` 같은 상대 경로는 현재 사이트 위치를 기준으로 파일을 찾습니다. `.nojekyll`은 GitHub Pages에서 Jekyll 처리를 건너뛰게 하는 파일이며 화면 디자인을 만드는 파일은 아닙니다.

**시연:** Live Server로 index.html을 열고 제목이나 버튼이 어디의 HTML인지 짚습니다.

**예상 질문:** “파일을 나누면 브라우저는 어떻게 찾나요?” → “HTML의 link와 script에 적힌 경로로 CSS와 JS를 불러옵니다.”

### 7-2. HTML: 태그로 내용의 역할 전달하기

시맨틱 태그는 ‘어떤 역할인지 뜻이 있는 태그’입니다. 보기 좋은 배치는 CSS가 담당하고, HTML은 문서의 의미를 전달합니다.

| 태그 | 이 사이트에서의 역할 |
| --- | --- |
| header | 로고와 상단 메뉴가 있는 머리말 |
| nav | 각 구역으로 이동하는 주요 링크 모음 |
| main | 페이지의 주요 내용 |
| section | Hero, About 등 제목이 있는 주제별 구역 |
| article | 기술·프로젝트처럼 독립적으로 읽을 수 있는 카드 |
| footer | 저작권과 소셜 링크가 있는 하단 |

> “소개 페이지의 의미를 전달하려고 역할에 맞는 태그를 골랐습니다. Hero는 인사와 행동 유도 버튼, About은 소개와 프로필, Skills는 기술 목록, Projects는 저장소 카드, Contact는 문의 폼, Footer는 저작권과 소셜 링크입니다. 단순히 배치를 묶는 곳에는 div도 사용합니다.”

**실제 위치:** index.html의 `href="#about"`, `id="about"`, `alt`, `for="email"`, `id="email"`.

`href="#about"`과 `id="about"`은 이동 링크와 목적지의 연결입니다. `alt`는 이미지의 내용을 글로 전달하며, 화면 낭독기나 이미지가 표시되지 않는 상황에 도움이 됩니다. `label`은 입력칸의 이름입니다. `for`와 입력칸의 `id`를 맞추면 이름과 입력칸이 연결됩니다.

**시연:** About 메뉴를 눌러 이동하고 ‘이메일’ 레이블을 눌러 입력칸에 포커스가 오는지 보여 줍니다.

**예상 질문:** “div는 금지인가요?” → “아닙니다. 전체를 div로만 만들지 않고 의미가 있는 부분에 적절한 태그를 씁니다.”

### 7-3. CSS: 공통 값과 반응형

CSS 변수는 여러 곳에서 함께 사용할 값에 이름을 붙이는 방법입니다. `:root`에 색상·폰트·간격을 정하고 `[data-theme="dark"]`에서 같은 이름의 색상 값을 바꿉니다.

> “메뉴는 가로 방향으로 로고와 링크를 정렬하므로 Flexbox를 썼습니다. 프로젝트는 여러 행과 열에 카드를 배치하므로 Grid를 썼습니다. 둘 다 배치를 만들 수 있지만 이 화면에서 다루기 쉬운 쪽을 골랐습니다.”

**실제 위치:** style.css의 `:root`, `[data-theme="dark"]`, `.nav`, `.projects-grid`, 두 `@media` 구간.

```css
grid-template-columns: repeat(auto-fit, minmax(min(100%, 290px), 1fr));
```

- `auto-fit`: 들어갈 수 있는 열 개수를 화면 너비에 맞춥니다.
- `minmax`: 각 열의 최소·최대 크기 범위를 정합니다.
- `min(100%, 290px)`: 좁은 화면에서 최소 너비가 부모 너비를 넘지 않게 합니다.
- `1fr`: 남은 공간을 같은 비율로 나눕니다.

> “모바일 화면을 기본으로 작성했습니다. 768px부터 태블릿 규칙을, 1024px부터 데스크톱 규칙을 더합니다. 모바일에서는 링크 메뉴를 숨기고 햄버거 버튼을 표시합니다. 버튼과 카드에는 마우스를 올렸을 때 바뀌는 hover, 변화가 부드럽게 이어지는 transition, 카드의 깊이감을 주는 box-shadow를 넣었습니다.”

**시연:** 375px·768px·1024px·1440px로 변경하고 카드와 메뉴를 보여 줍니다. 데스크톱에서 버튼과 카드 위에 마우스를 올립니다.

**예상 질문:** “모바일 퍼스트란 모바일만 만드는 건가요?” → “작은 화면 규칙부터 만들고 넓은 화면 규칙을 추가한다는 뜻입니다.”

### 7-4. JavaScript: DOM과 이벤트

DOM은 브라우저가 HTML을 읽어 만든 문서 요소 구조입니다. 이벤트는 클릭·입력처럼 발생한 일을 뜻합니다. 콜백은 그 일이 발생했을 때 실행하도록 전달한 함수입니다.

| 코드 | 쉬운 뜻 | 실제 사용 위치 |
| --- | --- | --- |
| querySelector | 조건에 맞는 첫 요소 찾기 | themeButton 등 공통 DOM 선택 |
| querySelectorAll | 조건에 맞는 여러 요소 찾기 | fields, 앵커 링크 목록 |
| addEventListener | 어떤 일이 생기면 함수 실행하기 | 메뉴·테마·폼·스크롤 이벤트 |
| textContent | 내용을 글자로 표시하기 | renderTheme, renderForm, summary |
| innerHTML | 문자열을 HTML 구조로 해석해 넣기 | renderProjects, renderFilters |
| classList.add/remove | 스타일 이름을 붙이거나 떼기 | Intersection Observer의 등장 클래스 |
| classList.toggle | 조건에 따라 스타일 이름 켜고 끄기 | renderMenu의 active, renderScroll의 scrolled |
| preventDefault | 브라우저가 원래 하려던 동작 막기 | 앵커 이동과 폼 제출 |

> “버튼 요소를 찾은 뒤 click 이벤트에 함수를 연결했습니다. 이벤트 함수가 상태를 바꾸면 렌더링 함수가 글자·클래스·속성을 바꿉니다. 폼 제출 때는 브라우저의 기본 제출을 막고 직접 검증 결과를 보여 줍니다.”

`click`은 클릭, `input`은 입력값 변경, `submit`은 폼 제출, `scroll`은 스크롤입니다. `blur`는 입력칸을 떠난 일을 뜻하며 현재 폼의 추가 UX에 사용합니다. HTML에 `onclick`이나 인라인 `style`을 넣지 않고 동작은 JS, 표현은 CSS에 둡니다.

**시연:** main.js에서 themeButton 선택, click 처리, renderTheme을 순서대로 찾습니다.

**예상 질문:** “innerHTML과 textContent는 같은가요?” → “전자는 태그를 해석하고 후자는 글자로 표시합니다. 외부 데이터를 HTML에 넣을 때는 escapeHTML로 특수 문자를 바꾸고 링크는 safeRepoURL로 검사합니다.”

### 7-5. ES6+ 문법과 배열: 여러 데이터를 다루기

아래 조각은 이해를 위한 예시입니다. 기존 main.js에 추가하지 않습니다.

```javascript
const names = ["메뉴", "테마"];
names.forEach((name) => console.log(name));
const labels = names.map((name) => `${name} 버튼`);
const selected = names.filter((name) => name === "테마");
const repo = { name: "B1-1", language: "JavaScript" };
const { name, language } = repo;
```

| 문법 | 쉬운 설명 | 프로젝트에서 찾을 곳 |
| --- | --- | --- |
| const / let | 재할당하지 않을 변수 / 재할당할 변수 | state, fetchAllRepos의 page |
| 화살표 함수 `=>` | 함수를 표현하는 문법 | 이벤트 콜백, renderTheme |
| 템플릿 리터럴 | 백틱 안에 `${값}`을 넣어 문자열 구성 | createProjectCard의 HTML |
| 구조분해 할당 | 객체나 배열에서 필요한 값을 꺼내 이름 붙이기 | createProjectCard의 repo 속성 추출 |
| map | 각 항목을 바꾼 새 배열 만들기 | 저장소 → 카드 HTML 문자열 |
| join | 배열의 문자열을 연결하기 | 카드 문자열을 하나로 합치기 |
| filter | 조건에 맞는 항목만 새 배열에 남기기 | 선택한 언어의 프로젝트 |
| forEach | 각 항목에 작업 실행하기 | 링크 이벤트 연결, 폼 필드 검사 |

> “GitHub 데이터는 저장소 객체들이 담긴 배열입니다. 구조분해로 이름과 언어 등을 꺼내고 템플릿 리터럴로 카드 한 개를 만듭니다. map이 저장소마다 이 함수를 호출하고 join이 결과를 합칩니다. 언어 필터는 filter로 조건에 맞는 저장소만 남깁니다.”

**예상 질문:** “filter도 필수인가요?” → “프로젝트 필터 구현은 선택입니다. 다만 map/filter의 사용 이유와 방법을 설명하는 것은 학습 목표이고, 현재 사이트에는 필터도 구현했습니다.”

### 7-6. API와 비동기: 응답을 기다리는 동안의 화면

API는 다른 서비스에 데이터를 요청하는 창구입니다. `fetch`는 요청하고, `async/await`는 응답을 기다리는 비동기 코드의 순서를 읽기 쉽게 표현합니다. 기다리는 동안 브라우저는 다른 클릭을 처리할 수 있습니다.

**실제 위치:** main.js의 `GITHUB_USERNAME`, `fetchAllRepos`, `checkRepoResponse`, `loadProjects`, `renderProjects`.

```text
https://api.github.com/users/dooolll00/repos
```

실제 코드는 정렬과 페이지 조회를 위해 `sort=updated&per_page=100&page=...`를 붙입니다. 응답은 JSON이라는 데이터 형식이며 `response.json()`으로 JS에서 다룰 값으로 읽습니다.

> “요청 직전에 로딩 화면을 표시합니다. 응답 상태를 검사한 뒤 저장소 배열을 저장하고 성공 화면을 그립니다. try는 시도할 처리, catch는 실패했을 때의 처리, finally는 성공·실패 뒤 공통 마무리입니다. 마지막에 요청 제한 타이머를 정리하고 화면을 갱신합니다.”

| 상황 | 사용자에게 보여 주는 결과 |
| --- | --- |
| 요청 중 | 스피너와 로딩 안내 |
| 성공, 저장소 있음 | 프로젝트 카드 리스트 |
| 오류 | 불러올 수 없다는 안내, 구체적 오류, 재시도 버튼 |
| 성공, 저장소 없음 | 표시할 프로젝트가 없다는 안내 |

원문은 비인증 GitHub API 요청을 시간당 60회로 안내합니다. 실제 요청을 반복해 한도를 소진하지 않고 4장의 모의 응답으로 403을 시연합니다. 403/429, 404, 서버 오류, 네트워크 오류를 처리합니다. `fetch`는 HTTP 오류 응답을 받았다고 자동으로 예외를 던지지 않으므로 `response.ok`를 검사합니다.

**추가 기능:** readProjectCache는 5분 캐시를 읽고, fetchAllRepos는 100개 단위로 다음 페이지를 조회합니다. AbortController는 전체 조회가 15초를 넘으면 중단합니다. 이들은 미션 필수로 지정된 방식은 아니며 현재 기능 보존을 위해 유지했습니다.

**예상 질문:** “저장소가 0개면 실패인가요?” → “정상 응답의 결과가 비어 있는 경우입니다. 현재 코드는 success 상태에서 배열 길이로 구분합니다.”

### 7-7. 폼과 사용자 경험

**실제 위치:** index.html의 contact-form과 label/required, main.js의 validateField, renderForm, input/blur/submit 처리.

> “이름·이메일·메시지를 입력받습니다. trim으로 앞뒤 공백을 제외한 값이 비었는지 확인하고, 이메일은 정규식과 입력 요소의 형식 검사 결과를 사용합니다. 문제가 있으면 각 입력칸 근처에 이유를 표시합니다. 모든 값이 정상이면 검증 성공을 표시하지만 실제 메일은 보내지 않습니다.”

`errors`는 오류 문구, `touched`는 한 번 떠난 입력칸, `submitted`는 제출을 시도했는지, `success`는 검증 성공 여부입니다. 처음부터 오류를 표시하지 않으며, 입력을 수정하면 이전 성공 안내가 사라집니다. `novalidate`로 브라우저 기본 검증 팝업 대신 직접 만든 오류 UI를 사용하고, JS에서 필수값을 검사합니다.

**시연:** 빈 제출 → 공백만 입력 → 잘못된 이메일 → 정상 입력 → 성공 후 수정. 오류 시 첫 입력칸으로 포커스가 이동하는 것도 보여 줍니다.

**예상 질문:** “성공이면 메일이 도착한 건가요?” → “아닙니다. 입력 형식 검증 성공입니다. 실제 전송은 선택 과제입니다.”

## 8. 상태 → 렌더링을 최소 세 가지 설명하기

상태는 ‘지금 화면이 기억할 값’이고, 렌더링은 ‘그 값으로 화면을 갱신하는 일’입니다. localStorage는 새로고침 이후에도 값을 보관하는 별도 저장 공간입니다.

| 기능 | 시작 사건 | 바뀌는 상태 | 화면 갱신 함수와 결과 |
| --- | --- | --- | --- |
| 테마 | 테마 버튼 클릭 | state.theme, explicitTheme | renderTheme → html data-theme, 버튼 안내, CSS 색상 |
| 메뉴 | 햄버거 클릭 등 | setMenuOpen → state.menuOpen | renderMenu → active, aria-expanded |
| API | 최초 로드 또는 재시도 | projects.status, repos, error | renderProjects → 로딩·카드·오류·빈 안내 |
| 폼 | input/blur/submit | form.values/errors/success 등 | renderForm → 오류·글자 수·성공 안내 |
| 필터(선택) | 언어 버튼 클릭 | projects.filter | 버튼 선택 상태 갱신, renderProjects → 해당 언어 카드 |

발표할 때는 테마·API·폼 세 줄을 반드시 자기 말로 설명합니다. 상태 변수만 바꾸면 DOM이 저절로 바뀌는 것이 아니므로 각 흐름의 마지막 렌더링 호출을 찾아 보여 줍니다.

```text
테마: 클릭 → state.theme 변경 → localStorage 저장 → renderTheme → CSS 변수 적용
API: 요청 시작 → loading → 데이터 또는 오류 저장 → success/error → renderProjects
폼: 입력 → values 갱신 → 검사 시점이면 errors 갱신 → renderForm → 오류 표시/숨김
```

API의 빈 결과는 별도 empty 상태 변수를 두지 않고 성공한 배열의 길이로 판단합니다. 스크롤 UI는 현재 scrollY를 읽어 바로 갱신합니다. 모든 기능에 억지로 별도 상태 변수가 필요한 것은 아닙니다.

## 9. 발표 시연 순서와 제출 설명

| 순서 | 실행할 행동 | 관찰하고 말할 내용 |
| --- | --- | --- |
| 1 | 로컬 사이트 전체 훑기 | Hero·About·Skills·Projects·Contact·Footer 역할 |
| 2 | 375 → 768 → 1024 → 1440px | 모바일 메뉴와 카드 배치, 가로 넘침 여부 |
| 3 | 햄버거 두 번 클릭 | 열림/닫힘, state.menuOpen과 active 연결 |
| 4 | 메뉴의 섹션 링크 클릭 | 부드러운 이동, 메뉴 닫힘 |
| 5 | 아래로 스크롤 후 맨 위 버튼 클릭 | 60px 헤더 배경, 300px 버튼 표시, 최상단 이동 |
| 6 | 테마 변경 후 새로고침 | 선택값 복원, localStorage의 portfolio-theme |
| 7 | 구역이 나타나는 지점으로 스크롤 | Observer threshold 0.2, 한 번 등장; 동작 줄이기 설정에서는 생략 |
| 8 | 프로젝트와 언어 필터 선택 | 실제 데이터 또는 모의 데이터인지 구분해 설명 |
| 9 | 4장의 모의 시연 | 로딩·빈 결과·403·재시도 성공, 시연 뒤 캐시와 fetch 복원 |
| 10 | 빈 폼부터 정상 폼까지 제출 | 필수·이메일 검사, 오류·성공 안내, 실제 미전송 |
| 11 | README와 제출물 확인 | 저장소·Pages URL, 설명·사용 기술·스크린샷 |

스크롤 60px·300px은 현재 구현 기준입니다. 원문은 README에 명시하면 변경을 허용합니다. Observer는 0.2 이상 권장이며 역시 값을 바꾸면 README에 명시합니다.

**배포 설명 대본:**

> “로컬 서버는 내 컴퓨터에서 확인하는 용도이고 GitHub Pages는 다른 사람도 접속하는 공개 사이트입니다. GitHub에 코드를 반영하고 Pages 배포가 완료되면 공개 주소에서 반응형·메뉴·테마·스크롤·API·폼을 다시 확인해야 합니다. README에는 프로젝트 설명, 사용 기술, 배포 URL과 화면 캡처를 담았습니다.”

현재까지 기록된 검증을 구분합니다.

| 기준일·대상 | 확인된 범위 | 발표 시 한계 |
| --- | --- | --- |
| 2026-09-07 기존 공개본 | Pages 배포 및 주요 실제 기능 검증 기록 | 9월 10일 코드 정리의 배포 결과는 아님 |
| 2026-09-10 로컬 정리본 | Chrome 146.0.7680.165, tests/review.py 일반 실행 27개 통과 | API는 모의 응답, 실제 API·공개본 재검증 아님 |
| 2026-09-10 전후 화면 비교 | 1440px 밝은 화면·375px 모바일·1440px 다크 전체 이미지 일치 | 동일 모의 데이터, 외부 폰트 차단 조건 |

미션은 최신 Chrome 동작을 요구합니다. 제출 시점의 Chrome 버전을 확인하고 해당 환경에서 점검합니다. 기존 검증 버전이 언제나 최신이라는 뜻은 아닙니다. `tests/review.py`는 개발용 Python/Playwright 검사이며 사이트에 로드되는 라이브러리가 아닙니다. 이번 가이드 수정에서는 브라우저 테스트를 다시 실행하지 않았습니다.

제출 자료는 GitHub 저장소 URL, GitHub Pages URL, 데스크톱·모바일·다크 모드 스크린샷입니다. 실제 제출 전 공개 사이트와 제출 캡처가 최종 코드에 맞는지 확인합니다.

## 10. 미션 원문 전체 대응표

아래 빈 체크는 **발표자가 설명·시연 준비를 마쳤는지** 표시하는 칸입니다. 구현이 없다는 표시나 자동 합격 판정이 아닙니다. 파일은 1장의 링크로 열고 검색어를 Cmd+F로 찾습니다.

| 준비 | 원문 요구사항·목표 | 설명 위치 | 코드·자료 검색어 또는 확인 방법 |
| --- | --- | --- | --- |
| [ ] | 순수 HTML/CSS/JS 반응형 포트폴리오 완성, 웹 동작 이해와 React 기초 | 2, 7, 8장 | index.html, style.css, main.js |
| [ ] | 시맨틱 설계 이유를 스스로 설명 | 7-2 | header/nav/main/section/article/footer |
| [ ] | Flexbox/Grid 차이와 선택 이유 설명 | 7-3 | .nav, .projects-grid |
| [ ] | querySelector→addEventListener 흐름 설명 | 7-4 | themeButton, click |
| [ ] | 화살표·구조분해·map/filter 필요성과 사용 설명 | 7-5 | createProjectCard, visible |
| [ ] | fetch/async/await와 상태 UI 설명 | 7-6 | fetchAllRepos, loadProjects |
| [ ] | 이벤트→상태→DOM 연결 설명 | 8장 | renderTheme, renderProjects, renderForm |
| [ ] | index.html/css/js/images 역할 분리 | 7-1 | 프로젝트 파일 구조 |
| [ ] | 외부 CSS·JS 연결, VS Code+Live Server | 7-1 | stylesheet, script, .vscode/ |
| [ ] | 시맨틱 태그 6종 사용, 전체 div만 사용하지 않기 | 7-2 | header/nav/main/section/article/footer |
| [ ] | Hero 인사·CTA | 7-2 | id="hero", 버튼 링크 |
| [ ] | About 자기소개·프로필 이미지 | 7-2 | id="about", 프로필 img |
| [ ] | Skills 기술 목록 | 7-2 | id="skills" |
| [ ] | Projects API 카드 | 7-6 | id="projects", project-list |
| [ ] | Contact 문의 폼 | 7-7 | contact-form |
| [ ] | Footer 저작권·소셜 링크 | 7-2 | id="footer", year |
| [ ] | 각 섹션 앵커 링크 | 7-2, 9장 | nav-menu의 href와 대상 id |
| [ ] | 이미지에 의미 있는 alt | 7-2 | img의 alt |
| [ ] | label의 for와 입력 id 일치 | 7-2, 7-7 | name/email/message 레이블 |
| [ ] | 외부 css/style.css | 7-1 | link stylesheet |
| [ ] | :root 색상·폰트·간격 변수 | 7-3 | :root |
| [ ] | 다크 모드 CSS 변수 별도 정의 | 7-3 | [data-theme="dark"] |
| [ ] | nav Flexbox, 로고 왼쪽·메뉴 오른쪽 | 7-3 | .nav |
| [ ] | Projects Grid, auto-fit/minmax | 7-3 | .projects-grid |
| [ ] | 모바일 퍼스트·768px·1024px | 7-3, 9장 | 두 min-width 미디어 쿼리 |
| [ ] | 모바일 메뉴 숨김·햄버거 표시 | 7-3, 9장 | nav-menu, menu-toggle |
| [ ] | 버튼·카드 hover와 transition, 카드 box-shadow | 7-3 | :hover, transition, box-shadow |
| [ ] | JS defer 연결 | 7-1 | script defer |
| [ ] | var 대신 const/let | 7-5 | main.js 선언 |
| [ ] | onclick 대신 addEventListener | 7-4 | 이벤트 연결과 HTML 속성 |
| [ ] | querySelector/querySelectorAll | 7-4 | 공통 DOM 선택, 앵커 순회 |
| [ ] | textContent/innerHTML | 7-4 | renderForm, renderProjects |
| [ ] | classList.add/remove/toggle | 7-4 | Observer, renderMenu |
| [ ] | click/submit/scroll/input 이벤트 | 7-4 | 각 addEventListener |
| [ ] | event.preventDefault() | 7-4, 7-7 | 앵커, submit |
| [ ] | 햄버거 재클릭 열기·닫기, active 토글 | 8, 9장 | setMenuOpen, renderMenu |
| [ ] | 네비게이션 클릭 부드러운 스크롤 | 9장 | scrollIntoView, scrollBehavior |
| [ ] | 맨 위 버튼 300px 표시·클릭 이동 | 9장 | renderScroll, scrollTo |
| [ ] | 네비게이션 배경 60px 변경 | 9장 | scrolled |
| [ ] | 다크 모드 토글·localStorage·새로고침 유지 | 8, 9장 | renderTheme, THEME_KEY |
| [ ] | Intersection Observer 등장 효과 | 9장 | IntersectionObserver, threshold |
| [ ] | 스크롤 기준 변경 허용·README 명시, 0.2 이상 권장 | 9장 | README 수치 설명 |
| [ ] | 이름·이메일·메시지 폼 | 7-7 | contact-form |
| [ ] | 필수값·이메일 검사·필드 근처 오류 | 7-7 | validateField, 각 -error 요소 |
| [ ] | 제출 기본 동작 방지·성공 안내 | 7-7 | submit, form-status |
| [ ] | 화살표 함수·템플릿 리터럴·구조분해 사용 | 7-5 | createProjectCard |
| [ ] | map으로 카드 변환, forEach 순회 | 7-5 | visible.map, fields.forEach |
| [ ] | filter 조건별 프로젝트 표시(선택) | 7-5 | repos.filter |
| [ ] | 본인 /users/{아이디}/repos, fetch/async/await | 7-6 | GITHUB_USERNAME, fetchAllRepos |
| [ ] | 로딩 스피너 또는 글, 성공 카드 | 7-6, 4장 | renderProjects loading/success |
| [ ] | 오류 메시지와 재시도 버튼 | 7-6, 4장 | retry-projects |
| [ ] | 빈 결과 안내 | 7-6, 4장 | visible.length |
| [ ] | try/catch 오류 처리 | 7-6 | loadProjects |
| [ ] | 최소 3가지 상태→렌더링 흐름 | 8장 | 테마·API·폼, 추가 메뉴·필터 |
| [ ] | GitHub Pages 외부 접속 URL | 9장 | Pages URL, 배포 완료 확인 |
| [ ] | 공개본 반응형·인터랙션·API·폼 정상 동작 | 9장 | 새 변경 배포 후 다시 확인 필요 |
| [ ] | README 설명·기술·배포 URL·스크린샷 | 9장 | README.md |
| [ ] | 언어별 필터 버튼·array.filter(보너스) | 7-5 | 구현됨: renderFilters |
| [ ] | Hero 타이핑 효과(보너스) | 5장 | 미구현, 선택 사항 |
| [ ] | Formspree/EmailJS 실제 전송(보너스) | 7-7 | 미구현, 현재 검증 데모 |
| [ ] | 시스템 테마 감지(보너스) | 8장 | 구현됨: systemTheme, prefers-color-scheme |
| [ ] | React/Vue/jQuery/Bootstrap/Tailwind 등 외부 라이브러리 금지 | 7-1, 9장 | 사이트는 순수 HTML/CSS/JS |
| [ ] | 아이콘·웹 폰트 허용 | 이 표 | 현재 Pretendard 웹 폰트 사용, UI 프레임워크와 구분 |
| [ ] | UI 화려함보다 이벤트·상태·렌더링 이해 우선 | 8장 | 디자인 도식은 참고 예시이며 정답 아님 |
| [ ] | 인라인 style 금지 | 7-4 | index.html에 style 속성 없음 |
| [ ] | 최신 Chrome 동작 | 9장 | 제출 시 버전·동작 확인, 기존 검증 범위 구분 |
| [ ] | 저장소 URL·Pages URL 제출 | 1, 9장 | 두 공개 링크 |
| [ ] | 데스크톱·모바일·다크 스크린샷 제출 | 9장 | images/screenshots/desktop.png, mobile.png, dark.png |
| [ ] | 비인증 시간당 60회 안내·반복 새로고침 주의·403 UI | 7-6, 4장 | checkRepoResponse, 모의 응답 시연 |

설명을 마친 항목도 실제 코드에서 해당 부분을 찾을 수 있는지 확인하세요. 이해가 어려운 항목은 “사용자가 무엇을 했나 → 어떤 값이 달라졌나 → 어느 함수가 화면을 바꿨나” 세 문장으로 다시 풀어 연습합니다.
