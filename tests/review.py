# -*- coding: utf-8 -*-
"""사이트 기능을 Chrome으로 자동 점검하는 개발용 파일입니다.

사이트 화면을 만드는 파일은 아닙니다. index.html에서 불러오지 않습니다.
Python은 검사 도구를 실행하고, Playwright는 Chrome의 클릭·입력·확인을 자동화합니다.
미션 필수 구현은 HTML/CSS/JavaScript이며 이 파일의 Python 학습은 필수가 아닙니다.

실행 준비와 파일 역할: ../FILE_GUIDE.md 참고.
B1-1 폴더에서 로컬 서버를 먼저 실행합니다:
    python3 -m http.server 5511 --bind 127.0.0.1
다른 터미널에서 Python + Playwright가 설치된 환경으로 실행합니다:
    python tests/review.py          # 모의 GitHub 데이터로 검사
    python tests/review.py --live   # 실제 API·공개 사이트도 검사, 스크린샷 갱신

--live는 images/screenshots의 기존 이미지 3개를 덮어씁니다. 배포 명령은 아닙니다.
PASS는 해당 검사 통과, ALL PASS는 실행한 검사 전체 통과입니다.
실패하면 오류가 난 위치에서 중단하므로 마지막 오류 내용을 확인합니다.

읽는 순서: 01 설정 → 02 공통 검사 → 03~14 기능별 검사 → 15 실제 사이트 → 16 실행.
"""
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

# 01. 검사 주소와 연습용 저장소 데이터: 실제 계정에 저장하거나 업로드하지 않습니다.
BASE = 'http://127.0.0.1:5511'
API = 'https://api.github.com/**'
KEY = 'portfolio-repos-dooolll00'
REPOS = [dict(name='alpha', description='First project', language='JavaScript',
              html_url='https://github.com/dooolll00/alpha', updated_at='2026-09-01T00:00:00Z',
              stargazers_count=2, forks_count=1),
         dict(name='beta', description=None, language='HTML',
              html_url='https://github.com/dooolll00/beta', updated_at='2026-09-02T00:00:00Z',
              stargazers_count=0, forks_count=0)]
passed = []

# 02. 공통 검사 도우미: 검사 실행 후 통과한 이름을 기록합니다.
def check(name, fn):
    fn()
    passed.append(name)
    print('PASS', name, flush=True)


