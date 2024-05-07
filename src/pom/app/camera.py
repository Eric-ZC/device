import time

from soium import Keys

from src.deps import *


class Camera(BasePage):
    """
    相机页
    """

    class loc:

        photo_btn = Selector(
            XPath(has_content= "照片"), description="设置菜单"
        )
        HDR_btn = Selector(
            XPath(id = "com.mediatek.camera:id/hdr_icon"), description="HDR按钮"
        )
        camera_mode = Selector(
            XPath(has_content = "相机模式"), description="相机模式"
        )
        setting_btn = Selector(
            XPath(has_content = "设置"),description="设置"
        )
        time_lapse = Selector(
            XPath(has_content= "自拍计时"),description= "自拍计时"
        )


    def click_photo(self):
        self.driver.find(self.loc.photo_btn).click()
        console.print("点击拍照")

    def resting_screen(self):
        self.driver.press_keycode(Keys.POWER)
        console.print("熄屏")
        time.sleep(5)
        self.driver.press_keycode(Keys.POWER)

    def click_hdr(self):
        self.driver.find(self.loc.HDR_btn).click()
        console.print("点击HDR模式")

    def volume_keys(self):
        self.driver.press_keycode(Keys.VOLUME_UP)
        console.print("增加音量")
        self.driver.press_keycode(Keys.VOLUME_DOWN)
        console.print("减小音量")

    def continuous_shooting(self,times):
        for _ in range(times):
            self.driver.find(self.loc.photo_btn).click()
        console.print("快照")

    def click_camera_mode(self):
        self.driver.find(self.loc.camera_mode).click()
        console.print("查看相机模式")

    def click_setting_btn(self):
        self.driver.find(self.loc.setting_btn).click()
        console.print("点击设置按钮")

    def click_time_lapse(self):
        self.driver.find(self.loc.time_lapse).click()
        console.print("点击自拍计时")

    def click_time_lapse_on(self):
        self.driver.find(self.loc.time_lapse_on).click()
        console.print("启动自拍计时")
