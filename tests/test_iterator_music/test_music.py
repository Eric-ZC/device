import pytest
from soium import Driver
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestMusic:

    @pytest.fixture(autouse=True, scope="class")
    def launch_app(self, driver,files_page):
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
        driver.launch_app(*settings.packages.music)
        console.print("启动文件")
        # yield

    @pytest.mark.android11
    @pytest.mark.D4_504
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    @pytest.mark.swan_1_pro
    def test_play_music(self,driver: Driver, music_page):
        """播放音乐"""
        music_page.click_songs()
        music_page.list_click()
        music_page.click_next()
        music_page.click_prev()
        music_page.click_pause()

    @pytest.mark.android11
    @pytest.mark.D4_504
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    @pytest.mark.swan_1_pro
    def test_resting_screen(self,driver: Driver, music_page):
        """熄屏播放"""
        driver.launch_app(*settings.packages.music)
        music_page.click_songs()
        music_page.list_click()
        music_page.resting_screen()