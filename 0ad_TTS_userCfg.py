# this speaks what you send from your mode.
# howToUseIt: 

from pathlib import Path
home = str(Path.home())
#userCfgPath = home + "/.config/0ad/config/user.cfg" # if github installation or so
userCfgPath = home + "/snap/0ad/current/.config/0ad/config/user.cfg" # if snap installation

# install:
# sudo apt-get install espeak 
# autoKey

# in the mod:
# Engine.ConfigDB_WriteValueToFile("user", "AudioTTS.speak", "hello speak this 15", "config/user.cfg");

# in the AutoKey-Script or Python - Script use the following:
# https://gitlab.com/-/ide/project/sl5net/0ad_tts_for_mods/tree/main/-/0ad_TTS_userCfg/

# it reads every 0.5 seconds the modified time of your user.cfg 
# if changed it searchs line AudioTTS.speak and speak it (its maybe the fist and it needs not search long time)

#  ~/.config/0ad/config/user.cfg

ignoreTheFirstMessage = True # in the game 0ad its nice to ignore old messages. eventualls usless and to old
ignoreTheFirstMessage = False # in the game 0ad its nice to ignore old messages. eventualls usless and to old

# BTW in the javaScript function like this could be helpfull:
# function ttsPL(msg){
	# Engine.ConfigDB_WriteValueToFile("user", "AudioTTS.speak", msg, "config/user.cfg");
	# const date = new Date();
	# const isoDateTime = new Date(date.getTime() - (date.getTimezoneOffset() * 60000)).toISOString();
	# Engine.ConfigDB_WriteValueToFile("user", "AudioTTS.timestamp","" + isoDateTime, "config/user.cfg");
# }

msg = ""
msgOld = ""


import re, subprocess, os.path
# from plyer import notification
# def noti(x):
#     notification.notify(
#         title="",
#         message=" " + x,
#         timeout=2,
#         toast=False)
def espeakThis(m):
    espeak = 'espeak -vEN "' + m + '"'  
    p2 = subprocess.Popen(espeak, shell=True)


# noti("last modified: \n%s" % os.stat(userCfgPath).st_mtime)
# noti(str(time.time()))


# espeakThis("0ad speak script")
import datetime
# nowIsoTimeObj = datetime.datetime.now().isoformat() # no errors
datetimeObj = datetime.datetime.now()
# timestampStr = datetimeObj.strftime("%d-%m-%Y $h:$s.%f") 
#AudioTTS.timestamp = "2022-11-18T10:40:21.121Z"

# output = time.strftime("%F--%R__%b-%a")# 2022-11-18--12:31--Nov-Fr# 2022-11-18--12:32__Nov-Fr
# output = time.strftime("%F--%R")# # 2022-11-18--12:33
startIsoTimeStr = time.strftime("%FT%H:%M:%S")
# espeakThis(startIsoTimeStr)# works
# keyboard.send_keys("<end># " + startIsoTimeStr ) # 18-11-2022 $H:$S.063124# 2022-11-18T12:43:56
# delta = startIsoTimeStr - startIsoTimeStr
# espeakThis(delta)

# time.sleep(1)
# exit(1)




espeakThis("espeak script started")
# espeakThis('start')
# lineNr = 0
t2 = 0
while True:
    t1 = os.stat(userCfgPath).st_mtime
    if t1 != t2:
        lastChangeOlderInSeconds = round( time.time() - os.stat(userCfgPath).st_mtime )
        if lastChangeOlderInSeconds < 2: # ignore old updates older then 2 seconds. seems user.cfg will be updated everytime you start 0ad 

            # espeakThis(str(lastChangeOlderInSeconds) + " seconds") # works
            # noti(str(lastChangeOlderInSeconds))
            # exit(1)
            if(ignoreTheFirstMessage):
                ignoreTheFirstMessage = False
            else:
                with open(userCfgPath) as f:
                    while True:
                        line = f.readline()
                        # lineNr = lineNr + 1 # just for debugging
                        # espeakThis(lineNr)
                        # espeakThis('boom')

                        if not line:
                            break
                        if line[:14] == "AudioTTS.speak":
                            vRE = re.search('"(.+)"', line)
                            msg = vRE.group(1) if vRE else ""  # looks a bit ugly. that could be better.
                        if line[:18] == "AudioTTS.timestamp":
                            # espeakThis('hi')
                            vRE = re.search('"(.+)"', line)
                            dateISOString = vRE.group(1) if vRE else ""  # looks a bit ugly. that could be better.
                            dateISOString = dateISOString[:-5]
                            # keyboard.send_keys("<end># " + startIsoTimeStr )# 2022-11-18T13:03:49
                            dateISOobj = datetime.datetime.strptime( dateISOString, "%Y-%m-%dT%H:%M:%S")
                            
                            nowIsoTimeStr = time.strftime("%FT%H:%M:%S")
                            nowISOobj = datetime.datetime.strptime( nowIsoTimeStr, "%Y-%m-%dT%H:%M:%S")
                            
                            delta = nowISOobj - dateISOobj
                            
                            if delta.total_seconds() < 8: # this is probably from the curract game and not from a very old that maybe not exist anymore
                                if msgOld != msg:
                                    if delta.total_seconds() < 4:
                                        espeakThis(msg)
                                        msgOld = msg; 
                                else:
                                    msgOld = msg; 
                            # else:
                            #    espeakThis(f"difference {delta.total_seconds()} seconds") # this works
                            
                            #clipboard.fill_clipboard(f"difference {delta.total_seconds()} seconds")  # this works

                            time.sleep(2) # could be eventually disturbung to much if the sound is to often
                            break
                            
        t2 = t1
    
    # pyrogenesis.pyrogenesis
    # if not window.wait_for_exist("pyrogenesis.pyrogenesis", 9, matchClass=True):
    if not window.wait_for_exist("0 A.D.", 2):
        espeakThis("0ad not exist anymore. good bye. end of script.")
        exit(1)
    
    # window.resize_move(at, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=False)
    time.sleep(.5)
    