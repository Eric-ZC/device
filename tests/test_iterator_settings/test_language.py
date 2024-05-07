import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings



class TestLanguage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page,language_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        settings_page.click_language()
        language_page.click_language_title()
        yield
        console.print("\n执行后置操作")

    @pytest.mark.swift_2_pro
    def test_switch_language_oir(self, driver: Driver, settings_page, language_page):
        """横屏切换语言"""
        # language_page.click_language_title()
        language_page.click_language_btn()
        language_page.click_add_language()
        language_page.click_search_content()
        language_page.switch_language()
        console.print(language_page.get_toolbar_content())
        language_page.switch_language()
