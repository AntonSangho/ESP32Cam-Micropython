import camera
import network
import time

ssid_ = "showme_2.4G"
wp2_pass = "sangho1028"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

try:
    sta_if.connect(ssid_, wp2_pass)
    for i in range(0, 10):
        if not sta_if.isconnected():
            time.sleep(1)
    print("Connected to Wi-Fi")
except Exception as e:
    print(e)
finally:
    import upip
    upip.install('urequests')
    sta_if.disconnect()