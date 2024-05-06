import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestVideo:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.file_manager)
        folder_name = "新文件夹"
        for file in settings.path.resources.glob("*"):
            driver.push_file(
                destination_path=str(
                    settings.path.storage.joinpath(folder_name).joinpath(file.name)
                ),
                source_path=file,
            )
        driver.media_scanner_scan_file()
        console.print("启动文件")
        yield
        console.print("\n执行后置操作")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video(self, driver: Driver, files_page):
        """打开视频"""
        files_page.click_menu()
        files_page.click_storage_str("视频")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_play_video(self, driver: Driver, files_page):
        """播放"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.click_photo()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete_video(self, driver: Driver, files_page):
        """删除视频"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.hold_photo()
        files_page.delete_photo()
        files_page.delete_confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_sort_by(self, driver: Driver, files_page):
        """视频排序"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.click_more_options()
        files_page.click_sort_by()
        files_page.sort_by_type(True)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_select_all(self, driver: Driver, files_page):
        """视频全选"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.click_more_options()
        files_page.click_select_all()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_copy_to(self, driver: Driver, files_page):
        """复制到"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.hold_photo()
        files_page.click_more_options()
        files_page.click_copy_to()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_move_to(self, driver: Driver, files_page):
        """移动到"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.hold_photo()
        files_page.click_more_options()
        files_page.click_move_to()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_filter_large_file(self, driver: Driver, files_page):
        """过滤大型文件"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.click_recent_large_files()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_filter_week(self, driver: Driver, files_page):
        """过滤本周"""
        files_page.click_menu()
        files_page.click_storage_str("视频")
        files_page.click_new_folder()
        files_page.click_this_week()