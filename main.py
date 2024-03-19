from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager
from Lib.ModuleHandlers import OledHandler

oled_handler = OledHandler()

tester = I2CDeviceTester(22, 21)
wifiTester = WifiConnectionTester()

oled_handler("i am a genius")

tester.check_display_connection()

wifi_manager = WifiManager()

wifi_manager.RunServer()

wifiTester.CheckWifiConnection()
