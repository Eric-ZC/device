import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestDisplay:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, notification_panel):
        driver.launch_app(*settings.packages.settings)
        console.print("\n执行前置操作")

        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    def test_gradual_illumination(self, driver: Driver, settings_page, display_page):
        """亮度渐变"""
        settings_page.click_display()
        display_page.drag_brightness_bar(0)
        display_page.drag_brightness_bar(1)
        max_brightness = driver.get_screen_brightness()
        # assert_that(max_brightness).is_equal_to(255)
        # ele = notification_panel.brightness_view()
        # assert_that(ele).is_not_none()
