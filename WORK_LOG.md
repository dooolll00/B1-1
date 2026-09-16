# B1-1 작업 기록

> 이 파일은 Codex 채팅이 사라져도 프로젝트 작업 흐름을 이어가기 위한 기록입니다.
> Codex는 작업 시작 시 이 파일을 읽고, 작업 종료 시 새 기록을 맨 아래에 추가합니다.

## 프로젝트 상태

- 프로젝트: B1-1
- 상태: 기존 프로젝트 수정/개선 예정
- 기본 브랜치: `main`
- 작업 원칙: 기존 파일을 보존하면서 필요한 부분만 수정

---

## 2026-09-07 — 작업 기록 시스템 시작

### 요청
- 앞으로 Codex 작업 기록이 사라져도 이전 작업 내용을 이어갈 수 있도록 기록 체계를 만든다.

### 변경 파일
- `AGENTS.md` 추가
- `WORK_LOG.md` 추가

### 핵심 작업
- Codex가 작업 시작 시 이 기록을 읽도록 규칙을 작성했다.
- 작업 종료 시 요청, 변경 파일, 테스트 결과, 남은 문제, 다음 할 일을 기록하도록 했다.
- 민감정보는 기록하지 않도록 규칙을 추가했다.

### 다음 작업
- B1-1의 기존 기능을 수정하거나 개선할 때 이 기록을 계속 이어서 작성한다.

## 2026-09-07 — 미션 검토 사전 확인

- 요청: B1-1 요구사항 충족 여부 검토, README 체크리스트와 발표 설명 보완.
- 변경 파일: `WORK_LOG.md`에 이번 사전 확인 기록 추가.
- 핵심 작업: 기존 작업 기록, 파일 목록, README, 미션 수행 가이드 및 소스를 열어 기존 문서 구성을 확인했다. README에 검토표가 있으나 공식 미션 원문은 아직 전달되지 않았다.
- 명령/결과: `cat WORK_LOG.md`, `rg --files`, 문서·소스 읽기 실행. `git status --short`에서 시작 시 변경 없음 확인. Python 기록 추가는 인코딩 오류로 실패하여 셸 heredoc으로 추가했다. 동작 테스트는 아직 실행하지 않았으며 기존 검증 완료 주장은 재확인 전이다.
- 미해결/다음 작업: 미션 원문을 받은 뒤 항목별 코드 대조, 동작 검증, 구현 보완, README 체크리스트 및 발표 설명 작성. 기존 수행 가이드를 공식 요구사항 원문으로 간주하지 않는다.
- Git commit/push: 수행하지 않음.

## 2026-09-07 19:43 KST — 미션 원문 기준 구현 검토 및 발표 자료 보완 완료

### 요청
- 제공한 B1-1 미션 원문을 기준으로 모든 요구사항 충족 여부 검토, README 체크리스트 추가, 부족한 구현과 발표 설명 보완. 사용자가 작업을 끝까지 이어서 완료하도록 재요청함.

### 수정·추가 파일
- `index.html`: Footer 메뉴 링크와 `id="footer"` 추가.
- `js/main.js`: `isRepoList()` 추가 및 API 응답·캐시 검증에 적용.
- `README.md`: 원문에 대응하는 체크리스트, 구현 근거, 기술 설명, 실행·검증·배포 구분 정리.
- `MISSION_REQUIREMENTS.md`: 사용자가 제공한 미션 원문 보존.
- `PRESENTATION_GUIDE.md`: 5~7분 대본, 핵심 코드 위치, 로컬 API 상태 시연·복원 코드, 예상 질문, 학습 목표 확인표 추가.
- `MISSION_GUIDE.md`: 실제 폴더명·Git 상태·검증 방법·네트워크 실패 시연 설명 정정, 새 문서 연결.
- `tests/review.py`: 실제 Chrome을 사용하는 재현 가능한 개발용 자동 검증 추가.
- `images/screenshots/desktop.png`, `mobile.png`, `dark.png`: 로컬 최종 코드·실제 GitHub 데이터로 갱신.
- `WORK_LOG.md`: 이번 기록 추가. CSS와 기존 디자인 값은 변경하지 않음.

### 핵심 작업·판단
- 요구사항의 모든 구역 앵커를 충족하도록 Footer 이동을 추가했다.
- 기존 코드는 `[null]` 같은 캐시를 정상 배열로 취급해 API를 재조회하지 않고 네트워크 오류로 안내했다. 카드에 필요한 항목 형식을 검사하여 잘못된 캐시는 무시하고 API 응답 형식 오류는 별도로 안내하도록 수정했다.
- README에 적힌 Live Server가 실제 환경에는 없었으므로 `ritwickdey.LiveServer` v5.7.10을 설치했다. 기존 `.vscode` 설정(127.0.0.1:5500)은 유지했다.
- 필수 구현과 선택 과제를 구분했다. 언어 필터·시스템 테마는 구현됨. 타이핑·실제 이메일 전송은 선택 사항으로 미구현 유지.
- 발표자의 실제 설명 능력은 자동 검증할 수 없어 개인 연습 체크를 남겼다.
- 배포 URL은 기존 공개본이며 이번 수정은 로컬에만 있다. 기존 배포 정상 동작과 새 코드 배포 완료를 혼동하지 않도록 문서에 명시했다.

### 실행한 테스트·명령과 결과
- 미션 원문, 기존 작업 기록, 소스·문서·설정 읽기; `git status --short`, `git diff`로 기존 변경을 보존하며 검토.
- `code --list-extensions`로 Live Server 부재 확인 → `code --install-extension ritwickdey.LiveServer` 성공 → 설치 목록에서 재확인.
- `/tmp/b1-1-review-venv` 가상환경에 Playwright 1.60.0 설치. 사이트 런타임에는 외부 라이브러리를 추가하지 않음.
- 검증용 `python3 -m http.server 5511 --bind 127.0.0.1` 실행.
- `/tmp/b1-1-review-venv/bin/python tests/review.py --live`: Chrome 146.0.7680.165에서 29개 검증 항목 모두 통과.
- 범위: 시맨틱 구조·앵커·label·alt·이미지·Flex/Grid, 320/375/767/768/1024/1440px, 메뉴·포커스·스크롤 경계, 테마 저장·시스템 변경, 폼 검증, 필터, API 4가지 UI, 403/429/404/500·재시도·네트워크 오류, 비정상 응답, 손상/만료/유효 캐시·저장소 차단, 100+1 페이지네이션, HTML/URL 주입 방지, 15초 제한, 실제 Observer.
- 초기 테스트 실행 중 테스트 코드의 중복 Home 링크 가정, 메뉴에 가려진 클릭 대상, 비동기 화면 대기, Playwright 콜백 인자 처리 문제를 수정한 뒤 전체 검증을 통과했다.
- 로컬과 기존 Pages에서 실제 GitHub 저장소 각각 7개 확인. 기존 Pages에서도 테마·폼·모바일 메뉴·스크롤·반응형 통과. 검증 중 JS 실행 오류 없음.
- `curl -I -L --max-time 20 https://dooolll00.github.io/B1-1/`: HTTP 200. 웹 열기 도구 접근 실패는 curl과 실제 Chrome 접속으로 대체 확인.
- Python 문법, 문서의 로컬 링크, `var`/인라인 속성 부재, CSS 필수 선언·설정 파일 검사 통과. `git diff --check` 통과.
- Chrome 전체 화면 스크린샷 3종 갱신 후 이미지 열기로 육안 확인.
- 발표 Console 코드 별도 실행: 모의 403 → 재시도 성공 카드 → 원래 fetch 복원 및 캐시 교체 확인. 실제 네트워크는 이 시연 검증에서 모킹함.

