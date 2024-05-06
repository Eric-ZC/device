import time
from datetime import datetime

import pytest
import pytz
from soium import Driver, Keys
from soium.utils.asserts import assert_that
from soium.utils.logger import console
from soium.utils.random import random_number, random_boolean
from soium.utils.retry import retry_attempts

from src.conf import settings

@pytest.mark.skip
def test_screen_timeout(driver: Driver, settings_page, display_page):
    """屏幕超时测试用例"""
    driver.launch_app(*settings.packages.settings)
    console.print("打开设置页")
    settings_page.click_display()
    display_page.click_screen_timeout()
    # assert_that("屏幕超时设置：30秒，1分钟，5分钟，10分钟，30分钟，永不休眠")
    for screen_time_option in [
        "30 seconds",
        "1 minute",
        "5 minutes",
        "10 minutes",
        "30 minutes",
        None,
    ]:
        # display_page.click_screen_timeout()
        display_page.select_screen_timeout(screen_time_option)
        screen_timeout = driver.get_screen_timeout()
        if screen_time_option is None:
            assert_that(screen_timeout / 1000).is_greater_than(604800)
        else:
            value = int(screen_time_option.split(" ")[0])
            if "minute" in screen_time_option:
                value = value * 60
                assert_that(screen_timeout / 1000).is_equal_to(value)