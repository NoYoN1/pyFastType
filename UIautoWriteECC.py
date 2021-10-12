import pyautogui as pgui
import time


# screenWidth, screenHeight = pgui.size()


# def mouse_center():
#     pgui.moveTo(screenWidth / 2, screenHeight / 2)


# def clicker():
#     pgui.click(x=1249, y=52, duration=1)
# pgui.click()
# pgui.mouseInfo()

# mouse_center()
# clicker()
# for i in range(10):
#     pgui.moveTo(x=100, y=200, duration=0.25)
#     pgui.moveTo(x=200, y=200, duration=0.25)
#     pgui.moveTo(x=100, y=400, duration=0.25)

def ecc():
    # e
    pgui.moveTo(x=150, y=250)
    pgui.drag(xOffset=-40, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=60, duration=0.25)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.moveTo(x=110, y=280)
    pgui.drag(xOffset=30, yOffset=0, duration=0.25)

    # c1
    pgui.moveTo(x=210, y=250)
    pgui.drag(xOffset=-40, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=60, duration=0.25)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)

    # c2
    pgui.moveTo(x=270, y=250)
    pgui.drag(xOffset=-40, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=60, duration=0.25)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
#   # o
#     pgui.moveTo(x=220, y=340)
#     pgui.drag(xOffset=0, yOffset=50, duration=0.25)
#     pgui.moveTo(x=220, y=340)
#     pgui.drag(xOffset=40, yOffset=0, duration=0.25)
#     pgui.drag(xOffset=0, yOffset=50, duration=0.25)
#     pgui.moveTo(x=220, y=390)
#     pgui.drag(xOffset=40, yOffset=0, duration=0.25)

# pgui._mouseMoveDrag(moveOrDrag, x=100, y=200,
#                     xOffset=200, yOffset=200, duration=0.25)
# pgui._mouseMoveDrag(x=200, y=200, duration=0.25)
# pgui._mouseMoveDrag(x=100, y=400, duration=0.25)
# ecc()


def computer():
    # c
    pgui.moveTo(x=170, y=340)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=50, duration=0.25)
    pgui.moveTo(x=170, y=390)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)

    # n
    pgui.moveTo(x=225, y=350)
    pgui.drag(xOffset=10, yOffset=5, duration=0.25)
    pgui.moveTo(x=240, y=390)
    pgui.drag(xOffset=30, yOffset=-50, duration=0.25)
    # p
    pgui.moveTo(x=285, y=370)
    pgui.drag(xOffset=30, yOffset=-20, duration=0.25)
    pgui.moveTo(x=285, y=340)
    pgui.drag(xOffset=0, yOffset=45, duration=0.25)
    pgui.drag(xOffset=5, yOffset=5, duration=0.25)
    pgui.drag(xOffset=25, yOffset=0, duration=0.25)
    pgui.drag(xOffset=5, yOffset=-5, duration=0.25)
    pgui.moveTo(x=320, y=340)
    pgui.drag(xOffset=0, yOffset=-10, duration=0.25)
    pgui.drag(xOffset=10, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=10, duration=0.25)
    pgui.drag(xOffset=-10, yOffset=-0, duration=0.25)
    # u
    pgui.moveTo(x=330, y=365)
    pgui.drag(xOffset=20, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=25, duration=0.25)
    pgui.moveTo(x=330, y=390)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    # -
    pgui.moveTo(x=375, y=365)
    pgui.drag(xOffset=35, yOffset=0, duration=0.25)
    # t
    pgui.moveTo(x=440, y=340)
    pgui.drag(xOffset=-15, yOffset=15, duration=0.25)
    pgui.moveTo(x=440, y=340)
    pgui.drag(xOffset=30, yOffset=0, duration=0.25)
    pgui.drag(xOffset=-15, yOffset=25, duration=0.25)
    pgui.drag(xOffset=-25, yOffset=25, duration=0.25)
    pgui.moveTo(x=435, y=360)
    pgui.drag(xOffset=15, yOffset=5, duration=0.25)


# pgui.moveTo(x=170, y=390)
# pgui.drag(xOffset=600, yOffset=0, duration=0.25)
def open_paint():
    # pgui.moveTo(x=73, y=750)
    # pgui.click(x=73, y=750)
    pgui.hotkey('Win', 'd')
    pgui.hotkey('Win', 's')
    time.sleep(1)
    pgui.write('paint', interval=0.25)
    time.sleep(2)
    pgui.press('enter')
    time.sleep(2)
    pgui.hotkey('Win', 'up')
    time.sleep(2)


def paint_setting():
    time.sleep(1)
    # select brush
    pgui.click(x=331, y=100)
    time.sleep(1)
    pgui.click(x=328, y=222)
    time.sleep(1)
    pgui.click(x=632, y=110)
    time.sleep(1)
    # select size 8px
    # pgui.click(x=635, y=126)
    # select size 16px
    pgui.click(x=630, y=181)
    time.sleep(1)
    # select color by red
    pgui.click(x=830, y=61)


