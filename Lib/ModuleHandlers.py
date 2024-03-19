from machine import Pin, SoftI2C
import Drivers.SSD1306 as SSD1306
from DebugTools.DeviceConnectionTester import I2CDeviceTester

class OledHandler:
    def __init__(self):
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        oled_width = 128
        oled_height = 64
        self.oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)
        
    def DisplayMessage(self, message):
        self.oled.fill(0)
        lines = message.split('\n')
        for i, line in enumerate(lines):
            self.oled.text(line, 0, i * 10)
        self.oled.show()