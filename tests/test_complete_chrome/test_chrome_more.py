import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestMore:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page, chrome_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.chrome)
        chrome_page.chrome_init()
        yield
        console.print("\n执行后置操作")
        driver.clear_app("com.android.chrome")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_new_tab(self, driver: Driver, chrome_page):
        """打开新页签"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_open_tab()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_incognito(self, driver: Driver, chrome_page):
        """打开无痕页签"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_open_incognito()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_bookmark(self, driver: Driver, chrome_page):
        """打开书签"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_last_opened(self, driver: Driver, chrome_page):
        """最近打开"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_last_open()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_history(self, driver: Driver, chrome_page):
        """打开历史记录"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_open_history()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_download(self, driver: Driver, chrome_page):
        """打开下载内容"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_share(self, driver: Driver, chrome_page):
        """分享..."""
        chrome_page.click_home_page()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_share()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_findstr(self, driver: Driver, chrome_page):
        """网页中查找"""
        chrome_page.click_home_page()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_find_page()

    def test_add_to_screen(self, driver: Driver, chrome_page):
        """添加到主页"""
        chrome_page.click_home_page()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_desktop(self, driver: Driver, chrome_page):
        """桌面版网站"""
        chrome_page.click_home_page()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_desktop_site()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_setting(self, driver: Driver, chrome_page):
        """设置"""
        chrome_page.click_home_page()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_setting()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_help_feedback(self, driver: Driver, chrome_page):
        """帮助与反馈"""
        chrome_page.click_home_page()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_help_feedback()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_incognito_view(self, driver: Driver, chrome_page):
        """无痕浏览"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_open_incognito()
        chrome_page.editor_address("https://www.baidu.com/")

    @pytest.mark.D4pro
    def test_switch_incognito(self, driver: Driver, chrome_page):
        """无痕切换"""
        chrome_page.click_home_page()

    def test_open_last_page(self, driver: Driver, chrome_page):
        """打卡最近的标签页"""
        chrome_page.click_home_page()