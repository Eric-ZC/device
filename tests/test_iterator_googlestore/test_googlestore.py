import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestGoogleStore:

    @pytest.mark.D4_504_Pro
    def test_install_googlestore(self,driver: Driver):
        """安装GoogleStore"""
        driver.launch_app(*settings.packages.google_store)

    @pytest.mark.D4_504_Pro
    def test_google_authenticator_oir(self,driver: Driver, googlestore_page):
        """谷歌验证"""
        driver.launch_app(*settings.packages.google_store)
        googlestore_page.login_auth()
        googlestore_page.click_sign_in()
        googlestore_page.fill_account()
        googlestore_page.click_next()
        driver.swipe_up(5, duration=5)
        googlestore_page.fill_psd()
        googlestore_page.click_next()
        driver.swipe_up(2, duration=5)
        googlestore_page.click_agree()
        googlestore_page.click_more_infor()
        googlestore_page.click_accept()
        googlestore_page.click_more()
        googlestore_page.click_setting()
        googlestore_page.click_about()

    @pytest.mark.D4_504_Pro
    def test_google_download(self,driver: Driver, googlestore_page):
        """下载内容"""
        driver.launch_app(*settings.packages.google_store)
        googlestore_page.click_search_btn()
        googlestore_page.fill_app("Gmail")
        driver.press_keycode(Keys.ENTER)
        googlestore_page.click_install()
        for attempt in retry_attempts(timeout=300):
            with attempt:
                googlestore_page.launcher_app_view()

