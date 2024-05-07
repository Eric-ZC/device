import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestBluetooth:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        time.sleep(5)
        settings_page.click_connected_devices()
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    def test_pull_down_menu(self, driver: Driver, notification_panel):
        """下拉框"""
        notification_panel.expand(count=2)
        console.print("下拉快捷菜单")
        bluetooth_status = driver.bluetooth_on
        notification_panel.click_bluetooth()
        assert_that(driver.bluetooth_on).is_type_of(bool).is_not_equal_to(bluetooth_status)
        notification_panel.hold_press_bluetooth()

    @pytest.mark.swift_2_pro
    def test_bluetooth_receive_file(self, driver: Driver, connection_preferences_page, bluetooth_received_page, settings_page):
        """蓝牙接收文件"""
        connection_preferences_page.click_file_received_via_bluetooth()

    @pytest.mark.swift_2_pro
    def test_virtual_bluetooth(self, driver: Driver, settings_page, connection_preferences_page):
        """虚拟蓝牙"""
        connection_preferences_page.click_view_all()
        connection_preferences_page.click_set_btn()
        connection_preferences_page.click_rename()
        connection_preferences_page.input_rename("111")
        connection_preferences_page.click_confirm_rename()
