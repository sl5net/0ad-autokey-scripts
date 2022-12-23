# 39:22) abc.defg [abc.defg@lobby.wildfiregames.com/0ad-794B465150527918] entered the room.
import subprocess

from plyer import notification

# test ok
def noti(x):
    notification.notify(
        title="",
        message=" " + x,
        timeout=2,
        toast=False)


cPlayerName = ""
cPlayerNameOld = ""
cOld = ""
# acFirst = window.get_active_class()

x = 0


def espeakThis(m):
    espeak = 'espeak -vEN "' + m + '"'  #
    p2 = subprocess.Popen(espeak, shell=True)


window.activate("arena26")  # wait_for_focus(self, title, timeOut=5)
for x in range(600):  # it doesn't loop
    atFirst = window.get_active_title()
    if not window.wait_for_focus("arena26", 1):  # wait_for_focus(self, title, timeOut=5)
        espeakThis("ende last player script")
        exit(1)
    
    ac = window.get_active_class()
    if "Pidgin.Pidgin" != ac:
        noti("ac= " + ac)
        continue

    keyboard.send_keys("<ctrl>+<end>")
    keyboard.send_keys("<shift>+<up>" * 9)  # 2 is good in producaiont mode
    # time.sleep(.1)  # keyboard.send_keys("<ctrl>+c")

    c1 = clipboard.get_selection()    
    if not c1:
        espeakThis("get selection is empty")
        c1 = clipboard.get_selection()    
        if not c1:
            espeakThis("empty 2")
            c1 = clipboard.get_selection()    
            if not c1:
                espeakThis("empty 3")
        
    # keyboard.send_keys("<up>")

    window.activate(atFirst)

    if cOld == c1:
        c2 = clipboard.get_clipboard()
        if cOld == c2:  # exit(1)
            time.sleep(1)
            noti("clipboard not changed")
        else:
            c = c2
    else:
        c = c1
    cOld = c

    window.activate(atFirst)

    if not c:
        espeakThis("is empty")

    # c = """
    # some lines before
    # [oma@com/DA21] entered the room.
    # [opa@com/DA21] entered the room.
    # """


    import re
    cFistRE = re.search("[\s\S]*\[([\w_\.]+).*?\]\s+entered the room\.", c)
    cPlayerName = cFistRE.group(1) if cFistRE else ""  # looks a bit ugly. that could be better.
    if cPlayerName and cPlayerNameOld != cPlayerName:
        cPlayerNameOld = cPlayerName

        # .lower()
        if cPlayerName in [
            'leopard0ad', 
            'leopard', 
            'tom_0ad', 
            'valihrant', 
            'havrun', 
            'weirdJokes', 
            'vinme', 
            'borg-' , 
            'feldfeld' , 
            'marcaurel' , 
            'twainrick' , 
            'dunedam' , 
            'aslan' , 
            'xpert' , 
            'zizo' ,
            'mentula' ,
            '' ]:
            espeakThis(cPlayerName + ' entered the room.')
            noti(cPlayerName + ' entered the room.')

        if False:
            if cPlayerName == "leopard0ad":
                # espeakThis(cPlayerName + ' entered the room.')
                noti(cPlayerName + ' entered the room.')
            if cPlayerName == "valihrAnt":
                # espeakThis(cPlayerName + ' entered the room.')
                noti(cPlayerName + ' entered the room.')
            if cPlayerName == "weirdJokes":
                # espeakThis(cPlayerName + ' entered the room.')
                noti(cPlayerName + ' entered the room.')
            if cPlayerName == "vinme":
                # espeakThis(cPlayerName + ' entered the room.')
                noti(cPlayerName + ' entered the room.')
            if cPlayerName == "borg-":
                # espeakThis(cPlayerName + ' entered the room.')
                noti(cPlayerName + ' entered the room.')
            
        noti(cPlayerName + ' is cPlayer Name')

    # else:
    #     noti('nobody new entered the room. OLD = ' + cPlayerNameOld)
    time.sleep(5)



# -choices = [-
# "TTS endet"

# ]
# retCode, choice = dialog.list_menu(choices, title="t", message="m", default=None,  geometry="900x700" )

# if retCode == 0:
# clipboard.fill_clipboard(choice)

window.activate(atFirst)
# atFirst = window.get_active_title()
# acFirst = window.get_active_class()

espeakThis('Script endet')
time.sleep(1)
espeakThis('Script endet')
time.sleep(1)
espeakThis('Script endet')
time.sleep(1)
espeakThis('Script endet')
time.sleep(1)
