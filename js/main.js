"use strict";

/**
 * 읽는 순서: 01 공통 상태 → 02 테마 → 03 메뉴 → 04 스크롤
 *            → 05 프로젝트 API → 06 문의 폼 → 07 초기 화면.
 * [필수]는 미션 핵심, [추가]는 편의 기능 또는 예외 처리입니다.
 * 이벤트 함수는 state를 바꾸고, render 함수는 그 값을 DOM에 반영합니다.
 */

// 01. 공통 설정, 저장소 도우미, 상태와 DOM 선택
const GITHUB_USERNAME = "dooolll00";
const THEME_KEY = "portfolio-theme";
// [추가] API 캐시: 새로고침할 때 같은 요청을 반복하지 않도록 5분간 보관합니다.
const CACHE_KEY = `portfolio-repos-${GITHUB_USERNAME}`;
const CACHE_TTL = 5 * 60 * 1000;
const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const readStorage = (key) => {
  try {
    return localStorage.getItem(key);
  } catch {
    return null;
  }
};
const writeStorage = (key, value) => {
  try {
    localStorage.setItem(key, value);
  } catch {
    /* 저장소가 차단돼도 현재 페이지는 동작한다. */
  }
};
const savedTheme = readStorage(THEME_KEY);
const hasSavedTheme = ["light", "dark"].includes(savedTheme);
let initialTheme = "light";
if (systemTheme.matches) {
  initialTheme = "dark";
}
if (hasSavedTheme) {
  initialTheme = savedTheme;
}

// 화면이 기억해야 할 값을 한곳에 모읍니다. DOM 자체와 상태는 별개입니다.
const state = {
  theme: initialTheme,
  explicitTheme: hasSavedTheme,
  menuOpen: false,
  projects: { status: "idle", repos: [], filter: "all", error: "" },
  form: {
    values: { name: "", email: "", message: "" },
    errors: {},
    touched: {},
    submitted: false,
    success: false,
  },
};
const themeButton = document.querySelector("#theme-toggle");
const menuButton = document.querySelector("#menu-toggle");
const menu = document.querySelector("#nav-menu");
const header = document.querySelector(".site-header");
const topButton = document.querySelector("#scroll-top");
const projectList = document.querySelector("#project-list");
const filters = document.querySelector("#project-filters");
const summary = document.querySelector("#project-summary");
const form = document.querySelector("#contact-form");
const fields = [...form.querySelectorAll("input, textarea")];

// 02. [필수] 다크 모드: 클릭 → state.theme → renderTheme → CSS 변수 변경
const renderTheme = () => {
  const dark = state.theme === "dark";
  document.documentElement.dataset.theme = state.theme;
  themeButton.textContent = dark ? "☀" : "☾";
  themeButton.setAttribute("aria-pressed", String(dark));
  themeButton.setAttribute("aria-label", dark ? "라이트 모드 켜기" : "다크 모드 켜기");
};
themeButton.addEventListener("click", () => {
  state.theme = state.theme === "dark" ? "light" : "dark";
  state.explicitTheme = true;
  writeStorage(THEME_KEY, state.theme);
  renderTheme();
});
// [추가] 사용자가 직접 고르기 전에는 운영체제의 테마를 따릅니다.
systemTheme.addEventListener("change", ({ matches }) => {
  if (!state.explicitTheme) {
    state.theme = matches ? "dark" : "light";
    renderTheme();
  }
});

