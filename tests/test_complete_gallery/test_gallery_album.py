import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestAlbum:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
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
        driver.clear_app("com.android.gallery3d")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_open_gallery(self, driver: Driver, gallery_page):
        """打开图库"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.skip("系统跟新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_hide_lcoal(self, driver: Driver, files_page):
        """隐藏的相册"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.skip("系统跟新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_local(self, driver: Driver, files_page):
        """显示本地相册"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.skip("系统跟新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_setting(self, driver: Driver, files_page):
        """设置"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_slideshow(self, driver: Driver, gallery_page):
        """播放幻灯片"""

        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        gallery_page.click_more_options()
        gallery_page.click_play_slideshow()

    @pytest.mark.skip("系统跟新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_slideshow_music(self, driver: Driver, gallery_page):
        """幻灯片音乐"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_wallpaper(self, driver: Driver, gallery_page):
        """设置为壁纸"""
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        gallery_page.click_more_options()
        gallery_page.click_set_wallpaper()
        gallery_page.click_wallpaper_confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_share(self, driver: Driver, gallery_page):
        """分享"""
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        gallery_page.click_share()

    @pytest.mark.skip("系统跟新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_edit(self, driver: Driver, files_page):
        """编辑图片"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete(self, driver: Driver, gallery_page):
        """删除图片"""
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.swipe_up(count=2, duration=2)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_info(self, driver: Driver, gallery_page):
        """查看图片详情"""
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        gallery_page.click_more_options()
        gallery_page.click_detail()