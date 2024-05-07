import time

from src.deps import *


class DesktopFolder(BasePage):
    """
    启动器
    """

    class loc:
        uninstall = Selector(XPath(has_text="Uninstall"),description="卸载")
        folder_name = Selector(XPath(id="com.android.launcher3:id/folder_name"),description="文件名")
        app_task = Selector(XPath(id="com.android.launcher3:id/snapshot"), description="应用任务")
        share = Selector(XPath(has_text="Share"), description="分享")
        clear_all = Selector(XPath(has_text=["CLEAR ALL","Clear all"]), description="清除所有")
        del_tips = Selector(XPath(has_text="Do you want to uninstall this app?"),description="卸载提示")
        screen = Selector(XPath(has_text="Screenshot"), description="截图")
        app_info = Selector(XPath(has_text="App info"),description="应用信息")
        widget = Selector(XPath(has_text="Widgets"),description="微件")
        disalbe = Selector(XPath(has_text="DISABLE"),description="禁用")
        memory_info = Selector(XPath(id="com.android.launcher3:id/recents_memoryinfo"), description="内存信息")
        scr_pic = Selector(XPath(id="com.android.systemui:id/global_screenshot_preview"), description="截图图片")
        class folder:
            """
            文件夹
            """

            apps = Selector(
                XPath(id="com.android.launcher3:id/folder_content").join(
                    "/descendant::android.widget.TextView"
                ),
                description="文件夹内的应用",
            )

        screenshot_preview = Selector(
            XPath(
                id=[
                    "com.android.systemui:id/global_screenshot_preview",
                    "com.android.systemui:id/screenshot_preview",
                ]
            ),
            description="截图预览",
        )

        apps = Selector(
            XPath(id="com.android.launcher3:id/workspace").join(
                "/descendant::android.view.ViewGroup/android.widget.TextView"
            ),
            description="桌面应用",
        )
        folders = Selector(
            XPath(id="com.android.launcher3:id/workspace").join(
                "/descendant::android.widget.FrameLayout/android.widget.TextView"
            ),
            description="桌面文件夹",
        )
        folders_1 = Selector(
            XPath(id="com.android.launcher3:id/workspace").join(
                "/descendant::android.widget.FrameLayout"
            ),
            description="桌面文件夹"
        )
        just_once = Selector(
            XPath(id="android:id/button_once", has_text="Just once"), description="仅此一次"
        )
        always = Selector(
            XPath(id="android:id/button_always", has_text="Always"), description="永远"
        )
        allow = Selector(
            XPath(
                id="com.android.permissioncontroller:id/permission_allow_button",
                has_text="ALLOW",
            ),
        )

        @staticmethod
        def open_with(name: str = None):
            return Selector(
                XPath(id="android:id/resolver_list").join(
                    "descendant::*", id="android:id/text1", has_text=name or True
                ),
                description="打开方式",
            )

        class settings:
            wifi = Selector(XPath(has_text=["Wi‑Fi", "WLAN"]), description="Wi‑Fi")
            data_usage = Selector(XPath(has_text="Data usage"), description="流量数据")
            battery = Selector(XPath(has_text="Battery"), description="电量")


    def get_apps(self):
        """
        获取应用列表
        """
        return self.driver.find_all(self.loc.apps)

    def get_app(self, name: str):
        """
        获取应用
        """
        return next(filter(lambda app: app.get_text() == name, self.get_apps()), None)

    def click_allow(self):
        if el := self.driver.find(self.loc.allow, timeout=2, exist_ok=True):
            el.click()
            console.print("点击允许")

    def click_wifi(self):
        self.driver.find(self.loc.settings.wifi).click()
        console.print("点击Wi-Fi")

    def click_data_usage(self):
        self.driver.find(self.loc.settings.data_usage).click()
        console.print("点击流量数据")

    def click_battery(self):
        self.driver.find(self.loc.settings.battery).click()
        console.print("点击电量")

    def click_open_with(self, name: str = None):
        if not (
            el := self.driver.find(self.loc.open_with(name), timeout=2, exist_ok=True)
        ):
            return False
        if name is None:
            name = el.get_text()
        el.click()
        console.print(f"点击打开方式：{name}")
        return True

    def click_always(self):
        self.driver.find(self.loc.always).click()
        console.print("点击永远")

    def click_scr(self):
        self.driver.find(self.loc.screen).click()
        console.print("点击截图")

    def click_clear_all(self):
        self.driver.find(self.loc.clear_all).click(delay=2)
        console.print("点击清除所有,并等待2秒")

    def get_del_tips(self):
        return self.driver.find(self.loc.del_tips,exist_ok=True,timeout=3)

    def get_memory_info(self):
        memory_info = self.driver.find(self.loc.memory_info).get_text()
        console.print("设备内存信息：" + memory_info)
        return memory_info

    def get_scr_pic(self):
        return self.driver.find(self.loc.scr_pic, timeout=5, exist_ok=True)

    def get_task(self):
        return self.driver.find(self.loc.app_task, exist_ok=True)

    def click_share(self):
        self.driver.find(self.loc.share).click()
        console.print("点击分享")

    def click_app_info(self):
        self.driver.find(self.loc.app_info).click()
        console.print("点击应用信息")

    def get_disalbe(self):
        return self.driver.find(self.loc.disalbe,exist_ok=True)

    def click_folders(self):
        self.driver.find(self.loc.folders_1,exist_ok=True,timeout=5).click()
        console.print("点击文件夹")

    def get_folders(self):
        return self.driver.find(self.loc.folders, exist_ok=True, timeout=5)

    def get_no_folders(self):
        return self.driver.find(self.loc.folders, exist_ok=False, timeout=5)

    def move_folders_app(self):
        console.print("移动文件夹的应用")
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(self.driver.find(self.loc.folder.apps),duration=2)
            actions.move_to_element_with_offset(self.driver.find(self.loc.folder.apps),
                    xoffset=0,
                    yoffset=-300,
                    duration=1,
            )
            #设备的偏移值后续可直接改对应的值 D3-504(0,-300,1)
            actions.release()

    def get_two_app(self):
        icon_elems = self.driver.find_all(self.loc.apps, timeout=2)
        origin_el, destination_el = icon_elems.nth(0), icon_elems.nth(1)
        names = (origin_el.get_text(), destination_el.get_text())
        console.print(f"前面两个APP名字为：{names}")
        return names

    def all_folders(self):
        return self.driver.find_all(self.loc.folders)


    def click_edit_name(self,text:str = "abcde"):
        self.driver.find(self.loc.folder_name).click()
        self.driver.find(self.loc.folder_name).fill(text)
        console.print("点击文件夹名，并重命名为：" + text)

    def merge_app(self):
        console.print("合并文件夹")
        icon_elems = self.driver.find_all(self.loc.apps, timeout=2)
        origin_el, destination_el = icon_elems.nth(0), icon_elems.nth(1)
        names = (origin_el.get_text(), destination_el.get_text())
        console.print(f"拖动APP：{names} 合并文件夹")
        console.print("先长按第一个应用，并稍微拖动")
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(origin_el, duration=4)
            actions.move_to_element_with_offset(origin_el,
                                                xoffset=0,
                                                yoffset=30,
                                                duration=1,
                                                )
            app_center = destination_el.centre
            x = app_center[0]
            y = app_center[1]
            actions.move_to_location(x,y)
            actions.release()

    def get_all_app(self):
        return self.driver.find_all(self.loc.apps, timeout=3).get_all_texts()

    def get_all_folders(self):
        return self.driver.find_all(self.loc.folders,timeout=10).get_all_texts()


    def open_first_folders(self):
        folders_all = self.driver.find_all(self.loc.folders_1, exist_ok=True,timeout=2)
        if folders_all.count() >1 :
            console.print("文件夹数量大于1")
            time.sleep(3)
            console.print(folders_all.first.get_text())
            folders_all.first.click()
            console.print("点击第一个文件夹")
        else:
            console.print("文件夹数量等于1")
            time.sleep(3)
            self.driver.find(self.loc.folders_1,exist_ok=True,timeout=5).click()
            console.print("点击文件夹")

    def get_last_app(self):
        icon_elems = self.driver.find_all(self.loc.apps, timeout=2)
        console.print("移动最后一个APP名：" + icon_elems.last.get_text())
        return icon_elems.last.get_text()

    def move_last_app(self):
        size = self.driver.get_window_size()
        icon_elems = self.driver.find_all(self.loc.apps, timeout=2)
        console.print("移动最后一个APP名：" + icon_elems.last.get_text() + "到另一个桌面")
        app = icon_elems.last
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(app, duration=3)
            actions.move_to_location(size.width * 0.99,size.height * 0.5)
            actions.release()

    def move_app_del(self):
        size = self.driver.get_window_size()
        app_icon = self.driver.find(self.loc.apps, timeout=2)
        uninstall = self.driver.find(self.loc.uninstall, exist_ok=True, timeout=10)
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(app_icon, duration=4)
            actions.move_to_element_with_offset(app_icon,
                                                xoffset=0,
                                                yoffset=40,
                                                duration=1,
                                                )
            actions.move_to_location(size.width * 0.65,size.height * 0.05)
            actions.release()

    def get_widget(self):
        return self.driver.find(self.loc.widget,exist_ok=True,timeout=10)










