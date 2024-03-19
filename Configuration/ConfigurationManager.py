class ConfigManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.wifi_ssid = "defaultSSID"
            cls._instance.wifi_password = "defaulfPassword"
            
        return cls._instance
    
    def set_wifi_credentials(self, ssid, password):
        print("Config called")
        self.wifi_ssid = ssid
        self.wifi_password = password
        
    def get_wifi_credentials(self):
        return self.wifi_ssid, self.wifi_password