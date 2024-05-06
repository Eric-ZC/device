import pytest
import time
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
        # driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_del(self, driver: Driver,calculator_page):
        """DEL"""
        for i in range(1, 7):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("删除")
        text = calculator_page.get_input()
        assert_that(text).is_equal_to("12,345")
        calculator_page.hold_press_sym_btn("删除", duration=1)
        input_content = calculator_page.get_result()
        assert_that(input_content).is_equal_to("")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_clr(self, driver: Driver, calculator_page):
        """CLR"""
        calculator_page.click_num_btn("1")
        calculator_page.click_sym_btn("加")
        calculator_page.click_num_btn("1")
        calculator_page.click_sym_btn("等于")
        calculator_page.hold_press_sym_btn("清除")
        text = calculator_page.get_result()
        assert_that(text).is_equal_to("")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_operation(self, driver: Driver, calculator_page):
        """运算"""
        calculator_page.click_num_btn("1")
        buttons = [("加", "1"), ("减", "1"), ("×", "1"), ("除", "1"), ("等于", None)]
        for button in buttons:
            try:
                calculator_page.click_sym_btn(button[0])
                if button[1] is not None:
                    calculator_page.click_num_btn(button[1])
            except Exception as e:
                    print(f"Failed to click button: {button[0]} - {e}")
        text = calculator_page.get_result()
        assert_that(text).is_equal_to("1")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_operation_01(self, driver: Driver, calculator_page):
        """运算"""
        for i in range(1, 4):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("加")
        for i in range(4, 7):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("等于")
        text = calculator_page.get_result()
        assert_that(text).is_equal_to("579")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_operation_02(self, driver: Driver, calculator_page):
        """运算"""
        for i in range(9, 6, -1):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("减")
        for i in range(6, 3, -1):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("等于")
        text = calculator_page.get_result()
        assert_that(text).is_equal_to("333")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_operation_03(self, driver: Driver, calculator_page):
        """运算"""
        for i in range(1, 4):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("×")
        calculator_page.click_num_btn("5")
        calculator_page.click_sym_btn("等于")
        text = calculator_page.get_result()
        assert_that(text).is_equal_to("615")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_operation_04(self, driver: Driver, calculator_page):
        """运算"""
        for i in range(4, 7):
            calculator_page.click_num_btn(i)
        calculator_page.click_sym_btn("除")
        calculator_page.click_num_btn("3")
        calculator_page.click_sym_btn("等于")
        text = calculator_page.get_result()
        assert_that(text).is_equal_to("152")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_inv(self, driver: Driver, calculator_page):
        """INV"""
        calculator_page.click_func_btn("INV")
        arcsin_veiw = calculator_page.arcsin_veiw()
        assert_that(arcsin_veiw,"反正弦").is_equal_to("sin⁻¹")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_RAD_DEG(self,driver: Driver, calculator_page):
        """RAD、DEG"""
        calculator_page.click_func_btn("DEG")
        deg_veiw = calculator_page.deg_veiw()
        assert_that(deg_veiw,"").is_equal_to("DEG")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_percent(self, driver: Driver, calculator_page):
        """%"""
        calculator_page.click_num_btn("1")
        calculator_page.click_num_btn("0")
        calculator_page.click_func_btn("%")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        assert_that(res).is_equal_to("0.1")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_sin(self, driver: Driver, calculator_page):
        """sin"""
        calculator_page.click_func_btn("sin")
        calculator_page.click_num_btn("3")
        calculator_page.click_num_btn("0")
        calculator_page.click_sym_btn("除")
        calculator_page.click_num_btn("9")
        calculator_page.click_num_btn("0")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_cos(self, driver: Driver, calculator_page):
        """cos"""
        calculator_page.click_func_btn("cos")
        calculator_page.click_num_btn("6")
        calculator_page.click_num_btn("0")
        calculator_page.click_sym_btn("除")
        calculator_page.click_num_btn("9")
        calculator_page.click_num_btn("0")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_tan(self, driver: Driver, calculator_page):
        """tan"""
        calculator_page.click_func_btn("tan")
        calculator_page.click_num_btn("4")
        calculator_page.click_num_btn("5")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_ln(self, driver: Driver, calculator_page):
        """In"""
        calculator_page.click_func_btn("ln")
        calculator_page.click_func_btn("e")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_log(self, driver: Driver, calculator_page):
        """log"""
        calculator_page.click_func_btn("log")
        calculator_page.click_num_btn("1")
        calculator_page.click_num_btn("0")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_factorial(self, driver: Driver, calculator_page):
        """！"""
        calculator_page.click_num_btn("1")
        calculator_page.click_num_btn("0")
        calculator_page.click_func_btn("!")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_pi(self, driver: Driver, calculator_page):
        """π"""
        calculator_page.click_func_btn("π")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_e(self,driver: Driver, calculator_page):
        """e"""
        calculator_page.click_func_btn("e")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_pow(self,driver: Driver, calculator_page):
        """∧"""
        calculator_page.click_num_btn("1")
        calculator_page.click_num_btn("0")
        calculator_page.click_func_btn("^")
        calculator_page.click_num_btn("2")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_bracket(self,driver: Driver, calculator_page):
        """（）"""
        calculator_page.click_func_btn("(")
        calculator_page.click_num_btn("1")
        calculator_page.click_num_btn("0")
        calculator_page.click_sym_btn("减")
        calculator_page.click_num_btn("5")
        calculator_page.click_func_btn(")")
        calculator_page.click_sym_btn("×")
        calculator_page.click_num_btn("2")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_sqrt(self,driver: Driver, calculator_page):
        """√"""
        calculator_page.click_func_btn("√")
        calculator_page.click_num_btn("4")
        calculator_page.click_sym_btn("等于")
        res = calculator_page.get_result()
        console.print(res)

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_history(self,driver: Driver, calculator_page):
        """历史记录"""
        calculator_page.click_more()
        calculator_page.click_history()
        text = calculator_page.view_history_record()
        console.print(text)
        # assert_that(text).is_equal_to("历史记录")

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_more(self, driver: Driver, calculator_page):
        """更多"""
        calculator_page.click_more()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_fun_factory(self,driver: Driver, calculator_page):
        """工程模式"""
        calculator_page.click_num_btn(".")
        calculator_page.click_sym_btn("×")
        calculator_page.click_num_btn("3")
        calculator_page.click_num_btn("3")
        calculator_page.click_sym_btn("加")
