from src.deps import *
from appium.webdriver.common.touch_action import *

class WiFi(BasePage):
    """
    Wi-Fi页
    """

    class loc:
        title = Selector(
            XPath(id="com.android.settings:id/action_bar").join(
                has_text=["Wi‑Fi", "WLAN"]
            ),
            description="标题",
        )
        switch = Selector(
            XPath(id="com.android.settings:id/switch_text", has_text="Use Wi‑Fi"),
            description="WiFi开关",
        )
        scanning_tips = Selector(
            XPath(has_text="To see available networks, turn Wi‑Fi on"),
            description="断网提示",
        )
        password = Selector(
            XPath(id="com.android.settings:id/password"), description="密码框"
        )
        preferences = Selector(XPath(has_text="Wi‑Fi preferences"), description="偏好设置")
        saved_networks = Selector(
            XPath(has_text="Saved networks"), description="已保存的网络"
        )
        wifi_data_usage = Selector(
            XPath(has_text="Wi‑Fi data usage"), description="WLAN流量用量"
        )
        check_again = Selector(
            XPath(has_text="Check password and try again"), description="连接Wi-Fi失败提示"
        )
        add_network = Selector(XPath(has_text="Add network"), description="添加网络")
        disconnect = Selector(
            XPath(id="android:id/title", has_text="Disconnect"), description="断开连接"
        )
        forget = Selector(
            XPath(id="android:id/title", has_text="Forget"), description="取消保存"
        )
        connect = Selector(
            XPath(id="android:id/title", has_text="Connect"), description="连接"
        )
        show_password = Selector(
            XPath(id="com.android.settings:id/show_password", has_text="Show password"),
            description="显示密码",
        )
        heard_title = Selector(
            XPath(id='com.android.settings:id/entity_header_title'),
            description="wifi名称"
        )

        @staticmethod
        def wifi(name: str = None):
            return Selector(
                XPath(id="com.android.settings:id/recycler_view").join(
                    "android.widget.LinearLayout", has_content=name or True
                ),
                description="WiFi列表",
            )

    def is_open(self):
        """
        是否是Wi-Fi页
        """
        if self.driver.find(self.loc.title, exist_ok=True, timeout=3) is None:
            return False
        return True

    def get_wifi_list(self):
        """
        获取Wi-Fi列表
        """
        return self.driver.find_all(self.loc.wifi())

    def get_wifi(self, name: str, ):
        """
        获取Wi-Fi
        """
        return self.driver.find(
            self.loc.wifi(name), autodiscovery="down", timeout=90
        ).click()

    def click_switch(self):
        delay = {True: 3, False: 5}[self.driver.wifi_on]
        self.driver.find(self.loc.switch, autodiscovery="down", timeout=90).click(delay=delay)
        console.print("点击Wi-Fi开关")

    def click_preferences(self, look_up: bool = None, look_down: bool = None):
        self.driver.find(
            self.loc.preferences, autodiscovery="down", timeout=90
        ).click()
        console.print("点击偏好设置")

    def click_saved_networks(self, look_up: bool = None, look_down: bool = None):
        self.driver.find(
            self.loc.saved_networks, look_up=look_up, look_down=look_down, timeout=90
        ).click()
        console.print("点击已保存的网络")

    def click_wifi_data_usage(self, look_up: bool = None, look_down: bool = None):
        self.driver.find(
            self.loc.wifi_data_usage, look_up=look_up, look_down=look_down, timeout=90
        ).click(delay=3)
        console.print("点击WLAN流量用量")

    def click_show_password(self):
        self.driver.find(self.loc.show_password).click()
        console.print("点击显示密码")

    def has_saved_networks(self):
        """
        是否有已保存的网络
        """
        self.driver.find(self.loc.preferences, look_down=True, timeout=90).is_visible()
        if self.driver.find(
            self.loc.saved_networks, exist_ok=True, look_down=True, timeout=2
        ):
            return True
        return False

    def need_password(self):
        """
        是否需要密码
        """
        return self.driver.find(self.loc.password, timeout=3, exist_ok=True)

    def fill_password(self, password: str):
        self.driver.find(self.loc.password).fill(password)
        console.print(f"输入密码：{password}")

    def get_password(self):
        """
        获取密码
        """
        return self.driver.find(self.loc.password).get_text()

    def click_disconnect(self):
        if self.driver.find(self.loc.disconnect, timeout=2, exist_ok=True) is None:
            return False
        self.driver.find(self.loc.disconnect).click(delay=2)
        console.print("点击断开连接")
        return True

    def click_forget(self):
        if self.driver.find(self.loc.forget, timeout=2, exist_ok=True) is None:
            return False
        self.driver.find(self.loc.forget).click()
        console.print("点击取消保存")
        return True

    def click_connect(self):
        if self.driver.find(self.loc.connect, timeout=2, exist_ok=True) is None:
            return False
        self.driver.find(self.loc.connect).click()
        console.print("点击连接")
        return True

    def get_heard_title(self):
        console.print("获取标题名称")
        return self.driver.find(self.loc.heard_title,timeout=10).get_text()