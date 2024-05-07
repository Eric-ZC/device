import pytest
from soium import Driver

from src.pom.sys.bluetooth import Bluetooth
from src.pom.sys.settings import Settings
from src.pom.sys.about_devices import AboutDevice
from src.pom.sys.notification_panel import NotificationPanel
from src.pom.sys.camera import Camera
from src.pom.sys.connected_devices import ConnectedDevices
from src.pom.app.diagnosis import Diagnosis
from src.pom.app.gallery import Gallery
from src.pom.sys.display import Display
from src.pom.app.chrome import Chrome
from src.pom.app.calculator import Calculator
from src.pom.app.files import Files
from src.pom.app.music import Music
from src.pom.sys.gestures import Gestures
from src.pom.app.lanucher import Launcher
from src.pom.sys.bluetooth_received import BluetoothReceived
from src.pom.sys.connection_preferences import ConnectionPreferences
from src.pom.app.appstore import AppStore
from src.pom.app.google_store import GoogleStore
from src.pom.sys.network import Network
from src.pom.sys.wifi import WiFi
from src.pom.sys.networkdetails import NetworkDetails
from src.pom.sys.orientation import Orientation
from src.pom.sys.data_time import DataTime
from src.pom.sys.language import Language
from src.pom.sys.reset_wlan_network import ResetWlanNetwork
from src.pom.sys.security import Security
from src.pom.sys.sound import Sound
from src.pom.sys.reset_option import ResetOption


from src.pom import Pom

pytest_plugins = ("soium.plugin.report",)

@pytest.fixture(scope="session")
def bluetooth_page(driver: Driver):
    return Bluetooth(driver)

@pytest.fixture(scope="session")
def settings_page(driver: Driver):
    return Settings(driver)

@pytest.fixture(scope="session")
def about_device_page(driver: Driver):
    return AboutDevice(driver)

@pytest.fixture(scope="session")
def notification_panel(driver: Driver):
    return NotificationPanel(driver)

@pytest.fixture(scope="session")
def camera_page(driver: Driver):
    return Camera(driver)

@pytest.fixture(scope="session")
def connected_devices_page(driver: Driver):
    return ConnectedDevices(driver)

@pytest.fixture(scope="session")
def diagnosis_page(driver: Driver):
    return Diagnosis(driver)

@pytest.fixture(scope="session")
def gallery_page(driver: Driver):
    return Gallery(driver)

@pytest.fixture(scope="session")
def display_page(driver: Driver):
    return Display(driver)

@pytest.fixture(scope="session")
def chrome_page(driver: Driver):
    return Chrome(driver)

@pytest.fixture(scope="session")
def calculator_page(driver: Driver):
    return Calculator(driver)

@pytest.fixture(scope="session")
def files_page(driver: Driver):
    return Files(driver)

@pytest.fixture(scope="session")
def music_page(driver: Driver):
    return Music(driver)

@pytest.fixture(scope="session")
def gestures_page(driver: Driver):
    return Gestures(driver)

@pytest.fixture(scope="session")
def launcher_page(driver: Driver):
    return Launcher(driver)

@pytest.fixture(scope="session")
def bluetooth_received_page(driver: Driver):
    return BluetoothReceived(driver)

@pytest.fixture(scope="session")
def connection_preferences_page(driver: Driver):
    return ConnectionPreferences(driver)

@pytest.fixture(scope="session")
def appstore_page(driver: Driver):
    return AppStore(driver)

@pytest.fixture(scope="session")
def googlestore_page(driver:Driver):
    return GoogleStore(driver)

@pytest.fixture(scope="session")
def network_page(driver: Driver):
    return Network(driver)

@pytest.fixture(scope="session")
def network_details_page(driver: Driver):
    return NetworkDetails(driver)

@pytest.fixture(scope="session")
def wifi_page(driver: Driver):
    return WiFi(driver)

@pytest.fixture(scope="session")
def orientation_page(driver:Driver):
    return Orientation(driver)

@pytest.fixture(scope="session")
def data_time_page(driver:Driver):
    return DataTime(driver)

@pytest.fixture(scope="session")
def language_page(driver:Driver):
    return Language(driver)


@pytest.fixture(scope="session")
def reset_wlan_network_page(driver:Driver):
    return ResetWlanNetwork(driver)


@pytest.fixture(scope="session")
def security_page(driver: Driver):
    return Security(driver)


@pytest.fixture(scope="session")
def sound_page(driver: Driver):
    return Sound(driver)


@pytest.fixture(scope="session")
def reset_option_page(driver: Driver):
    return ResetOption(driver)

@pytest.fixture(scope="session")
def pom(driver: Driver):
    return Pom(driver)
