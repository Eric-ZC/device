import time

from soium import Keys

from src.deps import *


class Chrome(BasePage):
    """
    谷歌浏览器
    """

    class loc:

        search_bar = Selector(
            XPath(has_text="搜索或输入网址"),
            description="网址地址搜索框"
        )
        editor_address = Selector(
            XPath(has_text="搜索或输入网址"),
            description="编辑网址"
        )
        web_title = Selector(
            XPath('//android.view.View[@content-desc="YouTube"]'),
            description="网站标题"
        )
        home_page = Selector(
            XPath(has_content="首页"),
            description="主页"
        )
        more_btn = Selector(
            XPath(id="com.android.chrome:id/menu_button"),
            description="菜单按钮"
        )
        download_btn = Selector(
            XPath(has_content="下载内容"),
            description="下载内容"
        )
        close_btn = Selector(
            XPath(has_content="关闭"),
            description="下载内容"
        )
        addto_main_screen = Selector(
            XPath(has_content="添加到主屏幕"),
            description="添加到主屏幕"
        )
        home_page_back = Selector(
            XPath(has_content="打开主页",id="com.android.chrome:id/home_button"),
            description="打开主页"
        )
        logo = Selector(
            XPath(id="com.android.chrome:id/logo_holder"),
            description="google logo"
        )
        add_confirm = Selector(
            XPath(id="com.android.chrome:id/positive_button"),
            description="添加"
        )
        add_main_screen = Selector(
            XPath(has_text="添加到主屏幕"),
            description="添加到主屏幕"
        )
        d4_504_pro_home_page = Selector(
            XPath(id="com.android.chrome:id/home_button", has_content="首页"),
            description="首页"
            )
        advertising_privacy_settings = Selector(
            XPath(has_text="在 Chrome 中加强广告隐私设置"),
            description="在 Chrome 中加强广告隐私设置"
        )
        ack_know = Selector(
            XPath(id="com.android.chrome:id/ack_button", has_text="知道了"),
            description="知道了"
        )
        welcome_title = Selector(
            XPath(id="com.android.chrome:id/title", has_text="欢迎使用 Chrome"),
            description="欢迎使用 Chrome"
        )
        signin_fre = Selector(
            XPath(id="com.android.chrome:id/signin_fre_dismiss_button",has_text="在不登录账号的情况下使用"),
            description="在不登录帐号的情况下使用"
        )
        no_thanks_btn = Selector(
            XPath(id="com.android.chrome:id/negative_button", has_text="不用了，谢谢"),
            description="不用了，谢谢"
        )
        select_search = Selector(
            XPath(id="com.android.chrome:id/button_secondary",has_text="继续使用 Google"),
            description="继续使用 Google"
        )
        tab_switch = Selector(
            XPath(id="com.android.chrome:id/tab_switcher_button",has_content="切换或关闭标签页"),
            description="切换或关闭标签页"
        )
        close_tab = Selector(
            XPath(id="com.android.chrome:id/action_button",has_content="关闭“打开新的标签页”标签页"),
            description="关闭“首页 - YouTube”标签页"
        )
        open_new_tab = Selector(
            XPath(has_content="打开新的标签页"),
            description="打开新的标签页"
        )
        refresh = Selector(
            XPath(id="com.android.chrome:id/button_five",has_content="刷新"),
            description="刷新"
        )
        bookmarks = Selector(
            XPath(id="com.android.chrome:id/all_bookmarks_menu_id"),
            description="书签"
        )
        last_open = Selector(
            XPath(id="com.android.chrome:id/recent_tabs_menu_id"),
            description="最近打开的标签页"
        )
        open_history = Selector(
            XPath(id="com.android.chrome:id/open_history_menu_id"),
            description="历史记录"
        )
        desktop_site = Selector(
            XPath(id="com.android.chrome:id/request_desktop_site_id"),
            description="桌面版网站"
        )
        open_tab = Selector(
            XPath(id="com.android.chrome:id/new_tab_menu_id"),
            description="打开新页签"
        )
        link = Selector(
            XPath(id="com.android.chrome:id/mv_tiles_layout").join(
                "/descendant::android.widget.FrameLayout"),
            description="第一个链接"
        )
        hold_open_tab = Selector(
            XPath(id="android:id/title", has_text="在新标签页中打开"),
            description="在新标签页中打开"
        )
        hold_open_incognito = Selector(
            XPath(id="android:id/title", has_text="在无痕式标签页中打开"),
            description="在无痕式标签页中打开"
        )
        hold_download_link = Selector(
            XPath(id="android:id/title", has_text="下载链接"),
            description="下载链接"
        )
        hold_delete_link = Selector(
            XPath(id="android:id/title", has_text="移除"),
            description="移除"
        )
        open_incognito = Selector(
            XPath(id="com.android.chrome:id/title",has_content="打开新的无痕式标签页"),
            description="打开新的无痕式标签页"
        )
        share_btn = Selector(
            XPath(id="com.android.chrome:id/title",has_content="分享…"),
            description="分享"
        )
        find_in_page = Selector(
            XPath(id="com.android.chrome:id/find_in_page_id"),
            description="在网页中查找"
        )
        setting = Selector(
            XPath(id="com.android.chrome:id/preferences_id"),
            description="设置"
        )
        help_feedback = Selector(
            XPath(id="com.android.chrome:id/help_id"),
            description="帮助和反馈"
        )
        search_engines = Selector(
            XPath(id="android:id/title",has_text="搜索引擎"),
            description="搜索引擎"
        )
        password_tools = Selector(
            XPath(id="android:id/title", has_text="密码管理工具"),
            description="密码管理工具"
        )
        pay_way = Selector(
            XPath(id="android:id/title", has_text="付款方式"),
            description="付款方式"
        )
        address = Selector(
            XPath(id="android:id/title", has_text="地址和其他信息"),
            description="地址和其他信息"
        )
        setting_homepage = Selector(
            XPath(id="android:id/title", has_text="主页"),
            description="主页"
        )
        style_background = Selector(
            XPath(id="android:id/title", has_text="主题背景"),
            description="主题背景"
        )
        privacy_settings = Selector(
                XPath(id="android:id/title",has_text="隐私设置和安全性"),
                description="隐私设置和安全性"
            )
        accessibility = Selector(
            XPath(id="android:id/title", has_text="无障碍"),
            description="无障碍"
        )
        download_content = Selector(
            XPath(id="android:id/title", has_text="下载内容"),
            description="下载内容"
        )
        notification = Selector(
            XPath(id="android:id/title", has_text="通知"),
            description="通知"
        )
        bookmarks_sign = Selector(
            XPath(id="com.android.chrome:id/button_two",has_content="添加书签"),
            description="添加书签"
        )
        mobile_bookmark = Selector(
            XPath(id="com.android.chrome:id/title",has_text="移动设备书签"),
            description="移动设备书签"
        )
        select_bookmark = Selector(
            XPath(id="com.android.chrome:id/selectable_list_recycler_view").join(
                "/descendant::android.widget.FrameLayout"),
            description="第一个书签"
        )
        bookmarks_setting = Selector(
            XPath(id="com.android.chrome:id/more"),
            description="书签设置"
        )
        bookmarks_edit = Selector(
            XPath(id="com.android.chrome:id/menu_item_text",has_text="编辑"),
            description="编辑"
        )
        bookmarks_delete = Selector(
            XPath(id="com.android.chrome:id/menu_item_text",has_text="删除"),
            description="删除"
        )
        bookmarks_move = Selector(
            XPath(id="com.android.chrome:id/app_menu_list").join("/descendant::android.widget.LinearLayout[-1]"),
            description="移动书签"
        )
        search_result = Selector(
            XPath("//androidx.recyclerview.widget.RecyclerView[@resource-id=\"com.android.chrome:id/omnibox_suggestions_dropdown\"]").
            join("android.view.ViewGroup"),
            description="查询结果"
        )

    def click_search_bar(self):
        time.sleep(5)
        self.driver.find(self.loc.search_bar).click()
        console.print("点击搜索栏")

    def editor_address(self, text):
        self.driver.find(self.loc.editor_address).fill(text)
        time.sleep(5)
        self.driver.find_all(self.loc.search_result).random.click()
        time.sleep(10)
        console.print(f"搜索 {text}")

    def web_title(self):
        self.driver.find(self.loc.web_title, timeout=20).get_text()
        console.print("网站标题")

    def goto_homepage(self):
        self.driver.find(self.loc.home_page).click()
        console.print("返回主页")

    def click_more_btn(self):
        self.driver.find(self.loc.more_btn).click()
        console.print("点击更多按钮")

    def click_download_btn(self):
        self.driver.find(self.loc.download_btn).click()
        console.print("点击下载内容")

    def addto_main_screen(self):
        self.driver.find(self.loc.addto_main_screen).click()
        console.print("添加到主屏幕")

    def click_home_page_back(self):
        ele = self.driver.find(self.loc.home_page_back,exist_ok=True,timeout=5)
        if ele:
            ele.click()
        console.print("返回到主页")

    def click_add_confirm(self):
        self.driver.find(self.loc.add_confirm).click()
        self.driver.find(self.loc.add_main_screen,timeout=5).click()
        console.print("确认添加")

    def click_close_btn(self):
        self.driver.find(self.loc.close_btn).click()
        console.print("点击关闭")

    def click_home_page(self):
        self.driver.find(self.loc.home_page, exist_ok=True, timeout=5).click()
        console.print("返回主页")

    def click_d4_504_pro_home_page(self):
        ele = self.driver.find(self.loc.d4_504_pro_home_page,exist_ok=True,timeout=5)
        if ele:
            ele.click()
        console.print("点击主页")

    # def advertising_privacy_settings(self):
    #     self.driver.find(self.loc.advertising_privacy_settings, exist_ok=True)
    #     ele = self.driver.find(self.loc.ack_know, exist_ok=True)
    #     if ele is not None:
    #         ele.click()
    #     console.print("隐私广告")

    def chrome_init(self):
        self.driver.find(self.loc.welcome_title,exist_ok=True)
        ele = self.driver.find(self.loc.signin_fre,timeout=5,exist_ok=True)
        if ele is not None:
            ele.click()
        ele = self.driver.find(self.loc.ack_know,timeout=5, exist_ok=True)
        if ele is not None:
            ele.click()
        ele1 = self.driver.find(self.loc.no_thanks_btn,timeout=10,exist_ok=True)
        if ele1 is not None:
            ele1.click()
        ele = self.driver.find(self.loc.select_search, timeout=5, exist_ok=True)
        if ele is not None:
            ele.click()
        console.print("谷歌启动初始化")

    def click_tab_switch(self):
        self.driver.find(self.loc.tab_switch).click()
        console.print("页签切换")

    def click_close_tab(self):
        self.driver.find(self.loc.close_tab).click()
        console.print("关闭页签")

    def click_open_new_tab(self):
        self.driver.find(self.loc.open_new_tab).click()
        console.print("打开新标签")

    def click_refresh(self):
        self.driver.find(self.loc.refresh).click()
        console.print("刷新")

    def click_bookmarks(self):
        self.driver.find(self.loc.bookmarks).click()
        console.print("书签")

    def click_link(self):
        self.driver.find(self.loc.link).click()
        console.print("链接跳转")

    def hold_link(self):
        el = self.driver.find(self.loc.link)
        with self.driver.actions_manager() as action:
            action.click_and_hold(el, duration=5)

    def click_hold_link(self):
        self.driver.find(self.loc.hold_open_tab).click()
        console.print("新标签页中打开")

    def click_incognito_link(self):
        self.driver.find(self.loc.hold_open_incognito).click()
        console.print("无痕打开网页")

    def click_download_link(self):
        self.driver.find(self.loc.hold_download_link).click()
        console.print("无痕打开网页")

    def click_delete_link(self):
        self.driver.find(self.loc.hold_delete_link).click()
        console.print("无痕打开网页")

    def click_open_tab(self):
        self.driver.find(self.loc.open_tab).click()
        console.print("打开新页签")

    def click_open_incognito(self):
        self.driver.find(self.loc.open_incognito).click()
        console.print("打开新的无痕标签页")

    def click_last_open(self):
        self.driver.find(self.loc.last_open).click()
        console.print("最近打开的标签页")

    def click_open_history(self):
        self.driver.find(self.loc.open_history).click()
        console.print("历史记录")

    def click_share(self):
        self.driver.find(self.loc.share_btn).click()
        console.print("分享")

    def click_find_page(self):
        self.driver.find(self.loc.find_in_page).click()
        console.print("在网页中查找")

    def click_desktop_site(self):
        self.driver.find(self.loc.desktop_site).click()
        console.print("桌面版网站")

    def click_setting(self):
        self.driver.find(self.loc.setting).click()
        console.print("设置")

    def click_help_feedback(self):
        self.driver.find(self.loc.help_feedback).click()
        console.print("帮助和反馈")

    def click_search_engines(self):
        self.driver.find(self.loc.search_engines).click()
        console.print("搜索引擎")

    def click_password_tools(self):
        self.driver.find(self.loc.password_tools).click()
        console.print("密码管理工具")

    def click_pay_way(self):
        self.driver.find(self.loc.pay_way).click()
        console.print("付款方式")

    def click_address(self):
        self.driver.find(self.loc.address).click()
        console.print("地址和其他信息")

    def click_setting_homepage(self):
        self.driver.find(self.loc.setting_homepage).click()
        console.print("主页")

    def click_style_background(self):
        self.driver.find(self.loc.style_background).click()
        console.print("主题背景")

    def click_download_content(self):
        self.driver.find(self.loc.download_content).click()
        console.print("下载内容")

    def click_privacy_settings(self):
        self.driver.find(self.loc.privacy_settings).click()
        console.print("隐私设置和安全性")

    def click_accessibility(self):
        self.driver.find(self.loc.accessibility).click()
        console.print("无障碍")

    def click_notification(self):
        self.driver.find(self.loc.notification).click()
        console.print("通知")

    def click_bookmarks_sign(self):
        self.driver.find(self.loc.bookmarks_sign).click()
        console.print("点击添加书签")

    def click_mobile_bookmark(self):
        self.driver.find(self.loc.mobile_bookmark).click()
        console.print("移动设备书签")

    def click_select_bookmark(self):
        self.driver.find(self.loc.select_bookmark).click()
        console.print("选择第一个书签")

    def click_bookmarks_setting(self):
        self.driver.find(self.loc.bookmarks_setting).click()
        console.print("点击设置")

    def click_bookmarks_edit(self):
        self.driver.find(self.loc.bookmarks_edit).click()
        console.print("点击编辑")

    def click_bookmarks_delete(self):
        self.driver.find(self.loc.bookmarks_delete).click()
        console.print("删除标签")

    def click_bookmarks_move(self):
        self.driver.find(self.loc.bookmarks_move).click()
        console.print("移动书签")

