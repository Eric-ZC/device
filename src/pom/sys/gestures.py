from src.deps import *


class Gestures(BasePage):

    class loc:
        switch = Selector(XPath(id="com.android.settings:id/switch_widget"),description="开关")
        device_name = Selector(XPath(has_text="设备名称"), description="设备名称")
        device_name_input = Selector(XPath(has_text="重命名此设备")
            .join("ancestor::*", id="com.android.settings:id/parentPanel")
            .join("descendant-or-self::*", id="com.android.settings:id/edittext"),
            description="设备名称输入框")
        rename = Selector(XPath("android.widget.Button", has_text="重命名"), description="重命名")
        connection_preference_settings = Selector(XPath(has_text="连接偏好设置"), description="连接偏好设置")
        bluetooth = Selector(XPath(has_text="蓝牙"), description="蓝牙")

        gestures_btn = Selector(
            XPath(has_text="手势"),
            description="手势"
        )
        system_navigation_btn = Selector(
            XPath(has_text="系统导航"),
            description="系统导航"
        )
        gestures_navigation_checkbox = Selector(
            XPath('(//android.widget.RadioButton[@resource-id="android:id/checkbox"])[1]'),
            description="手势导航"
        )
        three_keys_navigation_checkbox = Selector(
            XPath('	(//android.widget.RadioButton[@resource-id="android:id/checkbox"])[2]'),
            description="“三按钮”导航"
        )
        back_btn = Selector(
            XPath(has_content="返回"),
            description = "返回"
        )
        home_page_btn = Selector(
            XPath(has_content="主屏幕"),
            description="主屏幕"
        )
        recent_apps_btn = Selector(
            XPath(has_content="概览"),
            description="概览"
        )
        screen_shot = Selector(
            XPath(id="com.android.launcher3:id/action_screenshot", has_text="屏幕截图"),
            description="屏幕截图"
        )
        screen_shot_share = Selector(
            XPath(has_content="分享屏幕截图"),
            description="分享屏幕截图"
        )
        clean_app_up = Selector(
            XPath(has_text="全部清除"),
            description="全部清除"
        )
        back_navigation = Selector(
            XPath(has_content="向上导航"),
            description="向上导航"
        )
        navigation_status = Selector(
            XPath(id="android:id/summary"),
            description="导航状态"
        )


    def click_gestures_btn(self):
        self.driver.find(self.loc.gestures_btn).click()
        console.print("点击手势按钮")

    def click_system_navigation_btn(self):
        self.driver.find(self.loc.system_navigation_btn).click()
        console.print("点击系统导航")

    def click_gestures_navigation_checkbox(self):
        self.driver.find(self.loc.gestures_navigation_checkbox).click()
        console.print("选择手势导航")

    def click_three_keys_navigation_checkbox(self):
        self.driver.find(self.loc.three_keys_navigation_checkbox).click()
        console.print("选择“三按钮”导航")

    def click_back_btn(self):
        self.driver.find(self.loc.back_btn).click()
        console.print("点击返回按钮")

    def click_home_page_btn(self):
        self.driver.find(self.loc.home_page_btn).click()
        console.print("点击主屏幕")

    def click_recent_apps_btn(self):
        self.driver.find(self.loc.recent_apps_btn).click()
        console.print("点击概览")

    def switch_recent_apps(self):
        self.driver.find(self.loc.recent_apps_btn).click(2)
        console.print("切换app")

    def screen_shot(self):
        self.driver.find(self.loc.screen_shot).click()
        console.print("任务截屏")

    def screen_shot_share(self):
        if self.driver.find(self.loc.screen_shot_share).is_visible() is not None:
            return console.print("截图可分享！")
        else:
            return console.print("元素未找到！")

    def clean_app_up(self):
        self.driver.find(self.loc.clean_app_up).click()
        console.print("全部清除")

    def click_back_navigation(self):
        self.driver.find(self.loc.back_navigation).click()
        console.print("返回")

    def get_navigation_status(self):
        ele = self.driver.find(self.loc.navigation_status).get_text()
        return ele

    def back_to_main(self):
        self.driver.find(self.loc.home_page_btn)
        console.print("主屏幕，主页")