// 03. [필수] 모바일 메뉴: 클릭 → state.menuOpen → active 클래스와 접근성 속성
const renderMenu = () => {
  menu.classList.toggle("active", state.menuOpen);
  menuButton.classList.toggle("active", state.menuOpen);
  menuButton.setAttribute("aria-expanded", String(state.menuOpen));
  menuButton.setAttribute("aria-label", state.menuOpen ? "메뉴 닫기" : "메뉴 열기");
};
menuButton.addEventListener("click", () => {
  state.menuOpen = !state.menuOpen;
  renderMenu();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && state.menuOpen) {
    state.menuOpen = false;
    renderMenu();
    menuButton.focus();
  }
});
document.addEventListener("click", (event) => {
  if (state.menuOpen && !event.target.closest(".nav")) {
    state.menuOpen = false;
    renderMenu();
  }
});
window.matchMedia("(min-width: 768px)").addEventListener("change", () => {
  state.menuOpen = false;
  renderMenu();
});
// 04. [필수] 앵커 이동, 스크롤에 따른 헤더와 맨 위 버튼, 등장 애니메이션
const scrollBehavior = () => (reducedMotion.matches ? "auto" : "smooth");
document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (event) => {
    const target = document.querySelector(link.getAttribute("href"));
    if (!target) {
      return;
    }
    event.preventDefault();
    state.menuOpen = false;
    renderMenu();
    target.scrollIntoView({ behavior: scrollBehavior(), block: "start" });
    if (!target.hasAttribute("tabindex")) {
      target.setAttribute("tabindex", "-1");
      target.addEventListener("blur", () => target.removeAttribute("tabindex"), {
        once: true,
      });
    }
    target.focus({ preventScroll: true });
    history.replaceState(null, "", link.getAttribute("href"));
  });
});
const renderScroll = () => {
  header.classList.toggle("scrolled", window.scrollY >= 60);
  topButton.hidden = window.scrollY < 300;
};
window.addEventListener("scroll", renderScroll, { passive: true });
topButton.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: scrollBehavior() });
  document.querySelector(".logo").focus({ preventScroll: true });
});
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(({ isIntersecting, intersectionRatio, target }) => {
        if (isIntersecting && intersectionRatio >= 0.2) {
          target.classList.remove("is-pending");
          target.classList.add("is-visible");
          observer.unobserve(target);
        }
      });
    },
    { threshold: 0.2 },
  );
  document.querySelectorAll(".reveal").forEach((element) => {
    if (!reducedMotion.matches) {
      element.classList.add("is-pending");
      observer.observe(element);
    }
  });
}

// 05. [필수] 프로젝트: 요청 시작 → loading → 성공/실패 → renderProjects
// 외부 문자열을 innerHTML로 삽입하기 전에 이스케이프해 코드 실행을 막습니다.
const escapeHTML = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (char) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[char],
  );
