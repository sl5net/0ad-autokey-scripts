#dialog.info_dialog(title='2_replays_speed1')

c = "pyrogenesis.pyrogenesis"
# window.activate(c, False, True)
# time.sleep(2000)
# window.wait_for_focus("0 A.D.")
# classActive = window.get_active_class()
# if classActive != c:
#     exit(1)
x1 = 2830
y1 = 42
x2 = x1 + 957 # 3787 # 957
x2 = 3787 # 957
y2 = 42

sleepTime = 0.1

if True: # set speed 1 at left game
    mouse.click_absolute(x1,y1+300,1)

    mouse.click_absolute(x1,y1,1)
    time.sleep(sleepTime*2)
    mouse.click_absolute(x1-140,76,1)
    time.sleep(sleepTime*2)
    mouse.click_absolute(x1-140,76+4*25,1) # speed 1
    time.sleep(sleepTime)
    mouse.click_absolute(x1,y1,1)
    time.sleep(sleepTime)


if True: # set speed 1 to right game
    mouse.click_absolute(x2,y2+300,1)
    
    mouse.click_absolute(x2,y2,1)
    time.sleep(sleepTime*2)
    mouse.click_absolute(x2-140,76,1)
    time.sleep(sleepTime*2)
    mouse.click_absolute(x2-140,76+4*25,1) # speed 1
    time.sleep(sleepTime)
    mouse.click_absolute(x2,y2,1)

# dialog.info_dialog(title='start toggle')
# far from menues
for i in range(1400):
    for i in range(3):
        mouse.click_absolute(x1 - 100,(y1 + 400 + i),1)
        time.sleep(1)
        mouse.click_absolute(x2 - 100,(y2 + 400 + i),1)
        time.sleep(1)
    time.sleep(3)

dialog.info_dialog(title='end script')
exit(1)
















sleepTime = 111
for i in range(400):
    mouse.click_absolute(x1,y1+100,1)
    mouse.click_absolute(x1+2,y1+100,1)
    mouse.click_absolute(x1+4,y1+100,1)
    mouse.click_absolute(x1+8,y1+100,1)

    mouse.click_absolute(x1,y1+100,1)
    mouse.click_absolute(x2+2,y1+100,1)
    mouse.click_absolute(x2+4,y1+100,1)
    mouse.click_absolute(x2+8,y1+100,1)

    time.sleep(2)
exit(1)







exit(1)


sleepTime = 111
for i in range(100):
    mouse.click_absolute(x1,y1,1)
    mouse.click_absolute(x1+2,y1,1)
    mouse.click_absolute(x1+4,y1,1)
    mouse.click_absolute(x1+8,y1,1)

    mouse.click_absolute(x1,y1,1)
    mouse.click_absolute(x2+2,y2,1)
    mouse.click_absolute(x2+4,y2,1)
    mouse.click_absolute(x2+8,y2,1)

    time.sleep(2)
exit(1)

for i in range(9):
    mouse.click_absolute(x1,(y1 + i),1)
    time.sleep(110)
    mouse.click_absolute(x2,(y2 + i),1)
    time.sleep(5000)
