import time

from src.deps import *
from soium import Keys

class Music(BasePage):
    """
    音乐APP
    """

    class loc:
        artists = Selector(XPath(has_text="音乐人"), description="音乐人")
        albums = Selector(XPath(has_text="专辑"), description="音乐专辑")
        songs = Selector(XPath(has_text="歌曲"), description="音乐")

        playlists = Selector(XPath(has_text="Playlists"), description="播放列表")
        now_playing = Selector(XPath(has_text="Now playing"), description="现在播放")
        recently_added = Selector(XPath(has_text="Recently added"), description="最近添加")
        save = Selector(XPath(has_text="Save"), description="保存")
        add_playlist = Selector(
            XPath(has_text="Add to playlist"), description="添加到播放列表"
        )
        play = Selector(XPath(has_text="Play"), description="播放")
        new = Selector(XPath(has_text="New"), description="新的")
        delete = Selector(XPath(has_text="Delete"), description="删除")
        searh = Selector(XPath(has_text="Search"), description="搜索")
        chrome = Selector(XPath(has_text="Chrome"), description="浏览器")
        play_all = Selector(XPath(has_text="Play all"), description="播放所有")
        party_shuffle = Selector(XPath(has_text="Party shuffle"), description="派对随机播放")
        party_shuffle_off = Selector(
            XPath(has_text="Party shuffle off"), description="关闭派对随机播放"
        )
        shuffle_all = Selector(XPath(has_text="Shuffle all"), description="全部随机播放")
        save_as_playlist = Selector(
            XPath(has_text="Save as playlist"), description="另存为播放列表"
        )
        music_name = Selector(XPath(id="com.android.music:id/line1"), description="音乐名")
        test_name = Selector(XPath(has_text="Test_Test"), description="测试名")
        progress_bar = Selector(XPath(id="android:id/progress"), description="音乐进度条")
        playlist_name = Selector(
            XPath(id="com.android.music:id/playlist"), description="重命名"
        )
        ok = Selector(XPath(has_text="OK"), description="好的")
        header = Selector(XPath(id="android:id/chooser_header"), description="面板")
        more_options = Selector(XPath(has_content="More options"), description="更多选项")
        rename = Selector(XPath(has_text="Rename"), description="重命名")
        rename_suc = Selector(XPath(has_text="Platlist renamed."), description="已重命名")
        clear_playlist = Selector(
            XPath(has_text="Clear playlist"), description="清空播放列表"
        )
        play_problem = Selector(XPath(has_text="Playback problem"), description="播放器异常")
        curplaylist_btn = Selector(
            XPath(id="com.android.music:id/curplaylist"), description="播放列表按钮"
        )
        shuffle_btn = Selector(
            XPath(id="com.android.music:id/shuffle"), description="随机播放按钮"
        )
        repeat_btn = Selector(
            XPath(id="com.android.music:id/repeat"), description="重复播放按钮"
        )
        shuffle_off = Selector(XPath(has_text="Shuffle is off."), description="关闭随机播放")
        shuffle_on = Selector(XPath(has_text="Shuffle is on."), description="开启随机播放")
        title = Selector(
            XPath(id="android:id/action_bar").join("android.widget.TextView"),
            description="标题",
        )
        repeat_off = Selector(XPath(has_text="Repeat is off."), description="关闭循环播放")
        repeat_all = Selector(
            XPath(has_text="Repeating all songs."), description="循环播放所有音乐"
        )
        repeat_one = Selector(
            XPath(has_text="Repeating current song."), description="单首循环"
        )
        prev_btn = Selector(XPath(id="com.android.music:id/prev"), description="上一首")
        pause_btn = Selector(XPath(id="com.android.music:id/pause"), description="暂停按钮")
        next_btn = Selector(XPath(id="com.android.music:id/next"), description="下一首")
        play_name = Selector(
            XPath(id="com.android.music:id/trackname"), description="正在播放的音乐"
        )
        currenttime = Selector(
            XPath(id="com.android.music:id/currenttime"), description="当前播放时间"
        )

        music_list = Selector(
            XPath(id="android:id/list").join("android.widget.RelativeLayout"),
            description="音乐列表",
        )

        list_name = Selector(
            XPath(id="android:id/list").join(
                "android.widget.RelativeLayout/android.widget.TextView"
            ),
            description="列表名",
        )

        mini_player = Selector(XPath(id="android:id/content"), description="迷你播放器")

        # toast_1 = ["song added to playlist.", "songs added to playlist."]
        add_toast = Selector(
            XPath(has_content="added to playlist."), description="添加音乐列表的Toast"
        )
        toast_2 = ["song were deleted.", "song was deleted."]
        delete_toast = Selector(XPath(has_text=toast_2), description="删除音乐的Toast")

        search_zr = Selector(XPath(has_content="搜索", id="com.android.music:id/search"), description="搜索")
        search_input_zr = Selector(XPath(id="android:id/search_src_text"), description="搜索内容")
        search_result_zr = Selector(XPath(id="com.android.music:id/line1"), description="搜索结果")
        settings_zr = Selector(XPath(id="com.android.music:id/setting"), description="设置")
        equalizer_zr = Selector(XPath(id="android:id/title",has_text="均衡器"), description="均衡器")
        turn_on_equalizer_zr = Selector(XPath("//android.widget.Switch"), description="启动均衡器")
        turn_on_scheduled_zr = Selector(XPath(id="android:id/switch_widget"), description="启动定时关闭")
        scheduled_setting_zr = Selector(XPath(id="com.android.music:id/radio_view").join("android.widget.RadioButton"),
                                        description="关闭时间设定")
        timer_done_zr = Selector(XPath(id="com.android.music:id/timer_done", has_text="完成"), description="完成设置")
        done_toast_zr = Selector(XPath(has_text="设置成功，音乐将在倒计时结束后自动关闭。"), description="完成提示")
        more_options_zr = Selector(XPath(has_content="更多选项"), description="更多选项")
        exit_zr = Selector(XPath(id="com.android.music:id/title", has_text="退出"), description="退出")
        artists_list_zr = Selector(XPath(id="android:id/list").join("android.widget.RelativeLayout"),description="音乐人列表")
        artists_detail_zr = Selector(XPath(id="com.android.music:id/grid").join("android.widget.LinearLayout"),
                                     description="专辑文件夹")
        music_play_zr = Selector(XPath(id="com.android.music:id/track_name",has_text="IMY_3_imy_3"),description="播放音乐")
        albums_options_zr = Selector(XPath(id="com.android.music:id/show_options"),description="专辑选项")
        options_expand_zr = Selector(XPath(has_text="添加到播放列表", id="android:id/title"),description="添加到播放列表")
        albums_list_zr = Selector(XPath(id="com.android.music:id/grid").join("android.widget.LinearLayout"),description="专辑列表")

    def list_tap_play(self):
        self.driver.find_all(self.loc.music_list).last.tap(7)
        self.driver.find(self.loc.play).click()
        console.print("长按最后一个音乐，点击播放")

    def list_tap_add(self):
        console.print("长按最后一个音乐，添加到新的播放列表")
        self.driver.find_all(self.loc.music_list).last.tap(7)
        self.driver.find(self.loc.add_playlist).click()
        self.driver.find(self.loc.new).click()
        self.driver.find(self.loc.save).click()

    def list_click(self):
        self.driver.find_all(self.loc.music_list).first.click()
        console.print("点击最后一个音乐")

    def list_tap_del(self):
        self.driver.find_all(self.loc.music_list).last.tap(7)
        self.driver.find(self.loc.delete).click()
        self.driver.find(self.loc.ok).click()
        console.print("长按最后一个音乐，删除")

    def playlist_del(self):
        self.driver.find_all(self.loc.music_list).last.tap(7)
        self.driver.find(self.loc.delete).click()
        console.print("长按最后一个播放列表，删除")

    def list_tap_search(self):
        self.driver.find_all(self.loc.music_list).last.tap(7)
        self.driver.find(self.loc.searh).click()
        console.print("长按最后一个音乐，搜索")

    def list_tap_rename(self, text: str = "test"):
        self.driver.find_all(self.loc.music_list).last.tap(7)
        self.driver.find(self.loc.rename).click()
        self.driver.find(self.loc.playlist_name).fill(text)
        self.driver.find(self.loc.save).click()
        console.print("长按最后一个音乐，重命名为:" + text)

    def click_artists(self):
        self.driver.find(self.loc.artists).click()
        console.print("点击音乐人")

    def click_albums(self):
        self.driver.find(self.loc.albums).click()
        console.print("点击音乐集")

    def click_songs(self):
        self.driver.find(self.loc.songs).click()
        console.print("点击歌曲")

    def click_playlists(self):
        self.driver.find(self.loc.playlists).click()
        console.print("点击播放列表")

    def click_playing(self):
        self.driver.find(self.loc.now_playing).click()
        console.print("点击正在播放")

    def click_recently_add(self):
        self.driver.find(self.loc.recently_added).click()
        console.print("点击最近添加")

    def click_party_shuffle(self):
        self.driver.find(self.loc.more_options).click()
        self.driver.find(self.loc.party_shuffle).click()
        console.print("点击随机播放")

    def click_save_test_playlist(self):
        self.driver.find(self.loc.more_options).click()
        self.driver.find(self.loc.save_as_playlist).click()
        self.driver.find(self.loc.save).click()
        console.print("点击保存到播放列表")

    def click_more_savelist(self, test: str = "Test"):
        self.driver.find(self.loc.more_options).click()
        self.driver.find(self.loc.save_as_playlist).click()
        self.driver.find(self.loc.playlist_name).fill(test)
        self.driver.find(self.loc.save).click()
        console.print("点击更多，重命名为Test,点击保存到播放列表")

    def click_off_shuffle(self):
        self.driver.find(self.loc.party_shuffle_off).click()
        console.print("点击关闭随机播放")

    def click_play(self):
        self.driver.find(self.loc.play).click()
        console.print("点击播放")

    def click_playall(self):
        self.driver.find(self.loc.more_options).click()
        self.driver.find(self.loc.play_all).click()
        console.print("播放所有")

    def click_shuffle_all(self):
        self.driver.find(self.loc.more_options).click()
        self.driver.find(self.loc.shuffle_all).click()
        console.print("随机播放所有")

    def click_clear_playlist(self):
        self.driver.find(self.loc.more_options).click()
        self.driver.find(self.loc.clear_playlist).click()
        console.print("清除播放列表")

    def click_shuffle(self):
        self.driver.find(self.loc.shuffle_btn).click()
        console.print("点击随机播放按钮")

    def click_repeat_btn(self):
        self.driver.find(self.loc.repeat_btn).click()
        console.print("点击循环按钮")

    def click_curplaylist(self):
        self.driver.find(self.loc.curplaylist_btn).click()
        console.print("点击播放列表")

    def click_prev(self):
        self.driver.find(self.loc.prev_btn).click()
        console.print("点击上一首")

    def click_next(self):
        self.driver.find(self.loc.next_btn).click()
        console.print("点击下一首")

    def click_pause(self):
        self.driver.find(self.loc.pause_btn).click()
        console.print("点击暂停or播放")

    def get_music_num(self):
        num = self.driver.find_all(self.loc.music_list).count()
        console.print("当前列表数量：" + str(num))
        return num

    def get_playing(self):
        return self.driver.find(self.loc.progress_bar, exist_ok=True)

    def get_add(self):
        return self.driver.find(
            self.loc.add_toast, timeout=10, exist_ok=True
        )  # 无法通过toast判断

    def get_del(self):
        return self.driver.find(
            self.loc.delete_toast, timeout=10, exist_ok=True
        )  # 无法通过toast判断

    def get_search_box(self):
        return self.driver.find(self.loc.header, timeout=10, exist_ok=True)

    def get_more(self):
        return self.driver.find(self.loc.more_options, timeout=5, exist_ok=True)

    def get_shuffle_off(self):
        self.driver.find(self.loc.more_options).click()
        return self.driver.find(self.loc.party_shuffle_off, timeout=5, exist_ok=True)

    def get_playing_name(self):
        playing_name = self.driver.find(self.loc.play_name).get_text()
        console.print("获取当前播放的音乐名：" + str(playing_name))
        return playing_name

    def get_playing_time(self):
        playing_time = self.driver.find(self.loc.currenttime).get_text()
        console.print("获取当前播放的音乐时间：" + str(playing_time))
        return playing_time

    def get_last_name(self):
        last_list = self.driver.find_all(self.loc.list_name).last
        name = last_list.get_text()
        console.print("获取最后一个列表的名字:" + str(name))
        return name

    def get_rename(self):
        return self.driver.find(self.loc.test_name, exist_ok=True, timeout=10)

    def mini_player_is_exist(self):
        return bool(self.driver.find(self.loc.mini_player, timeout=2, exist_ok=True))

    def resting_screen(self):
        self.driver.press_keycode(Keys.POWER)
        time.sleep(5)
        self.driver.press_keycode(Keys.POWER)
        console.print("息屏")

    def click_search_rz(self):
        self.driver.find(self.loc.search_zr).click()
        console.print("点击查询")
        self.driver.find(self.loc.search_input_zr).fill("awb")
        console.print("搜索awb")
        self.driver.find(self.loc.search_result_zr).click()
        console.print("点击查询结果")

    def click_settings_zr(self):
        self.driver.find(self.loc.settings_zr).click()
        console.print("点击设置")

    def click_equalizer_zr(self):
        self.driver.find(self.loc.equalizer_zr).click()
        console.print("点击均衡器")

    def turn_on_equalizer_zr(self):
        self.driver.find(self.loc.turn_on_equalizer_zr).click()
        console.print("开启均衡器")

    def turn_on_scheduled_zr(self):
        self.driver.find(self.loc.turn_on_scheduled_zr).click()
        console.print("开启定时关闭")

    def scheduled_setting_zr(self):
        self.driver.find_all(self.loc.scheduled_setting_zr).random.click()
        time.sleep(5)
        self.driver.find(self.loc.timer_done_zr).click()

    def done_toast_zr(self):
        ele = self.driver.find(self.loc.done_toast_zr).is_visible()
        if ele is not None:
            return True
        return False

    def click_more_options_zr(self):
        self.driver.find(self.loc.more_options_zr).click()
        console.print("点击更多选项")

    def click_exit_zr(self):
        self.driver.find(self.loc.exit_zr).click()
        console.print("点击退出")

    def click_artists_list_zr(self):
        self.driver.find_all(self.loc.artists_list_zr).random.click()
        console.print("选择音乐人")

    def click_artists_detail_zr(self):
        self.driver.find_all(self.loc.artists_detail_zr).random.click()
        console.print("选择专辑")

    def music_play_zr(self):
        self.driver.find(self.loc.music_play_zr).click()
        console.print("播放音乐")

    def music_albums_options_zr(self):
        self.driver.find(self.loc.albums_options_zr).click()
        console.print("点击专辑选项")

    def options_expand_zr(self):
        ele = self.driver.find(self.loc.options_expand_zr)
        if ele is not None:
            return True
        return False

    def click_albums_list_zr(self):
        self.driver.find_all(self.loc.albums_list_zr).random.click()
        console.print("点击专辑列表")


