import pytest
from soium import Driver
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestFiles:

    @pytest.fixture(autouse=True, scope="class")
    def launch_app(self, driver, files_page):
        driver.launch_app(*settings.packages.file_manager)
        console.print("启动文件")
        files_page.click_more_options()
        files_page.click_create_folder()
        files_page.fill_name("test01")
        files_page.confirm()
        # yield

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_enter_folder(self, driver: Driver, files_page):
         """进入文件夹"""
         driver.launch_app(*settings.packages.file_manager)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete_folder(self, driver: Driver, files_page):
        """删除文件"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.hold_floder()
        files_page.click_delete()
        files_page.confirm()
        # driver.media_scanner_scan_file()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_rename_folder(self, driver: Driver, files_page):
        """重命名文件"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_more_options()
        files_page.click_create_folder()
        files_page.fill_name("test01")
        files_page.confirm()
        files_page.hold_floder()
        files_page.click_more_options()
        files_page.click_rename()
        files_page.fill_name("test02")
        files_page.confirm()

    @pytest.mark.android11
    @pytest.mark.D4_504
    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_enter_folder_oir(self, driver: Driver, files_page):
         """进入文件夹"""
         driver.launch_app(*settings.packages.file_manager)

    @pytest.mark.android11
    @pytest.mark.D4_504
    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_delete_folder_oir(self, driver: Driver, files_page):
        """删除文件"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.hold_floder()
        files_page.click_delete()
        files_page.confirm()
        # driver.media_scanner_scan_file()

    @pytest.mark.android11
    @pytest.mark.D4_504
    @pytest.mark.swan_1_pro
    @pytest.mark.D4_504_Pro
    def test_rename_folder_oir(self, driver: Driver, files_page):
        """重命名文件"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_more_options()
        files_page.click_create_folder()
        files_page.fill_name("test01")
        files_page.confirm()
        files_page.hold_floder()
        files_page.click_more_options()
        files_page.click_rename()
        files_page.fill_name("test02")
        files_page.confirm()