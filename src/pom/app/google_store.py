import time

from src.deps import *


class GoogleStore(BasePage):
    """
    谷歌商店
    """

    class loc:
        @staticmethod
        def app_name(name: str = None, exact: bool = True, description: str = None):
            return Selector(
                XPath(has_text=name)
                .join("/following-sibling::android.widget.TextView")
                .join("/following-sibling::/android.view.View/android.widget.Button" ),
                description=description or "安装按钮",
            )
        calendar = app_name("Google Calendar", description="日历")

        # search_btn = Selector(XPath('//android.widget.TextView[@text="搜索应用和游戏"]'), description="搜索")
        search_btn = Selector(XPath('//android.view.View[@content-desc="在 Google Play 中搜索"]'),description="搜索")
        cancel = Selector(XPath(has_content="Cancel"),description="取消")
        open = Selector(XPath(has_content="Open"),description="打开")
        install = Selector(XPath(has_content="Install"),description="安装")

        input = Selector(XPath("android.widget.EditText"),
            description="应用商店的搜索框"
        )

        select_install = Selector(XPath(has_content="Install on more devices"),description="选择安装")
        install_btn = Selector(XPath(id="android:id/content").join(
            "//android.view.ViewGroup/android.view.View[1]/android.view.View[1]"
            "/android.view.View[1]/android.widget.Button"
        ))


        agree = Selector(XPath('//android.widget.Button[@text="我同意"]'), description="我同意")

        more = Selector(XPath(has_text="More"), description="更多")
        accept = Selector(XPath('//android.widget.Button[@text="接受"]'), description="接收")
        text_tips = Selector(XPath(has_text="Search apps & games"), description="输入框的提示语")
        account_management = Selector(XPath(has_text="Manage your Google Account"), description="管理账号")
        mgt_tips = Selector(XPath(id="com.google.android.gms:id/title_desc"), description="管理账号的提示")
        account = Selector(XPath(id="com.android.vending:id/0_resource_name_obfuscated").join(
            "android.widget.ImageView"
        ), description="账号"
        )

        sign_btn = Selector(
            XPath(id="com.android.vending:id/0_resource_name_obfuscated").join(
                "android.widget.Button"
            ),
            description="登录按钮",
        )
        ac_input = Selector(XPath(id="identifierId"), description="账号输入框")
        psd_input = Selector(XPath(id="password").join(
            "android.view.View[1]/android.view.View[1]/android.widget.EditText"
        ))
        next = Selector(XPath(has_text="下一步"), description="下一步")
        later = Selector(XPath(has_text="以后再说"), description="以后再说")
        more_btn = Selector(XPath('//android.widget.ImageView[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]'), description="设置按钮")
        more_infor = Selector(XPath(has_text="更多"),description="更多")
        about = Selector(XPath(has_text="关于"), description="关于")
        setting= Selector(XPath(has_text='设置'),description="设置")

        install_bt=Selector(XPath(has_content="在更多设备上安装").
                            join("//preceding-sibling::android.widget.TextView"),
                            description="安装")

        launcher_app = Selector(XPath(has_content="打开"),description="打开")


    def login_auth(self):

        if self.driver.find(self.loc.sign_btn).is_enabled():
            console.print("账号未登录")
        else:
            console.print("账号已登录")

    def click_sign_in(self):
        self.driver.find(self.loc.sign_btn,timeout=10).click(delay=15)
        console.print("点击登录")

    def click_next(self):
        self.driver.find(self.loc.next, exist_ok=True, timeout=10).click()
        console.print("点击下一步")

    def click_open(self):
        self.driver.find(self.loc.open).click()
        console.print("打开应用")

    def fill_account(self, text="yzzkik@gmail.com"):
        self.driver.find(self.loc.ac_input, timeout=30).fill(text)
        console.print("输入账号:" + text)

    def fill_psd(self, text="yzzkik123123"):
        self.driver.find(self.loc.psd_input, timeout=30).fill(text)
        console.print("输入密码:" + text)

    def click_search_btn(self):
        time.sleep(10)
        self.driver.find(self.loc.search_btn,timeout=10).click()
        console.print("点击搜索按钮")

    def fill_app(self, app: str):
        self.driver.find(self.loc.input).fill(app)
        time.sleep(5)
        console.print("搜索应用：" + app)

    def click_agree(self):
        self.driver.find(self.loc.agree, timeout=20, exist_ok=True).click()
        console.print("点击我同意")

    def click_later(self):
        console.print("以后再说")
        self.driver.find(self.loc.later, timeout=20, exist_ok=True).click()

    def click_accept(self):
        console.print("点击接受")
        self.driver.find(self.loc.accept,timeout=20,exist_ok=True).click()
        time.sleep(10)

    def click_more_infor(self):
        self.driver.find(self.loc.more_infor, exist_ok=True).click()

    def click_more(self):
        console.print("点击更多")
        self.driver.find(self.loc.more_btn, timeout=5,exist_ok=True).click()

    def click_setting(self):
        self.driver.find(self.loc.setting,timeout=20).click()

    def click_about(self):
        self.driver.find(self.loc.about,timeout=20).click()
        console.print("点击关于")

    def click_install(self):
        console.print("点击安装")
        self.driver.find(self.loc.install_bt,timeout=20,exist_ok=True).click()

    def in_ac_mgr(self):
        console.print("点击账号")
        self.driver.find(self.loc.account).click()
        console.print("点击管理账号,进入账号管理页面")
        self.driver.find(self.loc.account_management).click()

    def get_text_tips(self):
        return self.driver.find(self.loc.text_tips, timeout=60, exist_ok=True)

    def get_mgr_tips(self):
        return self.driver.find(self.loc.mgt_tips, timeout=60, exist_ok=True)

    def get_open(self):
        return self.driver.find(self.loc.open,timeout=900,exist_ok=True)

    def get_cancel(self):
        return self.driver.find(self.loc.cancel,timeout=30,exist_ok=True)

    def click_btn(self,app):
        self.driver.find(self.loc.app_name(app)).click()
        console.print("点击安装"+str(app))

    def launcher_app_view(self):
        self.driver.find(self.loc.launcher_app)