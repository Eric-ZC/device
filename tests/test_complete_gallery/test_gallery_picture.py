import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestPicture:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page,camera_page,files_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.camera)
        for _ in range(3):
            camera_page.click_photo()
        folder_name = "新文件夹"
        for file in settings.path.resources.glob("*"):
            driver.push_file(
                destination_path=str(
                    settings.path.storage.joinpath(folder_name).joinpath(file.name)
                ),
                source_path=file,
            )
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        driver.media_scanner_scan_file()
        console.print("启动文件")
        yield
        console.print("\n执行后置操作")
        driver.clear_app("com.android.gallery3d")
        driver.launch_app(*settings.packages.file_manager)
        files_page.click_menu()
        files_page.click_storage_str("图片")
        files_page.click_camera_folder()
        files_page.click_more_options()
        files_page.click_select_all()
        files_page.delete_photo()
        files_page.delete_confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_switch(self, driver: Driver, gallery_page,camera_page):
        """切换照片"""
        time.sleep(5)
        driver.click(0.5, 0.3)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.clear_app("com.mediatek.camera")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_view(self, driver: Driver, gallery_page):
        """查看照片"""
        driver.launch_app(*settings.packages.gallery)
        time.sleep(3)
        driver.click(0.5, 0.3)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)