import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestFunction:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        yield
        console.print("\n执行后置操作")

    @pytest.mark.run(order=-1)
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_reboot(self, driver: Driver):
        """重启设备"""
        driver.reboot()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_swip_screen(self, driver: Driver, security_page):
        """滑动锁屏"""
        security_page.click_screen_lock()
        security_page.select_slide_lock()
        security_page.lock_screen()
        driver.swipe_up(count=3, duration=8)
        status = security_page.get_screen_lock_status()
        console.print(status)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_re(self, driver: Driver, security_page, notification_panel):
        """通知"""
        security_page.click_screen_lock()
        security_page.select_slide_lock()
        security_page.lock_screen()

    def test_re(self):
        """通知"""

    def test_re(self):
        """状态栏"""

    def test_re(self):
        """快捷设置菜单"""

    def test_re(self):
        """桌面"""

    def test_re(self):
        """桌面"""

    def test_re(self):
        """微件"""

    def test_re(self):
        """微件"""

    def test_re(self):
        """虚拟按键“Back”键"""

    def test_re(self):
        """虚拟按键“Home”键"""

    def test_re(self):
        """虚拟按键“Recent”键"""

    def test_re(self):
        """虚拟按键“Recent”键"""

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_app_shoot(self, driver: Driver, gestures_page):
        """多任务页面截屏"""
        gestures_page.click_recent_apps_btn()
        gestures_page.screen_shot()
        gestures_page.screen_shot_share()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_background_application(self, driver: Driver, gestures_page):
        """后台应用"""
        gestures_page.click_recent_apps_btn()
        driver.swipe_up(count=2,duration=5)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_screen_shoot(self, driver: Driver, notification_panel):
        """截图屏幕"""
        notification_panel.expand(2)
        notification_panel.click_screenshot()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_clearn_app_up(self, driver: Driver, gestures_page):
        """全部清除"""
        gestures_page.click_recent_apps_btn()
        for attempt in retry_attempts(timeout=30):
            with attempt:
                gestures_page.clean_app_up()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_volume_control(self, driver: Driver):
        """音量调节"""
        driver.press_keycode(Keys.VOLUME_UP)
        driver.press_keycode(Keys.VOLUME_DOWN)
