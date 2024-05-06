from src.deps import *


class ConnectedDevices(BasePage):
    """
    连接设备页
    """

    class loc:
        pair_new_device = Selector(XPath(has_text="与新设备配对"), description="与新设备配对"
        )
        connection_preferences = Selector(XPath(has_text="Connection preferences"), description="连接偏好设置"
        )

    def click_pair_new_device(self):
        self.driver.find(self.loc.pair_new_device).click()
        console.print("点击与新设备配对")

    def click_connection_preferences(self):
        self.driver.find(self.loc.connection_preferences).click()
        console.print("点击连接偏好设置")
