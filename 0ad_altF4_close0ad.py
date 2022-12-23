# 22-0508_1352-34 funktioniert, obwhol es einen script fehler anzeigt. egal :)
# 22-1125_1802-03 intersting it helps. it does nothing but then its possibele to use alt+f4 again
import subprocess
# import time

exit(1)

choices = [
  "NOT close"
, "close"
]
# retCode, choice = dialog.list_menu(choices)
retCode, choice = dialog.list_menu(choices, title="Choose game", message="good luck ;)", default=None,  geometry="800x700" )
if retCode == 0:
    if choice == "close":
        p3 = subprocess.Popen(['killall' ,'main']) # works :) 22-0911_1153-11  
#autokey-qt.autokey-qt#autokey-qt.autokey-qt