import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestPlayInterface:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        yield
        console.print("\n执行后置操作")

    def test_share(self):
        """分享"""

    def test_options_expand(self):
        """展开"""

    def test_add_to_playlist(self):
        """添加到播放列表"""

    def test_view_singer_info(self):
        """查看音乐人信息"""

    def test_delete(self):
        """删除"""

    def test_settings(self):
        """设置"""

    def test_exit(self):
        """退出"""

    def test_slide_right(self):
        """右滑歌曲封面"""

    def test_songs_expand(self):
        """歌曲展开"""

    def test_slide_left(self):
        """左滑歌曲封面"""

    def test_like(self):
        """标记喜欢音乐"""

    def test_play_mode(self):
        """切换播放模式"""

    def test_play_functions(self):
        """播放功能"""

    def test_progress_bar(self):
        """调整播放"""