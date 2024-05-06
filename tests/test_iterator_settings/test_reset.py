import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestRest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.D4_504_Pro
    def test_rest_internet(self,driver:Driver, reset_wlan_network_page):
        """重置网络"""
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()
        status = reset_wlan_network_page.toast_display()
        console.print(status)
        assert_that(status).is_equal_to("网络设置已重置")
        # 重置 断言