### 중요한 설정·배포 방법
- 테마 키 `portfolio-theme`, API 캐시 키 `portfolio-repos-dooolll00`, 캐시 5분.
- 헤더 변경 60px, 맨 위 버튼 300px, Observer threshold 0.2, 전체 API 조회 제한 15초.
- `tests/review.py`는 localhost:5511 서버와 설치된 Google Chrome 필요. 일반 실행은 API 모킹, `--live`는 실제 API/기존 Pages 점검 및 스크린샷 덮어쓰기.
- Pages 일반 배포 절차는 main 루트의 정적 파일을 push하고 Actions 성공 후 URL 검증. 이번에는 설정 화면을 확인하거나 변경하지 않음.

### 미해결·다음 할 일
- 요청한 로컬 검토·수정·문서 보완 완료. 이번 변경의 GitHub 업로드와 배포 반영은 아직 수행하지 않음.
- 사용자가 배포를 요청하면 변경 파일을 확인해 커밋·push 후 Pages 최종본의 새 Footer 앵커와 기능을 재확인한다.
- 발표 전 `PRESENTATION_GUIDE.md`로 여섯 학습 목표와 최소 세 상태 흐름을 직접 연습한다.
- 검증 브라우저는 현재 설치된 Chrome 버전이며 모든 기기·모든 입력이나 다른 최신 버전까지 검증한 것은 아니다.
- Git commit/push: 수행하지 않음. 커밋 메시지 없음.

## 2026-09-07 19:50 KST — 사용자 제안 블루·퍼플 테마와 Pretendard 적용

### 요청
- 제공한 디자인 CSS를 분석하고 미션에 부합하는 경우에만 적용한다.

### 변경 파일
- `css/style.css`: 최상단 Pretendard @import, 라이트 블루·다크 퍼플 변수, 폰트, 공통 반경 10px, 그림자 적용.
- `README.md`: 디자인 설명·미션 적합성·검증 결과 및 새 디자인의 배포 반영 전 상태 명시.
- `MISSION_GUIDE.md`: 로컬 디자인 설명을 최신 상태로 수정.
- `images/screenshots/desktop.png`, `mobile.png`, `dark.png`: 새 디자인·실제 GitHub 데이터로 재생성.
- `WORK_LOG.md`: 이번 기록 추가.

### 핵심 작업과 판단
- 미션 원문의 웹 폰트 허용, 외부 CSS 사용, :root 및 [data-theme="dark"] 변수 요구에 부합하므로 반영했다. Pretendard는 웹 폰트이며 UI 프레임워크를 추가하는 변경이 아니다.
- 사용자 메시지의 Markdown 링크·이스케이프·HTML 공백 표기를 실제 CSS 문법으로 정리했다. @import에는 순수 CDN URL을 사용했다.
- 사용자가 제시한 변수 값을 적용했다. 별도 고정값을 사용하는 Hero 코드 그래픽 등의 색상과 모서리는 변수 변경 범위에 포함되지 않는다.
- 폰트 로딩 실패 시 --font에 지정된 시스템 폰트를 사용한다. 기존 반응형·상태·DOM 이벤트 기능을 유지했다.

### 테스트·명령과 결과
- WORK_LOG.md 및 미션 원문·현재 CSS 확인, git status/diff로 이전 미커밋 변경 보존.
- curl로 제공된 Pretendard CSS URL 정상 응답과 @font-face 내용 확인. 웹 열기 도구 접근 실패는 curl과 실제 브라우저 로딩으로 대체 확인.
- 검증용 localhost:5511 서버에서 `/tmp/b1-1-review-venv/bin/python tests/review.py --live` 실행: 설치된 Chrome 146.0.7680.165에서 29개 항목 모두 통과.
- 별도 Chrome 확인: 실제 Pretendard 400/600/700/800/900 로딩 성공, CDN 차단 시 시스템 폰트 표시와 사이트 동작 유지, 라이트 #f8f9fa·다크 #0f172a 배경 및 카드 10px 반경, 320/375/768/1024/1440px 가로 넘침 없음.
- 로컬·기존 배포에서 실제 GitHub 공개 저장소 각 7개 확인. 기존 배포에는 새 디자인이 아직 반영되지 않음.
- 스크린샷 3종 갱신, 데스크톱 라이트·다크 이미지를 열어 육안 확인. `git diff --check` 통과.

### 미해결·다음 작업
- 요청한 디자인 적용과 로컬 검증 완료. 이번 수정의 GitHub 업로드·배포 반영은 아직 수행하지 않음.
- 배포 요청 시 이전 기능·문서 보완과 이번 디자인 변경을 함께 검토해 반영한다.
- commit/push: 수행하지 않음, 커밋 메시지 없음.

## 2026-09-07 — 변경 사항 커밋·push 및 Pages 배포 시작

- 요청: 미션 보완과 새 디자인을 커밋하고 GitHub에 push한 뒤 배포한다.
- 포함 파일: index.html, css/style.css, js/main.js, README.md, MISSION_GUIDE.md, MISSION_REQUIREMENTS.md, PRESENTATION_GUIDE.md, tests/review.py, images/screenshots/{desktop,mobile,dark}.png, WORK_LOG.md.
- 사전 확인: WORK_LOG 확인, git fetch origin 성공, HEAD와 origin/main 차이 0/0, git diff --check 통과. 앞선 최종 코드의 Chrome 29개 검증 및 폰트 로딩·차단 검증 통과 결과를 사용한다. 이후 애플리케이션 소스 변경 없음.
- 커밋 메시지: feat: refresh portfolio theme and complete mission review materials
- 진행 상태: 이 기록을 포함해 main에 커밋·push하고, 해당 커밋의 Pages 배포와 공개 사이트에서 새 CSS·JS·Footer 및 주요 기능을 확인한다. 실제 push·배포 결과는 후속 기록에 추가한다.
- 미해결/다음 작업: 배포 완료 확인과 README·발표 가이드의 배포 상태 갱신.

## 2026-09-07 19:59 KST — 커밋·원격 업로드·Pages 배포 확인 완료

### 요청 및 변경 파일
- 사용자 요청: 누적 변경 사항의 커밋·push·배포.
- 기능·디자인·테스트·스크린샷·문서 12개 파일을 커밋했다. 이후 README.md, MISSION_GUIDE.md, PRESENTATION_GUIDE.md의 배포 전 안내를 완료로 수정하고 WORK_LOG.md에 결과를 추가했다.

