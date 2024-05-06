import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts
from appium.webdriver.common.touch_action import TouchAction

from src.conf import settings


class TestEntire:

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
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        console.print("启动文件")
        yield
        console.print("\n执行后置操作")
        driver.clear_app("com.android.gallery3d")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_swip(self, driver: Driver, gallery_page):
        """滑动查看"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.swipe(0.9, 0.5, 0.3, 0.5)


    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """编辑图片"""
        driver.launch_app(settings.packages.gallery)

    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """向左旋转"""
        driver.launch_app(settings.packages.gallery)

    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """向右旋转"""
        driver.launch_app(settings.packages.gallery)

    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """剪裁"""
        driver.launch_app(settings.packages.gallery)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """将图片设置为"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        gallery_page.click_more_options()
        gallery_page.click_set_wallpaper()
        gallery_page.click_wallpaper_confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """详细信息"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        gallery_page.click_more_options()
        gallery_page.click_detail()


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """查看详情"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        gallery_page.click_more_options()
        gallery_page.click_detail()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """左右滑动"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.3, 0.5, 0.9, 0.5)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """双击图片"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        for _ in range(2):
            driver.click(0.5, 0.5)

    @pytest.mark.skip
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_zoom(self, driver: Driver, gallery_page):
        """放大/缩小图片"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        height = gallery_page.size_screen()["height"]
        width = gallery_page.size_screen()["width"]

        x0 = height / 2
        y0 = width / 2

        x1 = height / 4
        y1 = width / 4

        x2 = height / 2 + height / 4
        y2 = width / 2 + width / 4

        driver.multitouch()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_voice(self, driver: Driver, gallery_page):
        """滑动删除"""
        driver.click(0.5, 0.5)
        gallery_page.click_camera_bar()
        driver.click(0.5, 0.5)
        time.sleep(2)
        driver.back()
        driver.swipe_up(count=2,duration=2)
