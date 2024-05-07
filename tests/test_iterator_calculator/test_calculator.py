import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestCalculator:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.calculator)
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    def test_base_operate(self, driver: Driver, calculator_page):
        """数字输入"""
        for i in range(9, 0, -1):
            calculator_page.click_num_btn(i)
        calculator_page.click_num_btn(".")
        for _ in range(0, 2):
            calculator_page.click_num_btn(_)
        calculator_page.click_sym_btn("删除")
        buttons = [("除", "1"), ("×", "1"), ("加", "1"), ("减", "1"), ("等于", None)]
        for button in buttons:
            try:
                calculator_page.click_sym_btn(button[0])
                if button[1] is not None:
                    calculator_page.click_num_btn(button[1])
            except Exception as e:
                print(f"Failed to click button: {button[0]} - {e}")
        item = calculator_page.get_result()
        assert_that(item).is_equal_to("987,654,321")
        calculator_page.hold_press_sym_btn("清除")

    @pytest.mark.swift_2_pro
    def test_factory_mode(self,driver:Driver, calculator_page):
        """工厂模式编号"""
        calculator_page.click_num_btn(".")
        calculator_page.click_sym_btn("×")
        for _ in range(2):
            calculator_page.click_num_btn("3")
        calculator_page.click_sym_btn("加")
        # ele = calculator_page.factory_mode()
        # assert_that(ele).is_equal_to(True)