### 커밋과 push 결과
- 기능 커밋 메시지: `feat: refresh portfolio theme and complete mission review materials`.
- 최초 로컬 커밋: `62ac6b6`. 터미널 `git push origin main`은 GitHub 사용자 인증이 없어 실패했다.
- 연결된 GitHub 앱으로 blob/tree/commit을 생성하고 force 없이 main을 갱신해 원격 업로드를 완료했다. 원격 커밋: `e318a2969fba0d9cb774c100dadcaf7c3194b2e6`.
- 로컬·원격 파일 트리는 `5db4167ce7654568c5082e158382eca2d0dc9bce`로 정확히 동일했다. 작성 메타데이터 차이로 커밋 SHA만 달라졌다.
- 최초 로컬 커밋은 `backup/b1-1-local-before-app-upload` 브랜치로 보존했다. fetch 후 rebase에서 이미 반영된 동일 변경이 생략되어 main이 원격과 동기화됐다. 원격 강제 push나 기존 파일 삭제 없음.
- 배포 완료 기록 커밋 메시지: `docs: record successful portfolio deployment`. 이 문서 갱신도 같은 GitHub 앱 방식으로 커밋하고 main에 반영한다.

### 배포 및 검증 결과
- `pages build and deployment` 실행 `34114075751`: completed / success, 대상 커밋 e318a29.
- 작업 URL: https://github.com/dooolll00/B1-1/actions/runs/34114075751
- 공개 URL: https://dooolll00.github.io/B1-1/
- 공개 index.html, css/style.css, js/main.js를 다운로드해 로컬 파일과 바이트 일치 확인.
- 실제 Chrome 공개 사이트 검증: HTTP 200, Pretendard 로딩, 새 라이트·다크 배경색, 테마 새로고침 유지, 320/375/768/1024/1440px 가로 넘침 없음, 모바일 메뉴·Footer 앵커·포커스, 맨 위 이동, 폼 필수값·성공 안내, 이미지, 실제 GitHub 저장소 7개 표시 통과. JS 실행 오류 없음.
- 검증 명령: 기존 Chrome 29개 통과 결과 확인, `/tmp/b1-1-review-venv/bin/python /tmp/b1-1-deploy-check.py`, git diff --check, GitHub Actions API 조회.
- 배포 설정은 변경하지 않았으며 main 갱신으로 기존 Pages 워크플로가 자동 실행됐다.

### 미해결·다음 작업
- 요청한 기능·디자인 변경의 공개 배포와 동작 검증 완료.
- 터미널 GitHub 인증은 설정하지 않았다. 이번 업로드는 인증된 앱 연결을 사용했으며, 향후 터미널에서 직접 push하려면 별도 GitHub 인증이 필요하다.
- 발표 가이드로 설명을 연습하고 이후 수정 때도 배포 후 주요 기능을 확인한다.

## 2026-09-07 20:06 KST — 제공된 평가 기준·미션 원문 삭제

- 요청: 사용자가 제공한 평가 기준과 미션 원문을 삭제한다.
- 변경 파일: `MISSION_REQUIREMENTS.md` 삭제, `README.md`와 `MISSION_GUIDE.md`의 원문 링크·소개·파일 구조·git add 예시 정리, `WORK_LOG.md`에 이 기록 추가.
- 핵심 작업: 원문 전문이 담긴 파일을 삭제하고 문서 연결을 제거했다. 구현 체크리스트·학습 가이드·발표 가이드는 유지했다. 기존 작업 기록에는 원문 전문이 없으며 이전 작업 이력은 보존했다.
- 검증: 문서 전체에서 원문 파일 참조 검색, 로컬 문서 링크 존재 검사, `git diff --check` 수행. 기능 소스 변경이 없어 브라우저 테스트는 반복하지 않는다.
- 미해결/다음 작업: 로컬 문서 삭제 완료. 이번 삭제는 아직 commit/push하지 않았으므로 원격 저장소·배포본에는 반영 전이다. Git 과거 이력이나 저장소 밖의 채팅 첨부 파일은 변경하지 않았다.
- Git commit/push: 수행하지 않음.

## 2026-09-07 20:08 KST — README 발표 가이드 안내 제거

- 요청: README 안의 발표 가이드를 삭제한다.
- 변경 파일: `README.md`, `WORK_LOG.md`.
- 핵심 작업: README 상단 발표 가이드 링크, 파일 구조의 가이드 항목, 발표 가이드 연결 체크 항목 및 발표 연습 안내 문장을 제거했다. `PRESENTATION_GUIDE.md` 파일 자체는 유지했다. 이전 미커밋 변경은 보존했다.
- 검증: README의 `PRESENTATION_GUIDE.md` 참조가 없고 가이드 파일은 존재함을 확인, `git diff --check` 통과. 문서 수정으로 브라우저 테스트는 생략했다.
- 미해결/다음 작업: 로컬 수정 완료. 원격 반영은 commit/push 시 진행한다.
- Git commit/push: 수행하지 않음.

## 2026-09-07 — 문서 정리 커밋 및 원격 반영

- 요청: 미션 원문 삭제와 README 발표 가이드 안내 제거를 커밋·push한다.
- 변경 파일: README.md, MISSION_GUIDE.md, WORK_LOG.md 수정; MISSION_REQUIREMENTS.md 삭제.
- 핵심 작업: 이전 두 요청의 문서 변경을 하나의 커밋으로 묶어 main에 반영한다. 발표 가이드 파일은 유지한다.
- 검증: git fetch origin 후 HEAD와 origin/main 차이 0/0, git diff --check 통과. 문서 변경만 있어 브라우저 테스트는 반복하지 않는다.
- 커밋 메시지: `docs: remove mission source and presentation guide references`.
- 원격 반영 방법: 터미널 인증 부재가 앞선 작업에서 확인되어 인증된 GitHub 앱으로 같은 파일 트리의 커밋을 생성하고 force 없이 main에 업로드한다. 로컬 main도 원격과 동기화하며 결과는 최종 응답에서 확인한다.
- 미해결/다음 작업: 원격 파일 삭제·문서 반영과 작업 폴더가 깨끗한지 확인한다. Git 과거 이력은 변경하지 않는다.

## 2026-09-10 14:56 KST — 사용자 제공 미션 원문 요구사항 정리

### 요청·출처·작업 범위

- 요청: 새로 제공한 미션 원문을 WORK_LOG.md에 정리해 보존한다.
- 출처: 이번 대화에 첨부된 pasted-text.txt 두 개. `cmp`로 내용이 동일함을 확인하여 한 번만 정리했다.
- 아래 내용은 원문의 요구사항 요약이며 원문 전문이나 새 구현 완료 판정이 아니다. 앞으로 단순화 여부를 판단할 때 이 기준을 사용한다.
- 변경 파일: WORK_LOG.md만 수정. 기존 기록은 보존하고 맨 아래에 추가했다.
- 앞선 요청인 “아직 수정하지 말기”는 사이트 구현에 계속 적용한다. 이번 요청으로 미션 정리 기록만 작성하며 기능 단순화는 아직 승인·실행되지 않았다.

