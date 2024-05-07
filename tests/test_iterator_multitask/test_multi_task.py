import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestMultiTask:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        driver.press_keycode(Keys.HOME)
        yield
        console.print("\n执行后置操作")
        # driver.close_app()

    @pytest.mark.swift_2_pro
    def test_enter_multi_task(self, driver: Driver, gestures_page):
        """进入多任务页面"""
        gestures_page.click_recent_apps_btn()

    @pytest.mark.swift_2_pro
    def test_screen_shoot(self, driver: Driver, gestures_page):
        """多任务页面截屏"""
        gestures_page.click_recent_apps_btn()
        gestures_page.screen_shot()
        gestures_page.screen_shot_share()
        # assert_that().contains_value()

    @pytest.mark.swift_2_pro
    def test_clearn_app_up(self,driver: Driver, gestures_page):
        """清除app"""
        gestures_page.click_recent_apps_btn()
        for attempt in retry_attempts(timeout=30):
            with attempt:
                gestures_page.clean_app_up()



