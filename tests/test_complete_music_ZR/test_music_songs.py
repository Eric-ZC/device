import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestSongs:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        yield
        console.print("\n执行后置操作")

    def test_expand(self):
        """展开详情"""

    def test_add_to_playlist(self):
        """添加到播放列表"""

    def test_view_info(self):
        """查看音乐人信息"""

    def test_share(self):
        """分享"""

    def test_delete(self):
        """删除"""