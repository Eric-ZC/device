import time
import re
from src.deps import *


class Diagnosis(BasePage):

    class loc:

        used_memory = Selector(
            XPath('//android.widget.TextView[@resource-id="com.neostra.hardwarehousekeeper:id/tv_sd"]'),
            description="已使用内存",
        )
        net_work_btn = Selector(
            XPath(has_text="网络"),

            description="网络"
        )
        network_icon = Selector(XPath(
            id='com.neostra.hardwarehousekeeper:id/iv_function_icon'),
            description="网络icon"
        )
        voice_icon = Selector(XPath(
            id='com.neostra.hardwarehousekeeper:id/tv_fuction_name',has_text="声音").join('/preceding-sibling:: android.widget.ImageView'),
            description='声音icon')


        display_icon = Selector(XPath(
            id='com.neostra.hardwarehousekeeper:id/tv_fuction_name',has_text="显示屏").join('/preceding-sibling:: android.widget.ImageView'),
            description='显示icon')
        voice_btn = Selector(
            XPath(has_text="声音"),

            description="声音"
        )

        display_btn = Selector(
            XPath(has_text="显示屏"),

            description="显示器"
        )

        speed_text = Selector(
            XPath(id="com.neostra.test.basic:id/speed_text"),

            description="网速"
        )
        speed_text_oir = Selector(
            XPath(id = 'com.neostra.hardwarehousekeeper:id/speed_text'),
            description="网速"
        )

        start_btn = Selector(
            XPath(has_text="开始测试"),

            description="开始测试网速"
        )
        restart_btn = Selector(
            XPath(has_text="重新测试"),

            description="重新测试"
        )
        MusicSeekBar = Selector(
            XPath(id="com.neostra.test.basic:id/MusicSeekBar"),

            description="音乐条"
        )

        voice_test = Selector(
            XPath(id="com.neostra.test.basic:id/voice_test_pass"),

            description="听到"
        )
        start_lcd_btn = Selector(
            XPath(id="com.neostra.test.basic:id/start_lcd_test"),

            description="开始测试"
        )
        start_lcd_btn_oir = Selector(
            XPath(id="com.neostra.hardwarehousekeeper:id/start_lcd_test",has_text="开始测试"),
            description="开始测试"
        )
        voice_bar = Selector(
            XPath(id="com.neostra.test.basic:id/MusicSeekBar"),
            description="音乐条"
        )
        voice_bar_oir = Selector(
            XPath(id="com.neostra.hardwarehousekeeper:id/MusicSeekBar"),
            description="音乐条"
        )

        display_pass = Selector(
            XPath(id="com.neostra.test.basic:id/display_test_pass"),
            description="正常"
        )


    def get_used_memory(self):
        console.print("获取内存容量")
        text = self.driver.find(self.loc.used_memory).get_text()
        match  = re.search(r'已用:(\d+\.\d+)GB', text)
        if match:
            used_memory = float(match.group(1))
            used_memory_int = int(used_memory)
            return used_memory_int
        else:
            print("未找到匹配的数字")

    def click_network_mian(self):
        self.driver.find(self.loc.net_work_btn).click()
        console.print("点击网络")

    def click_voice_btn(self):
        self.driver.find(self.loc.voice_btn).click()
        console.print("点击声音")

    def click_display_btn(self):
        self.driver.find(self.loc.display_btn).click()
        console.print("点击显示")

    def get_network_speed(self):
        time.sleep(10)
        console.print("获取网速")
        return self.driver.find(self.loc.speed_text).get_text()

    def click_network_btn(self):
        self.driver.find(self.loc.start_btn,timeout=600).click()
        console.print("开始测试,最长60")

    def click_lcd_btn(self):
        self.driver.find(self.loc.start_lcd_btn).click()
        console.print("开始测试")

    def get_restart(self):
        self.driver.find(self.loc.restart_btn, exist_ok=True, timeout=600)
        console.print("重新测试")

    def drag_voice_bar(self, percentage: float):

        bar = self.driver.find(self.loc.voice_bar)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

    def click_voice_test(self):
        self.driver.find(self.loc.voice_test).click()
        console.print("听到")

    def display_test(self):
        self.driver.find(self.loc.display_pass).is_visible()
        self.driver.find(self.loc.display_pass).click()
        console.print("正常")

    def click_network_icon(self):
        self.driver.find(self.loc.network_icon).click()
        console.print('点击网络')

    def click_vocie_icon(self):
        self.driver.find(self.loc.voice_icon).click()
        console.print("点击声音")

    def click_display_icon(self):
        self.driver.find(self.loc.display_icon).click()
        console.print("点击显示")

    def get_speed_text_oir(self):
        time.sleep(30)
        return self.driver.find(self.loc.speed_text_oir).get_text()

    def drag_voice_bar_oir(self, percentage: float):

        bar = self.driver.find(self.loc.voice_bar_oir)
        width = bar.size["width"]
        offset = width * percentage - width / 2
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0).release()

    def click_start_lcd_btn_oir(self):
        self.driver.find(self.loc.start_lcd_btn_oir).click()