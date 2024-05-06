import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestAlbums:

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
        driver.launch_app(*settings.packages.music)
        console.print("启动文件")
        yield
        console.print("\n执行后置操作")

    def test_select_songs(self, music_page):
        """点击任一歌曲"""
        music_page.click_albums()
        music_page.click_albums_list_zr()
        music_page.music_play_zr()

    def test_select_songs(self, music_page):
        """歌曲列表播放"""

    def test_select_songs(self, music_page):
        """添加到播放列表"""

    def test_select_songs(self, music_page):
        """全部随机播放"""

    def test_select_songs(self, music_page):
        """删除"""