const safeRepoURL = (value) => {
  try {
    const url = new URL(value);
    return url.protocol === "https:" && url.hostname === "github.com"
      ? url.href
      : `https://github.com/${GITHUB_USERNAME}`;
  } catch {
    return `https://github.com/${GITHUB_USERNAME}`;
  }
};
// [추가] 저장소의 언어 목록으로 필터 버튼을 만듭니다.
const renderFilters = () => {
  const languages = [
    ...new Set(state.projects.repos.map(({ language }) => language || "기타")),
  ].sort();
  filters.innerHTML = ["all", ...languages]
    .map(
      (language) => /* HTML */ `
        <button
          type="button"
          class="filter-button${state.projects.filter === language ? " active" : ""}"
          data-filter="${escapeHTML(language)}"
          aria-pressed="${state.projects.filter === language}"
        >
          ${language === "all" ? "전체" : escapeHTML(language)}
        </button>
      `,
    )
    .join("");
};
const renderProjects = () => {
  const { status, repos, filter, error } = state.projects;
  projectList.setAttribute("aria-busy", String(status === "loading"));
  if (status === "loading") {
    filters.innerHTML = "";
    summary.textContent = "프로젝트를 불러오는 중입니다.";
    projectList.innerHTML = /* HTML */ `
      <div class="state-panel">
        <span
          class="spinner"
          aria-hidden="true"
        ></span>
        프로젝트를 불러오는 중...
      </div>
    `;
    return;
  }
  if (status === "error") {
    summary.textContent = "프로젝트를 불러올 수 없습니다.";
    projectList.innerHTML = /* HTML */ `
      <div class="state-panel">
        <h3>프로젝트를 불러올 수 없습니다.</h3>
        <p>${escapeHTML(error)}</p>
        <button
          class="button secondary"
          id="retry-projects"
          type="button"
        >
          다시 시도 ↻
        </button>
      </div>
    `;
    return;
  }
  // [추가] 전체 선택이면 그대로, 언어 선택이면 일치하는 저장소만 남깁니다.
  const visible = repos.filter(
    ({ language }) => filter === "all" || (language || "기타") === filter,
  );
  summary.textContent = `${visible.length}개의 프로젝트가 표시됩니다.`;
  // 빈 결과는 성공 응답에서 파생됩니다. 별도의 상태값 없이 개수로 판단합니다.
  if (!visible.length) {
    projectList.innerHTML = /* HTML */ `
      <div class="state-panel">
        <h3>표시할 프로젝트가 없습니다.</h3>
        <p>공개 저장소가 추가되면 이곳에서 만날 수 있습니다.</p>
      </div>
    `;
    return;
  }
  // map은 저장소 객체를 HTML 문자열로 변환하고, join은 하나의 문자열로 합칩니다.
  projectList.innerHTML = visible
    .map(
      (
        {
          name,
          description,
          language,
          stargazers_count,
          forks_count,
          html_url,
          updated_at,
        },
        index,
      ) => {
        const date = new Date(updated_at);
        const updated = Number.isNaN(date.getTime())
          ? ""
          : date.toLocaleDateString("ko-KR", {
              year: "numeric",
              month: "short",
              day: "numeric",
            });
        return /* HTML */ `
          <article class="project-card">
            <div class="project-top">
              <span
                class="repo-icon"
                aria-hidden="true"
              >
                ⌘
              </span>
              <span class="project-number">
                PROJECT / ${String(index + 1).padStart(2, "0")}
              </span>
            </div>
            <h3>
              <a
                href="${escapeHTML(safeRepoURL(html_url))}"
                target="_blank"
                rel="noopener noreferrer"
              >
                ${escapeHTML(name)} ↗
              </a>
            </h3>
            <p>
              ${escapeHTML(description || "코드를 통해 배움을 기록하는 프로젝트입니다. GitHub에서 자세한 내용을 확인해 보세요.")}
            </p>
            <div class="project-meta">
              <span class="language">● ${escapeHTML(language || "기타")}</span>
              <span aria-label="별 ${Number(stargazers_count) || 0}개">
                ☆ ${Number(stargazers_count) || 0}
              </span>
              <span aria-label="포크 ${Number(forks_count) || 0}개">
                ⑂ ${Number(forks_count) || 0}
              </span>
            </div>
            <span class="project-date">${escapeHTML(updated)} 업데이트</span>
          </article>
        `;
      },
    )
    .join("");
};
// [필수] fetch + async/await + try/catch. 캐시와 시간 제한은 [추가] 처리입니다.
const loadProjects = async (force = false) => {
  if (state.projects.status === "loading") {
    return;
  }
  state.projects.status = "loading";
  state.projects.error = "";
  renderProjects();
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 15000);
  try {
    let cached = null;
    try {
      cached = JSON.parse(readStorage(CACHE_KEY));
    } catch {
      /* 손상된 캐시는 무시한다. */
    }
    const validCache =
      !force &&
      cached &&
      Array.isArray(cached.repos) &&
      Date.now() - cached.time >= 0 &&
      Date.now() - cached.time < CACHE_TTL;
    let repos = validCache ? cached.repos : [];
    if (!validCache) {
      // 100개를 넘는 계정도 전체 공개 저장소를 불러온다.
      let page = 1;
      let hasMore = true;
      while (hasMore) {
        const response = await fetch(
          `https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=updated&per_page=100&page=${page}`,
          {
            signal: controller.signal,
            headers: { Accept: "application/vnd.github+json" },
          },
        );
        if (!response.ok) {
          if (response.status === 403 || response.status === 429) {
            throw new Error(
              "GitHub 요청 한도에 도달했거나 접근이 제한되었습니다. 잠시 후 다시 시도해 주세요.",
            );
          }
          if (response.status === 404) {
            throw new Error("GitHub 계정을 찾을 수 없습니다. 계정 설정을 확인해 주세요.");
          }
          throw new Error(
            `GitHub 서버 응답 오류 (${response.status}). 잠시 후 다시 시도해 주세요.`,
          );
        }
        const data = await response.json();
        if (!Array.isArray(data)) {
          throw new Error("올바르지 않은 응답을 받았습니다.");
        }
        repos.push(...data);
        hasMore = data.length === 100;
        page += 1;
      }
      writeStorage(CACHE_KEY, JSON.stringify({ time: Date.now(), repos }));
    }
    state.projects.repos = repos;
    state.projects.status = "success";
    state.projects.filter = "all";
    renderFilters();
  } catch (error) {
    state.projects.status = "error";
    if (error.name === "AbortError") {
      state.projects.error = "요청 시간이 초과되었습니다. 네트워크 연결을 확인해 주세요.";
    } else if (error instanceof TypeError) {
      state.projects.error = "네트워크 연결을 확인하고 다시 시도해 주세요.";
    } else {
      state.projects.error = error.message;
    }
  } finally {
    clearTimeout(timeout);
    renderProjects();
  }
};
filters.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-filter]");
  if (!button) {
    return;
  }
  state.projects.filter = button.dataset.filter;
  // 버튼 DOM을 보존해 키보드 포커스가 사라지지 않게 한다.
  filters.querySelectorAll("button").forEach((item) => {
    const active = item.dataset.filter === state.projects.filter;
    item.classList.toggle("active", active);
    item.setAttribute("aria-pressed", String(active));
  });
  renderProjects();
});
projectList.addEventListener("click", async (event) => {
  if (!event.target.closest("#retry-projects")) {
    return;
  }
  await loadProjects(true);
  (document.querySelector("#retry-projects") || filters.querySelector("button"))?.focus({
    preventScroll: true,
  });
});

