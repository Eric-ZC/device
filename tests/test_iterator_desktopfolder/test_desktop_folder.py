import time

import pytest
from soium import Driver
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from soium import Keys
from src.conf import settings


class TestDesktopFolder:

    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self, driver):
        driver.press_keycode(Keys.HOME)

    @pytest.mark.D4_504_Pro
    def test_create_folder_oir(self, driver: Driver, launcher_page):
        """创建文件夹"""
        while True:
            launcher_page.merge_app_oir()
            if launcher_page.folder_name_display():
                break

    @pytest.mark.D4_504_Pro
    def test_rename_folder(self, driver:Driver,launcher_page):
        """重命名文件"""
        launcher_page.click_edit_name()

    @pytest.mark.D4_504_Pro
    def test_delete_folder_oir(self, driver:Driver,launcher_page):
        """删除文件夹"""
        launcher_page.click_folder_adbcd()
        launcher_page.move_folders_app_oir()

