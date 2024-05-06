import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestBookMark:

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
    def test_search(self, driver: Driver, chrome_page):
        """书签查找"""
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()
        chrome_page.click_mobile_bookmark()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_select(self, driver: Driver, chrome_page):
        """选择书签"""
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()
        chrome_page.click_mobile_bookmark()
        chrome_page.click_select_bookmark()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_move(self, driver: Driver, chrome_page):
        """移动书签"""
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()
        chrome_page.click_mobile_bookmark()
        chrome_page.click_select_bookmark()
        chrome_page.click_bookmarks_setting()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_edit(self, driver: Driver, chrome_page):
        """编辑书签"""
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()
        chrome_page.click_mobile_bookmark()
        chrome_page.click_select_bookmark()
        chrome_page.click_bookmarks_setting()
        chrome_page.click_bookmarks_edit()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete(self, driver: Driver, chrome_page):
        """删除书签"""
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()
        chrome_page.click_mobile_bookmark()
        chrome_page.click_select_bookmark()
        chrome_page.click_bookmarks_setting()
        chrome_page.click_bookmarks_delete()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_move_to(self, driver: Driver, chrome_page):
        """书签上下移动"""
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_bookmarks()
        chrome_page.click_mobile_bookmark()
        chrome_page.click_select_bookmark()
        chrome_page.click_bookmarks_setting()
        chrome_page.click_bookmarks_move()
