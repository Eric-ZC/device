import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestSystemNavigation:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    def test_gestures_navigation(self, driver: Driver, gestures_page):
        """手势导航"""
        gestures_page.click_gestures_btn()
        gestures_page.click_system_navigation_btn()
        gestures_page.click_gestures_navigation_checkbox()
        gestures_page.click_back_navigation()
        status = gestures_page.get_navigation_status()
        assert_that(status).is_equal_to("手势导航")

    @pytest.mark.swift_2_pro
    def test_Three_key_navigation(self, driver: Driver, gestures_page):
        """三键导航"""
        gestures_page.click_gestures_btn()
        gestures_page.click_system_navigation_btn()
        gestures_page.click_three_keys_navigation_checkbox()
        gestures_page.click_back_navigation()
        status = gestures_page.get_navigation_status()
        assert_that(status).is_equal_to("“三按钮”导航")

    @pytest.mark.swift_2_pro
    def test_back_to_last_page(self, driver: Driver, gestures_page):
        """返回至上一级页面"""
        gestures_page.click_gestures_btn()
        gestures_page.click_system_navigation_btn()
        gestures_page.click_three_keys_navigation_checkbox()
        gestures_page.click_back_btn()
        status = gestures_page.get_navigation_status()
        assert_that(status).is_equal_to("“三按钮”导航")

    @pytest.mark.swift_2_pro
    def test_back_to_home_page(self, driver: Driver, gestures_page):
        """跳转至主屏幕"""
        gestures_page.click_home_page_btn()
        assert_that(gestures_page.back_to_main).is_not_none()

    @pytest.mark.swift_2_pro
    def test_switch_app(self, driver: Driver, gestures_page):
        """切换App"""
        driver.launch_app(*settings.packages.chrome)
        app1 = driver.get_current_app()
        gestures_page.switch_recent_apps()
        app2 = driver.get_current_app()
        assert_that(app1).is_not_equal_to(app2)




