import math
import time
from soium import Keys
from src.deps import *



class Sound(BasePage):
    """
    屏幕方向
    """

    class loc:

        media_volume = Selector(
            XPath(has_content="媒体音量"),
            description="媒体音量"
        )
        notification_volume = Selector(
            XPath(has_content="通知音量"),
            description="通知音量"
        )
        touchu_tone_volume = Selector(
            XPath(has_content="触摸提示音音量"),
            description="触摸提示音音量"
        )
        touch_tone_volume = Selector(
            XPath(has_content="触屏音量",id="android:id/seekbar"),
            description="触屏音量"
        )
        media_volume_title = Selector(
            XPath(has_text="媒体音量"),
            description="媒体音量"
        )
        notification_volume_title = Selector(
            XPath(has_text="通知音量"),
            description="通知音量"
        )
        touchu_tone_volume_title = Selector(
            XPath(has_text="触摸提示音音量"),
            description="触摸提示音音量"
        )


    def drag_media_volume(self, level: int):
        """
        拖动媒体音量
        """
        bar = self.driver.find(self.loc.media_volume)
        width = bar.size["width"]
        max_level = self.driver.get_max_volume_level()
        mid_level = math.ceil(max_level / 2)
        offset = -(width / max_level * (mid_level - level))
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0, duration=2).release()

    def drag_notification_volume(self, level: int):
        """
        拖动通知音量
        """
        bar = self.driver.find(self.loc.notification_volume)
        width = bar.size["width"]
        max_level = self.driver.get_max_notification_level()
        mid_level = math.ceil(max_level / 2)
        offset = -(width / max_level * (mid_level - level))
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0, duration=2).release()

    def drag_touchu_tone_volume(self, level: int):
        """
        拖动通知音量
        """
        bar = self.driver.find(self.loc.touchu_tone_volume)
        width = bar.size["width"]
        max_level = self.driver.get_max_notification_level()
        mid_level = math.ceil(max_level / 2)
        offset = -(width / max_level * (mid_level - level))
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0, duration=2).release()


    def media_volume_title(self):
        self.driver.find(self.loc.media_volume_title)
        console.print("媒体音量")

    def notification_volume_title(self):
        self.driver.find(self.loc.notification_volume_title)
        console.print("通知音量")

    def touchu_tone_volume_title(self):
        self.driver.find(self.loc.touchu_tone_volume_title)
        console.print("触摸提示音音量")

    def drag_touch_tone_volume(self, level: int):
        """
        拖动通知音量
        """
        bar = self.driver.find(self.loc.touch_tone_volume)
        width = bar.size["width"]
        max_level = self.driver.get_max_notification_level()
        mid_level = math.ceil(max_level / 2)
        offset = -(width / max_level * (mid_level - level))
        with self.driver.actions_manager() as actions:
            actions.click_and_hold(bar)
            actions.move_by_offset(offset, 0, duration=2).release()