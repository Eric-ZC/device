import math
import time
from soium import Keys
from src.deps import *



class Security(BasePage):
    """
    屏幕方向
    """

    class loc:

        screen_lock = Selector(
            XPath("android.widget.TextView", has_text="屏幕锁定"),
            description="屏幕锁定"
        )
        screen_lock_status = Selector(
            XPath("android.widget.TextView", has_text="屏幕锁定")
            .join("following-sibling::*[@resource-id=\"android:id/summary\"]"),
            description="锁屏状态"
        )
        no_screen_lock = Selector(XPath(has_text="无"), description="无锁屏")

        slide_screen_lock = Selector(XPath(has_text="滑动"), description="滑动解锁")

        PIN_screen_lock = Selector(XPath(has_text="PIN 码"), description="PIN 码解锁")

        input_pin = Selector(XPath(id="com.google.android.inputmethod.latin:id/key_pos_number_line1_1"),
                         description="输入pin")

    def click_screen_lock(self):
        self.driver.find(self.loc.screen_lock).click()
        console.print("点击屏幕锁定")

    def get_screen_lock_status(self):
        self.driver.find(self.loc.screen_lock_status,timeout=5).get_attribute("text")
        console.print("锁屏状态")

    def select_no_lock(self):
        self.driver.find(self.loc.no_screen_lock).click()
        console.print("无锁屏")

    def select_slide_lock(self):
        self.driver.find(self.loc.slide_screen_lock).click()
        console.print("滑动解锁")

    def select_pin_lock(self):
        self.driver.find(self.loc.PIN_screen_lock).click()
        console.print("PIN 码解锁")

    def setting_pin_lock(self):
        for _ in range(4):
            self.driver.find(self.loc.input_pin).click()
        console.print("pin 码1111")

    def lock_screen(self):
        self.driver.press_keycode(Keys.POWER)
        time.sleep(3)
        self.driver.press_keycode(Keys.POWER)