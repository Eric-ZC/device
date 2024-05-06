import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TesDownLoad:

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
        """下载查看"""

        driver.launch_app(*settings.packages.chrome)
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_setting(self, driver: Driver, chrome_page):
        """下载设置"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_share(self, driver: Driver, chrome_page):
        """下载分享"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_rename(self, driver: Driver, chrome_page):
        """下载重命名"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete(self, driver: Driver, chrome_page):
        """下载删除"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_download_btn()