### 1. 미션 목적과 학습 목표

- 외부 라이브러리 없이 순수 HTML/CSS/JavaScript로 반응형 포트폴리오 웹사이트를 완성한다.
- 화면의 화려함보다 **사용자 이벤트 → 상태 변경 → DOM 업데이트/렌더링 → 화면 변화**를 이해하는 것이 우선이다. 다음 React 학습을 위한 DOM·이벤트·상태·비동기 처리의 기초를 익힌다.
- 스스로 설명할 내용: 시맨틱 태그 선택과 구조 설계 이유, Flexbox/Grid 차이와 선택 기준, querySelector와 addEventListener 연결, 화살표 함수·구조분해·map/filter 사용 이유와 방법, fetch/async/await와 로딩·성공·실패 UI, 기능별 이벤트·상태·렌더링 흐름.

### 2. 필수 기본 구성·HTML

- index.html, css/, js/, images/ 역할을 분리하고 외부 CSS와 JavaScript를 올바르게 연결한다. VS Code + Live Server 개발 환경을 구성한다.
- header, nav, main, section, article, footer 등 시맨틱 태그를 사용한다.
- Hero: 인사말과 CTA 버튼. About: 자기소개와 프로필 이미지. Skills: 기술 스택 목록. Projects: GitHub API 카드. Contact: 문의 폼. Footer: 저작권과 소셜 링크.
- 네비게이션에 각 섹션으로 이동하는 앵커 링크를 둔다.
- 모든 이미지에 의미 있는 alt를 작성하고 폼 label의 for와 입력 요소 id를 맞춘다.

### 3. 필수 CSS·반응형

- 외부 css/style.css를 사용한다. :root에 색상·폰트·간격 변수를 정의하고 [data-theme="dark"]에 다크 모드 변수를 별도로 정의한다.
- 네비게이션은 Flexbox로 로고 왼쪽·메뉴 오른쪽에 배치한다. Projects 카드는 Grid의 auto-fit과 minmax로 반응형을 구현한다.
- 모바일 퍼스트로 작성하며 768px(태블릿), 1024px(데스크톱) 브레이크포인트를 사용한다. 모바일에서는 네비게이션을 숨기고 햄버거 버튼을 표시한다.
- 버튼과 카드에 hover 및 transition, 카드에 box-shadow를 적용한다.

### 4. 필수 JavaScript 문법·DOM·이벤트

- JavaScript를 defer로 연결한다. var 대신 const/let, HTML onclick 대신 addEventListener를 사용한다. 인라인 style 속성은 금지한다.
- querySelector/querySelectorAll, textContent/innerHTML, classList.add/remove/toggle을 활용한다.
- click, submit, scroll, input 이벤트를 다루고 event.preventDefault()로 기본 동작을 방지한다.
- 화살표 함수, 템플릿 리터럴을 통한 동적 HTML, 객체/배열 구조분해 할당을 활용한다.
- map으로 GitHub 데이터를 HTML 카드로 변환하고 forEach로 순회한다. filter를 사용한 프로젝트 표시 기능은 선택 사항이다.

### 5. 필수 인터랙션

| 기능 | 원문 요구사항 |
| --- | --- |
| 햄버거 메뉴 | 모바일에서 클릭하면 열리고 다시 클릭하면 닫힘. classList.toggle('active') 활용 |
| 부드러운 스크롤 | 네비게이션 메뉴 클릭 시 해당 섹션으로 부드럽게 이동 |
| 맨 위 버튼 | 스크롤 300px 이상에서 표시, 클릭 시 페이지 맨 위로 이동 |
| 네비게이션 배경 | 스크롤 60px 이상에서 배경색 변경 |
| 다크 모드 | 버튼 클릭으로 테마 전환, localStorage 저장, 새로고침 후 복원 |
| 스크롤 애니메이션 | Intersection Observer 사용, threshold 0.2 이상 권장 |

- 300px·60px 기준값과 Observer 임계값은 자유롭게 변경할 수 있으나 README에 명시한다. 0.2는 고정 필수값이 아니라 권장값이다.

### 6. 필수 문의 폼

- 이름·이메일·메시지 입력 필드를 둔다.
- 필수값과 이메일 형식을 검사하며 빈 필드를 제출할 수 없게 한다.
- 오류 메시지를 해당 입력 필드 근처에 표시한다.
- 제출 시 preventDefault()를 사용하고 검증 성공 메시지를 표시한다.
- 실제 이메일 전송은 필수가 아니다.

### 7. 필수 GitHub API·상태 관리

- 본인 계정의 `https://api.github.com/users/{본인아이디}/repos`를 fetch와 async/await로 호출하고 try/catch로 오류를 처리한다.
- 로딩: 스피너 또는 “로딩 중...” 안내. 성공: 저장소 카드 목록. 오류: “프로젝트를 불러올 수 없습니다” 안내와 재시도 버튼. 빈 결과: “표시할 프로젝트가 없습니다” 안내.
- 원문은 비인증 요청을 시간당 60회로 안내하며 짧은 시간 내 반복 새로고침을 피하도록 한다. 레이트 리밋의 403 응답도 오류 UI로 처리해야 한다.
- **최소 3개 이상의 상태 → 렌더링 흐름**이 명확하게 존재해야 한다. 원문 예시는 테마 전환, API 요청 상태, 폼 입력에 따른 유효성 상태, 선택 과제인 필터 상태다.
- 원문은 하나의 전역 state 객체나 특정 함수 이름을 강제하지 않는다. 단순화하더라도 이벤트·상태·화면 갱신의 연결과 최소 3개 흐름을 보존한다.

### 8. 배포·제출·개발 제약

- GitHub Pages로 배포하여 외부에서 접속 가능한 URL을 제공한다. 배포본에서 반응형, 메뉴·테마·스크롤 등 인터랙션, GitHub API, 폼 검증이 정상 동작해야 한다.
- README에 프로젝트 설명, 사용 기술, 배포 URL, 스크린샷을 포함한다.
- 제출물: GitHub 저장소 URL, GitHub Pages 사이트 URL, 데스크톱·모바일·다크 모드 스크린샷.
- 최신 Chrome에서 정상 동작해야 한다.
- React, Vue, jQuery, Bootstrap, Tailwind CSS 등 외부 라이브러리는 금지한다. 순수 HTML/CSS/JavaScript만 사용하며 아이콘(Font Awesome)과 웹 폰트(Google Fonts)는 허용한다.
- 원문의 화면 도식은 참고 예시이며 정답 디자인이 아니다. 디자인은 자유롭게 구성하되 필수 섹션을 모두 포함한다.

### 9. 선택 과제와 향후 단순화 판단

