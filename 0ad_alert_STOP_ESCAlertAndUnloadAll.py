# recomandet hotkey ESC

winClass = window.get_active_class()
if winClass != 'pyrogenesis.pyrogenesis':
    exit(1)

winT = window.get_active_title()
if winT != '0 A.D.':
    exit(1)


import time
time.sleep(.25)
keyboard.send_keys('<ctrl>+c')
time.sleep(.25)

# endof alert
x = 784
y = 1064
mouse.click_relative(x + 2,y,1)
#mouse.click_relative(x + 4,1050,1)
mouse.click_relative(x + 6,y + 2,1)
mouse.click_relative(x + 8,y + 2,1)

# unload all
# time.sleep(.21)
# keyboard.send_keys('u') 

if True:
    from plyer import notification
    notification.notify(
        title = "unloaded hopefully",
        message = "unloaded hopefully",
        timeout= 2,
        toast=False)

