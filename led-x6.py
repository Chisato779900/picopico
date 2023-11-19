from machine import Pin
import time

# 内蔵LEDのピン定義
led_int = Pin("WL_GPIO0", Pin.OUT)
# チェックしたい「GPIO番号」の定義
led_num_0 = Pin(0, Pin.OUT)
led_num_1 = Pin(1, Pin.OUT)
led_num_2 = Pin(2, Pin.OUT)
led_num_3 = Pin(3, Pin.OUT)
led_num_4 = Pin(4, Pin.OUT)
led_num_5 = Pin(5, Pin.OUT)
# 点灯時間highのsleep時間変数化
on_time = 0.3

# 内蔵LEDの作動兼消灯
led_int.high()
time.sleep(3)
led_int.low()
# time.sleep(1)

# 定義された「GPIO番号」のLEDの無限ループ
while True:
    led_num_0.high()
    time.sleep(on_time)
    led_num_0.low()
    # time.sleep(0.5)
    led_num_1.high()
    time.sleep(on_time)
    led_num_1.low()
    # time.sleep(0.5)
    led_num_2.high()
    time.sleep(on_time)
    led_num_2.low()
    # time.sleep(0.5)
    led_num_3.high()
    time.sleep(on_time)
    led_num_3.low()
    # time.sleep(0.5)
    led_num_4.high()
    time.sleep(on_time)
    led_num_4.low()
    # time.sleep(0.5)
    led_num_5.high()
    time.sleep(on_time)
    led_num_5.low()
    # time.sleep(0.5)


# LED 中華　緑LED 3mm
# 抵抗　120Ω　電流 6.65mA
# 抵抗　100Ω　電流 7.82mA
# 抵抗　 82Ω　電流 8.69mA
# 抵抗　 75Ω　電流 8.76mA これ　採用


    
