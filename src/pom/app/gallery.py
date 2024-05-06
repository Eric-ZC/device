from src.deps import *


class Gallery(BasePage):

    class loc:

        gallery_title = Selector(XPath(has_text="相册"), description="相册")

        camera_to_gallery = Selector(XPath(has_content="Has Content"),description="相机跳转相册")

        gallery_screen = Selector(XPath(id="com.android.gallery3d:id/gl_root_view"),description="图库屏幕")

        switch_styles = Selector(XPath(id="android:id/text1",has_text="新文件夹"),description="切换风格")

        ppt_styles = Selector(XPath(id="android:id/text1",has_text="幻灯片视图"),description="幻灯片视图")

        pause_btn = Selector(XPath(id="android.widget.ImageView",has_content="暂停视频"),description="暂停视频")

        # play_btn = Selector(XPath(id="android.widget.ImageView", has_content="播放视频"), description="播放视频")

        play_btn = Selector(XPath(has_content="播放视频"), description="播放视频")

        play_time_bar = Selector(XPath(has_content="视频播放器时间栏"),description="视频播放器时间栏")

        play_screen = Selector(XPath('//android.widget.VideoView[@resource-id="com.android.gallery3d:id/surface_view"]'),description="播放屏幕")

        more_options = Selector(XPath(has_content="更多选项"),description="更多选项")

        play_slideshow = Selector(XPath(id="android:id/title",has_text="播放幻灯片"), description="播放幻灯片")

        set_wallpaper = Selector(XPath(id="android:id/title",has_text="设置壁纸"), description="设置壁纸")

        wallpaper_confirm = Selector(XPath(id="com.android.gallery3d:id/filtershow_done",has_text="设置壁纸"))

        share = Selector(XPath(id="android:id/image", has_content="分享方式"), description="分享方式")

        detail = Selector(XPath(id="android:id/title", has_text="详细信息"), description="详细信息")

        delete = Selector(XPath(id="android:id/title", has_text="删除"), description="删除")

        delete_confirm = Selector(XPath(id="android:id/button1", has_text="确定"), description="确定")

        camera_bar = Selector(XPath(id="android:id/action_bar_spinner"),description="相机栏")

        screen_size = Selector(XPath(id="com.android.gallery3d:id/gl_root_view"),description="屏幕大小")

    def get_gallery_title(self):
        """
        获取相册标题
        """
        console.print("获取相册标题")
        return self.driver.find( self.loc.gallery_title)

    def camera_to_gallery(self):
        self.driver.find(self.loc.camera_to_gallery).click()
        console.print("相机跳转相册")

    def switch_styles(self):
        self.driver.find(self.loc.switch_styles).click()
        self.driver.find(self.loc.ppt_styles).click()

    def click_play_(self):
        self.driver.find(self.loc.play_btn,timeout=10).click()
        console.print("视频播放")

    def view_play_btn(self):
        ele = self.driver.find(self.loc.play_btn,exist_ok=True)
        if ele is None:
            return False
        return True

    def view_play_time_bar(self):
        ele = self.driver.find(self.loc.play_time_bar,exist_ok=True)
        if ele is None:
            return False
        return True

    def click_play_time_bar(self):
        self.driver.find(self.loc.play_time_bar).click()
        console.print("播放进度条")

    def click_play_screen(self):
        with self.driver.actions_manager() as action:
            action.click_and_hold(self.driver.find(self.loc.play_screen), duration=5)

    def click_more_options(self):
        self.driver.find(self.loc.more_options,timeout=5).click()
        console.print("更多选项")

    def click_play_slideshow(self):
        self.driver.find(self.loc.play_slideshow,timeout=5).click()
        console.print("播放幻灯片")

    def click_set_wallpaper(self):
        self.driver.find(self.loc.set_wallpaper, timeout=5).click()
        console.print("设置壁纸")

    def click_wallpaper_confirm(self):
        self.driver.find(self.loc.wallpaper_confirm, timeout=5).click()
        console.print("设置壁纸成功")

    def click_share(self):
        self.driver.find(self.loc.share, timeout=5).click()
        console.print("分享")

    def click_detail(self):
        self.driver.find(self.loc.detail, timeout=5).click()
        console.print("详细信息")

    def click_camera_bar(self):
        self.driver.find(self.loc.camera_bar).click()
        self.driver.find(self.loc.ppt_styles).click()
        console.print("切换到PPT")

    def click_delete(self):
        self.driver.find(self.loc.delete).click()
        console.print("点击删除")

    def click_delete_confirm(self):
        self.driver.find(self.loc.delete_confirm).click()
        console.print("点击确定")

    def size_screen(self):
        return self.driver.find(self.loc.screen_size).size