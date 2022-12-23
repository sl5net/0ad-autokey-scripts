import time

# Active window information:
#Title: 'GetMomo Financial GmbH – Kalender - 4 Tage, ab Donnerstag, 31. März 2022 - Google Chrome'
#Class: 'google-chrome.Google-chrome'

import subprocess
p2 = subprocess.Popen("screenkey", shell=True)

c = "pyrogenesis.pyrogenesis"
if True:
    window.activate(c, False, True)
    window.resize_move(c, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=True)

if False:
    time.sleep(.5)
    at = window.get_active_title()
    c = "0 A.D. <2>‎" # sometimes this is opene a second 0ad 
    # window.activate(c, False, False)
    window.resize_move(at, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=False)

# window.activate('.js')

if True:
    from plyer import notification
    notification.notify(
        title = ">" + "< do Alert-Check! ",
        message = "before you play! \nSometimes needs linux reboot",
        timeout= 2,
        toast=False)

