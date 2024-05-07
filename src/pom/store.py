from src.deps import *


class AppStores(BasePage):
    """
    应用商店
    """

    class Loc:
        SearchBox = Selector(
            XPath(id="com.imin.appstore:id/search_bar"), description="搜索框"
        )
        Recommend = Selector(
            XPath(id="com.imin.appstore:id/title", has_text="Recommend"),
            description="推荐",
        )
        Classify = Selector(
            XPath(id="com.imin.appstore:id/title", has_text="Classify"),
            description="分类",
        )
        MyProfile = Selector(
            XPath(id="com.imin.appstore:id/title", has_text="My Profile"),
            description="个人资料",
        )
        SearchHistory = Selector(
            XPath(id="com.imin.appstore:id/history_rv").join("android.widget.TextView"),
            description="搜索历史",
        )

    @console.step("点击推荐")
    def click_recommend(self):
        """
        点击推荐
        Returns:

        """
        self.driver.find(self.Loc.Recommend).click()

    @console.step("点击分类")
    def click_classify(self):
        """
        点击分类
        Returns:

        """
        self.driver.find(self.Loc.Classify).click()

    @console.step("点击个人资料")
    def click_my_profile(self):
        """
        点击个人资料
        Returns:

        """
        self.driver.find(self.Loc.MyProfile)

    @console.step("点击搜索框")
    def click_searchbox(self):
        """
        点击搜索框
        Returns:

        """
        self.driver.find(self.Loc.SearchBox).click()
