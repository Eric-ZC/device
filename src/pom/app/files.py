import time

from src.deps import *


class Files(BasePage):
    """
    文件管理器
    """

    class loc:
        menu = Selector(XPath(has_content="显示根目录"), description="菜单")
        no_file_tips = Selector(XPath(has_text="No matches"),description="没有文件")

        @staticmethod
        def menu_options(name: str = None, exact: bool = True, description: str = None):
            return Selector(
                XPath(id="com.android.documentsui:id/roots_list").join(
                    "descendant::android.widget.TextView", has_text=name, exact=exact
                ),
                description=description or "菜单栏选项",
            )

        recent = menu_options("最近", description="最近浏览")
        images = menu_options("图片", description="图片")
        videos = menu_options("Videos", description="视频")
        audio = menu_options("Audio", description="音频")
        documents = menu_options("文档", description="文档")
        downloads = menu_options("下载", description="下载")
        sd_card = menu_options("SD card", exact=False, description="SD卡")
        folder_or_file = Selector(
            XPath(id="com.android.documentsui:id/item_root"), description="文件夹/文件"
        ).or_(
            XPath(id="com.android.documentsui:id/dir_list").join(
                "descendant::android.widget.LinearLayout"
            )
        )
        filename = Selector(XPath(id="android:id/title"), description="文件名")
        create_date = Selector(
            XPath(
                id="com.android.documentsui:id/date",
                has_text=[*[str(num) for num in range(10)]],
            ),
            description="文件日期",
        )
        size = Selector(
            XPath(
                id=[
                    "com.android.documentsui:id/size",
                    "com.android.documentsui:id/details",
                ],
                has_text=[*[str(num) for num in range(10)]],
            ),
            description="文件大小",
        )
        check_status = Selector(
            XPath(id="com.android.documentsui:id/icon_check"), description="选中状态"
        )
        more_options = Selector(XPath(has_content="更多选项"), description="更多选项")

        copy_to = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="复制到…"),
            description="复制到",
        )
        move_to = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="移至…"),
            description="移至",
        )
        new_folder = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="新建文件夹"),
            description="新建文件夹",
        )
        sort_by = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="排序方式…"),
            description="排序方式",
        )
        copy = Selector(
            XPath(
                id=["com.android.documentsui:id/title", "android:id/button1"],
                has_text="COPY",
            ),
            description="复制",
        )
        move = Selector(
            XPath(
                id=["com.android.documentsui:id/title", "android:id/button1"],
                has_text="MOVE",
            ),
            description="移动",
        )
        compress = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="压缩"),
            description="压缩",
        )
        rename = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="重命名"),
            description="重命名",
        )
        get_info = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="获取信息"),
            description="获取信息",
        )
        new_window = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="New window"),
            description="新建窗口",
        )
        show_hidden_files = Selector(
            XPath(id="com.android.documentsui:id/title", has_text="Show hidden files"),
            description="显示隐藏的文件",
        )
        dont_show_hidden_files = Selector(
            XPath(
                id="com.android.documentsui:id/title",
                has_text="Don’t show hidden files",
            ),
            description="不显示隐藏的文件",
        )  # 中文符号
        name_input = Selector(XPath(id="android:id/text1"), description="输入框")
        search_input = Selector(
            XPath(id="com.android.documentsui:id/search_src_text"), description="输入框"
        )
        delete = Selector(
            XPath(id="com.android.documentsui:id/action_menu_delete"), description="删除"
        )
        share = Selector(
            XPath(id="com.android.documentsui:id/action_menu_share"), description="分享"
        )
        search = Selector(
            XPath("//android.widget.TextView[@content-desc=\"搜索\"]"), description="搜索"
        )
        ok = Selector(
            XPath(id="android:id/button1", has_text="确定", exact=True), description="确认"
        )
        cancel = Selector(
            XPath(id="android:id/button2", has_text="CANCEL", exact=True),
            description="确认",
        )
        image_tag = Selector(
            XPath(
                "com.google.android.material.chip.Chip", has_text="图片", exact=True
            ),
            description="图片标签",
        )
        audio_tag = Selector(
            XPath(
                "com.google.android.material.chip.Chip", has_text="Audio", exact=True
            ),
            description="音频标签",
        )
        videos_tag = Selector(
            XPath(
                "com.google.android.material.chip.Chip", has_text="Videos", exact=True
            ),
            description="视频标签",
        )
        documents_tag = Selector(
            XPath(
                "com.google.android.material.chip.Chip",
                has_text="Documents",
                exact=True,
            ),
            description="文档标签",
        )
        large_files_tag = Selector(
            XPath(
                "com.google.android.material.chip.Chip",
                has_text="Large files",
                exact=True,
            ),
            description="大型文件标签",
        )
        this_week_tag = Selector(
            XPath(
                "com.google.android.material.chip.Chip",
                has_text="本周",
                exact=True,
            ),
            description="本周标签",
        )
        tag_bar = Selector(
            XPath(id="com.android.documentsui:id/search_chip_group"), description="标签栏"
        )
        tags = Selector(
            XPath("com.google.android.material.chip.Chip"),
            description="分类标签",
        )
        modified = Selector(
            XPath(
                id="com.android.documentsui:id/table_row_key", has_text="Modified"
            ).join("following-sibling::android.widget.TextView"),
            description="上次修改时间",
        )
        switch_views = Selector(
            XPath(
                id=[
                    "com.android.documentsui:id/sub_menu_list",
                    "com.android.documentsui:id/sub_menu_grid",
                ]
            ),
            description="切换视图",
        )
        recent_files = Selector(
            XPath(id="com.android.documentsui:id/header_title", has_text="RECENT FILES")
        )
        enable_bluetooth = Selector(
            XPath(
                id="com.android.bluetooth:id/content",
                has_text="To use Bluetooth services",
            )
            .join("ancestor::*", id="android:id/customPanel")
            .join("following-sibling::*", id="android:id/buttonPanel")
            .join("descendant::*", has_text="TURN ON")
        )

        folder = Selector(
            XPath(
                id="android:id/title",
                has_text="新文件夹"),
                description="相册文件夹")

        unknown_folder = Selector(
            XPath(
                id="android:id/title",
                has_text="未知"),
            description="未知文件夹")

        screenshoot_floder = Selector(
            XPath(
                id="android:id/title",
                has_text="Screenshots"),
            description="相册文件夹")

        movies_floder = Selector(
            XPath(
                id="android:id/title",
                has_text="Movies"),
                description="视频"
        )

        floder = Selector(
            XPath(id="android:id/title",has_text="test01"),
            description="文件夹"
        )
        photo = Selector(
            XPath('(//androidx.cardview.widget.CardView[@resource-id="com.android.documentsui:id/item_root"])[1]'),
            description="照片"
        )

        del_photo = Selector(
            XPath(id='com.android.documentsui:id/action_menu_delete',has_content="删除"),
            description="删除照片"
        )

        del_confirm = Selector(
            XPath(id="android:id/button1"),
            description="确定删除"
        )
        video = Selector(
            XPath('//androidx.cardview.widget.CardView[@resource-id="com.android.documentsui:id/item_root"]/androidx.cardview.widget.CardView/android.widget.RelativeLayout'),
            description="视频"
        )
        device_name = Selector(
            XPath("//android.widget.ListView[@resource-id=\"com.android.documentsui:id/roots_list\"]/android.widget.LinearLayout[7]").
            join("/descendant::android.widget.TextView",id="android:id/title")
        )

        recent_image = Selector(
            XPath("//android.widget.CompoundButton[@text=\"图片\"]"),
            description = "图片"
        )
        recent_voice = Selector(
            XPath("//android.widget.CompoundButton[@text=\"音频\"]"),
            description="音频"
        )
        recent_video = Selector(
            XPath("//android.widget.CompoundButton[@text=\"视频\"]"),
            description="视频"
        )
        recent_file = Selector(
            XPath("//android.widget.CompoundButton[@text=\"文档\"]"),
            description="文档"
        )
        recent_large_files = Selector(
            XPath("//android.widget.CompoundButton[@text=\"大型文件\"]"),
            description="大型文件"
        )
        recent_this_week = Selector(
            XPath("//android.widget.CompoundButton[@text=\"本周\"]"),
            description="本周"
        )
        frist_file = Selector(
            XPath("(//android.widget.ImageView[@resource-id=\"com.android.documentsui:id/icon_thumb\"])[1]"),
            description="第一个文件"
        )
        recent_more = Selector(
            XPath(has_content="更多选项"),
            description="更多选项"
        )
        open_ways = Selector(
            XPath(id="com.android.documentsui:id/title",has_text="打开方式"),
            description="打开方式"
        )
        select_all = Selector(
            XPath(id="com.android.documentsui:id/title",has_text="全选"),
            description="全选")

        local = Selector(
            XPath("//android.widget.ListView[@resource-id=\"com.android.documentsui:id/roots_list\"]/android.widget.LinearLayout[7]"),
            description="本地"
        )
        camera_folder = Selector(
            XPath(id="android:id/title",has_text="Camera"),
            description="相机"
        )

        @staticmethod
        def sort_by_type(reverse: bool):
            return Selector(
                XPath(
                    id="android:id/text1",
                    has_text="文件名（从 A 到 Z）" if reverse else "文件名（从 Z 到 A）",
                )
            )

        @staticmethod
        def sort_by_modified(reverse: bool):
            return Selector(
                XPath(
                    id="android:id/text1",
                    has_text="Modified (newest first)"
                    if reverse
                    else "Modified (oldest first)",
                )
            )

        @staticmethod
        def sort_by_name(reverse: bool):
            return Selector(
                XPath(
                    id="android:id/text1",
                    has_text="File name (Z to A)" if reverse else "File name (A to Z)",
                )
            )

    def click_menu(self):
        if (el := self.driver.find(self.loc.menu, timeout=2, exist_ok=True)) is None:
            return
        el.click()
        console.print("点击菜单")

    def click_storage(self):
        self.driver.find(self.loc.menu_options(self.driver.get_model())).click(delay=2)
        console.print("点击内部存储")

    def click_storage_str(self, str):
        self.driver.find(self.loc.menu_options(str)).click(delay=2)
        console.print("点击内部存储")

    def click_recent(self):
        self.driver.find(self.loc.recent).click(delay=2)
        console.print("点击最近的文件分类")

    def click_images(self):
        self.driver.find(self.loc.images).click(delay=2)
        console.print("点击图片分类")

    def click_videos(self):
        self.driver.find(self.loc.videos).click(delay=2)
        console.print("点击视频分类")

    def click_audio(self):
        self.driver.find(self.loc.audio).click(delay=2)
        console.print("点击音频分类")

    def click_documents(self):
        self.driver.find(self.loc.documents).click(delay=2)
        console.print("点击文档分类")

    def click_downloads(self):
        self.driver.find(self.loc.downloads).click(delay=2)
        console.print("点击下载分类")

    def click_more_options(self):
        self.driver.find(self.loc.more_options).click()
        console.print("点击更多选项")

    def click_create_window(self):
        self.driver.find(self.loc.new_window).click(delay=2)
        console.print("点击新建窗口")

    def click_create_folder(self):
        self.driver.find(self.loc.new_folder).click()
        console.print("点击新建文件夹")

    def click_sort_by(self):
        self.driver.find(self.loc.sort_by).click()
        console.print("点击排序方式")

    def fill_name(self, name: str):
        self.driver.find(self.loc.name_input).fill(name)
        console.print(f"输入: {name}")

    def search(self, value: str):
        self.driver.find(self.loc.search_input).fill(value)
        time.sleep(1)
        console.print(f"输入: {value}")

    def click_rename(self):
        self.driver.find(self.loc.rename).click()
        console.print("点击重命名")

    def click_compress(self):
        self.driver.find(self.loc.compress).click()
        console.print("点击压缩")

    def click_move_to(self):
        self.driver.find(self.loc.move_to).click()
        console.print("点击移动到")

    def click_copy_to(self):
        self.driver.find(self.loc.copy_to).click()
        console.print("点击复制到")

    def click_copy(self):
        self.driver.find(self.loc.copy).click()
        console.print("点击复制")

    def click_move(self):
        self.driver.find(self.loc.move).click()
        console.print("点击移动")

    def click_get_info(self):
        self.driver.find(self.loc.get_info).click()
        console.print("点击获取信息")

    def is_recent_page(self):
        """
        判断是否为最近的文件页面
        """
        return bool(self.driver.find(self.loc.recent_files, timeout=2, exist_ok=True))

    def click_show_hidden_files(self):
        if el := self.driver.find(self.loc.show_hidden_files, timeout=2, exist_ok=True):
            el.click(delay=2)
            console.print("点击显示隐藏文件")
        else:
            self.driver.back()

    def click_dont_show_hidden_files(self):
        if el := self.driver.find(
                self.loc.dont_show_hidden_files, timeout=2, exist_ok=True
        ):
            el.click(delay=2)
            console.print("点击不显示隐藏文件")
        else:
            self.driver.back()

    def click_delete(self):
        self.driver.find(self.loc.delete).click()
        console.print("点击删除")

    def click_share(self):
        self.driver.find(self.loc.share).click()
        console.print("点击分享")

    def click_search(self):
        self.driver.find(self.loc.search,timeout=5).click()
        console.print("点击搜索")

    def click_switch_views(self):
        self.driver.find(self.loc.switch_views).click(delay=2)
        console.print("点击切换视图")

    def click_image_tag(self):
        while True:
            if el := self.driver.find(self.loc.image_tag, timeout=1, exist_ok=True):
                break
            self.driver.find(self.loc.tag_bar).swipe(0.8, 0, 0.2, 0)
        el.click(delay=2)
        console.print("点击图片标签")

    def click_audio_tag(self):
        while True:
            if el := self.driver.find(self.loc.audio_tag, timeout=1, exist_ok=True):
                break
            self.driver.find(self.loc.tag_bar).swipe(0.8, 0, 0.2, 0)
        el.click(delay=2)
        console.print("点击音频标签")

    def click_videos_tag(self):
        while True:
            if el := self.driver.find(self.loc.videos_tag, timeout=1, exist_ok=True):
                break
            self.driver.find(self.loc.tag_bar).swipe(0.8, 0, 0.2, 0)
        el.click(delay=2)
        console.print("点击视频标签")

    def click_documents_tag(self):
        while True:
            if el := self.driver.find(self.loc.documents_tag, timeout=1, exist_ok=True):
                break
            self.driver.find(self.loc.tag_bar).swipe(0.8, 0, 0.2, 0)
        el.click(delay=2)
        console.print("点击文档标签")

    def click_large_files_tag(self):
        while True:
            if el := self.driver.find(
                    self.loc.large_files_tag, timeout=1, exist_ok=True
            ):
                break
            self.driver.find(self.loc.tag_bar).swipe(0.8, 0, 0.2, 0)
        el.click(delay=2)
        console.print("点击大型文件标签")

    def click_this_week_tag(self):
        while True:
            if el := self.driver.find(self.loc.this_week_tag, timeout=1, exist_ok=True):
                break
            self.driver.find(self.loc.tag_bar).swipe(0.8, 0, 0.2, 0)
        el.click(delay=2)
        console.print("点击本周标签")

    def sort_by_type(self, reverse: bool):
        self.driver.find(self.loc.sort_by_type(reverse)).click()
        console.print(f"选择排序方式：类型 ({'从Z到A' if reverse else '从A到Z'})")

    def sort_by_modified(self, reverse: bool):
        self.driver.find(self.loc.sort_by_modified(reverse)).click()
        console.print(f"选择排序方式：修改日期 ({'从新到旧' if reverse else '从旧到新'})")

    def sort_by_name(self, reverse: bool):
        self.driver.find(self.loc.sort_by_name(reverse)).click()
        console.print(f"选择排序方式：文件名 ({'从Z到A' if reverse else '从A到Z'})")

    def get_folders(self):
        """
        获取文件夹列表
        """
        for item in self.driver.find_all(self.loc.folder_or_file, timeout=2):
            if item.find(self.loc.create_date, timeout=0.5, exist_ok=True) is None:
                yield item

    def get_files(self):
        """
        获取文件列表
        """
        for item in self.driver.find_all(self.loc.folder_or_file, timeout=2):
            if item.find(self.loc.create_date, timeout=0.5, exist_ok=True) is not None:
                yield item

    def get_folder(self, name: str = None):
        """
        获取文件夹
        """
        folders = self.get_folders()
        if name is None:
            return next(folders, None)
        return next(
            (folder for folder in folders if self.get_name(folder) == name), None
        )

    def get_file(self, name: str = None):
        """
        获取文件
        """
        files = self.get_files()
        if name is None:
            return next(files, None)
        return next((file for file in files if self.get_name(file) == name), None)

    def get_name(self, context):
        """
        获取文件名
        """
        return context.find(self.loc.filename).get_text()

    def get_size(self, context):
        """
        获取文件文件
        """
        return context.find(self.loc.size).get_text()

    def get_tags(self):
        """
        获取文件标签
        """
        return self.driver.find_all(self.loc.tags)

    def get_create_time(self):
        """
        获取文件创建时间
        """
        return self.driver.find(self.loc.create_date).get_text()

    def get_modified(self):
        """
        获取上次修改时间
        """
        return self.driver.find(self.loc.modified).get_text()

    def get_no_file_tips(self):
        return self.driver.find(self.loc.no_file_tips,exist_ok=True,timeout=10)

    def confirm(self):
        self.driver.find(self.loc.ok).click(delay=2)
        console.print("点击确定")

    def click_enable_bluetooth(self):
        self.driver.find(self.loc.enable_bluetooth).click(delay=2)
        console.print("点击启用蓝牙")

    def click_new_folder(self):
        self.driver.find(self.loc.folder).click()
        console.print("点击新建文件夹")

    def click_screenshot_floder(self):
        self.driver.find(self.loc.screenshoot_floder).click()
        console.print("点击相机文件夹")

    def hold_floder(self):
        with self.driver.actions_manager() as action:
            action.click_and_hold(self.driver.find(self.loc.floder),duration=5)
        console.print("长按文件夹")

    def hold_photo(self):
        with self.driver.actions_manager() as action:
            action.click_and_hold(self.driver.find(self.loc.photo),duration=5)
        console.print("长按照片")

    def click_photo(self):
        self.driver.find(self.loc.photo).click()
        console.print("点击照片")

    def delete_photo(self):
        self.driver.find(self.loc.del_photo).click()
        console.print("删除照片")

    def delete_confirm(self):
        self.driver.find(self.loc.del_confirm).click()
        console.print("确定删除")

    def click_video(self):
        self.driver.find(self.loc.video).click()
        console.print("点击视频")

    def click_movies_floder(self):
        self.driver.find(self.loc.movies_floder).click()
        console.print("点击电影")

    def get_devices_name(self):
        return self.driver.find(self.loc.device_name).get_text()

    def click_recent_image(self):
        self.driver.find(self.loc.recent_image).click()
        console.print("最近图片")

    def click_recent_voice(self):
        self.driver.find(self.loc.recent_voice).click()
        console.print("最近音频")

    def click_recent_video(self):
        self.driver.find(self.loc.recent_video).click()
        console.print("最近视频")

    def click_recent_file(self):
        self.driver.find(self.loc.recent_file).click()
        console.print("最近文件")

    def click_recent_large_files(self):
        self.driver.find(self.loc.recent_large_files).click()
        console.print("最近图片")

    def click_recent_this_week(self):
        ele = self.driver.find(self.loc.recent_large_files, exist_ok=True)
        el = self.driver.find(self.loc.recent_image, exist_ok=True)
        el2 = self.driver.find(self.loc.recent_this_week,exist_ok=True)
        while True:
            with self.driver.actions_manager() as actions:
                actions.click_and_hold(ele, duration= 5)
                actions.move_to_element(el, duration=3)
            if el2:
                self.driver.find(self.loc.recent_this_week).click()
                break
        console.print("最近本周")

    def click_this_week(self):
        self.driver.find(self.loc.recent_this_week, exist_ok=True).click()
        console.print("最近本周")

    def click_first_file(self, duration = None):
        ele = self.driver.find(self.loc.frist_file)
        if duration is None:
            ele.click(delay=2)
        else:
            with self.driver.actions_manager() as actions:
                actions.click_and_hold(ele, duration=duration)

    def click_recent_more(self):
        self.driver.find(self.loc.recent_more).click()
        console.print("更多")

    def click_open_ways(self):
        self.driver.find(self.loc.open_ways).click()
        console.print("点击打开方式")

    def click_select_all(self):
        self.driver.find(self.loc.select_all).click()
        console.print("全选")

    def click_unknown_folder(self):
        self.driver.find(self.loc.unknown_folder).click()
        console.print("未知文件夹")

    def click_local(self):
        self.driver.find(self.loc.local).click()
        console.print("点击本地")

    def click_camera_folder(self):
        self.driver.find(self.loc.camera_folder).click()
        console.print("点击相机文件夹")

