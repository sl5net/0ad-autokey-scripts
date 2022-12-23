import subprocess  # p2 = subprocess.Popen("obs --startrecording", shell=True)
from pathlib import Path

# home = str(Path.home())

c = "pyrogenesis.pyrogenesis"
# window.activate(c, False, True)
# time.sleep(2000)
# window.wait_for_focus("0 A.D.")
# classActive = window.get_active_class()
# if classActive != c:
#     exit(1)

if True: # start replay

    x1 = 2740
    y1 = 1025
    x2 = 3700
    y2 = 1025
    sleepTime = 111
    for i in range(5):
        mouse.click_absolute(x1,y1,1)
        mouse.click_absolute(x1+2,y1,1)
        mouse.click_absolute(x1+4,y1,1)
        mouse.click_absolute(x1+8,y1,1)

        mouse.click_absolute(x1,y1,1)
        mouse.click_absolute(x2+2,y2,1)
        mouse.click_absolute(x2+4,y2,1)
        mouse.click_absolute(x2+8,y2,1)

    #time.sleep(2000)

# start OBS
p2 = subprocess.Popen("obs --startrecording", shell=True)

if False: # dont work is blocked by obs start toggle games windows
    for i in range(9):
        mouse.click_absolute(x1,(y1 + i),1)
        time.sleep(110)
        mouse.click_absolute(x2,(y2 + i),1)
        time.sleep(5000)
