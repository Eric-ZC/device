from src.deps import *


class Keyboard(BasePage):
    """
    键盘
    """

    class Loc:
        InputArea = Selector(XPath(id="android:id/inputArea"), description="键盘输入框")
        Search = Selector(
            XPath(id="com.google.android.inputmethod.latin:id/key_pos_ime_action"),
            description="搜索",
        )

    def is_exists(self):
        """
        判断键盘是否存在
        Returns:

        """
        return self.driver.find(self.Loc.InputArea).is_visible()

    def click_search(self):
        """
        点击搜索
        Returns:

        """
        self.driver.find(self.Loc.Search).click(delay=1)
