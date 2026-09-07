# B1-1 발표 가이드

발표의 중심은 **“버튼이나 입력이 어떤 상태를 바꾸고, 그 상태가 어떻게 화면에 반영되는가”**입니다. 아래 대본을 본인 말투로 바꾸어 연습하세요. 실제로 수행한 작업과 이해한 범위만 설명하고, 자동 검증 결과와 본인의 설명 능력은 구분합니다.

## 1. 시작 전 준비

- 로컬 최종본을 Live Server로 실행하고 Chrome 개발자 도구를 엽니다.
- `index.html`, `css/style.css`, `js/main.js`를 열어 둡니다.
- GitHub API 카드가 표시되는지 확인합니다. 5분 캐시가 있으므로 새로고침해도 로딩이 아주 짧거나 보이지 않을 수 있습니다.
- 제출 URL은 [배포된 Pages](https://dooolll00.github.io/B1-1/)입니다. 2026-09-07 새 디자인과 Footer 메뉴·데이터 검증 보완의 배포를 확인했습니다.
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
> 모바일 메뉴도 같은 구조입니다. 클릭하면 state.menuOpen이라는 참·거짓 값을 뒤집고 renderMenu가 active 클래스와 aria-expanded를 맞춥니다. 상태는 기억하는 값이고 렌더링은 그 값을 실제 화면에 반영하는 작업입니다.

다크 모드 전환 → 새로고침 → 모바일 메뉴 열기·닫기를 시연합니다. `const state`여도 객체 내부 속성은 변경할 수 있다는 점을 설명할 준비를 합니다.

### 2:30~3:50 — GitHub API와 네 가지 화면

> loadProjects는 요청 전에 상태를 loading으로 바꾸고 스피너를 먼저 보여 줍니다. fetch와 async/await로 GitHub 응답을 기다린 뒤 response.ok를 확인합니다. 정상 데이터는 repos에 저장하고 success로 바꿉니다. renderProjects는 저장소 객체를 map으로 카드 문자열로 변환하고 join으로 합쳐 화면에 넣습니다.
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

맨 위 버튼과 README 체크리스트를 보여 줍니다. “GitHub Pages에 새 디자인과 기능 보완을 배포했고, 공개 사이트에서도 주요 기능을 검증했습니다”라고 설명합니다. 이후 수정이 있으면 README의 최신 배포 현황을 확인하세요.

## 3. 설명할 코드 위치

검색(Cmd+F)으로 아래 이름을 찾으면 됩니다. 설명용으로 상태 값을 직접 변경할 때는 로컬에서만 연습하세요.

| 질문 | 파일·검색어 | 설명해야 할 연결 |
| --- | --- | --- |
| 시맨틱 구조 | `index.html`: `header`, `main`, `article`, `footer` | 역할 기준으로 나눈 이유 |
| Flexbox와 Grid | `css/style.css`: `.nav`, `.projects-grid` | 한 축 정렬과 행·열 구성 |
| 모바일 퍼스트 | `css/style.css`: `min-width: 768px`, `min-width: 1024px` | 기본 모바일 규칙에 넓은 화면 규칙을 추가 |
| DOM 선택·이벤트 | `js/main.js`: `themeButton`, `addEventListener` | 버튼 선택 → 클릭 감지 |
| 상태와 렌더링 | `state`, `renderTheme`, `renderMenu`, `renderForm` | 값 변경만으로 DOM은 자동 변경되지 않음 |
| 비동기 API | `loadProjects`, `response.ok`, `finally` | 요청 전 로딩, 응답 검사, 성공·오류, 렌더링 |
| 배열·ES6+ | `renderProjects`, `visible`, `.map`, `.join` | 구조분해로 속성 추출, filter로 선택, map으로 변환 |
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
