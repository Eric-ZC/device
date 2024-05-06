import time

import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestChrome:

    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self, driver: Driver, settings_page, chrome_page):
    #     console.print("\n执行前置操作")
    #     driver.launch_app(*settings.packages.chrome)
    #     chrome_page.chrome_init()
    #     yield
    #     console.print("\n执行后置操作")
    #     driver.clear_app("com.android.chrome")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_goto_page(self, driver: Driver, chrome_page):
        """进入youtube"""

        # chrome_page.click_home_page()
        driver.launch_app(*settings.packages.chrome)
        chrome_page.chrome_init()
        chrome_page.click_home_page_back()

        chrome_page.click_search_bar()
        chrome_page.editor_address("m.youtube.com")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_play_video(self, driver:Driver, chrome_page):
        """下载内容"""
        # chrome_page.click_home_page()
        chrome_page.click_home_page_back()

        chrome_page.click_more_btn()
        chrome_page.click_download_btn()
        chrome_page.click_close_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_add_to_main_screen(self,driver: Driver, chrome_page):
        """添加到主屏幕"""
        chrome_page.click_home_page_back()
        chrome_page.click_search_bar()
        chrome_page.editor_address("m.youtube.com")
        chrome_page.click_more_btn()
        chrome_page.addto_main_screen()
        chrome_page.click_add_confirm()
        chrome_page.click_home_page_back()
        driver.clear_app("com.android.chrome")


    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_goto_page_oir(self, driver: Driver, chrome_page):
        """进入youtube"""
        chrome_page.click_d4_504_pro_home_page()
        chrome_page.click_home_page_back()
        chrome_page.click_search_bar()
        chrome_page.editor_address("m.youtube.com")


    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_play_video_oir(self, driver:Driver, chrome_page):
        """下载内容"""
        chrome_page.click_d4_504_pro_home_page()
        chrome_page.click_home_page_back()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()
        chrome_page.click_close_btn()

    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_add_to_main_screen_oir(self,driver: Driver, chrome_page):
        """添加到主屏幕"""
        chrome_page.click_d4_504_pro_home_page()
        chrome_page.click_home_page_back()
        chrome_page.click_search_bar()
        chrome_page.editor_address("www.sina.com.cn")
        chrome_page.click_more_btn()
        chrome_page.addto_main_screen()
        chrome_page.click_add_confirm()
        chrome_page.click_d4_504_pro_home_page()
        chrome_page.click_home_page_back()
        driver.close_app()



