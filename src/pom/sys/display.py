from typing import Optional

from src.deps import *


class Display(BasePage):
    """
    显示设置页
    """

    class loc:

        screen_timeout = Selector(XPath(has_text="屏幕超时"), description="屏幕超时")

        primary_screen_brightness_level = Selector(
            XPath(has_text=["Primary screen brightness level", "Brightness level"]),
            description="主屏亮度",
        )
        brightness_bar = Selector(
            XPath(id="android:id/content"),
            description="亮度条",
        )

        wallpaper_btn = Selector(
            XPath(has_text="主屏幕、锁定屏幕"),
            description="主屏幕、锁定屏幕"
        )
        wallpaper_android11 =Selector(
            XPath(has_text="壁纸",id="android:id/title"),
            description="壁纸"
        )

        select_wallpaper = Selector(
            XPath('//android.widget.TextView[@resource-id="android:id/title" and @text="壁纸"]'),
            description="壁纸"
        )

        wallpaper_options = Selector(
            XPath(has_content="第2张壁纸，共16张"),
            description="第2张壁纸，共16张"
        )

        wallpaper_options_oir = Selector(
            XPath(has_content="第3张壁纸，共16张"),
            description="第3张壁纸，共16张"
        )
        wallpaper_options_swan = Selector(
            XPath("//android.widget.FrameLayout[@content-desc=\"第3张壁纸，共16张\"]"),
            description="第3张壁纸，共16张"
        )
        wallpaper_options_d5 = Selector(
            XPath("//android.widget.FrameLayout[@content-desc=\"第3张壁纸，共16张\"]"),
            description="第1张壁纸，共1张"
        )

        setting_wallpaper_oir = Selector(
            XPath(id="com.android.wallpaperpicker:id/wallpaper_set",has_text="设置壁纸"),
            description="设置壁纸"
        )

        setting_wallpaper_d5 = Selector(
            XPath(id="com.android.wallpaperpicker:id/wallpaper_set",has_text="设置壁纸"),
            description="设置壁纸"
        )

        setting_wallpaper = Selector(
            XPath(has_text="设置壁纸"),
            description="设置壁纸"
        )

        setting_main_wallpaper = Selector(
            XPath(has_text="主屏幕"),
            description="主屏幕"
        )

        mian_screen_bright = Selector(
            XPath(id='android:id/seekbar',has_content='主屏亮度'),
            description="主屏幕亮度"
        )
        secondary_screen_bright = Selector(
            XPath(id='android:id/seekbar',has_content='副屏亮度'),
            description="副屏幕亮度"
        )
        main_android11 = Selector(
            XPath(id="android:id/title", has_text="主屏亮度"),
            description="主屏亮度"
        )
        android11_bar = Selector(
            XPath("//android.widget.SeekBar[@resource-id=\"com.android.systemui:id/slider\"]"),
            description="亮度条"
        )
        secondary_android11 = Selector(
            XPath(id="android:id/title", has_text="副屏亮度"),
            description="副屏亮度"
        )

        @staticmethod
        def screen_timeout_options(value: str = None):
            return Selector(
                XPath(id="com.android.settings:id/action_bar_root").join(
                    "descendant::android.widget.CheckedTextView",
                    has_text=value or True,
                ),
                description="超时设置选项",
            )

    def click_primary_screen_brightness_level(self):
        self.driver.find(self.loc.primary_screen_brightness_level).click()
        console.print("点击主屏亮度")

    def click_screen_timeout(self):
        self.driver.find(self.loc.screen_timeout).click(delay=2)
        console.print("点击屏幕超时")

    # def click_advanced(self):
    #     self.driver.find(self.loc.advanced).click()
    #     console.print("点击屏幕超时")

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

    def select_screen_timeout(self, value: Optional[str]):
        if value is None:
            for option in self.driver.find_all(self.loc.screen_timeout_options()):
                value = option.get_text()
                if "never" in value.lower():
                    option.click()
                    break
        else:
            self.driver.find(self.loc.screen_timeout_options(value)).click()
        console.print(f"选择屏幕超时：{value}")

    def click_wallpaper(self):
        self.driver.find(self.loc.wallpaper_btn).click()
        console.print("点击主屏幕、锁定屏幕")

    def select_wallpaper(self):
        self.driver.find(self.loc.select_wallpaper).click()
        console.print("来源方式选择壁纸")

    def wallpaper_options(self):
        self.driver.find(self.loc.wallpaper_options).click()
        console.print("选择壁纸")

    def wallpaper_options_oir(self):
        self.driver.find(self.loc.wallpaper_options_oir,exist_ok=True ,timeout=10).click()
        console.print("选择壁纸")

    def wallpaper_options_swan(self):
        self.driver.find(self.loc.wallpaper_options_swan).click()
        console.print("选择壁纸")

    def wallpaper_options_d5(self):
        self.driver.find(self.loc.wallpaper_options_d5).click()
        console.print("选择壁纸")

    def setting_wallpaper_oir(self):
        self.driver.find(self.loc.setting_wallpaper_oir).click()
        console.print("设置壁纸")

    def setting_wallpaper(self):
        self.driver.find(self.loc.setting_wallpaper).click()
        console.print("设置壁纸")

    def setting_wallpaper_d5(self):
        self.driver.find(self.loc.setting_wallpaper_d5).click()
        console.print("设置壁纸")

    def setting_main_wallpaper(self):
        self.driver.find(self.loc.setting_main_wallpaper,timeout=5).click()
        console.print("设置主屏幕壁纸")

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

    def main_brightness_android11(self):
        self.driver.find(self.loc.main_android11).click()
        console.print("主屏亮度")

    def secondary_brightness_android11(self):
        self.driver.find(self.loc.secondary_android11).click()
        console.print("副屏亮度")

    def brightness_bar(self, percentage: float):
        """
        拖动亮度条
        1为最大，0为最小
        """
        bar = self.driver.find(self.loc.android11_bar)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

    def click_wallpaper_android11(self):
        self.driver.find(self.loc.wallpaper_android11).click()
        console.print("点击壁纸")