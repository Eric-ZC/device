from src.deps import *


class AboutDevice(BasePage):
    """
    关于设备页
    """

    class loc:

        bluetooth_address = Selector(XPath("android.widget.TextView", has_text="蓝牙地址").join(
            "/following-sibling::android.widget.TextView"
        ),
            description="蓝牙地址",
        )
        ip_address = Selector(XPath("android.widget.TextView", has_text="IP address").join(
                "/following-sibling::android.widget.TextView"
            ),
            description="IP地址",
        )
        about_device_toolbar = Selector(
            XPath(id="com.android.settings:id/collapsing_toolbar"),
            description="关于设备标题"
        )
        secondary_screen = Selector(
            XPath(id="com.android.settings:id/content_parent"),
            description="副屏"
        )
        main_screen = Selector(
            XPath(id="com.android.settings:id/homepage_container"),
            description="主屏"
        )
        build_number = Selector(
            XPath(has_text="版本号"),
            description="版本号"
        )
        action_bar = Selector(
            XPath(id="com.android.settings:id/action_bar").join("/descendant::android.widget.TextView"),
            description="项目栏"
        )

    def get_size_secondary_screen(self):
        """
        获取副屏尺寸
        """
        size = self.driver.find(self.loc.secondary_screen).size
        return size

    def get_centre_secondary_screen(self):
        """
        获取副屏中心轴
        """
        centre = self.driver.find(self.loc.secondary_screen).centre
        return centre

    def find_secondary_screen(self):
        """
        判断副屏情况
        """
        if self.driver.find(self.loc.secondary_screen, exist_ok=True, timeout=5):
            return True
        return False

    def secondary_screens_ele(self, ele):

        self.find_secondary_screen()
        size = self.get_size_secondary_screen()
        centre = self.get_centre_secondary_screen()
        console.print(size)
        console.print(centre)
        x = size['width']
        y = size['height']
        start_x = centre[0]
        start_y = centre[1]
        print(x, y, x, start_y)
        return self.driver.find(ele, timeout=10, scroll_on=centre, autodiscovery="down")

    def get_toolbar_content(self):
        """
        返回工具栏标题
        """
        if self.find_secondary_screen():
            console.print("存在副屏")
            element = self.secondary_screens_ele(self.loc.about_device_toolbar)
        else:
            console.print("不存在副屏")
            element = self.driver.find(self.loc.about_device_toolbar)

        return element.get_attribute("content-desc")


    def get_bluetooth_address(self):
        """
        获取蓝牙地址
        """
        return self.driver.find(
            self.loc.bluetooth_address, autodiscovery="down"
        ).get_text()

    def get_ip_address(self):
        """
        获取IP地址
        """
        return self.driver.find(
            self.loc.ip_address, autodiscovery ="down"
        ).get_text()

    def enter_developer(self):
        for _ in range(5):
            self.driver.find(self.loc.build_number, autodiscovery="down").click()
        console.print("进入开发者模式")

    def get_action_bar(self):
        return self.driver.find(self.loc.action_bar).get_text()
