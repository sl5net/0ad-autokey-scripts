import time
time.sleep(.15)
# mouse.click_relative_self(50,50,2)
sleepSec = 0.08
buttonNr = 3
x = 20
y = 20
keyboard.press_key('<shift>')
for i in range(4):
    if True:
        time.sleep(sleepSec)
        mouse.click_relative_self(-x,-y, buttonNr)
        time.sleep(sleepSec)
        mouse.click_relative_self(x,-y, buttonNr)
        time.sleep(sleepSec)
        mouse.click_relative_self(x,y, buttonNr)
        time.sleep(sleepSec)
        mouse.click_relative_self(-x,y, buttonNr)
        time.sleep(sleepSec)
        mouse.click_relative_self(-x,-y, buttonNr)
time.sleep(sleepSec)
keyboard.release_key('<shift>')
# mouse.click_relative(20,20,1)
# mouse.click_relative(20,20,2)
# mouse.click_relative(20,20,1)
# mouse.click_relative(20,20,2)


# for i in range(3):
#    time.sleep(1)
#    mouse.click_relative_self(0,y, buttonNr)
