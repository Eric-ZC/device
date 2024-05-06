import re
import time

import math

from soium import Keys

from src.deps import *


class Settings(BasePage):
    """
    设置页
    """

    class loc:
        menu = Selector(
            XPath(id="com.android.settings:id/settings_homepage_container"),
            description="设置菜单",
        )
        options = Selector(
            XPath(id="com.android.settings:id/content_parent"), description="菜单选项"
        )
        current_sound = Selector(
            XPath(has_text="Default notification sound").join(
                "/following-sibling::android.widget.TextView"
            ),
            description="当前提示音"
        )
        default_sound = Selector(
            XPath(has_text="Default notification sound"),
            description="设备提示音"
        )
        add_notification = Selector(
            XPath(has_text="Add notification"),
            description="添加通知音"
        )
        ok = Selector(XPath(has_text="OK"), description="OK")
        apps = Selector(XPath(has_text="Apps & notifications"), description="应用和通知")
        battery = Selector(XPath(has_text="电池"), description="电池")
        display = Selector(XPath(has_text="显示"), description="显示")
        storage = Selector(XPath(has_text="存储"), description="存储")
        connected_devices = Selector(
            XPath(has_text="已连接的设备"), description="已连接的设备"
        )

        about_device = Selector(XPath(has_text="关于设备"), description="关于设备")

        network = Selector(XPath(has_text="网络和互联网"), description="网络")
        sound = Selector(XPath(has_text="提示音"), description="声音")
        sound_android11 = Selector(XPath(id="android:id/title",has_text="声音"))
        system = Selector(XPath(has_text="系统", exact=True), description="系统")
        search_btn = Selector(
            XPath(has_content="Search settings"), description="搜索按钮"
        ).or_(XPath(has_text="Search settings"))
        search_input = Selector(
            XPath(id="android:id/search_src_text"), description="搜索框"
        )
        search_bar = Selector(
            XPath(id="com.android.settings:id/search_bar"), description="搜索栏"
        )
        search_clear_btn = Selector(
            XPath(id="android:id/search_close_btn"), description="清除按钮"
        )
        search_results = Selector(
            XPath(id="com.android.settings.intelligence:id/list_results").join(
                "android.widget.LinearLayout"
            ),
            description="搜索结果",
        )
        search_menu = Selector(
            XPath(id="com.android.settings.intelligence:id/search_toolbar").join(
                "android.widget.LinearLayout/android.widget.ImageButton"
            ),
            description="搜索菜单",
        )
        clear_history = Selector(XPath(has_text="Clear history"), description="清除历史记录")
        choose_music = Selector(XPath(has_text="Choose music track"),description="选择音乐")
        sound_list = Selector(
            XPath(id="com.android.soundpicker:id/checked_text_view"),
            description="声音列表"
        )

        music_list = Selector(
            XPath(id="com.android.music:id/line1"),
            description="音乐名"
        )
        none_sound = Selector(XPath(id="android:id/text1"),description="空提示音")

        security_btn = Selector(XPath(has_text="安全"), description="安全")

        screen_lock = Selector(XPath("android.widget.TextView",has_text="屏幕锁定"), description="屏幕锁定")

        screen_lock_status = Selector(XPath("android.widget.TextView",has_text="屏幕锁定").join
                                      ("/following-sibling::android.widget.TextView"),
                                      description="锁屏状态"
        )


        confirm_btn = Selector(XPath(has_text="确认"), description="确认")

        setp_btn = Selector(XPath(has_text="下一步"), description="下一步")

        accomplish_btn = Selector(XPath(has_text="完成"), description="完成")





        build_number = Selector(XPath(has_text="版本号"), description="版本号")

        developer_options = Selector(XPath(has_text="开发者选项"), description="开发者选项")

        setting_memroy = Selector(XPath(id="com.android.settings:id/usage_summary"),description="储存内存")


        language = Selector(
            XPath(has_text="语言和输入法"),
            description="语言和输入法"
        )


        select_language = Selector(
            XPath(id="com.android.settings:id/dragHandle"),
            description="选择语言"
        )

        reset_wlan_network_bluetooth = Selector(
            XPath(has_text="重置 WLAN、移动数据网络和蓝牙设置"),
            description="重置 WLAN、移动数据网络和蓝牙设置"
        )


        main_screen = Selector(
            XPath(id="com.android.settings:id/homepage_container"),
            description="主屏"
        )


        @staticmethod
        def list(name: str = None, exact: bool = True, description: str = None):
            return Selector(
                XPath(id="com.android.soundpicker:id/checked_text_view").join(
                    has_text=name, exact=exact
                ),
                description=description or "音乐列表",
            )

    def find_main_screen(self):
        if self.driver.find(self.loc.main_screen, exist_ok=True, timeout=5):
            return True
        return False

    def get_size_main_screen(self):
        size = self.driver.find(self.loc.main_screen).size
        return size

    def get_centre_main_screen(self):
        centre = self.driver.find(self.loc.main_screen).centre
        return centre

    def main_screen_ele(self, ele):

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

    def click_system(self):

        if self.find_main_screen():
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.system)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.system)

        elements.click()

    def click_battery(self):
        self.driver.find(self.loc.battery,autodiscovery="down").click()
        console.print("点击电池")

    def click_display(self):
        if self.find_main_screen():
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.display)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.display)

        elements.click()

    def click_sound(self):
        if self.find_main_screen():
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.sound)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.sound)
        elements.click()

    def click_sound_android11(self):
        self.driver.find(self.loc.sound_android11,autodiscovery="down").click()
        console.print("点击音量")

    def click_storage(self):
        if self.find_main_screen():
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.storage)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.storage)

        elements.click()

    def click_connected_devices(self):
        self.driver.find(
            self.loc.connected_devices, autodiscovery="down"
        ).click()
        console.print("点击已连接的设备")

    def click_about_device(self):

        if self.find_main_screen() :
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.about_device)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.about_device)

        elements.click()


    def click_apps(self):
        self.driver.find(self.loc.apps,autodiscovery="down").click()
        console.print("点击应用和通知")

    def click_ok(self):
        self.driver.find(self.loc.ok).click()
        console.print("点击确认")

    def click_network(self):
        self.driver.find(self.loc.network).click()
        console.print("点击网络")

    def click_search_bar(self):
        self.driver.find(self.loc.search_bar).click()
        console.print("点击搜索栏")

    def click_search_input(self):
        self.driver.find(self.loc.search_input).click()
        console.print("点击搜索框")

    def click_search_btn(self):
        self.driver.find(self.loc.search_btn).click()
        console.print("点击搜索按钮")

    def click_clear(self):
        self.driver.find(self.loc.search_clear_btn).click()
        console.print("点击清除按钮")

    def click_search_menu(self):
        self.driver.find(self.loc.search_menu).click()
        console.print("点击搜索菜单")

    def click_clear_history(self):
        self.driver.find(self.loc.clear_history).click()
        console.print("点击清除历史记录")

    def click_sounds(self):
        self.driver.find(self.loc.default_sound).click()
        console.print("点击提示音")

    def get_search_text(self):
        """
        获取搜索框中的文本
        """
        return self.driver.find(self.loc.search_input).get_text()

    def get_search_results(self):
        """
        获取搜索结果
        """
        return self.driver.find_all(self.loc.search_results, timeout=2)

    def get_sounds(self):
        return self.driver.find(self.loc.current_sound, timeout=5).get_text()

    def select_random_sound(self):
        random_sound = self.driver.find_all(self.loc.sound_list).random
        random_sound.click()
        console.print("随机选中提示音：" + random_sound.get_text() + "并点击")
        return random_sound.get_text()

    def get_sound_count(self):
        return self.driver.find_all(self.loc.list()).count()

    def select_random_music(self):
        random_music = self.driver.find_all(self.loc.music_list).random
        random_music.click()
        console.print("随机选中提示音：" + random_music.get_text() + "并点击")
        return random_music.get_text()

    def select_none_sound(self):
        self.driver.find(self.loc.none_sound,autodiscovery="down",timeout=60).click()
        console.print("选中无提示音，并点击")

    def click_add_sounds(self):
        self.driver.find(self.loc.add_notification,autodiscovery="down",timeout=60).click()
        console.print("点击添加通知")

    def click_list(self,text):
        self.driver.find(self.loc.list(text),autodiscovery="down",timeout=60).click()
        console.print("选择提示音"+str(text))

    def click_choose_music(self):
        self.driver.find(self.loc.choose_music).click()
        console.print("点击选择音乐")

    def search(self, text: str):
        self.driver.find(self.loc.search_input).fill(text)
        self.driver.press_keycode(Keys.ENTER)
        console.print(f"搜索 {text}")

    def click_security(self):
        if self.find_main_screen():
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.security_btn)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.security_btn)

        elements.click()

    def click_next_step(self):
        self.driver.find(self.loc.setp_btn).click()
        console.print("下一步")

    def click_confirm(self):
        self.driver.find(self.loc.confirm_btn).click()
        console.print("确定")

    def click_accomplish(self):
        self.driver.find(self.loc.accomplish_btn).click()
        console.print("完成设定")




    def developer_options(self):
        if self.driver.find(self.loc.developer_options,timeout=2, exist_ok=True).is_visible() is None:
            return False
        console.print("开发者选项可见")
        return True


    def get_setting_memroy(self):

        text = self.driver.find(self.loc.setting_memroy,timeout=10).get_text()

        match = re.search(r'\d+', text)
        if match:
            extracted_number = match.group()
            return extracted_number
        else:
            print("未找到匹配的数字")

    def click_language(self):
        if self.find_main_screen():
            console.print("存在主屏")
            elements = self.main_screen_ele(self.loc.language)
        else:
            console.print("不存在主屏")
            elements = self.driver.find(self.loc.language)

        elements.click()

    def select_language(self):
        self.driver.find(self.loc.language).click()
        console.print("语言设输入法")




