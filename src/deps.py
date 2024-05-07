from soium import Driver
from soium import Selector, XPath
from soium.utils.logger import console

__all__ = [
    "Selector",
    "XPath",
    "BasePage",
    "console",
]


class BasePage:
    def __init__(self, driver: Driver):
        self.driver = driver
