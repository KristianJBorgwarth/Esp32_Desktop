from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager
from Lib.ModuleHandlers import OledHandler
from Lib import ugit
import time

class Application:
    
    def __init__(self):
        self.oled_handler = OledHandler()
        self.wifi_manager = WifiManager(self.oled_handler)
        self.wifi_tester = WifiConnectionTester()
        
    def Initialize(self):
        self.oled_handler.DisplayMessage("Initializing..")
        self.wifi_manager.RunServer()
        self.wifi_tester.CheckWifiConnection()
    
        
    def Start(self):
        self.oled_handler.DisplayMessage("Running Start")
        #ugit.pull_all(isconnected = True)
        time.sleep(1)
        
    def Update(self):
        self.oled_handler.DisplayMessage("Running Update")
        while True:
            
            #continous update logic should run here
            #consider creating a statemachine to run within update
            time.sleep(0.2)
    
    def ShutdownApplication():
        pass