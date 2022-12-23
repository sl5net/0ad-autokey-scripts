import time
if False:
    import subprocess
    # c = home + "/git/0a26/binaries/system/pyrogenesis"
    c = "firefox https://meet.jit.si/0ad1v1"
    p2 = subprocess.Popen(c, shell=True) # works
# exit(1)
time.sleep(.30)
keyboard.send_keys("<shift>+<home>")
keyboard.send_keys("<delete>")
# "pls test if map could loaded and then play some seconds. helps me alot. ty"
rulesDuringTG ="""| Rules: / 1. Be kind and helpful to newbies and other players. / 2. Toxic comments can lead to immediate expulsion / 3. Pro players must set an example of good behavior. / 4. Don't quit or leave early. Play as a team and share resources."""
# choices = ["1v1 unrated", "1v1 rated +-50", "2v2", "3v3", "better tab+space not enter", "1. https://meet.jit.si/0adTalkBefore | 2. 1v1/2v2 unrated | get PASS from 1."]
MLB = "" # [] install balanced-map https://wildfiregames.com/forum/topic/27654-balanced-maps-mod/ "
MLB = """ FAQ: my rating is real | played 500games | like: learn/teach | what your hobbies/interests? """
MLB = """ FAQ: my rating is real | like: learn/teach | what your hobbies/interests? """
winHistory = "| best win 1400 player. also lose against 1100 players"
mainland = "| lilke mainland "
iOld = "| i am old person"
hotKeyTeach = " | i can teach beginners 99% hotkeys in 1min"
choices = [
"ping me in https://matrix.to/#/#0ad1v1:tchncs.de "
,"LetswaveaBook vs seeh"
,"in mainland | ask PASS in https://matrix.to/#/#0ad1v1:tchncs.de |" + MLB + hotKeyTeach + winHistory + mainland + iOld
, "Plan&Go: 0 A.D"  + MLB + hotKeyTeach + mainland
, "__ normal mainland / no balanced-map"
, "1v1 unrated"
, "1v1 rated +-50"
, "1v1 / 2v2" + rulesDuringTG
, "1v1 / 2v2 / 3v3" + rulesDuringTG
, "2v2" + rulesDuringTG
, "3v3" + rulesDuringTG
, ""
, "__with balanced-map"
, "Plan&Go: 0 A.D"  + MLB
, "1v1 unrated" + MLB
, "1v1 rated +-50" + MLB
, "2v2" + MLB + rulesDuringTG
, "3v3" + MLB + rulesDuringTG
, ""
, "Hi^_^ 1. https://meet.jit.si/0adTalkBefore | 2. 1v1/2v2AI | ask PASS in 1."
, "Hi^_^ 1. https://meet.jit.si/0adTalkBefore || ask PASS in 1."
, "Hi^_^ 1. https://meet.jit.si/0adTalkBefore | hobbies/interests? / favorite 0AD? beginner? | ask PASS in 1."
]

# , "better tab+space not enter"

# clipboard.fill_clipboard("jitsi")

# retCode, choice = dialog.list_menu(choices)
retCode, choice = dialog.list_menu(choices, title="Choose game", message="good luck ;)", default=None,  geometry="900x700" )
if retCode == 0:
    # keyboard.send_keys("" + choice)
    clipboard.fill_clipboard(choice)

# clipboard.fill_clipboard(t)
