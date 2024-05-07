import time

from src.deps import *


class DataTime(BasePage):
    """
    日期和时间
    """

    class loc:

        data_time = Selector(
            XPath(has_text="日期和时间"),
            description="日期和时间"
        )
        time_zone = Selector(
            XPath('(//android.widget.Switch[@resource-id="android:id/switch_widget"])[2]'),
            description="自动设置时区"
        )
        time_zone_btn = Selector(
            XPath('(//android.widget.TextView[@resource-id="android:id/title"])[6]'),
            description="时区"
        )
        time_zone_btn_oir = Selector(
            XPath('(//android.widget.TextView[@resource-id="android:id/title"])[5]'),
            description="时区"
        )
        zone = Selector(
            XPath( id ="android:id/title",has_text="区域"),
            description="区域"
        )
        time_zone_android11 = Selector(
            XPath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[4]')
            .join("/descendant::android.widget.TextView[@resource-id=\"android:id/title\" and @text=\"时区\"]"),
            description="时区"
        )
        search_src = Selector(
            XPath(id="android:id/search_src_text",has_text="搜索区域"),
            description="搜索区域"
        )
        search_result = Selector(
            XPath(id="android:id/title",has_text="英国"),
            description="搜索结果"
        )

        zone_result = Selector(XPath("android.widget.TextView", has_text="区域").join(
            "/following-sibling::android.widget.TextView"
        ),
            description="区域地址",
        )
        current_time_zone = Selector(XPath(id="android:id/title",has_text="时区").join(
            "/following-sibling::android.widget.TextView"
        ),
            description="当前时区"
        )


    def click_data_time(self):
        self.driver.find(self.loc.data_time).click()
        console.print("日期和时间")

    def switch_time_zone(self):
        self.driver.find(self.loc.time_zone).click()
        console.print("自动设置时区")

    def time_zone_click(self):
        ele = self.driver.find(self.loc.time_zone_btn).is_enabled()
        if ele is True:
            console.print("当前时区为手动")
            self.switch_time_zone()
        else:
            console.print("当前时区为自动")

    def click_zone(self):
        self.driver.find(self.loc.zone).click()
        console.print("选择区域")

    def search_src(self, text="英国"):
        self.driver.find(self.loc.search_src).fill(text)
        self.driver.find(self.loc.search_result,timeout=5).click()
        console.print("切换英国时区")

    def zone_result(self):
        console.print("选择返回时区")
        return self.driver.find(self.loc.zone_result,timeout=5).get_text()

    def current_time_zone(self):
        console.print("返回当前时区")
        return self.driver.find(self.loc.current_time_zone,timeout=5).get_text()

    def click_time_zone_btn(self):
        console.print("点击时区")
        self.driver.find(self.loc.time_zone_btn, timeout=5).click()

    def click_time_zone_btn_oir(self):
        console.print("横屏点击时区")
        self.driver.find(self.loc.time_zone_btn_oir, timeout=5).click()

    def click_time_zone_android11(self):
        self.driver.find(self.loc.time_zone_android11, timeout=5).click()
        console.print("点击时区")