def save():
    pgui.hotkey('ctrl', 's')
    time.sleep(1)
    pgui.write('ecc_school', interval=0.25)
    time.sleep(3)
    pgui.hotkey('enter')
    time.sleep(1)
    # pgui.hotkey('Win', 'd')


# senmon kanji
def senmon_gakkou():
    pgui.moveTo(x=285, y=430)
    pgui.drag(xOffset=70, yOffset=0, duration=0.25)
    pgui.moveTo(x=285, y=445)
    pgui.drag(xOffset=0, yOffset=30, duration=0.25)
    pgui.moveTo(x=285, y=445)
    pgui.drag(xOffset=70, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=30, duration=0.25)
    pgui.moveTo(x=285, y=460)
    pgui.drag(xOffset=70, yOffset=0, duration=0.25)
    pgui.moveTo(x=285, y=475)
    pgui.drag(xOffset=70, yOffset=0, duration=0.25)
    pgui.moveTo(x=320, y=415)
    pgui.drag(xOffset=0, yOffset=60, duration=0.25)
    pgui.moveTo(x=275, y=495)
    pgui.drag(xOffset=90, yOffset=0, duration=0.25)
    pgui.moveTo(x=340, y=475)
    pgui.drag(xOffset=0, yOffset=60, duration=0.25)
    pgui.drag(xOffset=-10, yOffset=-10, duration=0.25)
    pgui.moveTo(x=290, y=500)
    pgui.drag(xOffset=5, yOffset=5, duration=0.25)
    pgui.drag(xOffset=5, yOffset=3, duration=0.25)
    ##########
    pgui.moveTo(x=380, y=415)
    pgui.drag(xOffset=0, yOffset=120, duration=0.25)
    pgui.moveTo(x=380, y=415)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=30, duration=0.25)
    pgui.moveTo(x=380, y=430)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.moveTo(x=380, y=445)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.moveTo(x=430, y=415)
    pgui.drag(xOffset=0, yOffset=30, duration=0.25)
    pgui.moveTo(x=430, y=415)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=120, duration=0.25)
    pgui.drag(xOffset=-10, yOffset=-10, duration=0.25)
    pgui.moveTo(x=430, y=430)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.moveTo(x=430, y=445)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    ##############
    pgui.moveTo(x=510, y=415)
    pgui.drag(xOffset=8, yOffset=10, duration=0.25)
    pgui.moveTo(x=525, y=415)
    pgui.drag(xOffset=8, yOffset=10, duration=0.25)
    pgui.moveTo(x=560, y=415)
    pgui.drag(xOffset=-6, yOffset=10, duration=0.25)
    pgui.moveTo(x=490, y=430)
    pgui.drag(xOffset=8, yOffset=10, duration=0.25)
    pgui.moveTo(x=490, y=430)
    pgui.drag(xOffset=90, yOffset=0, duration=0.25)
    pgui.drag(xOffset=0, yOffset=10, duration=0.25)
    pgui.moveTo(x=510, y=450)
    pgui.drag(xOffset=60, yOffset=0, duration=0.25)
    pgui.drag(xOffset=-30, yOffset=30, duration=0.25)
    pgui.drag(xOffset=0, yOffset=55, duration=0.25)
    pgui.drag(xOffset=-10, yOffset=-5, duration=0.25)
    pgui.moveTo(x=490, y=495)
    pgui.drag(xOffset=90, yOffset=0, duration=0.25)
    #################
    pgui.moveTo(x=590, y=435)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.moveTo(x=610, y=415)
    pgui.drag(xOffset=0, yOffset=120, duration=0.25)
    pgui.moveTo(x=610, y=435)
    pgui.drag(xOffset=-20, yOffset=50, duration=0.25)
    pgui.moveTo(x=610, y=435)
    pgui.drag(xOffset=20, yOffset=50, duration=0.25)

    pgui.moveTo(x=665, y=415)
    pgui.drag(xOffset=0, yOffset=20, duration=0.25)
    pgui.moveTo(x=645, y=435)
    pgui.drag(xOffset=40, yOffset=0, duration=0.25)
    pgui.moveTo(x=660, y=450)
    pgui.drag(xOffset=-15, yOffset=20, duration=0.25)
    pgui.moveTo(x=680, y=455)
    pgui.drag(xOffset=10, yOffset=20, duration=0.25)
    pgui.moveTo(x=675, y=475)
    pgui.drag(xOffset=-10, yOffset=30, duration=0.25)
    pgui.drag(xOffset=-20, yOffset=30, duration=0.25)
    pgui.moveTo(x=655, y=475)
    pgui.drag(xOffset=20, yOffset=30, duration=0.25)
    pgui.drag(xOffset=30, yOffset=30, duration=0.25)
    time.sleep(3)


open_paint()
paint_setting()
ecc()
computer()
senmon_gakkou()
save()

# get mouse position
# time.sleep(2)
# print(pgui.position())
