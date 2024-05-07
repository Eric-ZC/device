import pytest
from soium.utils.asserts import assert_that
# from soium.utils.image import Imutils
from soium.utils.logger import console

from src.conf import settings

@pytest.mark.skip
class TestSuite:
    @pytest.fixture(autouse=True, scope="class")
    def launch_app(self, driver):
        driver.launch_app(*settings.packages.store)
        console.print("启动应用商店")

    @console.step("搜索框测试用例")
    def test_searchbox(self, driver, pom):
        """
        搜索框测试用例
        Args:
            pom:

        Returns:

        """
        pom.store.click_recommend()
        pom.store.click_searchbox()
        pom.keyboard.click_search()
        assert_that(driver.get_screenshot_as_png()).contains()
        # assert_that(
             # Imutils.get_text(driver.get_screenshot_as_png()),
             # description="断言搜索框为空点击是否展示‘请输入搜索关键词’",
         # ).contains("Please enter a search keyword")
