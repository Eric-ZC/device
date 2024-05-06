import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestSound:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swan_1_pro
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    def test_media_volume(self, driver: Driver, settings_page, sound_page):
        """媒体音量"""
        settings_page.click_sound()
        sound_page.drag_media_volume(0)
        sound_page.drag_media_volume(1)
        sounds = driver.get_max_volume_level()
        console.print(sounds)
        assert_that(sounds).is_true()

    @pytest.mark.swan_1_pro
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    def test_notification_volume(self, driver: Driver, settings_page,sound_page):
        """通知音量"""
        settings_page.click_sound()
        sound_page.drag_notification_volume(0)
        sound_page.drag_notification_volume(1)
        sounds = driver.get_max_volume_level()
        console.print(sounds)
        assert_that(sounds).is_true()

    @pytest.mark.swan_1_pro
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    def test_touch_tone_volume(self, driver: Driver, settings_page,sound_page):
        """触摸提示音音量"""
        settings_page.click_sound()
        sound_page.drag_touchu_tone_volume(0)
        sound_page.drag_touchu_tone_volume(1)
        sounds = driver.get_max_volume_level()
        console.print(sounds)

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_media_volume(self, driver: Driver,settings_page, sound_page):
        """媒体音量"""
        settings_page.click_sound_android11()
        sound_page.drag_media_volume(0)
        sound_page.drag_media_volume(1)
        sounds = driver.get_max_volume_level()
        console.print(sounds)
        assert_that(sounds).is_true()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_notification_volume(self, driver: Driver, settings_page,sound_page):
        """通知音量"""
        settings_page.click_sound_android11()
        sound_page.drag_notification_volume(0)
        sound_page.drag_notification_volume(1)
        sounds = driver.get_max_volume_level()
        console.print(sounds)
        assert_that(sounds).is_true()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_touch_tone_volume(self, driver: Driver, settings_page,sound_page):
        """触摸提示音音量"""
        settings_page.click_sound_android11()
        sound_page.drag_touch_tone_volume(0)
        sound_page.drag_touch_tone_volume(1)
        sounds = driver.get_max_volume_level()
        console.print(sounds)
