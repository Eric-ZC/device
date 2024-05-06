import time

import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestLaucher:

    @pytest.mark.D4_504_Pro
    def test_launch_gallery(self, driver:Driver, launcher_page):
        """创建桌面"""
        time.sleep(5)
        driver.press_keycode(Keys.HOME)
        launcher_page.move_last_app()

    @pytest.mark.D4_504_Pro
    def test_widgets(self, driver:Driver, launcher_page):
        """微件"""
        launcher_page.hold_wigdet()
        time.sleep(2)
        driver.back()

    @pytest.mark.D4_504_Pro
    def test_delete_desktop(self, driver:Driver , launcher_page):
        """删除桌面"""
        driver.back()
        launcher_page.delete_desktop()