- 명시된 보너스: 언어별 프로젝트 필터(array.filter), Hero 타이핑 효과, Formspree/EmailJS 실제 이메일 전송, prefers-color-scheme 시스템 다크 모드 감지.
- 기존 구현의 API 5분 캐시, 여러 페이지 조회, 15초 요청 제한, 폼 touched 관리는 원문에 필수로 명시되지 않은 구현 방식이다. 변경 시 동작 범위와 사용성을 검토할 수 있으나 이번 작업에서는 변경하지 않는다.
- 필터 기능은 선택이지만 map/filter의 개념 설명은 학습 목표에 포함되어 있다.
- 단순화하더라도 필수 API 네 가지 화면과 재시도, 테마 저장·복원, 폼 검증, 필수 DOM/문법/이벤트 사용, 최소 3개 상태·렌더링 흐름을 빠뜨리지 않는다.

### 검증·미해결·다음 작업

- 수행 명령: AGENTS.md 및 기존 WORK_LOG.md 확인, 첨부 두 개 읽기, cmp로 동일 내용 확인, git status --short로 시작 시 변경 없음 확인.
- 문서 변경 검증: git diff --check 및 WORK_LOG.md 변경 범위 확인. 기능 코드는 변경하지 않아 브라우저 테스트는 실행하지 않는다.
- 미해결: 이번 작업은 요구사항 기록이며 현재 구현의 충족 여부를 새로 테스트한 것은 아니다.
- 다음 작업: 요청 시 이 원문 요약과 현재 코드를 대조하여 필수 기능을 유지하는 단순화안을 구체화한다. 사이트 수정은 후속 요청에 따라 진행한다.
- Git commit/push: 수행하지 않음. 로컬 WORK_LOG.md에 정리했다.


## 2026-09-10 15:04 KST — 디자인과 기존 기능을 보존한 코드 정리

- 요청: 현재 사이트 디자인과 선택 기능을 보존하면서 코드를 더 이해하기 쉽게 수정한다. 앞선 구현 수정 보류는 이번 요청으로 해제됐다.
- 변경 파일: js/main.js, README.md, MISSION_GUIDE.md, PRESENTATION_GUIDE.md, WORK_LOG.md. 앞서 추가한 미션 요약과 기존 작업 기록을 보존했다.
- 핵심 작업: 반복되는 메뉴 상태 변경을 setMenuOpen으로 통합했다. 카드 생성은 createProjectCard, API 조회는 fetchAllRepos, HTTP 검사는 checkRepoResponse, 캐시 읽기는 readProjectCache로 분리하여 loadProjects에서 로딩→성공/오류→렌더링 흐름을 읽기 쉽게 했다. 폼 렌더링은 이미 선택한 입력 요소를 재사용한다. 가이드의 함수 위치와 설명을 맞췄다.
- 보존 범위: HTML/CSS/이미지 변경 없음. 언어 필터, 시스템 테마, 테마 저장, 캐시, 페이지네이션, 15초 제한, 폼 입력/blur/submit 검증, 키보드 포커스, 오류/빈 결과/재시도, 스크롤 동작을 유지했다. 기능 삭제나 새로운 프레임워크 도입 없음.
- 미션 대조: 기존 시맨틱 구조·반응형·필수 문법과 이벤트·배열 메서드를 유지했다. 테마, 메뉴, API, 폼, 필터의 상태→렌더링 흐름을 보존했다. 요구사항 충족 여부와 별도로 본인의 코드 설명 연습은 필요하다.
- 검증: 임시 가상환경에 Playwright 1.60.0 설치 후 로컬 5511 서버에서 `/tmp/b1-1-review-venv/bin/python tests/review.py` 실행. Chrome 146.0.7680.165에서 27개 항목 모두 통과, 테스트 시나리오에서 JavaScript 오류 없음. API는 모의 응답을 사용했고 실제 호출 제한을 소진하지 않았다.
- 디자인 검증: 임시 `/tmp/b1-1-visual-check.py`에서 이전 HEAD의 JS와 수정된 JS를 동일한 페이지에 각각 적용했다. 동일 모의 데이터·외부 웹 폰트 차단 조건에서 데스크톱 1440px, 모바일 375px, 다크 모드 1440px 전체 스크린샷이 바이트 단위로 일치했다. 기존 제출용 스크린샷은 덮어쓰지 않았다.
- 환경 처리: 샌드박스의 네트워크·로컬 서버 바인딩·Chrome 실행 제한으로 초기 시도가 실패하여 승인된 외부 실행으로 설치와 테스트를 완료했다.
- 문서/변경 검증: git diff --check 통과. 기존 tests/review.py는 변경하지 않았다.
- 미해결/다음 작업: 로컬 수정과 검증 완료. 실제 API 및 공개 Pages 재검증·새 코드 배포는 이번 범위에서 실행하지 않았다. 요청 시 커밋·업로드하고 공개본을 확인한다.
- Git commit/push: 수행하지 않음.


## 2026-09-10 15:10 KST — 비전공자용 발표 가이드 확장

- 요청: 앞서 제안한 구성대로 미션 요구사항을 빠짐없이 설명할 수 있도록 발표 가이드를 수정한다.
- 변경 파일: PRESENTATION_GUIDE.md, WORK_LOG.md. 기존 미커밋 코드·문서 수정은 보존했다.
- 핵심 작업: 기존 5~7분 대본과 모의 API 시연·복원 코드를 유지하고, 용어·파일 구조·HTML·CSS·DOM·문법·API·폼의 쉬운 설명과 추가 대본, 코드 검색 위치, 시연 방법, 예상 질문을 보완했다. 최소 세 상태→렌더링 흐름, 전체 시연 순서, 미션 원문의 학습 목표·필수·보너스·제약·제출물을 대응표로 정리했다.
- 정확성 보완: 60px/300px은 README 명시 시 변경 가능하고 Observer 0.2 이상은 권장임을 표시했다. 설명 연습 체크와 구현 판정을 구분했다. 9월 7일 기존 배포와 9월 10일 로컬 코드 정리·27개 모의 API 검증 결과를 구분하고 현재 수정본이 미배포임을 명시했다.
- 검증: 현재 함수명, HTML 폼 속성, CSS 기준값, VS Code 설정과 문서를 대조했다. 로컬 문서 링크 존재·코드 블록 짝·필수 주제 검색 검사 및 git diff --check 통과. 문서만 수정하여 브라우저 테스트는 반복하지 않았다.
- 미해결/다음 작업: 발표자가 체크표로 자기 설명을 연습한다. 향후 배포 시 가이드의 배포·검증 상태를 실제 결과에 맞춰 갱신한다.
- Git commit/push: 수행하지 않음.


## 2026-09-10 15:13 KST — 파일별 역할 안내와 검사 파일 설명 정리

