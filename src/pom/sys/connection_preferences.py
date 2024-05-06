import time

from src.deps import *


class ConnectionPreferences(BasePage):
    """
    连接偏好设置页
    """

    class loc:

        bluetooth = Selector(XPath(has_text="Bluetooth"), description="蓝牙")

        file_received_via_bluetooth = Selector(XPath(has_text="收到的文件"), description="通过蓝牙收到的文件")

        set_btn = Selector(XPath(has_content="设置"), description="设置")

        rename = Selector(XPath(has_content="重命名"), description="重命名")

        input_rename = Selector(XPath(id='com.android.settings:id/edittext'), description="设备名称")

        confirm_rename = Selector(XPath(has_text="重命名"), description="提交重命名")

        view_all = Selector(XPath(id="android:id/title",has_text="查看全部"), description="查看全部")

        device_set = Selector(XPath(id="com.android.settings:id/settings_button"), description="设备详情")

        device_name = Selector(XPath(id="android:id/title",has_text="设备名称").
                               join("/following-sibling::android.widget.TextView"),
                               description="设备名称")
        switch = Selector(XPath(id="android:id/switch_widget"),description="蓝牙开关")

    def click_bluetooth(self):
        self.driver.find(self.loc.bluetooth).click()
        console.print("点击蓝牙")

    def click_file_received_via_bluetooth(self):
        self.driver.find(self.loc.file_received_via_bluetooth, timeout=10, autodiscovery="down").click()
        console.print("点击通过蓝牙收到的文件")

    def click_view_all(self):
        self.driver.find(self.loc.view_all, timeout=10).click()

    def click_set_btn(self):
        time.sleep(5)
        self.driver.find(self.loc.set_btn,timeout=10).click()
        console.print("点击设置按钮")

    def click_rename(self):
        self.driver.find(self.loc.rename,timeout=10).click()
        console.print("点击重命名")

    def input_rename(self,text):
        self.driver.find(self.loc.input_rename).fill(text)
        console.print("重命名设备")

    def click_confirm_rename(self):
        self.driver.find(self.loc.confirm_rename).click()
        console.print("点击提交")

    def device_detail(self):
        self.driver.find(self.loc.device_set).click()
        console.print("设备详情")

    def device_name(self):
        return self.driver.find(self.loc.device_name).get_text()

    def switch_bluetooth(self):
        self.driver.find(self.loc.switch).click()
        console.print("切换蓝牙开关")