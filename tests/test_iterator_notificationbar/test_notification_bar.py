import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestNotificationBar:

    # @pytest.fixture(autouse=True, scope="class")
    # def launch_app(self, driver:Driver,notification_panel):
    #     notification_panel.expand(2)
    #     # driver.get_packages()
    #     # driver.launch_app(*settings.packages.music)
    #     # console.print("启动文件")
    #     # yield

    @pytest.mark.swift_2_pro
    def test_adjust_luminance(self,driver: Driver, notification_panel):
        """调整亮度"""
        notification_panel.expand(2)
        notification_panel.drag_brightness_bar(0)
        notification_panel.drag_brightness_bar(1)

    @pytest.mark.swift_2_pro
    def test_turn_on_off(self,driver: Driver, notification_panel):
        """通知栏开启/关闭"""
        notification_panel.expand(2)
        notification_panel.click_wifi()
        notification_panel.switch_wlan()
        notification_panel.click_done_bar()
        notification_panel.click_bluetooth()

    @pytest.mark.swift_2_pro
    def test_screen_recording(self, driver: Driver, notification_panel):
        """录制屏幕"""
        notification_panel.click_record()
        notification_panel.click_start()
        notification_panel.expand(1)
        notification_panel.click_stop()

    @pytest.mark.swift_2_pro
    def test_screen_shot(self,driver: Driver, notification_panel):
        """截图屏幕"""
        notification_panel.expand(1)
        notification_panel.click_screenshot()
