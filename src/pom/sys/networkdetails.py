from src.deps import *


class NetworkDetails(BasePage):
    """
    网络详情页
    """

    class loc:
        title = Selector(
            XPath(id="com.android.settings:id/action_bar").join(
                has_text="Network details"
            ),
            description="标题",
        )
        forget = Selector(
            XPath(id="com.android.settings:id/button1"), description="忘记网络"
        )
        disconnect = Selector(
            XPath(id="com.android.settings:id/button3"), description="断开网络"
        )
        share = Selector(
            XPath(id="com.android.settings:id/button4"), description="分享网络"
        )
        signal_strength = Selector(
            XPath(id="android:id/title", has_text="Signal strength"), description="信号强度"
        )
        signal_status = Selector(
            XPath(id="android:id/title", has_text="Signal strength").join(
                "following-sibling::android.widget.TextView"
            ),
            description="信号状态",
        )
        frequency = Selector(
            XPath(id="android:id/title", has_text="Frequency"), description="频率"
        )
        frequency_band = Selector(
            XPath(id="android:id/title", has_text="Frequency").join(
                "following-sibling::android.widget.TextView"
            ),
            description="频段",
        )
        security = Selector(
            XPath(id="android:id/title", has_text="Security"), description="安全性"
        )
        encry_mode = Selector(
            XPath(id="android:id/title", has_text="Security").join(
                "following-sibling::android.widget.TextView"
            ),
            description="加密模式",
        )
        advanced = Selector(
            XPath(id="android:id/title", has_text="Advanced"), description="高级"
        )
        network_usage = Selector(
            XPath(id="android:id/title", has_text="Network usage"),
            description="网络是否按流量计费",
        )
        billing_mode = Selector(
            XPath(id="android:id/title", has_text="Security").join(
                "following-sibling::android.widget.TextView"
            ),
            description="计费模式",
        )
        mac_address = Selector(
            XPath(id="android:id/title", has_text="MAC address").join(
                "following-sibling::android.widget.TextView"
            ),
            description="MAC地址",
        )
        ip_address = Selector(
            XPath(id="android:id/title", has_text="IP address").join(
                "following-sibling::android.widget.TextView"
            ),
            description="IP地址",
        )
        ip_way = Selector(
            XPath(id="com.android.settings:id/ip_settings").join(
                "android.widget.TextView"
            ),
            description="IP方式",
        )

        gateway = Selector(
            XPath(id="android:id/title", has_text="Gateway").join(
                "following-sibling::android.widget.TextView"
            ),
            description="网关",
        )
        subnet_mask = Selector(
            XPath(id="android:id/title", has_text="Subnet mask").join(
                "following-sibling::android.widget.TextView"
            ),
            description="子网掩码",
        )
        dns = Selector(
            XPath(id="android:id/title", has_text="DNS").join(
                "following-sibling::android.widget.TextView"
            ),
            description="DNS",
        )
        transmit_link_speed = Selector(
            XPath(id="android:id/title", has_text="Transmit link speed").join(
                "following-sibling::android.widget.TextView"
            ),
            description="传输链接速度",
        )
        receive_link_speed = Selector(
            XPath(id="android:id/title", has_text="Receive link speed").join(
                "following-sibling::android.widget.TextView"
            ),
            description="接收链接速度",
        )
        ipv6_address = Selector(
            XPath(id="android:id/title", has_text="IPV6").join(
                "ancestor::android.widget.LinearLayout/following-sibling::android.widget.LinearLayout/descendant::	android.widget.TextView"
            ),
            description="IPv6地址",
        )
        qr_tip = Selector(
            XPath(id="android:id/summary", has_text="Scan this QR code to connect to"),
        )
        qr_code = Selector(
            XPath(id="com.android.settings:id/qrcode_view"), description="二维码"
        )
        edit = Selector(XPath(has_content="Modify"), description="编辑")
        advanced_options = Selector(XPath(id="com.android.settings:id/wifi_advanced_togglebox"),description="高级选项")
        ip_settings = Selector(XPath(id="com.android.settings:id/ip_settings"),description="IP设置")
        static = Selector(XPath(has_text="Static"),description="静态IP")
        dhcp = Selector(XPath(has_text="DHCP"),description="动态IP")
        fill_ip = Selector(XPath(id="com.android.settings:id/ipaddress"),description="IP地址输入框")
        save = Selector(XPath(has_text="SAVE"),description="保存")

    def is_open(self):
        """
        是否是网络详情页
        """
        if self.driver.find(self.loc.title, exist_ok=True, timeout=3) is None:
            return False
        return True

    def click_forget(self):
        self.driver.find(self.loc.forget).click(delay=3)
        console.print("点击忘记密码")

    def click_advanced_options(self):
        self.driver.find(self.loc.advanced_options).click()
        console.print("点击高级选项")

    def fill_ip(self,text:str ="192.168.1.1"):
        self.driver.find(self.loc.fill_ip).fill(text)
        console.print("输入IP地址:" + text)

    def click_save(self):
        self.driver.find(self.loc.save).click()
        console.print("点击保存")

    def click_ip_settings(self):
        self.driver.find(self.loc.ip_settings).click()
        console.print("点击IP设置")

    def click_static(self):
        self.driver.find(self.loc.static).click()
        console.print("点击静态")

    def click_dhcp(self):
        self.driver.find(self.loc.dhcp).click()
        console.print("点击动态")

    def get_signal_status(self):
        """
        获取信号状态
        """
        return self.driver.find(self.loc.signal_status, look_up=True).get_text()

    def get_frequency_band(self):
        """
        获取频段
        """
        return self.driver.find(self.loc.frequency_band, look_up=True).get_text()

    def get_encry_mode(self):
        """
        获取安全性
        """
        return self.driver.find(self.loc.encry_mode, look_up=True).get_text()

    def get_billing_mode(self):
        """
        获取计费模式
        """
        return self.driver.find(self.loc.billing_mode, look_up=True).get_text()

    def get_mac_address(self):
        """
        获取MAC地址
        """
        return self.driver.find(self.loc.mac_address, look_down=True).get_text()

    def get_ip_address(self):
        """
        获取IP地址
        """
        return self.driver.find(self.loc.ip_address, look_down=True).get_text()

    def get_gateway(self):
        """
        获取网关
        """
        return self.driver.find(self.loc.gateway, look_down=True).get_text()

    def get_subnet_mask(self):
        """
        获取子网掩码
        """
        return self.driver.find(self.loc.subnet_mask, look_down=True).get_text()

    def get_dns(self):
        """
        获取DNS
        """
        return self.driver.find(self.loc.dns, look_down=True).get_text()

    def get_transmit_link_speed(self):
        """
        获取传输链接速度
        """
        return self.driver.find(self.loc.transmit_link_speed, look_down=True).get_text()

    def get_receive_link_speed(self):
        """
        获取接收链接速度
        """
        return self.driver.find(self.loc.receive_link_speed, look_down=True).get_text()

    def get_ipv6_address(self):
        """
        获取IPv6地址
        """
        return self.driver.find(self.loc.ipv6_address, look_down=True).get_text()

    def get_qr_tip(self):
        """
        获取二维码提示
        """
        return self.driver.find(self.loc.qr_tip).get_text()

    def click_advanced(self):
        self.driver.find(self.loc.advanced,timeout=5).click()
        console.print("点击高级")

    def click_share(self):
        self.driver.find(self.loc.share).click()
        console.print("点击分享")

    def click_edit(self):
        self.driver.find(self.loc.edit).click()
        console.print("点击编辑")

    def get_ip(self):
        return self.driver.find(self.loc.fill_ip).get_text()

    def get_ip_way(self):
        return self.driver.find(self.loc.ip_way).get_text()

    def has_qr_code(self):
        """
        判断是否有二维码
        """
        if self.driver.find(self.loc.qr_code, exist_ok=True, timeout=2) is None:
            return False
        return True
