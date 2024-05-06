from src.deps import *


class BluetoothReceived(BasePage):
    """
    通过蓝牙收到的文件页
    """

    class loc:
        histories = Selector(XPath(id="com.android.bluetooth:id/list").join(
                "android.widget.RelativeLayout"
            ),
            description="历史记录",
        )
        no_data = Selector(XPath(has_text="无任何文件"), description="无数据"
        )

    def get_histories(self):
        """
        获取历史记录
        """
        return self.driver.find_all(self.loc.histories)

    def is_empty(self):
        """
        是否为空数据页
        """
        return self.driver.find(self.loc.no_data, timeout=2).is_visible()
