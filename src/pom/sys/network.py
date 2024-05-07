from src.deps import *


class Network(BasePage):
    """
    网络页
    """

    class loc:
        airplane_mode = Selector(
            XPath(has_text="Airplane mode", exact=True), description="飞行模式"
        )
        tethering = Selector(
            XPath(has_text=["Tethering", "Hotspot & tethering"], exact=True),
            description="热点和网络共享",
        )
        wifi = Selector(XPath(has_text="互联网", exact=True), description="Wi‑Fi")
        wifi_android = Selector(XPath(has_text="WLAN",id="android:id/title"),description="Wi‑Fi")
        data_saver = Selector(
            XPath(id="android:id/title", has_text="Data Saver"), description="流量节省程序"
        )
        advanced = Selector(XPath(has_text="Advanced", exact=True), description="高级设置")
        vpn = Selector(XPath(has_text="VPN", exact=True), description="VPN")
        private_dns = Selector(
            XPath(has_text="Private DNS", exact=True), description="私有DNS"
        )

    def click_airplane_mode(self):
        self.driver.find(self.loc.airplane_mode).click()
        console.print("点击飞行模式")

    def click_wifi(self):
        delay = {True: 5, False: 3}[self.driver.wifi_on]
        self.driver.find(self.loc.wifi).click(delay=delay)
        console.print("点击Wi-Fi")

    def click_wifi_android(self):
        delay = {True: 5, False: 3}[self.driver.wifi_on]
        self.driver.find(self.loc.wifi_android).click(delay=delay)
        console.print("点击Wi-Fi")

    def click_tethering(self):
        self.driver.find(self.loc.tethering).click()
        console.print("点击热点和网络共享")

    def click_data_saver(self):
        self.driver.find(self.loc.data_saver).click()
        console.print("点击流量节省程序")

    def click_advanced(self):
        self.driver.find(self.loc.advanced).click()
        console.print("点击高级设置")

    def click_vpn(self):
        self.driver.find(self.loc.vpn).click()
        console.print("点击VPN")

    def click_private_dns(self):
        self.driver.find(self.loc.private_dns).click()
        console.print("点击私有DNS")
