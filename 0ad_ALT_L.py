import time
t = 'same rating. optional: matrix.to/#/#0ad-unofficial:matrix.org'
t = 'no CC at start!!, Mauryas+Nomad, TinyMap, WorldPopMax 100!! (100 for all players togehter), Start Resources(300each)'
t = """
Nomad=no CC at start | Mauryas | random TinyMap in random biome | 100 WorldPopMax(PopMax for all!! Player), if 2Player your popMax =~55 | low start Resources 300(f/f/s/m) ==> collect resources then build CC. u need 500(f/s/m). HF+GL :) How are you? What you doing?
"""

t = """2v2|3v3
https://github.com/0ad-matters/CartographyMode
https://wildfiregames.com/forum/topic/53880-feldmap-a25/
https://wildfiregames.com/forum/topic/37147-boongui-mod-compatible-with-a25/
( optional: https://gitlab.com/mentula0ad/LocalRatings or https://wildfiregames.com/forum/topic/80151-localratings-mod-evaluate-players-skills-based-on-previous-games/ )
"""

# clipboard.fill_clipboard(t)

time.sleep(.4)
if False: # dont work
    # keyboard.send_keys('<enter>') # dont work
    keyboard.send_keys('<ctrl>+<enter>')
    time.sleep(.5)
    keyboard.press_key('<enter>')
    time.sleep(.1)
    keyboard.press_key('<enter>')
    time.sleep(.1)

    keyboard.release_key('<enter>')

if True: # works :)
    # https://wildfiregames.com/forum/topic/91872-please-help-me-with-streaming-0ad-screen-is-cropped-in-obs-studio/?do=findComment&comment=519978
    # https://stackoverflow.com/a/73678026/2891692

    c = "pyrogenesis.pyrogenesis"
    for i in range(1):  
        time.sleep(.4)
        window.activate(c, False, True)
        window.resize_move(c, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=True)

    time.sleep(.5)
    
    mouse.click_absolute(2977,700,1)
    time.sleep(1.6) # 22-0905_1618-23 1.6 sometimes to short # 22-0905_1414-32 1.5 was a bit short maybe
    keyboard.send_keys('/away<enter>')  # 

    # retCode, choice = dialog.list_menu(["away?"]) # usefull the messure the time. if this happens to early or so.

# keyboard.send_keys('/a<tab><enter>')  # dont work
# clipboard.fill_clipboard('same rating')
clipboard.fill_clipboard(t)




    