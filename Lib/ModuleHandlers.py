from machine import Pin, SoftI2C
import Drivers.SSD1306 as SSD1306
from DebugTools.DeviceConnectionTester import I2CDeviceTester

class OledHandler:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OledHandler, cls).__new__(cls)
            i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
            oled_width = 128
            oled_height = 64
            cls._instance.oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)
            
        return cls._instance
        
    def DisplayMessage(self, message):
        self.oled.fill(0)  # Clear the display
        max_chars_per_line = 15  # Adjust this based on your display and font size
        words = message.split(' ')
        lines = []
        current_line = ''
        
        for word in words:
            if len(current_line) + len(word) + 1 <= max_chars_per_line:
                current_line += (word + ' ')
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)  # Add the last line
        
        for i, line in enumerate(lines):
            if i < 8:  # Prevent adding more lines than the display can show (adjust based on your display's capability)
                self.oled.text(line.strip(), 0, i * 10)
        
        self.oled.show()