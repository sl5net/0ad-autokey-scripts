import subprocess

# autokey-run -s 0ad_TTS_lastPlayers

# 22-1104_1946-56 N.: ensure that you're in alpha26 with pidgin before connecting 0ad
if False: # start pidgin
    p2 = subprocess.Popen("pidgin", shell=True)

if False: # start screenkey
    p2 = subprocess.Popen("screenkey", shell=True) # something usefull for teaching

if False: # start 0ad from git
    from pathlib import Path
    home = str(Path.home())
    c = home + "/git/0a26/binaries/system/pyrogenesis"

    # dont wait till the proccess is edndet . 
    from subprocess import Popen

    p = Popen([c, '']) # something long running
    # p = Popen([c, '--user=[user]']) # something long running and bit more explicit
    # p = Popen([c, '-writableRoot']) # not good idea to run 0ad as root. 

    # ... do other stuff while subprocess is running
    # p.terminate()

    time.sleep(.3)  # .2 works is maybe sometimes to fast
    c = "pyrogenesis.pyrogenesis"
    window.activate(c, False, True)
    window.resize_move(c, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=True)

if True: # start 0ad
    # dont wait till the proccess is edndet . 
    from subprocess import Popen
    c = "0ad"
    p2 = subprocess.Popen(c, shell=True)
    time.sleep(.3)
    
if True:
    c = "pyrogenesis.pyrogenesis"
    window.activate(c, False, True)
    window.resize_move(c, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=True)

# time.sleep(2)
p2 = subprocess.Popen("autokey-run -s 0ad_TTS_userCfg", shell=True)


if False:
    from plyer import notification
    notification.notify(
        title = "started ? :)",
        message = "hi from 0ad_start",
        timeout= 2,
        toast=False)



#### #jetbrains-pycharm-ce.jetbrains-pycharm-ce

if False:
    # join lobby
    mouse.click_absolute(2200,825,1)
    # keyboard.send_keys('/<alt>+l')  # 
    time.sleep(2.5)
    # mouse.click_absolute(2977,700,1)
    mouse.click_absolute(2977,700,1)
    time.sleep(1.6) # 22-0905_1618-23 1.6 sometimes to short # 22-0905_1414-32 1.5 was a bit short maybe
    keyboard.send_keys('/away<enter>')  # 




exit(1)

# single game start
x = 2080 - 1920
y = 230
mouse.click_relative(x + 2,y,1)
#mouse.click_relative(x + 4,1050,1)
mouse.click_relative(x + 6,y + 2,1)
mouse.click_relative(x + 8,y + 2,1)

time.sleep(.5)
x = 2320 - 1920
mouse.click_relative(x + 2,y,1)
#mouse.click_relative(x + 4,1050,1)
mouse.click_relative(x + 6,y + 2,1)
mouse.click_relative(x + 8,y + 2,1)

time.sleep(.5)
x = 3740 - 1920
y = 1065 # 1080 is screen height
mouse.click_relative(x + 2,y,1)
#mouse.click_relative(x + 4,1050,1)
mouse.click_relative(x + 6,y + 2,1)
mouse.click_relative(x + 8,y + 2,1)

