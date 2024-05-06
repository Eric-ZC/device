import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestArtists:

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

    def test_artists(self, music_page):
        """音乐人播放"""
        music_page.click_artists()
        music_page.click_artists_list_zr()
        music_page.click_artists_detail_zr()
        music_page.music_play_zr()

    def test_add_to_list(self, music_page):
        """添加到播放列表"""
        music_page.click_artists()
        music_page.click_artists_list_zr()
        music_page.music_albums_options_zr()
        status = music_page.options_expand_zr()
        assert_that(status).is_equal_to(True)
