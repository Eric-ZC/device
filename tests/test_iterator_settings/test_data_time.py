import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings



class TestDataTime:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page, data_time_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        data_time_page.click_data_time()

        yield
        console.print("\n执行后置操作")
        driver.close_app()

    @pytest.mark.D4_504_Pro
    def test_select_zone_oir(self, driver: Driver, data_time_page):
        """D4-504-Pro选择时区"""
        data_time_page.click_time_zone_btn_oir()
        data_time_page.click_zone()
        data_time_page.search_src()
        content = data_time_page.zone_result()
        assert_that(content).is_equal_to("英国")

    @pytest.mark.D4_504_Pro
    def test_select_zone_local_oir(self, driver: Driver, data_time_page):
        """D4-504-Pro手动设置时区地区验证"""
        data_time_page.click_time_zone_btn_oir()
        data_time_page.click_zone()
        data_time_page.search_src()
        content = data_time_page.current_time_zone()
        assert_that(content).contains("伦敦")

