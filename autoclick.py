import pyautogui
import time
pyautogui.FAILSAFE = True

# button7location = pyautogui.locateCenterOnScreen('btn4.png')
# pyautogui.click(button7location)

# pyautogui.typewrite(open('beemovie.txt'))
# pyautogui.press("enter")

# pyautogui.locateCenterOnScreen('44')

# file_name = 'test.png'

# prtsc = pyautogui.screenshot()
# prtsc.save(file_name)
# button7location = pyautogui.locateOnScreen('button.png')


def start_browser_newtab():
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/start.PNG'))
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/browser/chrome.PNG'))
    time.sleep(1)
    # pyautogui.click(pyautogui.locateCenterOnScreen(
    #     'C:/Users/2200228/Desktop/python/pic/newtab.PNG'))
    # pyautogui.moveTo(x=600, y=300, duration=1)
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/tab.PNG'))
    # pyautogui.moveTo(x=600, y=300, duration=1)
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/newtab_openbrowser.PNG'))

############################
# start browser
# start_browser_newtab()
#######################


def calc():
    # pyautogui.click(pyautogui.locateCenterOnScreen(
    #     'D:/Python/pic/start.PNG'))
    # time.sleep(3)
    # pyautogui.click(pyautogui.locateCenterOnScreen(
    #     'D:/Python/pic/calc.PNG'))
    # ###################numbers########################
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/1.PNG'))
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/2.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/2.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/3.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/4.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/5.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/6.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/7.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/8.PNG'))
    pyautogui.click(pyautogui.locateCenterOnScreen(
        'D:/Python/pic/numbers/9.PNG'))

    time.sleep(3)


calc()
