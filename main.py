from DebugTools.DeviceConnectionTester import I2CDeviceTester
from app import Application

tester = I2CDeviceTester(22, 21)
tester.check_display_connection()

app = Application()

app.Initialize()
app.Start()
app.Update()