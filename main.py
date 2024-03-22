from DebugTools.DeviceConnectionTester import I2CDeviceTester
from app import Application

tester = I2CDeviceTester(22, 21)
tester.check_display_connection()

wm = WifiManager("GodBless","696969420")
wm.connect()

app.Initialize()
app.Start()
app.Update()