import time

from soium import Keys

from src.deps import *


class Camera(BasePage):
    """
    相机页
    """

    class loc:

        photo_btn = Selector(
            XPath(has_content="照片"), description="设置菜单"
        )
        HDR_btn = Selector(
            XPath(id="com.mediatek.camera:id/hdr_icon"), description="HDR按钮"
        )
        camera_mode = Selector(
            XPath(has_content="相机模式"), description="相机模式"
        )
        setting_btn = Selector(
            XPath(has_content="设置"), description="设置"
        )
        time_lapse = Selector(
            XPath(has_content="自拍计时"), description="自拍计时"
        )

        time_lapse_on = Selector(
            XPath(id="android:id/list")
            .join('android.widget.LinearLayout[2]')
            .join('(android.widget.RadioButton[@resource-id="android:id/checkbox"])[2]')
        )
        switch_camera = Selector(
            XPath(id="com.mediatek.camera:id/camera_switcher"),
            description="摄像头切换"
        )
        self_time_setting = Selector(
            XPath(id="com.mediatek.camera:id/self_timer_setting", has_content="自拍计时"),
            description="自拍计时"
        )
        self_time = Selector(
            XPath("(//android.widget.RadioButton[@resource-id=\"android:id/checkbox\"])[2]"),
            description="选择自拍计时"
        )
        picture_size = Selector(
            XPath(id="com.mediatek.camera:id/picture_size_setting", has_content="照片大小"),
            description="照片大小"
        )
        select_size = Selector(
            XPath("(//android.widget.RadioButton[@resource-id=\"android:id/checkbox\"])[2]"),
            description="选择照片大小"
        )
        video = Selector(
            XPath(id="com.mediatek.camera:id/shutter_text", has_content="视频"),
            description="视频"
        )
        gallery = Selector(
            XPath(has_content="Has Content", id="com.mediatek.camera:id/thumbnail"),
            description="跳转相册"
        )
        picture_video = Selector(
            XPath(id="com.mediatek.camera:id/btn_vss"),
            description="拍照"
        )
        video_stop = Selector(
            XPath(id="com.mediatek.camera:id/video_stop_shutter"),
            description="视频停止"
        )
        view_camera = Selector(
            XPath("//android.widget.TextView[@resource-id=\"android:id/text2\"]"),
            description="相机"
        )

    def click_photo(self):
        self.driver.find(self.loc.photo_btn).click()
        console.print("点击拍照")

    def shut_down_screen(self):
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

    def continuous_shooting(self, times):
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

    def switch_camera(self):
        self.driver.find(self.loc.switch_camera).click()
        console.print("切换摄像头")

    def click_self_time_setting(self):
        self.driver.find(self.loc.self_time_setting).click()
        console.print("自拍计时")

    def click_self_time(self):
        self.driver.find(self.loc.self_time).click()
        console.print("设置拍照时间")

    def click_picture_size(self):
        self.driver.find(self.loc.picture_size).click()
        console.print("照片大小")

    def click_select_size(self):
        self.driver.find(self.loc.select_size).click()
        console.print("选择照片大小")

    def switch_video(self):
        self.driver.find(self.loc.video).click()
        console.print("切换视频")

    def click_gallery(self):
        self.driver.find(self.loc.gallery).click()
        console.print("相册")

    def click_picture_video(self):
        self.driver.find(self.loc.picture_video).click()
        console.print("视频拍照")

    def click_video_stop(self):
        self.driver.find(self.loc.video_stop).click()
        console.print("停止拍摄")
        self.driver.multitouch()


