import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestSetting:

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
    def test_search_engines(self, driver: Driver, chrome_page):
        """搜索引擎"""

        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_search_engines()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_passcode(self, driver: Driver, chrome_page):
        """密码"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_password_tools()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_pay(self, driver: Driver, chrome_page):
        """支付方式"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_pay_way()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_address(self, driver: Driver, chrome_page):
        """地址选项"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_address()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_notification(self, driver: Driver, chrome_page):
        """通知"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_notification()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_homepage(self, driver: Driver, chrome_page):
        """主页"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_setting_homepage()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_style(self, driver: Driver, chrome_page):
        """主题背景"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_style_background()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_privacy_pay(self, driver: Driver, chrome_page):
        """查询付款方式"""
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_privacy_settings()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_privacy_load(self, driver: Driver, chrome_page):
        """预加载网页"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_privacy_settings()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_privacy_follow(self, driver: Driver, chrome_page):
        """跟踪"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_privacy_settings()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_privacy_clear(self, driver: Driver, chrome_page):
        """清除浏览数据"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_setting()
        chrome_page.click_privacy_settings()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_advanced_options_scale(self, driver: Driver, chrome_page):
        """缩放"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_accessibility()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_advanced_options_force_scale(self, driver: Driver, chrome_page):
        """强制缩放"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_accessibility()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_simplified_view(self, driver: Driver, chrome_page):
        """简化视图"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_accessibility()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_captions(self, driver: Driver, chrome_page):
        """字幕"""
        chrome_page.click_home_page()
        chrome_page.click_home_page()
        chrome_page.click_more_btn()
        chrome_page.click_accessibility()

    def test_turn_on(self, driver: Driver, chrome_page):
        """开关"""
        chrome_page.click_home_page()

    def test_language(self, driver: Driver, chrome_page):
        """调整语言"""
        chrome_page.click_home_page()

    def test_download(self, driver: Driver, chrome_page):
        """下载内容"""
        chrome_page.click_home_page()

    def test_about(self, driver: Driver, chrome_page):
        """关于"""
        chrome_page.click_home_page()
