import mouse as ms
import time
import random
# print(ms.get_position())

len_ = random.randint(-70, -1)

def YouTube():
    ms.move(232, 887)
    time.sleep(2)
    ms.double_click()
    time.sleep(2)

    ms.move(1023, 515)
    time.sleep(3)
    ms.double_click()
    time.sleep(2)

    ms.move(937, 133)
    time.sleep(3)
    ms.click()
    time.sleep(2)

    ms.click('right')
    time.sleep(2)
    ms.move(950, 250)
    time.sleep(2)
    ms.double_click()
    time.sleep(2)

    ms.move(1055, 138)
    time.sleep(2)
    ms.double_click()
    time.sleep(2)
    ms.move(900, 500)
    time.sleep(2)
    ms.wheel(len_)
    time.sleep(2)
    ms.click()
