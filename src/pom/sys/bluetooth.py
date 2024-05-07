from src.deps import *


class Bluetooth(BasePage):

    class loc:
        switch = Selector(XPath(id="com.android.settings:id/switch_widget"),description="开关")
        device_name = Selector(XPath(has_text="设备名称"), description="设备名称")
        device_name_input = Selector(XPath(has_text="重命名此设备")
            .join("ancestor::*", id="com.android.settings:id/parentPanel")
            .join("descendant-or-self::*", id="com.android.settings:id/edittext"),
            description="设备名称输入框")
        rename = Selector(XPath("android.widget.Button", has_text="重命名"), description="重命名")
        connection_preference_settings = Selector(XPath(has_text="连接偏好设置"), description="连接偏好设置")
        bluetooth = Selector(XPath(has_text="蓝牙"), description="蓝牙")
        pair_new_device = Selector(
            XPath(id="android:id/title", has_text="与新设备配对"),
            description="与新设备配对"
        )
        bluetooth_setting = Selector(XPath(has_content="已连接的设备"), description="已连接的设备页")

    def switch(self):
        self.driver.find(self.loc.switch).click()

    def device_name(self):
        self.driver.find(self.loc.device_name).click()

    def device_name_input(self, text):
        self.driver.find(self.loc.device_name_input).fill(text)

    def rename(self):
        self.driver.find(self.loc.rename).click()

    def preference_settings(self):
        self.driver.find(self.loc.connection_preference_settings).click()

    def click_bluetooth(self):
        self.driver.find(self.loc.bluetooth).click()

    def click_pair_new_device(self):
        self.driver.find(self.loc.pair_new_device).click()
        console.print("点击与新设备配对")

    def connected_device_visible(self):
        ele = self.driver.find(self.loc.bluetooth_setting, timeout=5)
        if ele.is_visible():
            return True
        return False
