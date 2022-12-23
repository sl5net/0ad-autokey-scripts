winClass = window.get_active_class()
if winClass != 'pyrogenesis.pyrogenesis':
    exit(1)

winT = window.get_active_title()
if winT != '0 A.D.':
    exit(1)


# re-commanded hotkey ^
import time
time.sleep(.25)
keyboard.send_keys('<ctrl>+c')
time.sleep(.25)

# raise alert
x = 827
y = 1063
mouse.click_relative(x + 2 ,y , 1)
#mouse.click_relative(x + 4,1050,1)
mouse.click_relative(x + 6,y + 2,1)
mouse.click_relative(x + 8,y + 2,1)

# endof alert
# mouse.click_relative(780,1050,1)
# mouse.click_relative(782,1050,1)
# mouse.click_relative(788,1050,1)

if True:
    from plyer import notification
    notification.notify(
        title = "alerted",
        message = "alerted",
        timeout= 2,
        toast=False)
