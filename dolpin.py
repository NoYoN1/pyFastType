from os import dup
import pyautogui
import time
import cv2
import pytesseract
from pytesseract.pytesseract import save
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def writer():
    time.sleep(1)
    pyautogui.write(
        'while here took good don\'t hard idea too later did house day children there learn say set leave number few walk now ask how more when she high along always man next which face often animal them name my how form land watch write really big might life must another leave state children water near hand right begin page find never same almost own got keep seem here where just oil stop said no is off call does might answer important sometimes year river then mountain if say young was that last us family back quick mile in down than tell mother hand know letter time will being run but begin to day often with Indian did night made it\'s girl could then does song don\'t of world me made will think we also eat next left under paper above this point out close page year sometimes picture line she about turn something much animal show plant most learn paper carry up from never quite eye group good get far have live you grow list too different oil first to away write should four so into go him call letter something leave country sound Indian let never over got also well get paper that but being just mean his few began try head tell until sound miss those one thought he land enough ask could children left family different without went new be study time thought play city two no found more follow every let story four feet him want girl two might need say it stop ask open stop as came young set together last saw study into another our follow sound give place out point help until being point right miss while his very may boy can has every sentence kind would end had what hard do talk at each name high like word mean away read look form page men if they story three should other us thing your school add world at large man by three what head set high which eye its boy plant you about land is we can said big close want when of later would feet why example who know part long talk tree life keep father came school took was not those your were but good find house always no from also every down', interval=0.02)


def text_from_image():
    ### text from image ###
    print(pytesseract.image_to_string(
        r'D:\Python\python/Capture.PNG'))


def write_text():
    time.sleep(1)
    ### write text ###
    pyautogui.write(pytesseract.image_to_string(
        r'D:\Python\pythonCapture.PNG'), interval=0.045)


####### auto write from image ########
myScreenshot = pyautogui.screenshot(region=(357, 224, 500, 110))
myScreenshot.save(r'D:\Python\pythonCapture.PNG')
write_text()

####### auto write ########

# writer()


# img = cv2.imread('TextFill.png')
# text = pytesseract.image_to_string(img)
# print(text)

# time.sleep(1)
# pyautogui.write(
#     'hgajmga', interval=0.1)
