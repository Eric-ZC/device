import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestStorage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver):
        console.print("\n执行前置操作")
        yield
        console.print("\n执行后置操作")
        driver.close_app()
        # driver.press_keycode(Keys.HOME)


    @pytest.mark.swift_2_pro
    def test_factory_reset(self, driver:Driver, settings_page, reset_option_page):
        """回复出厂值"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_option_page.click_reset_options()
        reset_option_page.click_factory_reset()
        reset_option_page.erase_all_data()
        # reset_option_page.erase_all_data()
        # 恢复出厂值的验证

    @pytest.mark.swift_2_pro
    def test_developer_options(self, driver: Driver, settings_page, gestures_page, about_device_page):
        """开发者模式"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_about_device()
        about_device_page.enter_developer()
        gestures_page.click_back_btn()
        settings_page.click_system()
        state = settings_page.developer_options()
        assert_that(state).is_not_none()