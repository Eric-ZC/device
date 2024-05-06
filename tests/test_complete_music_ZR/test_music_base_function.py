import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestBaseFunction:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page,files_page):
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
        driver.launch_app(*settings.packages.music)
        console.print("启动文件")
        yield
        console.print("\n执行后置操作")

    @pytest.mark.zr
    def test_search(self, music_page):
        """搜索功能"""
        music_page.click_search_rz()

    @pytest.mark.zr
    def test_settings_equalizer(self, music_page):
        """设置均衡器"""
        music_page.click_settings_zr()
        music_page.click_equalizer_zr()
        music_page.turn_on_equalizer_zr()

    @pytest.mark.zr
    def test_settings_scheduled(self, music_page):
        """设置定时关闭"""
        music_page.click_settings_zr()
        music_page.turn_on_scheduled_zr()
        music_page.scheduled_setting_zr()
        status = music_page.done_toast_zr()
        assert_that(status).is_equal_to(True)

    @pytest.mark.zr
    def test_quits_application(self, music_page):
        """退出应用"""
        music_page.click_more_options_zr()
        music_page.click_exit_zr()

    @pytest.mark.zr
    def test_shortcut_menu_switch(self, music_page):
        """快捷菜单切换歌曲"""


    def test_shortcut_menu_exit(self):
        """快捷菜单关闭歌曲"""
        pass

    def test_background(self):
        """后台播放"""
        pass

    def test_home(self):
        """返回桌面"""
        pass

    def test_back(self):
        """返回上一级"""
        pass

    def test_menu(self):
        """菜单任务"""
        pass