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
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        yield
        console.print("\n执行后置操作")

    def test_view_list(self):
        """查看默认播放列表"""

    def test_expand(self):
        """查看展开内容"""

    def test_random_play(self):
        """随机播放全部歌曲"""

    def test_recent_play(self):
        """最近添加歌曲"""

    def test_list_expand(self):
        """列表展开"""

    def test_new_palylists(self):
        """新增播放列表"""

    def test_folder(self):
        """文件夹"""