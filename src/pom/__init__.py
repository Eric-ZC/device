from .keyboard import Keyboard
from .store import AppStores


class Pom:
    def __init__(self, driver):
        self.driver = driver

    @property
    def keyboard(self):
        return Keyboard(self.driver)

    @property
    def store(self):
        return AppStores(self.driver)
