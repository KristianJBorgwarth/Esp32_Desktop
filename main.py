from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager
from Lib.ModuleHandlers import OledHandler

oled_handler = OledHandler()

tester = I2CDeviceTester(22, 21)
tester.check_display_connection()

wifi_manager = WifiManager(oled_handler)
wifi_manager.RunServer()

wifiTester = WifiConnectionTester()
wifiTester.CheckWifiConnection()
