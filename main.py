from machine import Pin, SoftI2C
import Drivers.SSD1306 as SSD1306
from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager


tester = I2CDeviceTester(22, 21)
wifiTester = WifiConnectionTester()

tester.check_display_connection()
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('God save me', 0, 0)
oled.text("from this hell", 0, 10)
oled.text("I'm in", 0, 20)
oled.show()

wifi_manager = WifiManager()

wifi_manager.RunServer()

wifiTester.CheckWifiConnection()
