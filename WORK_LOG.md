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
