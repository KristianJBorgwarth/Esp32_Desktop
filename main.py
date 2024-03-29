from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager
from Lib.ModuleHandlers import OledHandler
from Lib import ugit

oled_handler = OledHandler()

tester = I2CDeviceTester(22, 21)
tester.check_display_connection()

wm = WifiManager("GodBless","696969420")
wm.connect()

wifiTester = WifiConnectionTester()
wifiTester.CheckWifiConnection()

ugit.pull_all(isconnected = True)