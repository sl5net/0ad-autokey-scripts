if True: 
    # TTS works. i like it :) https://wiki.ubuntuusers.de/eSpeak/#Beispiele
    # sudo apt-get install espeak 
    espeak = 'espeak -vEN "0 A. D. mute 4 profanity"'
    import subprocess
    p2 = subprocess.Popen(espeak , shell=True)

    if True: # this notify is visible before espeak endet talking :) thats nice
        from plyer import notification
        notification.notify(
            title = espeak,
            message = espeak,
            timeout= 2,
            toast=False)

# hotkey in arena26 for mute a player
# tested in ubuntu. its a autoKey-Script (python)
# https://gitlab.com/sl5net/0ad_mute4profanity/-/blob/main/0ad_mute4profanity.py
if "Pidgin.Pidgin" != window.get_active_class():
    exit(1)

c = clipboard.get_selection()

if False: # testing if get_selection works
    from plyer import notification
    notification.notify(
        title = c,
        message = c,
        timeout= 2,
        toast=False)

window.activate("helpers")

if "Pidgin.Pidgin" != window.get_active_class():
    exit(1)

# c = clipboard.get_clipboard()
# c = "aa bb cc" # test string
keyboard.send_keys("!mute 1 day -r profanity<home><ctrl>+<right> ") # paste and move to playerName Position

import re
cFistRE = re.search("[\w_\.]+", c)
cFist = cFistRE.group(0) if cFistRE else exit(1) # looks a bit ugly. that could be better.
# if cFist == "":
#     exit(1)
keyboard.send_keys(cFist) # paste only the first 
# keyboard.send_keys(c.split(" ", 1)[0]) # paste only the first word # works but not good pattern

keyboard.send_keys("<end>" + "<ctrl>+<left>" * 3) # replace day
keyboard.send_keys("<delete>" * 3) # number

choices = [
"minutes",
"day",
"mins",
""
]
retCode, choice = dialog.list_menu(choices, title="min / day", message="", default=None,  geometry="900x700" )
if retCode == 0:
    keyboard.send_keys("" + choice)
    #window.activate("helpers")
    #time.sleep(.4)
    #clipboard.fill_clipboard(choice)

if "Pidgin.Pidgin" != window.get_active_class():
    exit(1)

keyboard.send_keys("<ctrl>+<left>" * 2) # replace number
keyboard.send_keys("<delete>") # delete

if False: # works but is not needet probably
    retCode = keyboard.wait_for_keypress('d',modifiers=['<enter>'],timeOut=5)
    window.activate("arena26")

exit(1)

