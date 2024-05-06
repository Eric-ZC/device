import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestCamera:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")

        yield
        console.print("\n执行后置操作")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_rear_camera(self, driver: Driver,settings_page):
        """打开后摄"""
        driver.launch_app(*settings.packages.camera)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_front_camera_photo(self,driver: Driver,camera_page):
        """前摄连续拍照"""
        driver.launch_app(*settings.packages.camera)
        camera_page.switch_camera()
        camera_page.continuous_shooting(10)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_rear_camera_photo(self, driver: Driver, camera_page):
        """后摄连续拍照"""
        driver.launch_app(*settings.packages.camera)
        camera_page.continuous_shooting(10)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_rest_screen(self, driver: Driver, camera_page):
        """相机熄屏唤醒"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_photo()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_continuous_switching(self, driver: Driver, camera_page):
        """连续切换前后摄"""
        driver.launch_app(*settings.packages.camera)
        for _ in range(5):
            camera_page.switch_camera()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_delayed(self, driver: Driver, camera_page):
        """延时"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_camera_mode()
        camera_page.click_setting_btn()
        camera_page.click_self_time_setting()
        camera_page.click_self_time()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_hdr(self, driver: Driver, camera_page):
        """HDR功能"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_hdr()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_volume_keys(self,driver: Driver, camera_page):
        """音量键功能快门"""
        driver.launch_app(*settings.packages.camera)
        camera_page.volume_keys()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_picture_size(self,driver: Driver, camera_page):
        """照片大小"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_camera_mode()
        camera_page.click_setting_btn()
        camera_page.click_picture_size()
        camera_page.click_select_size()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_self_time(self, driver: Driver, camera_page):
        """自拍计时"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_camera_mode()
        camera_page.click_setting_btn()
        camera_page.click_self_time_setting()
        camera_page.click_self_time()

    def test_06(self):
        """触摸拍照"""

    def test_06(self):
        """还原默认设置"""

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_size(self, driver: Driver, camera_page):
        """视频大小"""
        driver.launch_app(*settings.packages.camera)
        # camera_page.switch_video()
        # camera_page.click_camera_mode()
        # camera_page.click_setting_btn()

    def test_06(self):
        """拍摄纯黑色图片"""

    def test_06(self):
        """拍摄纯白色图片"""

    def test_enlarge_reduce(self, driver: Driver, camera_page):
        """放大/缩小"""
        driver.launch_app(*settings.packages.camera)


    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_preview(self,driver: Driver, camera_page):
        """视频预览"""
        driver.launch_app(*settings.packages.camera)
        # camera_page.switch_video()
        # camera_page.click_photo()
        # time.sleep(5)
        # camera_page.click_video_stop()
        # camera_page.click_gallery()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_picture_video(self, driver: Driver, camera_page):
        """录像时拍照"""
        driver.launch_app(*settings.packages.camera)
        # camera_page.switch_video()
        # camera_page.click_photo()
        # time.sleep(5)
        # camera_page.click_picture_video()
        # camera_page.click_video_stop()
        # camera_page.click_gallery()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_enlarge_reduce(self,driver: Driver, camera_page):
        """录像放大/缩小"""
        driver.launch_app(*settings.packages.camera)
        # camera_page.switch_video()
        # camera_page.click_photo()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_hrd(self,driver: Driver, camera_page):
        """HDR功能"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_hdr()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_pciture_size(self,driver: Driver, camera_page):
        """照片大小"""
        driver.launch_app(*settings.packages.camera)
        camera_page.click_camera_mode()
        camera_page.click_setting_btn()
        camera_page.click_picture_size()
        camera_page.click_select_size()

    def test_06(self):
        """自拍计时"""

    def test_06(self):
        """触摸拍照"""

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_video_sized(self,driver: Driver, camera_page):
        """视频大小"""
        driver.launch_app(*settings.packages.camera)
        # camera_page.switch_video()

    def test_06(self):
        """白平衡"""

    def test_06(self):
        """视频预览"""

    def test_06(self):
        """录像时拍照"""

    def test_06(self):
        """拍摄放大/缩小"""