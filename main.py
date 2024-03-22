from DebugTools.DeviceConnectionTester import I2CDeviceTester
from DebugTools.WifiConnectionTester import WifiConnectionTester
from Lib.WifiManager import WifiManager
from Lib.ModuleHandlers import OledHandler
from Lib import ugit
import paho.mqtt.client as mqtt
from time import sleep
from ssl import SSLContext, PROTOCOL_TLS_CLIENT, CERT_REQUIRED

#oled_handler = OledHandler()

#tester = I2CDeviceTester(22, 21)
#tester.check_display_connection()

#wm = WifiManager("GodBless","696969420")
#wm.connect()

#wifiTester = WifiConnectionTester()
#wifiTester.CheckWifiConnection()

#ugit.pull_all(isconnected = True)

"""ESP32 Device using MS Azure IoT Hub and MQTT for publishing data.

This program is written for a ESP32 (FireBeetle) board and is using MS IoT Hub
for publishing data (temperatur). The code requires that micropython (version 1.14) is
installed on the board and that a WiFi connection is established (access to Internet).

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Ib Helmer Nielsen, UCN"
__copyright__ = "Copyright 2024"
__credits__ = ["Microsoft Corporation"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__date__ = "2024/03/18"
__maintainer__ = "Ib Helmer Nielsen"
__email__ = "ihn@ihn.dk"
__status__ = "Beta"
## Shared Access Signatur
sas_token_str = "SharedAccessSignature sr=ihniothub.azure-devices.net%2Fdevices%2FESP32%231&sig=vAm0mto5FbcEEXnwo8ZUfvQ3olR2lgJ8S86GcuLBeGk%3D&se=1711057020"
conn="HostName=ihniothub.azure-devices.net;DeviceId=ESP32#1;SharedAccessKey=T6RmHu7SGt/7Hs9DvkWcnI7fml+0EL1uG9UzQrh3wts="
## Import of lib

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.



IOT_HUB_NAME      = "Gruppe6Hub.azure-devices.net"
IOT_HUB_DEVICE_ID = "G6Device"
IOT_HUB_SAS_TOKEN = "SharedAccessSignature sr=Gruppe6Hub.azure-devices.net&sig=kY2nGXVdWNGsOXJq3u2JvFe%2B%2BZlCkHxbtQXfUN4%2FgJI%3D&se=1711108312&skn=iothubowner"

def on_connect(mqtt_client, obj, flags, rc):
    print("connect: " + str(rc))

def on_publish(mqtt_client, obj, mid):
    print("publish: " + str(mid))

mqtt_client = mqtt.Client(client_id=IOT_HUB_DEVICE_ID, protocol=mqtt.MQTTv311)
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

mqtt_client.username_pw_set(username=IOT_HUB_NAME + ".azure-devices.net/" + IOT_HUB_DEVICE_ID + "/?api-version=2021-04-12", 
                            password=IOT_HUB_SAS_TOKEN)

ssl_context = SSLContext(protocol=PROTOCOL_TLS_CLIENT)
ssl_context.load_default_certs()
ssl_context.verify_mode = CERT_REQUIRED
ssl_context.check_hostname = True
mqtt_client.tls_set_context(context=ssl_context)

mqtt_client.connect(host=IOT_HUB_NAME + ".azure-devices.net", port=8883, keepalive=120)

# start the MQTT processing loop
mqtt_client.loop_start()

# send telemetry
messages = ["Accio", "Aguamenti", "Alarte Ascendare", "Expecto Patronum", "Homenum Revelio"]
for i in range(0, len(messages)):
    print("sending message[" + str(i) + "]: " + messages[i])
    mqtt_client.publish("devices/" + IOT_HUB_DEVICE_ID + "/messages/events/", payload=messages[i], qos=1)
    sleep(1)