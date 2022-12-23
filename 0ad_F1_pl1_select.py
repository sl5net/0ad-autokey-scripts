import time
# keyboard.send_keys('<ctrl>+<f5>') # set Camera
x = 1700
y = 10
y1 = 10
mouse.click_relative(x,y,1)
playerNumer = 1
y += (2+playerNumer)*28
mouse.click_relative(x,y,1)
keyboard.send_keys('<ctrl>+c') # select CC 
# time.sleep(.1)
# keyboard.send_keys('<shift>') # select railway point

if False: # select cav  dont work
    for i in range(4):
        # keyboard.press_key('<alt>') # and folow it
        time.sleep(.4)
        # keyboard.send_keys('<shift>+f') # select railway point of CC
        keyboard.send_keys('<alt>+c') # select cav 
        # keyboard.send_key('c') # select cav 
        time.sleep(.4)
        # keyboard.release_key('<alt>') # and folow it

exit(1)

for i in range(1):
    # keyboard.press_key('<shift>') # and folow it
    # time.sleep(.4)
    # keyboard.send_keys('<alt>+c') # select cav 
    keyboard.send_keys('<shift>+f') # select railway point of CC
    # keyboard.release_key('<shift>') # and folow it


if False: # this not works
    time.sleep(.2)
    # keyboard.send_keys('<alt>+c') # select cav 
    time.sleep(.2)
    keyboard.release_key('<alt>') # and folow it

    time.sleep(.2)


    #time.sleep(.10)

    keyboard.press_key('<shift>') # and folow it
    # time.sleep(.1)
    keyboard.send_keys('f') # and folow it
    time.sleep(.1)
    keyboard.release_key('<shift>') # and folow it

# keyboard.send_keys('ä') # select relayPoint

# set eventually to Observer if double click
# retCode = keyboard.wait_for_keypress('d',modifiers=['<ctrl>'],timeOut=3) # works
# retCode = keyboard.wait_for_keypress('<f1>',modifiers=['<ctrl>'],timeOut=3) # works
time.sleep(.10)
# retCode = keyboard.wait_for_keypress('<f1>') # works
retCode = keyboard.wait_for_keypress('<f1>',modifiers=[],timeOut=1)
# retCode = keyboard.wait_for_keypress('f9',modifiers=[''],timeOut=3)
if retCode:
    # set to Observer
    mouse.click_relative(x,y1,1)
    playerNumer = 0
    y = 0 + (2+playerNumer)*28
    # y += y1 + 28
    time.sleep(.10)
    mouse.click_relative(x,y,1)
#    if yMouse > 100:
    time.sleep(.2)
    # mouse.click_relative(xMouse,500,1) # i want only mouseMove but i dont now how to. eventually this: https://stackoverflow.com/questions/63375098/move-mouse-relatively-in-linux
        # time.sleep(.2)
        # mouse.click_relative(xMouse,yMouse,1) # i want only mouseMove but i dont now how to. eventually this: https://stackoverflow.com/questions/63375098/move-mouse-relatively-in-linux

    # myMessage = 'Wait for keypress exit code was: ' + str(retCode)
    # dialog.info_dialog(title='You pressed <ctrl>+d')

    time.sleep(.5)

# keyboard.send_keys('<f5>') # Camera

# mouse.click_absolute(x,500,1) # i want only mouseMove but i dont now how to. eventually this: https://stackoverflow.com/questions/63375098/move-mouse-relatively-in-linux
