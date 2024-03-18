from machine import Pin, SoftI2C
import SSD1306
from DebugTools.displayConnectTester import I2CDeviceTester


tester = I2CDeviceTester(22, 21)

tester.check_display_connection()
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
# Use the correct case for SSD1306
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('God save me', 0, 0)
oled.text("from this hell", 0, 10)

oled.show()
