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
        driver.launch_app(*settings.packages.gallery)
        time.sleep(5)
        yield
        console.print("\n执行后置操作")
        driver.clear_app("com.android.gallery3d")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_switch_video(self, driver: Driver, gallery_page):
        """切换视频"""
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_share(self, driver: Driver, gallery_page):
        """蓝牙分享"""
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        gallery_page.click_share()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delete(self, driver: Driver, gallery_page):
        """删除视频"""
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        gallery_page.click_more_options()
        gallery_page.click_delete()
        gallery_page.click_delete_confirm()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_detail_info(self, driver: Driver, gallery_page):
        """详细信息"""

        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        gallery_page.click_more_options()
        gallery_page.click_detail()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_swip(self, driver: Driver, gallery_page):
        """向左/右滑动"""

        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.3, 0.5, 0.9, 0.5)

    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_lock(self, driver: Driver, gallery_page):
        """锁定"""
        driver.launch_app(settings.packages.gallery)

    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_screen(self, driver: Driver, gallery_page):
        """截图"""
        driver.launch_app(settings.packages.gallery)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_play_bar(self, driver: Driver, gallery_page):
        """播放进度条"""

        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        while True:
            driver.click(0.5, 0.5)
            if gallery_page.view_play_time_bar():
                gallery_page.click_play_time_bar()
                break
            else:
                driver.click(0.5, 0.5)
        driver.click(0.5, 0.5)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_pause(self, driver: Driver, gallery_page):
        """视频暂停"""

        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        while True:
            driver.click(0.5, 0.5)
            if gallery_page.view_play_btn():
                break
            else:
                driver.click(0.5, 0.5)

    @pytest.mark.skip("系统更新")
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fill_screen(self, driver: Driver, gallery_page):
        """全屏"""
        driver.launch_app(*settings.packages.gallery)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_back(self, driver: Driver, gallery_page):
        """返回键"""
        driver.click(0.5, 0.5)
        gallery_page.switch_styles()
        driver.click(0.5, 0.5)
        for _ in range(4):
            driver.swipe(0.9, 0.5, 0.3, 0.5)
        driver.swipe(0.9, 0.5, 0.3, 0.5)
        while True:
            driver.click(0.5, 0.5)
            if gallery_page.view_play_btn():
                break
            else:
                driver.click(0.5, 0.5)
        driver.back(count=1)