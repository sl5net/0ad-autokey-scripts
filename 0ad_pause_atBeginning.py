exit(1)

from plyer import notification
    
lastFtime = store.get_global_value("pauseBeginningFtime")    # pauseBeginningFtime
if lastFtime:
    qpwoeruqpweoiruqwpeoruqpwoeiurqpwoeru = 0
else:
    lastFtime = 0

from datetime import datetime;
from math import floor
from pathlib import Path
home = str(Path.home())
from datetime import datetime
keyboard.send_keys('<ctrl>+c')
n = str(datetime.now())
n1 = n[-1:]
if int(n1) < 3: # 3 is default

    ftime = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    timeDiffInSeconds = int(ftime) - lastFtime
    timeDiffInMin = 0
    if timeDiffInSeconds > 0:
        timeDiffInMin = floor(timeDiffInSeconds / 60)
    if timeDiffInMin == 0 or timeDiffInMin >= 55:
        store.set_global_value("pauseBeginningFtime",ftime)
        # clipboard.fill_clipboard("hi :) sorry need a minute. BTW are you stil there? HF")
        clipboard.fill_clipboard("sorry sec")
        # keyboard.send_keys(" " + n + " " )
        keyboard.send_keys('<pause>')

    if False:
        # deactivate the hotkey by replaceing <ctrl> with <meta>
        # it works but its not updated into the GUI
        # replace it with ctrl again to enable it.
        # keep this script insied the autokey and you only need to save.
        with open(home + '/.config/autokey/data/Sample Scripts/.0ad_pause_atBeginning.json', 'r') as file:
            data = file.read().replace('"<ctrl>"', '"<ctrlOff>"')
        # clipboard.fill_clipboard(data) # was used as backup
        with open(home + '/.config/autokey/data/Sample Scripts/.0ad_pause_atBeginning.json', 'w') as file:
            file.write(data)




notification.notify(
    title = "Alt + Left = military",
    message = "Alt+Z+Left = non-military",
    timeout= 3,
    toast=False)

