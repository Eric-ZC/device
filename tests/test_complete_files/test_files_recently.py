import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestRecently:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        # driver.launch_app(*settings.packages.file_manager)
        yield
        console.print("\n执行后置操作")


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_recent(self, driver: Driver, files_page):
        """打开最近"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_recent_switch_view(self, driver: Driver, files_page):
        """最近切换视角"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_switch_views()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_selected(self, driver: Driver, files_page):
        """选中取消"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_first_file()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_share(self, driver: Driver, files_page):
        """分享"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_share()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_ways(self, driver: Driver, files_page):
        """打开方式"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_recent_more()
        files_page.click_open_ways()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_sort_by(self, driver: Driver, files_page):
        """排列方式"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_recent_more()
        files_page.click_sort_by()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_select_all(self, driver: Driver, files_page):
        """全选"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_recent_more()
        files_page.click_select_all()


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_copy(self, driver: Driver, files_page):
        """复制"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_recent_more()
        files_page.click_copy_to()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_get_info(self, driver: Driver, files_page):
        """获取信息"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_first_file(5)
        files_page.click_recent_more()
        files_page.click_get_info()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_image(self, driver: Driver, files_page):
        """图片"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_recent_image()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, files_page):
        """音频"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_recent_voice()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video(self, driver: Driver, files_page):
        """视频"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_recent_video()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_file(self, driver: Driver, files_page):
        """文档"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_recent_file()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_large_files(self, driver: Driver, files_page):
        """大型文档"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        files_page.click_recent_large_files()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_this_week(self, driver: Driver, files_page):
        """本周"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_recent()
        # files_page.click_recent_this_week()