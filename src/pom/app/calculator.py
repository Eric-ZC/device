from src.deps import *


class Calculator(BasePage):
    """
    计算器
    """
    class loc:
        @staticmethod
        def num_btn(name: str = None, exact: bool = True, description: str = None):
            return Selector(
                XPath(id="com.android.calculator2:id/pad_numeric").join(
                    "android.widget.Button", has_text=name, exact=exact
                ),
                description=description or "数字按钮",
            )
        zero = num_btn("0", description="0")
        one = num_btn("1", description="1")
        two = num_btn("2", description="2")
        three = num_btn("3", description="3")
        four = num_btn("4", description="4")
        five = num_btn("5", description="5")
        six = num_btn("6", description="6")
        seven = num_btn("7", description="7")
        eight = num_btn("8", description="8")
        nine = num_btn("9", description="9")
        dec_point = num_btn(".", description='.')



        @staticmethod
        def sym_btn(name: str = None, exact: bool = True, description: str = None):
            return Selector(XPath(id="com.android.calculator2:id/pad_operator").join(
                    "android.widget.Button", has_content=name,exact=exact
                ),
                description=description or "符号按钮",
            )

        add = sym_btn("加", description="+")
        sub = sym_btn("减", description="-")
        mul = sym_btn("×", description="×")
        div = sym_btn("除", description="÷")
        dele = sym_btn("删除", description="DEL")
        clr = sym_btn("清除", description="CLR")
        eq = num_btn("等于", description="=")


        @staticmethod
        def func_btn(name: str = None, exact: bool = True, description: str = None):
            return Selector(XPath(id="com.android.calculator2:id/pad_advanced").join(
                    "android.widget.Button", has_text=name, exact=exact
                ),
                description=description or "函数按钮",
            )

        perc = func_btn("%", description="%")
        sin = func_btn("sin", description="sin")
        arcsin = func_btn("sin⁻¹", description="sin⁻¹")
        cos = func_btn("cos", description="cos")
        tan = func_btn("tan", description="tan")
        ln = func_btn("ln", description="ln")
        log = func_btn("log", description="log")
        fact = func_btn("!", description="!")
        pi = func_btn("π", description="圆周率")
        e = func_btn("e", description="e")
        pow = func_btn("^", description="次方")
        lparen = func_btn("(", description="左括号")
        rparen = func_btn(")", description="右括号")
        sqrt = func_btn("√", description="根号")
        deg = func_btn("DEG", description="DEG")
        inv = func_btn("INV", description="INV")
        rad = func_btn("RAD", description="RAD")

        err_info = Selector(XPath(has_text="Bad expression"),description="错误输入")
        result = Selector(XPath(id="com.android.calculator2:id/result"), description="运算结果")
        # input = Selector(XPath(id="com.android.calculator2:id/formula_container"), description="输入内容")
        input = Selector(XPath(id="com.android.calculator2:id/formula"), description="输入内容")
        empty_result = Selector(XPath(id="com.android.calculator2:id/formula_container"),description="清空运算结果")
        factory_mode = Selector(XPath(id='android:id/list'),description="工厂模式列表")
        more_btn = Selector(XPath(has_content="更多选项"),description="更多选项")
        history_btn = Selector(XPath(id="android:id/title",has_text="历史记录"))
        history_record = Selector(XPath(has_not_text="历史记录"),description="历史记录")
        arcsin_veiw = Selector(XPath(id="com.android.calculator2:id/fun_arcsin",has_content="反正弦"),description="反正弦")
        deg_veiw = Selector(XPath(id="com.android.calculator2:id/mode",has_content="角度模式"),description="角度模式")
    def click_num_btn(self,num):
        self.driver.find(self.loc.num_btn(num)).click()
        console.print("点击按键"+str(num))

    def click_sym_btn(self,sym):
        self.driver.find(self.loc.sym_btn(sym)).click()
        console.print("点击符号" + str(sym))

    def hold_press_sym_btn(self, sym, duration: float = None):
        el = self.driver.find(self.loc.sym_btn(sym))
        if duration is None:
            el.click(delay=1)
            console.print("点击"+str(sym))
        else:
            with self.driver.actions_manager() as action:
                action.click_and_hold(el, duration=3)
            console.print("长按"+str(sym))

    def click_func_btn(self,func):
        self.driver.find(self.loc.func_btn(func),exist_ok=True).click()
        console.print("点击函数" + str(func))

    def get_result(self):
        console.print("获取运算结果")
        return self.driver.find(self.loc.result,exist_ok=True).get_text()

    def get_empty_result(self):
        console.print("获取运算结果是否被清除")
        return self.driver.find(self.loc.empty_result)

    def get_func(self, func):
        console.print("是否存在按键" + str(func))
        return self.driver.find(self.loc.func_btn(func))

    def get_deg(self):
        return self.driver.find(self.loc.deg, timeout=3, exist_ok=True)

    def get_input(self):
        console.print("获取输入内容")
        return self.driver.find(self.loc.input ,timeout=3).get_text()

    def factory_mode(self):
        ele = self.driver.find(self.loc.factory_mode)
        if ele is not None:
            return True
        return False

    def click_more(self):
        self.driver.find(self.loc.more_btn).click()
        console.print("点击更多")

    def click_history(self):
        self.driver.find(self.loc.history_btn).click()
        console.print("历史记录")

    def view_history_record(self):
        return self.driver.find(self.loc.history_record).get_text()

    def arcsin_veiw(self):
        return self.driver.find(self.loc.arcsin_veiw).get_text()

    def deg_veiw(self):
        return self.driver.find(self.loc.deg_veiw).get_text()
