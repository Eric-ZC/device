import time

import pytest
from soium import Driver
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestGallery:


    @pytest.fixture(autouse=True, scope="class")
    def launch_app(self, driver, files_page):
        driver.launch_app(*settings.packages.file_manager)
        folder_name = "新文件夹"
        files_page.click_more_options()
        files_page.click_create_folder()
        files_page.fill_name(folder_name)
        files_page.confirm()
        for file in settings.path.resources.glob("*"):
            driver.push_file(
                destination_path=str(
                    settings.path.storage.joinpath(folder_name).joinpath(file.name)
                ),
                source_path=file,
            )
        driver.media_scanner_scan_file()
        driver.launch_app(*settings.packages.gallery)
        console.print("启动文件")
        yield
        console.print("结束执行")

    @pytest.mark.D4_504_Pro
    def test_launch_gallery_oir(self, driver: Driver, gallery_page):
        """进入图库"""
        assert_that(gallery_page.get_gallery_title().get_text()).is_equal_to("相册")

    @pytest.mark.D4_504_Pro
    def test_view_picture_oir(self, driver: Driver, files_page, gallery_page):
        """浏览图片"""
        time.sleep(5)
        driver.click(0.5,0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        console.print("查看详情")
        time.sleep(2)
        driver.click(0.5, 0.5)
        driver.click(0.5, 0.5)
        driver.back()

    @pytest.mark.D4_504_Pro
    def test_play_video_oir(self, driver: Driver, settings_page,files_page,gallery_page):
        """图库播放视频"""
        for _ in range(5):
            driver.swipe(0.9,0.5,0.3,0.5)
        driver.click(0.5,0.5)
        console.print("点击视频")
        driver.click(0.5, 0.5)
        console.print("视频详情")
        time.sleep(2)
        driver.click(0.5, 0.5)
        console.print("视频播放")
        while True:
            driver.click(0.5, 0.5)
            if gallery_page.view_play_time_bar():
                gallery_page.click_play_time_bar()
                break
            else:
                driver.click(0.5, 0.5)
        driver.click(0.5, 0.5)

    @pytest.mark.D4_504_Pro
    def test_delete_picture_oir(self,driver: Driver, files_page):
        """删除照片"""
        driver.back(count=2)
        driver.swipe_up(count=2,duration=2)




