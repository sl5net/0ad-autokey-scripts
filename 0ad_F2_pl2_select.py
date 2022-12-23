import time
# keyboard.send_keys('<ctrl>+<f5>') # set Camera
x = 1700
y = 10
y1 = 10
mouse.click_relative(x,y,1)
# time.sleep(.15)
playerNumer = 2
y += (2+playerNumer)*28

mouse.click_relative(x,y,1)
# time.sleep(.10)
keyboard.send_keys('<ctrl>+c')
 # select relayPoint keyboard.send_keys('ä')
 
exit(1)
 
keyboard.send_keys('<shift>+f') # select railway point of CC
 
# set eventually to Observer if double click
time.sleep(.10)
retCode = keyboard.wait_for_keypress('<f2>',modifiers=[],timeOut=1)
if retCode:
    # set to Observer

    mouse.click_relative(x,y1,1)
    playerNumer = 0
    y = 0 + (2+playerNumer)*28
    # y += y1 + 28
    time.sleep(.10)
    mouse.click_relative(x,y,1)

    time.sleep(.2)
    # mouse.click_relative(xMouse,yMouse,1) # i want only mouseMove but i dont now how to. eventually this: https://stackoverflow.com/questions/63375098/move-mouse-relatively-in-linux
    # time.sleep(.2)
    # mouse.click_relative(xMouse,yMouse,1) # i want only mouseMove but i dont now how to. eventually this: https://stackoverflow.com/questions/63375098/move-mouse-relatively-in-linux

    # myMessage = 'Wait for keypress exit code was: ' + str(retCode)
    # dialog.info_dialog(title='You pressed <ctrl>+d')

time.sleep(.5)
