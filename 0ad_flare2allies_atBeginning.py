# Alt+c ### i solved autoFlare at beginng by using a autoKey - script (works in linux):
# is use my recommended hotkey Alt+c (select cavalry. i do it always at beginning in the first minute as last step)
# at same time it flares the first time if i use Alt+c . only the first time

from plyer import notification
notification.notify(
    title = "Alt + Left = military",
    message = "Alt+Z+Left = non-military",
    timeout= 2,
    toast=False)
    
from math import floor
time.sleep(.1)
lastFtime = store.get_global_value("ftime")
# time.sleep(.2)
from datetime import datetime;
time.sleep(.1)
ftime = datetime.utcnow().strftime("%Y%m%d%H%M%S")
store.set_global_value("ftime",ftime)
timeDiffInSeconds = int(ftime) - int(lastFtime)
timeDiffInMin = 0
if timeDiffInSeconds > 0:
    timeDiffInMin = floor(timeDiffInSeconds / 60)
if timeDiffInMin >= 55:
    keyboard.press_key('<backspace>')
    time.sleep(.12)
    mouse.click_relative(500,500,1)
    time.sleep(.2)
    keyboard.release_key('<backspace>')
# keyboard.send_ke
# deactivate the hotkey by replacing
# keep this script inside the autokey GUI open and you only need to save for reset the correct hotkey
# with open(home + '/.config/autokey/data/Sample Scripts/.0ad_flare2allies_atBeginning.json', 'r') as file:
#     data = file.read().replace('"<altUFF>"', '"<altOFF>"')
# with open(home + '/.config/autokey/data/Sample Scripts/.0ad_flare2allies_atBeginning.json', 'w') as file:
#     file.write(data)
