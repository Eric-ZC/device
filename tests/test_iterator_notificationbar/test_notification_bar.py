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
    @pytest.mark.swift_1_pro
    def test_adjust_luminance(self,driver: Driver, notification_panel):
        """调整亮度"""
        notification_panel.expand(2)
        notification_panel.drag_brightness_bar(0)
        notification_panel.drag_brightness_bar(1)


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_turn_on_off(self,driver: Driver, notification_panel):
        """通知栏开启/关闭"""
        notification_panel.expand(2)
        notification_panel.click_wifi()
        notification_panel.switch_wlan()
        notification_panel.click_done_bar()
        notification_panel.click_bluetooth()


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_screen_recording(self, driver: Driver, notification_panel):
        """录制屏幕"""

        notification_panel.click_record()
        notification_panel.click_start()
        notification_panel.expand(1)
        notification_panel.click_stop()


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_screen_shot(self,driver: Driver, notification_panel):
        """截图屏幕"""
        notification_panel.expand(1)
        notification_panel.click_screenshot()

    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_adjusting_volume_oir(self,driver: Driver, notification_panel):
        """调整音量"""
        notification_panel.expand(1)
        notification_panel.click_voice_btn()
        notification_panel.drag_notification_volume(0)
        notification_panel.drag_notification_volume(1)
        notification_panel.drag_media_volume(0)
        notification_panel.drag_media_volume(1)
        notification_panel.click_complete_btn()

    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_main_adjust_luminance_oir(self,driver: Driver, notification_panel):
        """调整主屏亮度"""
        notification_panel.expand(1)
        notification_panel.drag_main_brightness_bar(0)
        notification_panel.drag_main_brightness_bar(1)


    @pytest.mark.D4_504_Pro
    def test_secondary_adjust_luminance_oir(self, driver: Driver, notification_panel):
        """调整副屏亮度"""
        notification_panel.expand(1)
        notification_panel.drag_secondary_brightness_bar(0)
        notification_panel.drag_secondary_brightness_bar(1)

    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_turn_on_off_oir(self,driver: Driver, notification_panel):
        """通知栏开启/关闭"""
        notification_panel.expand(1)
        notification_panel.click_wifi()
        notification_panel.switch_wlan()
        notification_panel.click_done_bar()
        notification_panel.click_bluetooth()

    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_screen_recording_oir(self, driver: Driver, notification_panel):
        """录制屏幕"""
        notification_panel.click_record()
        notification_panel.click_start()
        notification_panel.expand(1)
        notification_panel.click_stop()

    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_screen_shot_oir(self,driver: Driver, notification_panel):
        """截图屏幕"""
        notification_panel.expand(1)
        notification_panel.click_screenshot()
        driver.press_keycode(Keys.HOME)

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_volume_control(self,driver: Driver, notification_panel):
        """音量调整"""
        notification_panel.expand(2)
        notification_panel.click_voice_btn()
        notification_panel.drag_media_volume(0)
        notification_panel.drag_media_volume(1)
        notification_panel.drag_notification_volume(0)
        notification_panel.drag_notification_volume(1)
        notification_panel.click_complete_btn()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_main_luminance_oir(self,driver: Driver, notification_panel):
        """调整主屏亮度"""
        notification_panel.expand(2)
        notification_panel.drag_main_brightness_bar11(0)
        notification_panel.drag_main_brightness_bar11(1)

    # @pytest.mark.android11
    @pytest.mark.D4_504
    def test_secondary_luminance_oir(self, driver: Driver, notification_panel):
        """调整副屏亮度"""
        notification_panel.expand(2)
        notification_panel.drag_secondary_brightness_bar11(0)
        notification_panel.drag_secondary_brightness_bar11(1)

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_screen_recording11(self, driver: Driver, notification_panel):
        """录制屏幕"""
        notification_panel.click_record()
        notification_panel.click_start()
        notification_panel.expand(1)
        notification_panel.click_stop()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_screen_shot11(self, driver: Driver, notification_panel):
        """截图屏幕"""
        notification_panel.expand(2)
        notification_panel.click_screenshot()
        driver.press_keycode(Keys.HOME)

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_turn_on_off_oir(self,driver: Driver, notification_panel):
        """通知栏开启/关闭"""
        notification_panel.expand(2)
        notification_panel.switch_wlan()
        notification_panel.click_bluetooth()
        notification_panel.switch_wlan()