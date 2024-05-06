import math
from src.deps import *



class Orientation(BasePage):
    """
    屏幕方向
    """

    class loc:

        secondary_screen = Selector(XPath(id="com.android.settings:id/content_parent"), description="副屏")

        main_screen = Selector(XPath(id="com.android.settings:id/homepage_container"), description="主屏")

        about_devices = Selector(XPath(has_text="关于设备"), description="关于设备")

        version = Selector(XPath(id="android:id/title",has_text="版本号"),description="版本号")

        # @staticmethod
        # def notification_title(text: str = None):
        #     """
        #     获取通知面板标题
        #     """
        #     return Selector(
        #         XPath(id="android:id/title", has_text=text or True), description="通知"
        #     )

    def find_main_screen(self):
        ele = self.driver.find(self.loc.main_screen)
        console.print("存在主屏幕")
        return bool(ele)

    def get_size_main_screen(self):
        size = self.driver.find(self.loc.main_screen).size
        return size

    def get_centre_main_screen(self):
        centre = self.driver.find(self.loc.main_screen).centre
        return centre

    def find_secondary_screen(self):
        ele = self.driver.find(self.loc.secondary_screen)
        console.print("存在副屏幕")
        return bool(ele)

    def main_screens(self, ele):

        self.find_main_screen()
        size = self.get_size_main_screen()
        centre = self.get_centre_main_screen()
        console.print(size)
        console.print(centre)
        x = size['width']
        y = size['height']
        start_x = centre[0]
        start_y = centre[1]
        print(start_x, y, start_x, start_y)
        return self.driver.find(ele, timeout=10, scroll_on=centre, autodiscovery="down")

    def secondary_screens(self):

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
        self.driver.find(self.loc.about_devices, timeout=10, scroll_on=centre, autodiscovery="down")


    def get_size_secondary_screen(self):
        size = self.driver.find(self.loc.secondary_screen).size
        return size

    def get_centre_secondary_screen(self):
        centre = self.driver.find(self.loc.secondary_screen).centre
        return centre

    def click_about_devices(self):
        if self.find_main_screen() is True:
            self.main_screens(self.loc.about_devices).click()
        else:
            self.driver.find(self.loc.about_devices).click()
        # return self.driver.find(self.loc.about_devices).click()


    def click_version(self):
        self.driver.find(self.loc.version).click()