- 요청: review 파일의 존재 이유, 읽기 쉬운 정리, 각 파일의 목적과 기능 설명.
- 변경 파일: FILE_GUIDE.md 추가, tests/review.py·README.md·WORK_LOG.md 수정. 기존 미커밋 변경은 보존했다.
- 핵심 작업: 모든 프로젝트 파일을 화면 코드·문서·설정·이미지·검사 도구별로 설명하고 목적별로 열 파일을 안내했다. review.py에 한국어 실행 설명과 01~16 기능별 구분 주석을 추가했다. README에 파일 안내 링크를 추가했다.
- 주요 설명: Python/Playwright는 사이트에 연결되지 않은 개발용 검사 도구이며 미션의 필수 구현 언어가 아니다. 일반 검사와 --live의 실제 API·공개본 검사 및 스크린샷 덮어쓰기 차이, 서버 5500/5511 포트 차이를 명시했다.
- 검증: Python AST를 수정 전후 비교해 모듈 설명문을 제외한 실행 코드가 동일함을 확인했다. FILE_GUIDE 로컬 링크·코드 블록 검사와 git diff --check 통과. 주석·문서만 변경하여 브라우저 검사는 반복하지 않았다.
- 미해결/다음 작업: 안내 문서의 HTML→CSS→JS 순서로 학습하고, 실제 동작 수정 시 기존 자동 검사를 활용한다.
- Git commit/push: 수행하지 않음.


## 2026-09-10 15:15 KST — 푸시 전 검토

- 요청: GitHub 푸시 전에 수정할 사항이 있는지 검토한다.
- 변경 파일: WORK_LOG.md에 검토 결과만 추가. 사이트·설명 문서는 이번 검토에서 수정하지 않았다.
- 확인 사항: MISSION_GUIDE.md의 git add 예시에 새 FILE_GUIDE.md가 빠져 있어 그대로 실행하면 README의 새 링크 대상이 업로드되지 않는다. README 상단에는 과거 배포 완료가 강조되고 현재 미배포 안내는 맨 아래에 있어 최신 상태를 상단에 요약하면 더 명확하다.
- 검증: git diff --check 통과, Markdown 로컬 파일 링크 누락 없음, review.py는 HEAD 대비 모듈 설명문·주석 외 실행 구문 동일. HTML/CSS/이미지 변경 없음. 앞선 로컬 Chrome 27개 통과 이후 기능 코드 변경이 없어 브라우저 테스트는 반복하지 않았다.
- 미해결/다음 작업: 푸시 시 FILE_GUIDE.md를 반드시 포함하고 배포 후 공개본을 검증한다. 문서 개선 두 항목은 제안 상태다. 원격 최신 커밋과 인증은 이번 로컬 검토에서 확인하지 않았다.
- Git commit/push: 수행하지 않음.


## 2026-09-10 15:17 KST — README 미션 안내 내용 제거

- 요청: README 안의 미션 가이드 내용을 뺀다.
- 변경 파일: README.md, WORK_LOG.md.
- 핵심 작업: 미션 가이드 링크·파일 구조 항목, 요구사항 체크리스트·보너스 과제, 학습용 개념과 코드 설명을 README에서 제거했다. 프로젝트 소개·주요 기능·사용 기술·실행·설정·검증·스크린샷·배포 정보를 유지했다. 스크롤과 Observer 설정 수치도 유지했다. 최신 로컬 수정·미배포 상태를 상단에 명시했다.
- 보존: MISSION_GUIDE.md 등 별도 안내 파일과 사이트 코드는 변경하지 않았다. 기존 미커밋 변경을 보존했다.
- 검증: README 미션/MISSION_GUIDE 참조 제거 확인, 로컬 링크 존재·코드 블록 검사, git diff --check 통과. 문서 수정으로 브라우저 테스트는 생략했다.
- 미해결/다음 작업: 요청 시 변경 파일을 커밋·푸시하고 배포 상태를 갱신한다. 앞선 검토의 MISSION_GUIDE git add 예시 보완은 이번 범위 밖으로 남았다.
- Git commit/push: 수행하지 않음.


## 2026-09-10 15:18 KST — README 파일 안내 링크 제거

- 요청: README에서 파일별 역할 안내와 단계별 구현 가이드도 뺀다.
- 변경 파일: README.md, WORK_LOG.md.
- 핵심 작업: 파일별 역할 안내 링크와 파일 구조 항목을 제거했다. 단계별 구현 가이드 안내는 앞선 수정으로 이미 제거되어 있음을 확인했다. 별도 FILE_GUIDE.md와 MISSION_GUIDE.md 파일은 보존했다.
- 검증: README에서 두 파일 참조·안내 문구 부재와 원본 가이드 파일 존재 확인, git diff --check 통과. 문서 수정으로 브라우저 테스트는 생략했다.
- 미해결/다음 작업: 로컬 수정 완료. 원격 반영은 후속 요청 시 진행한다.
- Git commit/push: 수행하지 않음.


## 2026-09-10 15:30 KST — 누적 변경 GitHub 반영

- 요청: 지금까지 변경한 B1-1과 B2-1 파일을 모두 푸시한다.
- 범위: 기능을 유지한 코드 정리, README 정리, 파일·미션·발표 가이드, 테스트 설명 및 작업 기록의 누적 변경 전체.
- 검증: git fetch 후 HEAD와 origin/main 차이 0/0, git diff --check 통과. 앞선 B1-1 Chrome 27개 및 B2-1 unittest 21개 통과 이후 기능 코드 추가 변경 없음.
- 반영 방법: 터미널 git push --dry-run에서 쓰기 인증 부재 확인. 인증된 GitHub 앱으로 커밋을 만들고 force 없이 main에 반영한다. 결과와 실제 커밋은 후속 기록으로 남긴다.
- 커밋 메시지: refactor: simplify code and improve beginner documentation
- 현재 단계: 업로드 시작 전 기록. 원격 반영·로컬 동기화 결과 확인이 남아 있다.

## 2026-09-16 14:04 KST — 미션 기준 추가 단순화 가능성 검토

- 요청: B1-1을 미션에 맞게 더 간단하게 만들 수 있는 부분만 검토하고 구현에는 반영하지 않는다.
- 변경 파일: 저장소 기록 규칙에 따라 WORK_LOG.md에 이번 검토만 추가. 사이트 코드·기타 문서는 수정하지 않았다.
- 핵심 검토: 9월 10일 미션 원문 요약과 현재 HTML/CSS/JS를 대조했다. 기능 유지 후보는 폼 submitted/touched 상태 통합(제출 시 모든 필드를 touched로 설정), renderForm의 고정 DOM 조회 사전 선택, 1024px about-grid의 중복 열 정의 제거다. 기능 축소 후보는 API 캐시, 여러 페이지 조회, 시스템 테마 감지다. 캐시 제거 시 요청 증가, 단일 조회 시 100개 초과 저장소 누락, 시스템 감지 제거 시 자동 테마 동기화 상실을 설명해야 한다.
- 판단: 기존 함수 분리는 이미 읽기 쉽게 정리되어 있어 합치는 것을 권하지 않는다. 필수 API 네 가지 화면·재시도·403 오류 처리, 테마 저장·복원, input/submit 폼 검증과 최소 세 상태→화면 흐름은 보존해야 한다. 선택 언어 필터는 map/filter 학습 설명에 유용하여 유지 권장. 외부 데이터 이스케이프·URL 검사·접근성 처리는 단순히 줄 수를 줄이기 위해 제거하지 않는다.
- 실행 명령/결과: cat/sed/nl/rg로 기록·소스·가이드 확인, git status --short에서 시작 시 변경 없음, git diff --check 통과. 구현 변경 없는 정적 검토로 브라우저 테스트는 실행하지 않았다.
- 미해결/다음 작업: 제안은 미반영 상태이며 실제 수정 요청 시 선택 범위에 맞춰 구현·관련 테스트·문서를 함께 검증한다.
- Git commit/push: 수행하지 않음.

