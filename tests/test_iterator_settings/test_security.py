import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestSettings:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        settings_page.click_security()
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    def test_no_screen_lock(self,driver: Driver,security_page):
        """无锁屏解锁"""

        security_page.click_screen_lock()
        security_page.select_no_lock()
        security_page.lock_screen()
        status = security_page.get_screen_lock_status()
        console.print(status)
        # assert_that(status).is_equal_to("无")

    @pytest.mark.swift_2_pro
    def test_slide_screen_lock(self,driver: Driver,security_page):
        """滑动解锁"""

        security_page.click_screen_lock()
        security_page.select_slide_lock()
        security_page.lock_screen()
        driver.swipe_up(count=3, duration=8)
        status = security_page.get_screen_lock_status()
        console.print(status)
        # assert_that(status).is_equal_to("滑动")

    # def test_pin_screen_lock(self,driver:Driver,settings_page):
    #     """PIN 码解锁"""
    #     settings_page.click_security()
    #     settings_page.click_screen_lock()
    #     settings_page.select_pin_lock()
    #     settings_page.setting_pin_lock()
    #     settings_page.click_next_step()
    #     settings_page.setting_pin_lock()
    #     settings_page.click_confirm()
    #     settings_page.click_accomplish()
    #     settings_page.lock_screen()
    #     driver.swipe_up(count=2, duration=3)