def main(live):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        print('Chrome:', browser.version, flush=True)

        # 각 검사를 새 브라우저 환경에서 시작해 이전 테마·캐시가 섞이지 않게 합니다.
        # handler는 GitHub 대신 돌려줄 모의 응답, init은 페이지 시작 전 준비 코드입니다.
        def scenario(name, test, handler=None, init=None, **options):
            context = browser.new_context(color_scheme='light', reduced_motion='reduce', **options)
            if init:
                context.add_init_script(init)
            page = context.new_page()
            page.clock.install()
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            route_handler = handler or (lambda r: r.fulfill(json=REPOS))
            page.route(API, lambda route: route_handler(route))
            try:
                page.goto(BASE)
                test(page)
                assert not errors, errors
                print('PASS', name, flush=True)
                passed.append(name)
            finally:
                context.close()

        # 03. HTML 구조: 섹션·링크·레이블·이미지·Flex/Grid 확인
        def structure(page):
            expect(page.locator('.project-card')).to_have_count(2)
            for tag in ['header', 'nav', 'main', 'section', 'article', 'footer']:
                assert page.locator(tag).count() > 0, tag
            assert page.locator('[style], [onclick]').count() == 0
            assert page.locator('script[src="js/main.js"][defer]').count() == 1
            assert page.locator('link[rel="stylesheet"][href="css/style.css"]').count() == 1
            for section in ['hero', 'about', 'skills', 'projects', 'contact', 'footer']:
                assert page.locator('#' + section).count() == 1
                assert page.locator('nav a[href="#' + section + '"]').count() >= 1
            for field in ['name', 'email', 'message']:
                assert page.locator('label[for="' + field + '"]').count() == 1
            assert page.locator('img').evaluate_all('(imgs) => imgs.every(i => i.alt.trim())')
            page.locator('#about').scroll_into_view_if_needed()
            page.wait_for_function('Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)')
            assert page.locator('.nav').evaluate('(e) => getComputedStyle(e).display') == 'flex'
            assert page.locator('.projects-grid').evaluate('(e) => getComputedStyle(e).display') == 'grid'
        scenario('semantic structure, all anchors, labels, alt, assets, Flex/Grid', structure)

        # 04. 반응형: 여러 화면 너비에서 가로 넘침과 메뉴 표시 확인
        def responsive(page):
            expect(page.locator('.project-card')).to_have_count(2)
            for width in [320, 375, 767, 768, 1024, 1440]:
                page.set_viewport_size(dict(width=width, height=900))
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), width
                if width < 768:
                    expect(page.locator('#menu-toggle')).to_be_visible()
                    expect(page.locator('#nav-menu')).to_be_hidden()
                    page.locator('#menu-toggle').click()
                    expect(page.locator('#nav-menu')).to_be_visible()
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), width
                    page.locator('#menu-toggle').click()
                    expect(page.locator('#nav-menu')).to_be_hidden()
                else:
                    expect(page.locator('#menu-toggle')).to_be_hidden()
                    expect(page.locator('#nav-menu')).to_be_visible()
                    assert page.locator('#nav-menu').evaluate('(e) => e.getBoundingClientRect().right <= document.querySelector(".nav-actions").getBoundingClientRect().left'), width
        scenario('responsive 320/375/767/768/1024/1440, mobile menu', responsive)

        # 05. 메뉴와 스크롤: 닫기·포커스·60px/300px 경계 확인
        def menu_scroll(page, target='footer'):
            page.locator('#menu-toggle').click()
            page.keyboard.press('Escape')
            expect(page.locator('#menu-toggle')).to_be_focused()
            expect(page.locator('#nav-menu')).to_be_hidden()
            page.locator('#menu-toggle').click()
            page.mouse.click(10, 850)
            expect(page.locator('#nav-menu')).to_be_hidden()
            page.locator('#menu-toggle').click()
            page.locator('#nav-menu a[href="#' + target + '"]').click()
            expect(page.locator('#' + target)).to_be_focused()
            expect(page.locator('#nav-menu')).to_be_hidden()
            page.locator('#scroll-top').click()
            page.wait_for_function('scrollY === 0')
            for y, header, top in [(59, False, False), (60, True, False), (299, True, False), (300, True, True)]:
                page.evaluate('(y) => scrollTo(0,y)', y)
                page.wait_for_function('(y) => scrollY === y', arg=y)
                page.wait_for_function('(expected) => document.querySelector(".site-header").classList.contains("scrolled") === expected', arg=header)
                if top:
                    expect(page.locator('#scroll-top')).to_be_visible()
                else:
                    expect(page.locator('#scroll-top')).to_be_hidden()
            page.locator('#menu-toggle').click()
            page.set_viewport_size(dict(width=1024, height=900))
            expect(page.locator('#menu-toggle')).to_have_attribute('aria-expanded', 'false')
        scenario('menu Escape/outside/anchor/resize, focus, 59/60/299/300px scroll', menu_scroll, viewport=dict(width=375, height=900))

        # 06. 테마: 시스템 설정·직접 선택·새로고침 후 저장 확인
        def theme(page):
            expect(page.locator('html')).to_have_attribute('data-theme', 'light')
            page.emulate_media(color_scheme='dark')
            expect(page.locator('html')).to_have_attribute('data-theme', 'dark')
            page.locator('#theme-toggle').click()
            expect(page.locator('html')).to_have_attribute('data-theme', 'light')
            page.reload()
            expect(page.locator('html')).to_have_attribute('data-theme', 'light')
            page.locator('#theme-toggle').click()
            page.reload()
            expect(page.locator('html')).to_have_attribute('data-theme', 'dark')
            assert page.evaluate("localStorage.getItem('portfolio-theme')") == 'dark'
        scenario('system theme, manual preference, reload persistence', theme)

        # 07. 문의 폼: 빈 값·공백·이메일 오류·성공·수정 후 초기화 확인
        def form(page):
            submit = page.locator('#contact-form button[type="submit"]')
            submit.click()
            for field in ['name', 'email', 'message']:
                expect(page.locator('#' + field)).to_have_attribute('aria-invalid', 'true')
                expect(page.locator('#' + field + '-error')).not_to_be_empty()
            expect(page.locator('#name')).to_be_focused()
            page.locator('#name').fill('   ')
            page.locator('#email').fill('invalid')
            page.locator('#message').fill('   ')
            submit.click()
            expect(page.locator('#form-status')).to_be_empty()
            page.locator('#name').fill('발표 테스트')
            page.locator('#email').fill('hello@example.com')
            page.locator('#message').fill('안녕하세요')
            submit.click()
            expect(page.locator('#form-status')).to_contain_text('검증에 성공')
            expect(page.locator('#message-count')).to_have_text('5 / 2000')
            for field in ['name', 'email', 'message']:
                expect(page.locator('#' + field)).to_have_attribute('aria-invalid', 'false')
            page.locator('#message').fill('수정')
            expect(page.locator('#form-status')).to_be_empty()
        scenario('form required/whitespace/email/success/reset/counter', form)

        # 08. 언어 필터: 선택한 언어만 남고 키보드 포커스가 유지되는지 확인
        def filtering(page):
            expect(page.locator('.project-card')).to_have_count(2)
            page.locator('[data-filter="HTML"]').click()
            expect(page.locator('.project-card')).to_have_count(1)
            expect(page.locator('.project-card h3')).to_contain_text('beta')
            expect(page.locator('[data-filter="HTML"]')).to_be_focused()
            page.locator('[data-filter="all"]').click()
            expect(page.locator('.project-card')).to_have_count(2)
        scenario('language filter and focus', filtering)

        # 09. API 화면: 응답을 기다리는 로딩과 빈 결과 확인
        pending = []
        def loading(page):
            expect(page.locator('#project-list')).to_have_attribute('aria-busy', 'true')
            expect(page.locator('.spinner')).to_be_visible()
            assert len(pending) == 1
            pending.pop().fulfill(json=REPOS)
            expect(page.locator('.project-card')).to_have_count(2)
            expect(page.locator('#project-list')).to_have_attribute('aria-busy', 'false')
        scenario('loading to success', loading, lambda r: pending.append(r))
        scenario('empty success', lambda page: expect(page.locator('#project-list')).to_contain_text('표시할 프로젝트가 없습니다'), lambda r: r.fulfill(json=[]))
        # 10. API 실패: 모의 HTTP 오류·재시도·네트워크 오류·잘못된 데이터 확인
        for status in [403, 429, 404, 500]:
            calls = []
            def handler(route, *, status=status):
                calls.append(1)
                route.fulfill(status=status, json={}) if len(calls) == 1 else route.fulfill(json=REPOS)
            def retry(page, status=status):
                expect(page.locator('#retry-projects')).to_be_visible()
                expect(page.locator('#project-list')).to_contain_text('프로젝트를 불러올 수 없습니다')
                if status in [403, 429]:
                    expect(page.locator('#project-list')).to_contain_text('요청 한도')
                page.locator('#retry-projects').click()
                expect(page.locator('.project-card')).to_have_count(2)
            scenario('HTTP %s and retry' % status, retry, handler)
        scenario('network failure', lambda page: expect(page.locator('#project-list')).to_contain_text('네트워크 연결'), lambda r: r.abort())
        for body in [{}, [None], ['bad'], [dict(REPOS[0], language={})]]:
            scenario('invalid response ' + str(body)[:40], lambda page: expect(page.locator('#project-list')).to_contain_text('올바르지 않은 응답'), lambda r, *, body=body: r.fulfill(json=body))

        # 11. 캐시: 손상·만료·정상 데이터와 저장 공간 차단 확인
        for cache in ['{', json.dumps(dict(time=0, repos=REPOS))]:
            scenario('broken or expired cache', lambda page: expect(page.locator('.project-card')).to_have_count(2), init='localStorage.setItem(%s, %s)' % (json.dumps(KEY), json.dumps(cache)))
        scenario('cache with null item recovers via network', lambda page: expect(page.locator('.project-card')).to_have_count(2), init="localStorage.setItem('%s', JSON.stringify({time: Date.now(), repos:[null]}))" % KEY)
        requests = []
        scenario('valid cache skips network', lambda page: (expect(page.locator('.project-card')).to_have_count(2), check('zero network calls with valid cache', lambda: assert_zero(requests))), lambda r: (requests.append(1), r.abort()), init="localStorage.setItem('%s', JSON.stringify({time: Date.now(), repos: %s}))" % (KEY, json.dumps(REPOS)))
        scenario('blocked storage preserves page and API', lambda page: (expect(page.locator('.project-card')).to_have_count(2), page.locator('#theme-toggle').click(), expect(page.locator('html')).to_have_attribute('data-theme', 'dark')), init="Storage.prototype.getItem = Storage.prototype.setItem = () => { throw new Error('blocked'); }")
        # 12. 여러 페이지 조회: 저장소 100개 + 다음 페이지 1개 확인
        pages = []
        def pagination(route):
            pages.append(route.request.url)
            route.fulfill(json=[dict(REPOS[0], name='repo-%s' % i) for i in range(100)] if len(pages) == 1 else [REPOS[1]])
        scenario('pagination 100 + 1', lambda page: expect(page.locator('.project-card')).to_have_count(101), pagination)
        assert len(pages) == 2 and 'page=2' in pages[1]
        # 13. 외부 데이터: 문자열이 코드로 실행되지 않고 링크가 검사되는지 확인
        unsafe = dict(REPOS[0], name='<img src=x onerror="window.injected=1">', description='<script>bad()</script>', html_url='javascript:alert(1)')
        def escaping(page):
            expect(page.locator('.project-card')).to_have_count(1)
            assert page.locator('.project-card img, .project-card script').count() == 0
            expect(page.locator('.project-card h3 a')).to_have_attribute('href', 'https://github.com/dooolll00')
            assert page.evaluate('window.injected === undefined')
        scenario('API HTML escaping and URL validation', escaping, lambda r: r.fulfill(json=[unsafe]))

        # 14. 시간 제한과 애니메이션: 응답 지연 중단·실제 Observer 등장 확인
        def timeout(page):
            page.clock.fast_forward(15001)
            expect(page.locator('#project-list')).to_contain_text('요청 시간이 초과')
        # GitHub 응답만 기다리게 만든 뒤, 가상 시간을 진행해 실제 AbortController 중단을 확인합니다.
        scenario('15-second request timeout', timeout, init="const nativeFetch = window.fetch; window.fetch = (...args) => String(args[0]).startsWith('https://api.github.com/') ? new Promise((resolve,reject) => args[1].signal.addEventListener('abort', () => reject(new DOMException('Aborted','AbortError')))) : nativeFetch(...args);")

        context = browser.new_context(viewport=dict(width=375, height=900), reduced_motion='no-preference')
        page = context.new_page()
        page.route(API, lambda r: r.fulfill(json=REPOS))
        page.goto(BASE)
        assert page.locator('.reveal.is-pending').count() > 0
        page.locator('#about').scroll_into_view_if_needed()
        expect(page.locator('.about-grid')).to_have_class('container about-grid reveal is-visible')
        assert page.locator('html').evaluate('(e) => getComputedStyle(e).scrollBehavior') == 'smooth'
        context.close()
        print('PASS real Intersection Observer and smooth scrolling CSS', flush=True)
        passed.append('real Intersection Observer and smooth scrolling CSS')

        # 15. --live 전용: 실제 API·공개 사이트 확인 후 로컬 스크린샷 갱신
        if live:
            for url in [BASE, 'https://dooolll00.github.io/B1-1/']:
                context = browser.new_context(viewport=dict(width=1440, height=1000), reduced_motion='reduce', color_scheme='light')
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda e: errors.append(str(e)))
                response = page.goto(url)
                assert response.status == 200
                expect(page.locator('.project-card').first).to_be_visible(timeout=25000)
                print('LIVE', url, page.locator('.project-card').count(), 'repositories', flush=True)
                theme(page)
                form(page)
                page.set_viewport_size(dict(width=375, height=900))
                page.evaluate('scrollTo(0,0)')
                menu_scroll(page, target='about')
                for width in [320, 375, 768, 1024, 1440]:
                    page.set_viewport_size(dict(width=width, height=1000))
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (url, width)
                assert not errors, errors
                if url == BASE:
                    page.reload()
                    expect(page.locator('.project-card').first).to_be_visible()
                    page.locator('#contact-form').evaluate('(form) => form.reset()')
                    folder = Path(__file__).resolve().parents[1] / 'images/screenshots'
                    for name, width, dark in [('desktop',1440,False), ('mobile',375,False), ('dark',1440,True)]:
                        page.set_viewport_size(dict(width=width,height=1000))
                        if (page.locator('html').get_attribute('data-theme') == 'dark') != dark:
                            page.locator('#theme-toggle').click()
                        page.locator('#about').scroll_into_view_if_needed()
                        page.wait_for_function('Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)')
                        page.evaluate('scrollTo(0,0)')
                        page.wait_for_timeout(150)
                        page.screenshot(path=str(folder / (name + '.png')), full_page=True)
                context.close()
                passed.append('live smoke ' + url)
        browser.close()
        print('ALL PASS:', len(passed), 'checks', flush=True)


def assert_zero(items):
    assert not items, items


# 16. 터미널에서 이 파일을 직접 실행했을 때 시작하는 부분
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true', help='Also check real GitHub API and Pages; refresh screenshots.')
    main(parser.parse_args().live)
