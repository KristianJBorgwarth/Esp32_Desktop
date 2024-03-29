import network
import urequests

class WifiConnectionTester:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
    
    def CheckWifiConnection(self):
        if not self.wlan.isconnected():
            return False
        
        try:
            response = urequests.get("http://httpbin.org/get")
            response.close()
            print("WifiConnectionTester: Connected to the internet")
            return True
        except:
            print("WifiConnectionTester: Not connected to the internet")
            return False
 
    
    