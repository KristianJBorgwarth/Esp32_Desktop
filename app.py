from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager
from Lib.ModuleHandlers import OledHandler
from Lib import ugit
import time

class Application:
    
    def __init__(self)
        self.oled_handler = OledHandler()
        self.wifi_manager = WifiManager(oled_handler)
        self.wifi_tester = WifiConnectionTester()
        
    def Initialize(self):
        oled_handler.DisplayMessage("Initializing..")
        time.sleep(1)
        
        wifi_manager.RunServer()
        wifi_tester.CheckWifiConnection()
        
    def Start(self):
        oled_handler.DisplayMessage("Running Start")
        ugit.pull_all(isconnected = True)
        
    def Update(self):
        oled_handler.DisplayMessage("Running Update")
        while True:
            
            
            time.sleep(0.2)
    
    def ShutdownApplication():
        pass