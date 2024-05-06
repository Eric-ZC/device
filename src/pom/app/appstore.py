from src.deps import *
from soium.code.adb import adb
from soium import Keys


class AppStore(BasePage):
    """
    应用商店页
    """

    class loc:
        search = Selector(XPath(id="com.imin.appstore:id/search_bar"), description="搜索按钮")
        search_result = Selector(XPath(id="com.imin.appstore:id/tv"), description="搜索结果")
        install = Selector(XPath(id="com.imin.appstore:id/install_btn", has_text="Install"), description="下载按钮")
        upgrade_all = Selector(XPath(has_text="全部升级"), description="升级所有")
        pause = Selector(XPath(has_text="Pause"), description="暂停按钮")
        open = Selector(XPath(has_text="Open"), description="打开")
        my_profile = Selector(XPath(has_text="我的"), description="我的")
        update_list = Selector(XPath(has_text="应用更新"), description="更新列表")
        inst_list = Selector(XPath(has_text="安装列表"), description="安装列表")
        chrome = Selector(XPath(has_text="Chrome"), description="chrome浏览器")
        about = Selector(XPath(has_text="About"), description="关于")
        no_down = Selector(XPath(has_text="暂无下载任务"), description="无下载队列")
        no_update = Selector(XPath(id="com.imin.appstore:id/tv",has_text='当前应用已是最新版本'), description="无更新应用")
        recommend = Selector(XPath(has_text="Recommend"), description="推荐")
        ver_toast = Selector(XPath(has_text="The current version is the latest version"),
                             description="检查版本Toast")
        bro_toast = Selector(XPath(has_text="Missing Browser"), description="检测浏览器Toast")

        set_ver = Selector(XPath(id="com.imin.appstore:id/setting_rv").join(
            "/descendant::android.widget.LinearLayout/android.widget.TextView[2]"),
            description="检测版本号")

        version = Selector(XPath(id="com.imin.appstore:id/content_rv").join(
            "/descendant::android.widget.LinearLayout/android.widget.TextView[2]"),
            description="版本号")

        add = lambda brand: Selector(
            XPath(has_text={"yimin": "https://www.neostra.com", "imin": "https://imin.sg"}[brand]))

        classify = Selector(XPath(has_text="Classify"))
        rec_app = Selector(XPath(id="com.imin.appstore:id/recommend_rv").join(
            "android.view.ViewGroup/android.widget.TextView"),
            description="推荐应用列表", )

        rec_app_btn = Selector(XPath(id="com.imin.appstore:id/recommend_rv").join(
            "/android.view.ViewGroup[1]/android.widget.Button[1]"),
            description="首个应用的按钮")

        install_list = Selector(XPath(id="com.imin.appstore:id/data_rv").join(
            "android.widget.LinearLayout"),
            description="下载列表")

        clas_list = Selector(XPath(id="com.imin.appstore:id/menu_rv").join(
            "android.widget.LinearLayout/android.widget.TextView"),
            description="分类列表")

    def get_rec_app(self):
        console.print("获取应用列表")
        return self.driver.find_all(self.loc.rec_app)

    def get_inst_list(self):
        console.print("获取下载列表")
        return self.driver.find_all(self.loc.install_list)

    def get_rec_fist(self):
        console.print("获取首个应用的按钮")
        return self.driver.find(self.loc.rec_app_btn)

    def click_rec_fist(self):
        console.print("点击首个应用的按钮")
        return self.driver.find(self.loc.rec_app_btn).click()

    def click_add(self):
        self.driver.find(self.loc.add(self.driver.get_brand())).click()
        console.print("点击官网")

    logo = lambda brand: Selector(
        XPath(has_text={"yimin": "https://www.neostra.com", "imin": "https://imin.sg"}[brand]))

    def click_search(self):
        self.driver.find((self.loc.search)).click()
        console.print("点击搜索按钮")

    def click_rec(self):
        self.driver.find((self.loc.recommend)).click()
        console.print("点击推荐按钮")

    def click_classify(self):
        self.driver.find((self.loc.classify)).click()
        console.print("点击推荐按钮")

    def click_upgrade(self):
        self.driver.find(self.loc.upgrade_all).click()
        console.print("点击升级所有应用")

    def fill_search(self, text):
        self.driver.find((self.loc.search)).fill(text)
        console.print("输入" + str(text))
        # self.driver.press_keycode(121)

    """
    def search_app(self,text:str):
        self.driver.find(self.loc.search).click()
        self.driver.find(self.loc.search).fill(text)
        self.driver.press_keycode(Keys.ENTER)

        console.print("搜索应用")
    """

    def get_search(self):
        return self.driver.find((self.loc.search_result)).get_text()

    def get_upgrade_btn(self):
        return self.driver.find(self.loc.upgrade_all, exist_ok=True, timeout=10)

    def get_no_update(self):
        return self.driver.find(self.loc.no_update, exist_ok=True)

    def click_inst(self):
        self.driver.find(self.loc.install).click()
        console.print("点击下载")

    def click_mypro(self):
        self.driver.find(self.loc.my_profile).click()
        console.print("点击我的")

    def click_about(self):
        self.driver.find(self.loc.about).click()
        console.print("点击关于")

    def click_ver(self):
        self.driver.find(self.loc.set_ver).click()
        console.print("点击版本号")

    def get_start_inst(self):
        return self.driver.find(self.loc.pause, timeout=20, exist_ok=True)

    def get_inst_statu(self):
        return self.driver.find(self.loc.open, timeout=900, exist_ok=True)

    def get_chrome(self):
        return self.driver.find(self.loc.chrome, timeout=30, exist_ok=True)

    def in_inst_list(self):
        console.print("进入下载列表")
        self.driver.find(self.loc.my_profile).click()
        self.driver.find((self.loc.inst_list)).click()

    def in_update_list(self):
        console.print("进入更新列表")
        self.driver.find(self.loc.my_profile).click()
        self.driver.find((self.loc.update_list)).click()

    def get_clas_list(self):
        console.print("获取分类列表")
        return self.driver.find_all(self.loc.clas_list)

    def radiom_inst_clas_app(self):
        console.print("随机下载一个分类首个应用")
        random_app = self.driver.find_all(self.loc.clas_list).random
        random_app_text = random_app.get_text()
        random_app.click()
        console.print("随机分类" + str(random_app_text))
        self.driver.find(self.loc.install).click()

    def get_down(self):
        return self.driver.find(self.loc.no_down, timeout=600, exist_ok=True)

    def get_set_ver(self):
        console.print("获取商店设置的版本号")
        return self.driver.find((self.loc.set_ver)).get_text()

    def get_about_ver(self):
        console.print("获取关于页的版本号")
        return self.driver.find((self.loc.version)).get_text()

    def get_ver_tip(self):
        return self.driver.find(self.loc.ver_toast, timeout=30, exist_ok=True)

    def get_bro_tip(self):
        return self.driver.find(self.loc.bro_toast, timeout=10, exist_ok=True)

    def delete_chrome(self):
        """卸载chrome"""
        for pkg in adb.get_packages():
            if "com.android.chrome" in pkg:
                console.print("存在chrome浏览器，卸载")
                adb.delete_app(pkg)

    def install_chrome(self):
        # 后续需要本地放一个chrome的APK
        adb.install_app("./resources/chrome.apk", launch=False)
        console.print("安装完浏览器后打开官网")
        self.driver.find(self.loc.add(self.driver.get_brand())).click()

    def install_echrome(self):
        console.print("安装3.1.6的e浏览器")
        adb.install_app("./resources/echrome.apk", launch=False)
        console.print("安装完成")