## 2026-09-16 14:10 KST — 화면과 기존 동작을 보존한 중복 정리 반영

- 요청: 최종 페이지의 디자인·문구·배치·동작을 유지하면서 앞선 단순화 제안을 실제 코드에 반영한다.
- 변경 파일: js/main.js, css/style.css, MISSION_GUIDE.md, PRESENTATION_GUIDE.md, WORK_LOG.md. 기존 검토 기록은 보존했다.
- 핵심 작업: 폼 submitted를 제거하고 제출 시 모든 필드의 touched를 true로 설정하여 기존 검사 시점을 유지했다. 오류 메시지·글자 수·성공 안내 DOM을 처음에 선택해 재사용한다. 1024px about-grid의 열 비율 중복 선언을 제거하고 768px 선언을 그대로 적용한다. 두 설명 문서의 폼 상태 설명을 맞췄다.
- 보존: HTML·이미지·화면 문구 변경 없음. 캐시·페이지네이션·15초 제한·시스템 테마·언어 필터·접근성·오류 처리 유지. 배포 설정 변경 없음.
- 검증 환경: 수정 전 JS/CSS를 /tmp/b1-preserve.x9D51l에 보관하고 임시 가상환경에 Playwright 1.60.0 및 비교 확인용 Pillow 설치. localhost:5511 서버와 Chrome 146.0.7680.165 사용. 프로젝트 의존성 및 기존 tests/review.py 변경 없음.
- 기능 검사: `/tmp/b1-preserve.x9D51l/venv/bin/python tests/review.py`에서 27개 모두 통과. 반응형·메뉴·테마·폼·필터·API 네 가지 화면·HTTP/네트워크 오류·재시도·캐시·페이지네이션·보안 처리·타임아웃·Observer 포함. 실제 GitHub 요청 대신 모의 데이터 사용.
- 수정 전후 비교: 임시 compare.py로 320/375/767/768/1024/1440px × 라이트/다크 12개 초기 화면 및 375px 폼의 입력/blur/오류 제출/수정/성공/성공 후 수정/재제출을 확인. 총 30개 상태에서 DOM·입력값·포커스·About 열 너비 동일, 총 18개 전체 화면 PNG 바이트 일치. 비교 시 동일 날짜·모의 데이터·시스템 폰트(CDN 차단)·동작 줄이기 설정을 사용했다.
- 비교 과정: 초기 캡처에서 스크롤 처리 시점과 GPU 렌더링에 따른 차이가 발생했다. 캡처 스크롤 위치·대기 조건을 맞추고 두 버전 모두 GPU 및 threaded scrolling을 비활성화한 동일 조건에서 전체 비교를 다시 실행하여 통과했다. 해당 조정은 임시 검사 스크립트에만 적용했다.
- 기타 검증: git diff --check 통과. 제출용 스크린샷은 변경하지 않았다. 임시 검사 서버 종료.
- 미해결/다음 작업: 로컬 반영과 검증 완료. 모든 기기·입력 조합까지 검증한 것은 아니며, 실제 API/공개 Pages 재검증 및 업로드·배포는 수행하지 않았다. 추후 배포 요청 시 이번 변경을 포함해 확인한다.
- Git commit/push: 수행하지 않음.

## 2026-09-16 14:14 KST — 새로 제공된 미션 전문 기준 최종 검토

- 요청: 첨부한 미션 전문을 기준으로 최종 검토한다. 기존 화면·동작 유지 조건을 보존하고 이번에는 검토만 수행한다.
- 원문 출처: /Users/dooolll5969/.codex/attachments/3ec9eada-046e-44eb-a4f3-5139a913c010/pasted-text.txt 전체를 읽었다. 소개·결과물·학습 목표·기능 요구·보너스·개발 환경·제약·예시를 현재 파일과 대조했다. 앞서 기록한 미션 요약에서 새 필수 요구 누락은 발견하지 못했다.
- 변경 파일: WORK_LOG.md에 이번 결과만 추가. 기존 미커밋 JS/CSS/설명 문서와 이전 기록 보존. 소스·README·제출용 이미지 수정 없음.
- HTML/구성: index.html/css/js/images 역할 분리, 외부 파일 연결·defer, 시맨틱 태그, Hero 인사말·CTA/자기소개·프로필/기술 목록/API 카드/문의 폼/저작권·GitHub 링크, 모든 구역 앵커·alt·label 확인.
- CSS: 색상·폰트·간격 변수, 다크 테마 변수, nav Flex 및 Projects auto-fit/minmax Grid, 모바일 퍼스트와 768/1024px 분기, 모바일 메뉴, 버튼·카드 hover/transition/그림자 확인.
- JS: const/let·화살표 함수·템플릿 리터럴·객체 구조분해·map/filter/forEach, DOM 선택·내용·classList 조작, click/submit/scroll/input·preventDefault 확인. var·HTML 이벤트 속성·인라인 스타일 없음. 외부 실행 라이브러리 없음. Pretendard는 허용 범주인 웹 폰트이며 Python/Playwright는 사이트에 로드되지 않는 검사 도구다.
- 기능/상태: 메뉴·부드러운 이동·60px 헤더·300px 맨 위 버튼·테마 저장 복원·Observer 0.2, 문의 폼 필수값/이메일/근처 오류/성공 안내, fetch/async/await/try-catch·API 로딩/성공/오류/빈 결과/403·재시도 확인. 테마·메뉴·API·폼·필터의 다섯 상태→렌더링 흐름을 확인했다.
- 보너스: 언어 필터·시스템 테마 구현. 타이핑·실제 메일 전송은 미구현이나 선택 사항이므로 필수 누락이 아니다.
- 제출 자료: README에 설명·기술·저장소/Pages URL·세 스크린샷 및 60/300/0.2 설정 명시 확인. 기존 스크린샷 PNG 검증 및 육안 확인(1440x3943, 375x7077, 1440x3943). README 로컬 링크 정상.
- 동작 검증: tests/review.py를 /tmp/b1-final-review/tests/review.py에 그대로 복사하고 `/tmp/b1-preserve.x9D51l/venv/bin/python /tmp/b1-final-review/tests/review.py --live` 실행, Chrome 146.0.7680.165에서 29개 모두 통과. --live의 캡처는 /tmp/b1-final-review/images/screenshots에만 저장했다. 모의 API 27개 검사와 실제 로컬/공개 사이트 API·테마·폼·메뉴·스크롤·반응형 점검 통과. 실제 저장소 양쪽 각 8개, 검사 중 JS 오류 없음.
- 공개본 확인: 웹 열기 도구 실패 후 Python urllib와 실제 Chrome으로 HTTP 200 확인. 공개 index.html은 로컬과 동일, CSS/JS는 이번 9월 16일 단순화 전 보관본과 동일하다. git ls-remote로 원격 main ea6526e562a1ee7e9b9e22bb29582496edc39452 확인. 현재 로컬 최신 변경은 아직 미배포.
- 발견 1(개발 환경): `code --list-extensions` 결과 현재 VS Code 환경에 ritwickdey.LiveServer 없음. .vscode 추천·5500 포트 설정은 있으나 설치 확인이 필요하다. 미션은 VS Code + Live Server를 명시한다. 검토 요청이므로 설치하지 않았다.
- 발견 2(배포): 공개본 주요 기능은 정상이나 최신 로컬 정리와 불일치. 최신 제출본으로 맞추려면 커밋·업로드·배포 확인이 남는다.
- 발견 3(문서): README.md:10의 9월 10일 변경이 로컬 전용이라는 설명은 이미 반영된 공개 코드와 다르며, 현재 미배포 변경은 9월 16일 작업이다. README.md:44의 현 환경 Live Server 설치 확인 설명도 현 목록과 맞지 않는다. 검토만 요청되어 수정하지 않았다.
- 한계: 설치된 Chrome 146에서 통과했으나 현재 최신 Chrome 버전인지 확인하거나 새 버전으로 검사하지 않았다. 학습 목표의 '스스로 설명할 수 있음'은 코드/자동 검사로 판정할 수 없어 별도 발표 연습이 필요하다. 모든 기기·입력에 대한 무오류 보장은 아니다.
- 명령/검증: cat/sed/rg 및 Git 읽기 명령, code --list-extensions, urllib 공개 파일 비교, 임시 복사본 --live 실행, PNG/README 링크/Python AST/필수 구문·금지 속성 정적 검사, git diff --check 통과. 정적 검사 스니펫의 괄호 오타를 고쳐 재실행 후 통과했다. 검사 서버 종료.
- 미해결/다음 작업: 위 개발 환경·배포·README 항목을 제출 전 맞추고, 최신 Chrome 및 본인의 여섯 학습 목표 설명을 최종 확인한다. 사이트 필수 구현의 기능 결함은 이번 검토 범위에서 발견하지 못했다.
- Git commit/push: 수행하지 않음.

