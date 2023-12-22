# ESP32-Cam 을 활용한 프로젝트  
ESP32cam을 raspberry pi Pico와 같이 사용할수 있을까?

# 설치하는 법 
1. esp32cam 연결하기  
    - Linux의 경우   
    ```bash
    ls -l /dev/ttyUSB0
    ```

    - Window의 경우   
    
2. 초기화하기  
    1. esp32를 연결하고 **BOOT Button**을 누른 상태에서 아래 명령어를 실행한다.     
    <img src="https://lastminuteengineers.com/wp-content/uploads/iot/ESP32-CAM-MB-Programmer-Hardware-Overview.jpg"></img>
    ```bash
    esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
    ```
    2. 아래와 같은 결과나 나오면서 정상적으로 초기화된다. 
    ![message](/img/message.png)
3. firmware 업로드하기  
    1. firmware 폴더로 이동한다. 
    2. esp32를 연결하고 **BOOT Button**을 누른 상태에서 아래 명령어로 flash 한다. 어느정도 시간이 지나고 나면 버튼을 놓아도 된다.  
    ```bash
    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 build-ESP32_CAM/firmware.bin
    ```
    3. 아래와 같은 결과가 나오면서 정상적으로 업로드된다.
    ![img](/img/message_2.png)
4. 예제 실행해보기  
    1. Thonny를 실행한다.
    2. 포트를 **Micropython(ESP32)** 로 연결한다. 
    3. [cameratest.py](/cameratest.py)를 실행한다. 



    

esptool



# 참고 
- [How to use the ESP32-CAM and Micropython](https://youtu.be/TDgM8eMTpIw?si=HP6gWAHNA701UzDd) 

