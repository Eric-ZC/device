import math
from src.deps import *



class ResetWlanNetwork(BasePage):
    """
    屏幕方向
    """

    class loc:

        reset_wlan_network_bluetooth = Selector(
            XPath(has_text="重置 WLAN、移动数据网络和蓝牙设置"),
            description="重置 WLAN、移动数据网络和蓝牙设置"
        )
        reset_setting = Selector(
            XPath(id="com.android.settings:id/initiate_reset_network", has_text="重置设置"),
            description="重置设置"
        )
        exec_reset = Selector(
            XPath(id="com.android.settings:id/execute_reset_network", has_text="重置设置"),
            description="重置设置"
        )

        reset_toast = Selector(
            XPath(has_text="网络设置已重置"),
            description="网络设置已重置"
        )

        reset_options = Selector(
            XPath(has_text="重置选项"),
            description="重置选项"
        )

    def click_reset_options(self):
        self.driver.find(self.loc.reset_options,timeout=5).click()
        console.print("点击重置")

    def reset_wlan_network_bluetooth(self):
        self.driver.find(self.loc.reset_wlan_network_bluetooth, timeout=5).click()
        console.print("点击重置")

    def click_reset_setting(self):
        self.driver.find(self.loc.reset_setting, timeout=5).click()
        console.print("点击重置网络")

    def click_exec_reset(self):
        self.driver.find(self.loc.exec_reset,timeout=5).click()
        console.print("执行网络重置")

    def toast_display(self):
        ele = self.driver.find(self.loc.reset_toast,timeout=30).get_text()
        return ele
