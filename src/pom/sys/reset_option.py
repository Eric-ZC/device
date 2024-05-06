import math
from src.deps import *



class ResetOption(BasePage):
    """
    屏幕方向
    """

    class loc:

        factory_reset = Selector(XPath(has_text="清除所有数据（恢复出厂设置）"), description="清除所有数据（恢复出厂设置）")

        erase_all_data = Selector(XPath(has_text="清除所有数据"), description="清除所有数据")

        reset_options = Selector(XPath(has_text="重置选项"),description="重置选项")


    def click_factory_reset(self):
        self.driver.find(self.loc.factory_reset).click()
        console.print("点击恢复出场设置")

    def erase_all_data(self):
        self.driver.find(self.loc.erase_all_data).click()
        console.print("清除所有数据")

    def click_reset_options(self):
        self.driver.find(self.loc.reset_options).click()