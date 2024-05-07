import pytest
import time
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestDiagnosis:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, launcher_page):
        console.print("\n执行前置操作")
        yield
        console.print("\n执行后置操作")

    @pytest.mark.swift_2_pro
    def test_network(self, driver:Driver, diagnosis_page, notification_panel):
        """网络测试"""
        driver.launch_app(*settings.packages.diagnosis)
        diagnosis_page.click_network_mian()
        diagnosis_page.click_network_btn()
        diagnosis_page.get_network_speed()
        console.print(diagnosis_page.get_network_speed())

    @pytest.mark.swift_2_pro
    def test_voice(self, driver:Driver, diagnosis_page):
        """声音测试"""
        driver.launch_app(*settings.packages.diagnosis)
        diagnosis_page.click_voice_btn()
        diagnosis_page.drag_voice_bar(0)
        diagnosis_page.drag_voice_bar(1)
        diagnosis_page.click_voice_test()

    @pytest.mark.swift_2_pro
    def test_screen(self, driver:Driver, diagnosis_page):
        """显示器"""
        driver.launch_app(*settings.packages.diagnosis)
        diagnosis_page.click_display_btn()  # 后续需要增加全屏的判断
        diagnosis_page.click_lcd_btn()
        for _ in range(5):
            driver.click(0.5, 0.5)
        diagnosis_page.display_test()
