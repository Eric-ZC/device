import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestDownLoad:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page, files_page):
        console.print("\n执行前置操作")
        folder_name = "新文件夹"
        driver.launch_app(*settings.packages.file_manager)
        download_file = "Download"
        for file in settings.path.resources.glob("*"):
            driver.push_file(
                destination_path=str(
                    settings.path.storage.joinpath(download_file).joinpath(folder_name).joinpath(file.name)
                ),
                source_path=file,
            )
        driver.media_scanner_scan_file()
        console.print("启动文件")
        yield
        console.print("\n执行后置操作")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_create_files(self, driver: Driver, files_page):
        """新建文件夹"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_more_options()
        files_page.click_create_folder()
        files_page.fill_name("测试文件夹")
        files_page.confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_bluetooth_share(self, driver: Driver, files_page):
        """蓝牙分享"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_share()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_opens_ways(self, driver: Driver, files_page):
        """打开方式"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_open_ways()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_sort_ways(self, driver: Driver, files_page):
        """排列方式"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_sort_by()
        files_page.sort_by_type(True)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_select_all(self, driver: Driver, files_page):
        """全选"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_select_all()


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_copy_to(self, driver: Driver, files_page):
        """复制到"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_copy_to()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_move_to(self, driver: Driver, files_page):
        """移至"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_move_to()
    #
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_compress(self, driver: Driver, files_page):
        """压缩"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_compress()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_rename(self, driver: Driver, files_page):
        """重命名"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_rename()
        files_page.fill_name("test0001")
        files_page.confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_get_info(self, driver: Driver, files_page):
        """获取信息"""
        files_page.click_menu()
        files_page.click_storage_str("下载")
        files_page.click_recent_image()
        files_page.click_first_file(5)
        files_page.click_more_options()
        files_page.click_get_info()