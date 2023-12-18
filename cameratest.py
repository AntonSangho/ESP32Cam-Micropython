import camera
import network
import time 

try:
    print('Taking a Photo')
    camera.init(0, format=camera.JPEG)
    buffer = camera.capture()
    print(len(buffer))
    file_path = "captured_image.jpg"
    file = open(file_path, "w")
    file.write(buffer)
    file.close()
except Exception as e:
    print('An issue occured')
finally:
    print('Deinitializing Camera')
    camera.deinit()
