import network
import socket
import time

class WifiManager:
    def __init__(self, oled_display=None):
        self.ap = network.WLAN(network.AP_IF)
        self.station = network.WLAN(network.STA_IF)
        self.oled = oled_display
        self.StartAp()
        
    
    def StartAp(self):
        self.ap.active(True)
        self.ap.config(essid="ESP32-AP", password="setup69420")
        print("AP started. Connect to WIFI: ESP32-AP with password: setup69420")
        
    
    def RunServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 80))
        s.listen(1)
        
        while True:
            conn, addr = s.accept()
            request = conn.recv(1024)
            request_str = request.decode('utf-8')
            ssid, password = self.parse_request(request_str)
            if ssid and password:
                self.try_connect_wifi(ssid, password)
                break  # Break after attempt to connect
            else:
                self.serve_form(conn)
            conn.close()
        self.ap.active(False)
        
    def parse_request(self, request):
        ssid = None
        password = None

        # Find the start and end of the query string within the request
        query_start = request.find('?') + 1
        query_end = request.find(' ', query_start)
        if query_start > 0 and query_end > query_start:
            query = request[query_start:query_end]
            queries = query.split('&')

            for q in queries:
                parts = q.split('=')
                if len(parts) == 2:
                    key, value = parts
                    if key == 'ssid':
                        ssid = value.replace('%20', ' ')  # Decodes space character
                    elif key == 'password':
                        password = value.replace('%20', ' ')
        return ssid, password
    
    def try_connect_wifi(self, ssid, password):
        self.station.active(True)
        self.station.connect(ssid, password)
        print("Trying to connect to WiFi network: {}".format(ssid))

        # Set a timeout for the connection attempt
        timeout = 10  # 10 seconds timeout
        start_time = time.ticks_ms()

        # Wait for connection with timeout
        while not self.station.isconnected():
            if time.ticks_diff(time.ticks_ms(), start_time) > (timeout * 1000):
                rint("Failed to connect within the timeout period.")
                return False

            print("Attempting to connect...")
            time.sleep(1)

        print("Successfully connected to: {}".format(ssid))
        return True

    def serve_form(self, conn):
        response = """<!DOCTYPE html><html><head><title>ESP32 WiFi Setup</title></head><body>
                      <h2>WiFi Setup</h2><form method="get">SSID:<input type="text" name="ssid">
                      Password:<input type="text" name="password"><input type="submit" value="Submit"></form></body></html>"""
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
    