## 2026-09-16 — 제출 준비 정리 및 현재 코드 기준 README 재작성

- 요청: 최종 검토에서 남은 개발 환경·배포·문서 사항을 정리하고 README를 현재 코드 기준으로 새로 작성한다.
- 변경 파일: README.md 전면 재작성, MISSION_GUIDE.md/PRESENTATION_GUIDE.md의 오래된 배포 안내 및 업로드 예시 수정, WORK_LOG.md 추가. 앞서 검증한 js/main.js/css/style.css 정리도 이번 업로드에 포함한다.
- 핵심 작업: Live Server 5.7.10 설치 후 code --list-extensions --show-versions로 확인. README를 소개·기능·기술·실행·설정·API·검사·스크린샷·배포 중심으로 다시 작성했다. 과거 요청대로 미션 체크리스트·학습 가이드 링크는 추가하지 않았다. 9월 7일 기존 스크린샷은 촬영일을 정확히 명시하고 보존했다.
- 검증: 직전 최종 코드의 Chrome 29개 검사 통과 후 사이트 실행 코드 변경 없음. README의 설정값·명령·링크를 현재 파일과 대조하고 git diff --check 확인. 라이브러리나 사이트 디자인 변경 없음.
- 배포 준비: git fetch origin 후 HEAD와 origin/main 차이 0/0. Git 터미널 dry-run은 쓰기 인증 부재로 실패하여 연결된 GitHub 앱으로 파일 트리·커밋 생성 후 force 없이 main을 갱신한다.
- 커밋 메시지: `docs: rewrite README and publish verified portfolio cleanup`.
- 미해결/다음 작업: 업로드·Pages 완료와 공개 파일 일치 및 주요 기능을 확인하고 결과를 추가 기록한다. 현재 단계는 배포 전이며 성공을 선기록하지 않는다.

## 2026-09-16 14:19 KST — README 재작성·최신 코드 업로드·배포 완료

- 요청: 최종 검토의 정리 사항 해결 및 현재 코드 기준 README 재작성.
- 결과: Live Server 5.7.10 설치 확인. README 재작성과 설명 문서 정리, 앞선 CSS/JS 중복 제거를 원격 main에 반영했다. 사이트 디자인·콘텐츠·기능 변경 없이 정리했다.
- 업로드 커밋: `612a8fd20907785d1340027dd0d7fe374fa5759d`, 메시지 `docs: rewrite README and publish verified portfolio cleanup`. 터미널 push 대신 연결된 GitHub 앱으로 force 없이 main 업로드 완료.
- 로컬 동기화: fetch 후 작업 파일과 origin/main 차이가 없고 스테이징 트리 ed5d672d228fa4b044dce56a46362a7adbc92ba6가 원격 트리와 동일함을 확인한 뒤 soft reset으로 로컬 main을 원격 커밋에 맞췄다. 작업 파일 삭제나 강제 push 없음.
- Pages: `pages build and deployment` 실행 35058991744 completed/success. https://github.com/dooolll00/B1-1/actions/runs/35058991744
- 공개 검증: /tmp/b1-final-review/deploy_check.py 실행, 공개 index.html/css/style.css/js/main.js/README.md HTTP 200 및 로컬과 바이트 일치. 실제 GitHub 저장소 8개, 테마 저장·새로고침 복원, 폼 오류·성공·성공 후 수정, 모바일 메뉴·Footer 포커스·맨 위 이동, 320/375/767/768/1024/1440px 가로 넘침 없음, 이미지 로딩 통과. 검사 중 JS 오류 없음.
- 후속 문서: README의 검사 결과 문단에 최신 배포 후 확인 사실을 추가하고 이 기록과 함께 `docs: record verified portfolio deployment` 메시지로 업로드한다. 기능 코드는 재변경하지 않는다.
- 검증 명령: code 설치/목록 확인, git fetch/rev-list/diff/write-tree, README 링크·코드 블록 검사, git diff --check, GitHub API Actions 조회, urllib 파일 비교 및 Chrome 배포 검사. 전체 29개 검사는 직전 최종 검토 통과 결과를 유지하고 신규 배포 대상만 다시 검사했다.
- 미해결/다음 작업: 요청한 개발 환경·문서·최신 배포 정리 완료. 본인의 코드 설명 연습은 별도로 필요하며, Chrome 최신 버전 여부는 이번 범위에서 변경·검증하지 않았다. 후속 기능 수정은 요청 시 진행한다.
