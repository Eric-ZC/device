import time
import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestWiFi:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page,reset_wlan_network_page):
        console.print("\n执行前置操作")
        driver.switch_wifi(True)

        yield
        console.print("\n执行后置操作")
        # driver.launch_app(*settings.packages.settings)
        # settings_page.click_system()
        # reset_wlan_network_page.click_reset_options()
        # reset_wlan_network_page.reset_wlan_network_bluetooth()
        # reset_wlan_network_page.click_reset_setting()
        # reset_wlan_network_page.click_exec_reset()

    @pytest.mark.swift_2_pro
    def test_connect_WiFi(self, driver: Driver,
                          notification_panel,
                          settings_page,
                          network_page,
                          wifi_page,
                          network_details_page,
                          reset_wlan_network_page):
        """连接WiFi"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

        wifi_list = {"yimin": {"Neostra-admin": "ad@666999"},
                     "imin": {"Neostra-VIP": "vip999999"}
                     }[driver.get_brand()]
        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi()
        wifi_page.get_wifi(*wifi_list)
        wifi_page.fill_password(*wifi_list.values())
        driver.press_keycode(Keys.ENTER)
        ssid = driver.get_current_ssid()

    @pytest.mark.swift_2_pro
    def test_view_wifi_info(self, driver: Driver, wifi_page, settings_page, network_page):
        """查看wifi信息"""
        wifi_list = {"yimin": {"Neostra-admin": "ad@666999"},
                     "imin": {"Neostra-VIP": "vip999999"}
                     }[driver.get_brand()]
        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi()
        wifi_page.get_wifi(*wifi_list)

    @pytest.mark.swift_2_pro
    def test_wifi_without_(self,driver: Driver,wifi_page, settings_page, network_page,reset_wlan_network_page):
        """添加无密码wifi"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi()
        time.sleep(5)
        wifi_page.get_wifi("AA_2.4")
        time.sleep(5)
        ssid = driver.get_current_ssid()
        # console.print(ssid)
        # assert_that(ssid, f"Actual value '{ssid}' is not equal to expected value '{'中兴'}'").is_equal_to("中兴")

        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

