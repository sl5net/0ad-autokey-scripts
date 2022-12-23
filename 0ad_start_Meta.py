import subprocess
p2 = subprocess.Popen("screenkey", shell=True)

# 22-0508_1352-34 funktioniert, obwhol es einen script fehler anzeigt. egal :)
# keyboard.send_keys("<meta>+<space>")
keyboard.send_keys("<super>+  ")
# keyboard.press_key("<Meta>") # dont work
# keyboard.release_key("<Meta>") # dont work

  
# <space><space>