// 06. [필수] 문의 폼: input/submit → values와 errors → renderForm
// 검증 함수는 오류 문구를 반환하고, DOM 변경은 renderForm에서만 처리합니다.
const validateField = (name) => {
  const value = state.form.values[name].trim();
  if (!value) {
    return {
      name: "이름을 입력해 주세요.",
      email: "이메일을 입력해 주세요.",
      message: "메시지를 입력해 주세요.",
    }[name];
  }
  if (
    name === "email" &&
    (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ||
      document.querySelector("#email").validity.typeMismatch)
  ) {
    return "올바른 이메일 주소를 입력해 주세요.";
  }
  return "";
};
const renderForm = () => {
  fields.forEach(({ name, id }) => {
    const error = state.form.errors[name] || "";
    document.querySelector(`#${id}-error`).textContent = error;
    document.querySelector(`#${id}`).setAttribute("aria-invalid", String(Boolean(error)));
  });
  document.querySelector("#message-count").textContent =
    `${state.form.values.message.length} / 2000`;
  document.querySelector("#form-status").textContent = state.form.success
    ? "입력값 검증에 성공했습니다! 학습용 폼이므로 메시지는 실제 전송되지 않았습니다."
    : "";
};
// [추가 UX] 입력을 시작하기도 전에 오류를 보이지 않도록 touched를 기억합니다.
fields.forEach((field) => {
  field.addEventListener("input", () => {
    state.form.values[field.name] = field.value;
    state.form.success = false;
    if (state.form.touched[field.name] || state.form.submitted) {
      state.form.errors[field.name] = validateField(field.name);
    }
    renderForm();
  });
  field.addEventListener("blur", () => {
    state.form.values[field.name] = field.value;
    state.form.touched[field.name] = true;
    state.form.errors[field.name] = validateField(field.name);
    renderForm();
  });
});
// 제출 → 기본 새로고침 방지 → 모든 필드 검증 → 성공 안내 또는 첫 오류 포커스
form.addEventListener("submit", (event) => {
  event.preventDefault();
  state.form.submitted = true;
  fields.forEach((field) => {
    state.form.values[field.name] = field.value;
    state.form.errors[field.name] = validateField(field.name);
  });
  state.form.success = !Object.values(state.form.errors).some(Boolean);
  renderForm();
  if (!state.form.success) {
    fields.find(({ name }) => state.form.errors[name]).focus();
  }
});
// 07. 처음 로드될 때 상태를 화면에 반영하고 프로젝트 요청을 시작합니다.
renderTheme();
renderMenu();
renderScroll();
document.querySelector("#year").textContent = new Date().getFullYear();
renderForm();
loadProjects();
