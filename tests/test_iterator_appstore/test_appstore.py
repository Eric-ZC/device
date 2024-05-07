import pytest
import time
from soium import Keys
from soium import Driver
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings

class TestAppStore:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.store)
        yield
        console.print("\n执行后置操作")
        driver.press_keycode(Keys.HOME)

    @pytest.mark.swift_2_pro
    def test_download_app(self, driver: Driver, appstore_page):
        """下载App"""
        appstore_page.get_rec_app()
        console.print(appstore_page.get_rec_app())
        if appstore_page.get_rec_fist().get_text() != "安装":
            pytest.skip("首个应用已下载")
        else:
            appstore_page.click_rec_fist()
            appstore_page.in_inst_list()
            console.print("等待应用下载完成，最多10分钟")
            for attempt in retry_attempts(timeout=600):
                with attempt:
                    assert_that(appstore_page.get_down()).is_not_none()

    @pytest.mark.swift_2_pro
    def test_update_app(self, driver:Driver, appstore_page):
        """升级App"""
        appstore_page.in_update_list()
        if appstore_page.get_no_update():
            pytest.skip("应用已更新")
        else:
            appstore_page.get_upgrade_btn()
            console.print("本地存在可升级的应用")
            appstore_page.click_upgrade()
            for attempt in retry_attempts(timeout=600):
                with attempt:
                    assert_that(appstore_page.get_no_update()).is_not_none()

    @pytest.mark.swift_2_pro
    def test_uninstall_app(self, driver:Driver, appstore_page,launcher_page):
        """卸载App"""
        driver.press_keycode(Keys.HOME)
        time.sleep(5)
        launcher_page.move_app_del()

