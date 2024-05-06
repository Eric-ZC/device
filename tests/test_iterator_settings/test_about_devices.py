import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestAboutDevices:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.press_keycode(Keys.HOME)
        driver.launch_app(*settings.packages.settings)
        yield
        console.print("\n执行后置操作")
        driver.close_app()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    @pytest.mark.swan_1_pro
    def test_about_devices(self, driver: Driver, settings_page,about_device_page):
        """关于设备"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_about_device()
        content = about_device_page.get_toolbar_content()
        assert_that(content).is_equal_to("关于设备")

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_about_devices(self, driver: Driver, settings_page, about_device_page):
        """关于设备"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_about_device()
        content = about_device_page.get_action_bar()
        assert_that(content).is_equal_to("关于设备")





