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

    @pytest.mark.D4_504_Pro
    def test_network_oir(self, driver:Driver, diagnosis_page,notification_panel):
        """网络测试"""
        driver.launch_app(*settings.packages.diagnosis_oir)
        diagnosis_page.click_network_icon()
        diagnosis_page.click_network_btn()
        for attempt in retry_attempts(timeout=300):
            with attempt:
                diagnosis_page.get_speed_text_oir()
        console.print(diagnosis_page.get_speed_text_oir())

    @pytest.mark.D4_504_Pro
    def test_voice_oir(self, driver:Driver, diagnosis_page):
        """声音测试"""
        driver.launch_app(*settings.packages.diagnosis_oir)
        diagnosis_page.click_vocie_icon()
        diagnosis_page.drag_voice_bar_oir(0)
        diagnosis_page.drag_voice_bar_oir(1)
        driver.back()

    @pytest.mark.D4_504_Pro
    def test_screen_oir(self, driver:Driver, diagnosis_page):
        """显示器"""
        driver.launch_app(*settings.packages.diagnosis_oir)
        diagnosis_page.click_display_icon()  # 后续需要增加全屏的判断
        diagnosis_page.click_start_lcd_btn_oir()
        for _ in range(5):
            driver.click(0.5, 0.5)
        driver.back()