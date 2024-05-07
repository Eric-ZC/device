import math
from src.deps import *



class NotificationPanel(BasePage):
    """
    通知面板
    """

    class loc:
        complete = Selector(XPath(has_text="COMPLETE"),description="保存")
        panel = Selector(
            XPath(id="com.android.systemui:id/expanded_qs_scroll_view"),
            description="下拉通知面板",
        )
        clear_all = Selector(XPath(has_text="Clear all"),description="清除所有")
        wifi = Selector(XPath(has_content=["互联网","Neostra-VIP"]), description="Wi-Fi")
        bluetooth = Selector(XPath(has_content="蓝牙。"), description="蓝牙")
        volume = Selector(XPath(has_content="Volume"), description="音量")
        screen_record = Selector(
            XPath(has_text=["屏幕录制", "开始"]), description="录制屏幕"
        )
        hotspot = Selector(XPath(has_content=["Hotspot", "热点"]), description="热点")
        screenshot = Selector(XPath(has_text=["屏幕截图", "开启 "]), description="截屏")
        flight_mode = Selector(XPath("//android.widget.Switch[@content-desc=\"飞行模式\"]"),description="飞行模式")
        notification_volume = Selector(XPath(id="com.android.systemui:id/imin_notification_sb"),description="通知滑动条")
        media_volume = Selector(XPath(id="com.android.systemui:id/imin_media_sb"),description="媒体音量")
        record_audio = Selector(
            XPath(id="com.android.systemui:id/screenrecord_audio_switch"),
            description="音频录制",
        )
        start = Selector(
            XPath(id="com.android.systemui:id/button_start"), description="开始"
        )
        cancel = Selector(
            XPath(id="com.android.systemui:id/button_cancel"), description="取消"
        )
        brightness_view = Selector(XPath(id="com.android.systemui:id/slider_title",has_text="亮度"),
                                   description="亮度")
        brightness_bar = Selector(
            XPath(id="com.android.systemui:id/brightness_slider"), description="亮度"
        )
        settings = Selector(
            XPath(id="com.android.systemui:id/settings_button_container"),
            description="设置",
        )
        data_saver_icon = Selector(
            XPath(has_content=["Data Saver is on", "流量节省程序已开启"]), description="数据节省模式"
        )
        clock = Selector(XPath(id="com.android.systemui:id/clock"), description="时钟")
        battery_percentage = Selector(
            XPath(id="com.android.systemui:id/battery_percentage_view"),
            description="电池百分比",
        )
        screen_photo = Selector(XPath(id="com.android.systemui:id/global_scrreenshot_preview"),description="截图文件")
        tap_to_stop = Selector(XPath(has_text="停止"),description="停止录屏")
        save_record = Selector(XPath(has_text="Screen recording saved, tap to view"),description="保存录屏")
        switch_wlan = Selector(XPath(has_content="WLAN"),description="启动/关闭")
        done_bar = Selector(XPath(id="com.android.systemui:id/done_button"), description="完成按钮")
        main_screen_android11 = Selector(XPath(id="com.android.systemui:id/brightness_slider",has_content="屏幕亮度"), description="主屏幕亮度")
        secondary_screen_android11 = Selector(XPath(id="com.android.systemui:id/brightness_slider2",has_content="屏幕亮度"), description="副屏幕亮度")
        mian_screen_bright = Selector(
            XPath('//android.widget.TextView[@resource-id="com.android.systemui:id/slider_title" and @text="主屏亮度"]').
            join( "/following-sibling::android.widget.SeekBar"),
            description="主屏幕亮度"
        )
        secondary_screen_bright = Selector(
            XPath('//android.widget.TextView[@resource-id="com.android.systemui:id/slider_title" and @text="副屏亮度"]').
            join("/following-sibling::android.widget.SeekBar"),
            description="副屏亮度"
            )
        voice_btn = Selector(
            XPath('//android.widget.TextView[@resource-id="com.android.systemui:id/tile_label" and @text="音量"]'),
            description="音量"
        )
        complete_btn =Selector(
            XPath(id='com.android.systemui:id/imin_complete_bt', has_text='完成'),
            description='完成'
        )

        @staticmethod
        def notification_title(text: str = None):
            """
            获取通知面板标题
            """
            return Selector(
                XPath(id="android:id/title", has_text=text or True), description="通知"
            )

    def has_data_saver_icon(self):
        """
        是否有数据节省模式图标
        """
        return self.driver.find(self.loc.data_saver_icon, timeout=3, exist_ok=True)

    def get_notifications(self):
        """
        获取通知列表
        """
        return self.driver.find_all(self.loc.notification_title())

    def get_notification(self, text: str, timeout: int = 10, exist_ok: bool = False):
        """
        获取通知
        """
        return self.driver.find(
            self.loc.notification_title(text), timeout=timeout, exist_ok=exist_ok
        )

    def expand(self, count: int = 1):
        """
        展开通知面板
        """
        self.driver.expand_status_bar(count=count)
        console.print(f"展开通知面板 下拉次数:{count}")

    def click_wifi(self, duration: float = None):
        """
        点击Wi-Fi
        """
        el = self.driver.find(self.loc.wifi)
        if duration is None:
            el.click(delay=2)
            console.print("点击Wi-Fi")
        else:
            self.driver.actions_manager().click_and_hold(el, duration=2)
            # el.tap(duration)
            console.print("长按击Wi-Fi")

    def click_stop(self):
        self.driver.find(self.loc.tap_to_stop).click()
        console.print("点击停止录屏")

    def click_bluetooth(self, duration: float = None):
        """
        点击蓝牙
        """
        el = self.driver.find(self.loc.bluetooth)
        if duration is None:
            el.click(delay=1)
            # console.print("点击蓝牙")
        else:
            with self.driver.actions_manager() as action:
                action.click_and_hold(el,duration=3)
            console.print("长按蓝牙")

    def click_flight_mode(self):
        self.driver.find(self.loc.flight_mode).click()
        console.print("点击飞行模式")

    def click_settings(self):
        self.driver.find(self.loc.settings).click()
        console.print("点击设置")

    def get_clock(self):
        """
        获取当前时间
        """
        return self.driver.find(self.loc.clock).get_text()

    def has_battery_percentage(self):
        """
        是否有电池百分比
        """
        return self.driver.find(self.loc.battery_percentage, timeout=3, exist_ok=True)

    def has_hotspot(self):
        """
        是否有热点
        """
        return self.driver.find(self.loc.hotspot, timeout=3, exist_ok=True)

    def click_record(self):
        self.driver.find(self.loc.screen_record).click()
        console.print("点击录屏")

    def click_screenshot(self):
        self.driver.find(self.loc.screenshot).click()
        console.print("点击截图")

    def click_start(self):
        self.driver.find(self.loc.start).click()
        console.print("点击开始")

    def click_save_record(self):
        self.driver.find(self.loc.save_record).click()
        console.print("点击录屏")

    def get_save_record(self):
        return self.driver.find(self.loc.save_record,timeout=10,exist_ok=True)

    def click_complete(self):
        self.driver.find(self.loc.complete).click()
        console.print("点击保存")

    def get_volume(self):
        return self.driver.find(self.loc.volume,timeout=10,exist_ok=True)

    def click_volume(self):
        self.driver.find(self.loc.volume, timeout=10, exist_ok=True).click()
        console.print("点击音量")

    def drag_brightness_bar(self, percentage: float):
        """
        拖动亮度条
        1为最大，0为最小
        """
        bar = self.driver.find(self.loc.brightness_bar)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()


    def drag_media_volume(self, level: int):
        """
        拖动媒体音量
        """
        bar = self.driver.find(self.loc.media_volume)
        width = bar.size["width"]
        max_level = self.driver.get_max_volume_level()
        mid_level = math.ceil(max_level / 2)
        offset = -(width / max_level * (mid_level - level))
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0, duration=2).release()

    def drag_notification_volume(self, level: int):
        """
        拖动通知音量
        """
        bar = self.driver.find(self.loc.notification_volume)
        width = bar.size["width"]
        max_level = self.driver.get_max_notification_level()
        mid_level = math.ceil(max_level / 2)
        offset = -(width / max_level * (mid_level - level))
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0, duration=2).release()

    def click_clear_all(self):
        console.print("点击清除所有")
        self.driver.find(self.loc.clear_all).click()

    def get_clear_all(self):
        return self.driver.find(self.loc.clear_all,exist_ok=True,timeout=20)

    def hold_press_bluetooth(self):
        el = self.driver.find(self.loc.bluetooth)
        with self.driver.actions_manager().click_and_hold(el, duration=5):
            console.print("长按蓝牙")

    def switch_wlan(self):
        self.driver.find(self.loc.switch_wlan).click()
        console.print("开关wifi")

    def click_done_bar(self):
        self.driver.find(self.loc.done_bar).click()
        console.print("完成按钮")

    def brightness_view(self):
        self.driver.find(self.loc.brightness_view)
        console.print("亮度视图")

    def drag_main_brightness_bar(self, percentage: float):
        """
        拖动亮度条
        1为最大，0为最小
        """
        bar = self.driver.find(self.loc.mian_screen_bright)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

    def drag_secondary_brightness_bar(self, percentage: float):
        """
        拖动亮度条
        1为最大，0为最小
        """
        bar = self.driver.find(self.loc.secondary_screen_bright)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

    def click_voice_btn(self):
        self.driver.find(self.loc.voice_btn).click()
        console.print("点击音量")

    def click_complete_btn(self):
        self.driver.find(self.loc.complete_btn).click()
        console.print("点击完成")

    def drag_main_brightness_bar11(self, percentage: float):
        """
        拖动亮度条
        1为最大，0为最小
        """
        bar = self.driver.find(self.loc.main_screen_android11)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

    def drag_secondary_brightness_bar11(self, percentage: float):
        """
        拖动亮度条
        1为最大，0为最小
        """
        bar = self.driver.find(self.loc.secondary_screen_android11)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

