import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestHomePage:

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
    def test_view_google(self, driver: Driver,chrome_page):
        """访问google网络"""
        driver.launch_app(*settings.packages.chrome)
        chrome_page.click_home_page()
        chrome_page.click_search_bar()
        chrome_page.editor_address("https://www.google.com")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_view_baidu(self, driver: Driver,chrome_page):
        """访问百度网络"""
        chrome_page.click_home_page()
        chrome_page.click_search_bar()
        chrome_page.editor_address("https://www.baidu.com/")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_launcher_chrome(self, driver: Driver,chrome_page):
        """启动浏览器"""
        chrome_page.click_home_page()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_close_tab(self, driver: Driver, chrome_page):
        """关闭页签"""
        chrome_page.click_home_page()
        chrome_page.click_tab_switch()
        chrome_page.click_close_tab()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_new_tab(self, driver: Driver, chrome_page):
        """新增页签"""
        chrome_page.click_home_page()
        chrome_page.click_tab_switch()
        chrome_page.click_open_new_tab()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_home_page(self, driver: Driver, chrome_page):
        """返回主页"""
        chrome_page.click_home_page()

    def test_forward_back(self, driver: Driver, chrome_page):
        """前进/后退"""
        chrome_page.click_home_page()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fresh_page(self, driver: Driver, chrome_page):
        """刷新"""
        chrome_page.click_home_page()
        chrome_page.click_search_bar()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_refresh()

    def test_web_info(self, driver: Driver, chrome_page):
        """网站信息"""
        chrome_page.click_home_page()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_bookmark(self, driver: Driver, chrome_page):
        """书签"""
        chrome_page.click_home_page()
        chrome_page.click_search_bar()
        chrome_page.editor_address("https://www.baidu.com/")
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_download(self, driver: Driver, chrome_page):
        """下载"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_frequently_visited(self, driver: Driver, chrome_page):
        """最常访问"""
        chrome_page.click_home_page()
        chrome_page.click_link()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_new_tab(self, driver:Driver,chrome_page):
        """打开新页签"""
        chrome_page.click_home_page()
        chrome_page.hold_link()
        chrome_page.click_hold_link()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_incognito(self, driver: Driver, chrome_page):
        """打开无痕"""
        chrome_page.click_home_page()
        chrome_page.hold_link()
        chrome_page.click_incognito_link()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_download_link(self, driver: Driver, chrome_page):
        """下载链接"""
        chrome_page.click_home_page()
        chrome_page.hold_link()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete_link(self, driver: Driver, chrome_page):
        """删除链接"""
        chrome_page.click_home_page()
        chrome_page.hold_link()
        chrome_page.click_delete_link()
