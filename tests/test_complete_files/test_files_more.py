import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestMore:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        # driver.launch_app(*settings.packages.file_manager)
        yield
        console.print("\n执行后置操作")


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_launcher(self, driver: Driver, files_page):
        """打开应用"""
        driver.launch_app(*settings.packages.file_manager)


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_device_name(self, driver: Driver, files_page):
        """设备名称"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.get_devices_name()

    @pytest.mark.skip("步骤更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_search_content (self, driver: Driver, files_page):
        """查询搜索"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_search()
        files_page.search("Download")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_create_folder(self,driver: Driver, files_page):
        """新建文件夹"""
        driver.launch_app(*settings.packages.file_manager)
        console.print("启动文件")
        files_page.click_more_options()
        files_page.click_create_folder()
        files_page.fill_name("test01")
        files_page.confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_sort_by(self, driver: Driver, files_page):
        """排序方式"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_more_options()
        files_page.click_sort_by()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_select_all(self, driver: Driver, files_page):
        """全选"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_more_options()
        files_page.click_select_all()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_hide_folder(self, driver: Driver, files_page):
        """显示隐藏文件"""
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_more_options()
        files_page.click_show_hidden_files()
