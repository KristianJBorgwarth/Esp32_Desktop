from umqtt.robust import MQTTClient
DELIMITER = ";"
VALUE_SEPARATOR = "="
## Keyword in Connection string  
HOST_NAME = "HostName"
SHARED_ACCESS_KEY_NAME = "SharedAccessKeyName"
SHARED_ACCESS_KEY = "SharedAccessKey"
SHARED_ACCESS_SIGNATURE = "SharedAccessSignature"
DEVICE_ID = "DeviceId"
MODULE_ID = "ModuleId"
GATEWAY_HOST_NAME = "GatewayHostName"


class MQTTClient(MQTTClient):     
    def __init__(self, connstr="", password="", port=8883, keepalive=120, ssl=True):
        ## Parse the connection string into constituent partsdef
        self.dict_keys = self.parse_connection(connstr)
        self.shared_access_key = self.dict_keys.get(SHARED_ACCESS_KEY)
        self.shared_access_key_name =  self.dict_keys.get(SHARED_ACCESS_KEY_NAME)
        self.gateway_hostname = self.dict_keys.get(GATEWAY_HOST_NAME)
        self.hostname = self.dict_keys.get(HOST_NAME)
        self.device_id = self.dict_keys.get(DEVICE_ID)
        self.module_id = self.dict_keys.get(MODULE_ID)
        ## Create username following the below format '<HOSTNAME>/<DEVICE_ID>'
        self.username = self.hostname + '/' + self.device_id
        if not keepalive:
            keepalive = 120
        if not ssl:
            ssl = True
        c = super().__init__(client_id=self.device_id, server=self.hostname, port=8883, user=self.username, password=password, keepalive=120, ssl=True)
        #c.DEBUG = True
        return c

    def get_telemetry_topic(self):
        return self.get_topic_base(self.device_id) + "/messages/events/"
    
    def get_c2d_topic(self):
         return self.get_topic_base(self.device_id) + "/temp/"

    def get_topic_base(self,device_id, module_id=None):
        if module_id:
            base_str = "devices/" + self.device_id + "/modules/" + self.module_id
        else:
            base_str = "devices/" + self.device_id
        return base_str

    def parse_connection(self,connection_string):
        cs_args = connection_string.split(DELIMITER)
        dictionary = dict(arg.split(VALUE_SEPARATOR, 1) for arg in cs_args)
        return dictionary