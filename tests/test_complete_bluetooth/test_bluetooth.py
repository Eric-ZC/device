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
        driver.clear_app("com.android.settings")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_bluetooth_address(self, driver: Driver, notification_panel, settings_page, about_device_page):
        """蓝牙地址"""
        driver.switch_bluetooth(True)
        driver.launch_app(*settings.packages.settings)
        settings_page.click_about_device()
        bluetooth_address = about_device_page.get_bluetooth_address()
        items = bluetooth_address.split(":")
        console.print(items)
        assert_that(items).is_length(6).does_not_contain("")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_quick_switch(self, driver: Driver, notification_panel):
        """下拉快捷菜单开关蓝牙"""
        driver.switch_bluetooth(True)
        notification_panel.expand(2)
        notification_panel.click_bluetooth()
        status = driver.bluetooth_on
        assert_that(status).is_equal_to(False)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_blue_detail(self, driver: Driver, notification_panel, bluetooth_page):
        """下拉快捷菜单到蓝牙详情"""
        notification_panel.expand(2)
        notification_panel.click_bluetooth(duration=3)
        status = bluetooth_page.connected_device_visible()
        assert_that(status).is_equal_to(True)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_close_bluetooth(self, driver: Driver, notification_panel, bluetooth_page):
        """关闭蓝牙返回上一级"""
        driver.switch_bluetooth(True)
        notification_panel.expand(2)
        notification_panel.click_bluetooth(duration=3)
        bluetooth_page.click_pair_new_device()
        notification_panel.expand(2)
        notification_panel.click_bluetooth()
        driver.back()
        status = bluetooth_page.connected_device_visible()
        assert_that(status).is_equal_to(True)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_switch_off(self, driver: Driver, notification_panel, bluetooth_page, connection_preferences_page):
        """开关蓝牙"""
        driver.switch_bluetooth(True)
        notification_panel.expand(2)
        notification_panel.click_bluetooth(duration=3)
        bluetooth_page.preference_settings()
        bluetooth_page.click_bluetooth()
        connection_preferences_page.switch_bluetooth()
        status = driver.bluetooth_on
        assert_that(status).is_equal_to(False)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_on_off_50_times(self, driver: Driver, notification_panel):
        """开关蓝牙"""
        notification_panel.expand(count=2)
        for _ in range(50):
            bluetooth_status = driver.bluetooth_on
            notification_panel.click_bluetooth()
            for attempt in retry_attempts(timeout=10):
                with attempt:
                    assert_that(driver.bluetooth_on).is_type_of(bool).is_not_equal_to(
                        bluetooth_status
                    )
        notification_panel.click_bluetooth(duration=1)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_edit_device_name(self, driver: Driver, notification_panel, bluetooth_page, connection_preferences_page):
        """修改设备名称"""
        driver.switch_bluetooth(True)
        notification_panel.expand(2)
        notification_panel.click_bluetooth(duration=3)
        bluetooth_page.preference_settings()
        bluetooth_page.click_bluetooth()
        bluetooth_page.device_name()
        bluetooth_page.device_name_input("LARK 1")
        bluetooth_page.rename()
        device_name = connection_preferences_page.device_name()
        assert_that(device_name).is_equal_to("LARK 1")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_flight_mode(self, driver: Driver, notification_panel):
        """飞行模式"""
        driver.switch_bluetooth(True)
        initial_status = driver.bluetooth_on
        assert_that(initial_status, "蓝牙初始状态应为开启").is_equal_to(True)

        notification_panel.expand(1)
        notification_panel.click_flight_mode()
        status_first = driver.bluetooth_on
        assert_that(status_first, "蓝牙状态应在飞行模式开启后变为关闭").is_equal_to(False)

        # notification_panel.expand(1)
        notification_panel.click_flight_mode()
        status_second = driver.bluetooth_on
        assert_that(status_second, "蓝牙状态应在飞行模式关闭后恢复为开启").is_equal_to(True)

    @pytest.mark.swift_2_pro
    def test_view_virtual_bluetooth(self, driver: Driver, connection_preferences_page):
        """虚拟蓝牙"""
        connection_preferences_page.click_view_all()
        connection_preferences_page.click_set_btn()
        connection_preferences_page.click_rename()
        connection_preferences_page.input_rename("111")
        connection_preferences_page.click_confirm_rename()

    @pytest.mark.swift_2_pro
    def test_cancel_virtual_bluetooth(self, driver: Driver, connection_preferences_page):
        """虚拟蓝牙"""
        connection_preferences_page.click_view_all()
        connection_preferences_page.click_set_btn()

    @pytest.mark.swift_2_pro
    def test_rename_virtual_bluetooth(self, driver: Driver, connection_preferences_page):
        """虚拟蓝牙"""
        connection_preferences_page.click_view_all()
        connection_preferences_page.click_set_btn()
        connection_preferences_page.click_rename()
        connection_preferences_page.input_rename("111")
        connection_preferences_page.click_confirm_rename()
