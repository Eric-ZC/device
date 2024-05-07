from src.deps import *


class Language(BasePage):
    """
    语言页面
    """
    class loc:

        language_title = Selector(
            XPath(id='android:id/title', has_text="语言"),
            description="语言"
        )

        language_btn = Selector(
            XPath('//android.widget.TextView[@resource-id="android:id/title" and @text="语言"]'),
            description="语言按钮"
        )

        switch_language = Selector(
            XPath('(//android.widget.ImageView[@resource-id="com.android.settings:id/dragHandle"])[2]'),
            description="切换语言"
        )
        add_language = Selector(
            XPath(id='com.android.settings:id/add_language', has_text="添加语言"),
            description="添加语言"
        )
        search_language = Selector(
            XPath(id='android:id/locale_search_menu', has_content="搜索"),
            description="搜索"
        )
        search_bar = Selector(
            XPath(id='android:id/search_src_text',has_text="输入语言名称"),
            description="输入语言名称"
        )
        search_result = Selector(
            XPath(id='android:id/locale',has_content='英语'),
            description="搜索结果"
        )
        select_accent = Selector(
            XPath(id='android:id/locale',has_content="美国")
        )

        toolbar_content = Selector(
            XPath(id='com.android.settings:id/collapsing_toolbar'),
            description="工具栏"
        )

        secondary_screen = Selector(
            XPath(id="com.android.settings:id/content_parent"),
            description="副屏"
        )

    def get_size_secondary_screen(self):
        """
        获取副屏尺寸
        """
        size = self.driver.find(self.loc.secondary_screen).size
        return size

    def get_centre_secondary_screen(self):
        """
        获取副屏中心轴
        """
        centre = self.driver.find(self.loc.secondary_screen).centre
        return centre

    def find_secondary_screen(self):
        """
        判断副屏情况
        """
        if self.driver.find(self.loc.secondary_screen, exist_ok=True, timeout=5):
            return True
        return False

    def secondary_screens_ele(self, ele):

        self.find_secondary_screen()
        size = self.get_size_secondary_screen()
        centre = self.get_centre_secondary_screen()
        console.print(size)
        console.print(centre)
        x = size['width']
        y = size['height']
        start_x = centre[0]
        start_y = centre[1]
        print(x, y, x, start_y)
        return self.driver.find(ele, timeout=10, scroll_on=centre, autodiscovery="down")

    def get_toolbar_content(self):
        """
        返回工具栏标题
        """
        if self.find_secondary_screen():
            console.print("存在副屏")
            element = self.secondary_screens_ele(self.loc.toolbar_content)
        else:
            console.print("不存在副屏")
            element = self.driver.find(self.loc.toolbar_content)

        return element.get_attribute("content-desc")

    def click_language_btn(self):
        self.driver.find(self.loc.language_btn).click()
        console.print("点击语言")

    def click_language_title(self):
        self.driver.find(self.loc.language_title, timeout=5).click()
        console.print("点击语言按钮")

    def switch_language(self):

        ele = self.driver.find(self.loc.switch_language)
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(ele, duration=2)
            actions.move_to_location(666, 300, duration=3)
            actions.release()

    def switch_language_android_11(self):

        ele = self.driver.find(self.loc.switch_language)
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(ele, duration=2)
            actions.move_to_location(666, 150, duration=3)
            actions.release()

    def click_add_language(self):
        self.driver.find(self.loc.add_language, timeout=5).click()
        console.print("添加语言")

    def click_search_content(self):

        self.driver.find(self.loc.search_language, timeout=5).click()
        console.print("点击查询框")
        self.driver.find(self.loc.search_bar, timeout=5).fill("English")
        console.print("查询english")
        self.driver.find(self.loc.search_result, timeout=5).click()
        console.print("选择查询结果")
        self.driver.find(self.loc.select_accent, timeout=5).click()
        console.print("选择美式英语")