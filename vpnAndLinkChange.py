import pyautogui as agui
import time
from random import randint

site_links = ['viewboxu.blogspot.com/2020/03/blog-post_73.html', 'viewboxu.blogspot.com/2020/03/136-adsbygoogle-window.html', 'viewboxu.blogspot.com/2019/11/opc911-adsbygoogle-window.html', 'viewboxu.blogspot.com/2018/05/full-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/11/ge-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/11/flatliners-2017.html',
              'viewboxu.blogspot.com/2017/09/wo.html', 'viewboxu.blogspot.com/2017/11/tho-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/11/ame-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/08/hi.html', 'viewboxu.blogspot.com/2017/08/de_26.html', 'viewboxu.blogspot.com/2017/08/pe.html', 'viewboxu.blogspot.com/2017/08/de_27.html', 'viewboxu.blogspot.com/2020/03/blog-post_1.html', 'viewboxu.blogspot.com/2020/03/blog-post_34.html', 'viewboxu.blogspot.com/2020/03/blog-post_36.html', 'viewboxu.blogspot.com/2020/03/blog-post_6.html']

link_range = len(site_links)

agui.FAILSAFE = True


def min_windows_start_chrome():
    time.sleep(1)
    agui.hotkey('Win', 'd')
    time.sleep(1)
    ###########кромыг сонгох############
    agui.click(x=271, y=753)
    time.sleep(1)
    ###########хоёр кром нээлттэй байх ба баруун гар талыг нь сонгох############
    agui.click(x=309, y=668)
    time.sleep(1)


def refresh():
    ###refresh###
    time.sleep(1)
    ###########нээгдсэн кромыг дахин ачааллах товч дээр дарах############
    agui.click(x=84, y=53)
    time.sleep(1)
    ###############


def country_germany():
    ####Germany####
    time.sleep(1)
    agui.click(x=918, y=227)
    time.sleep(1)
    ###############


def country_romania():
    ####Romania####
    time.sleep(1)
    agui.click(x=910, y=255)
    time.sleep(1)
    ###############


def country_singapore():
    ####Singapore####
    time.sleep(1)
    agui.click(x=920, y=291)
    time.sleep(1)
    ###############


def country_unitedstate():
    ####UnitedState####
    time.sleep(1)
    agui.click(x=929, y=316)
    time.sleep(1)
    ###############

###########бэлтгэгдсэн функцийг рандом оор сонгох############


def country_change_function():
    countrys_function_range_value = randint(0, 3)
    a = countrys_function_range_value
    if a == 0:
        country_germany()
    elif a == 1:
        country_romania()
    elif a == 2:
        country_singapore()
    elif a == 3:
        country_unitedstate()


def vpn_change_country():
    time.sleep(1)
    ###########vpn ын айкон дээр хулганаар дарах############
    agui.click(x=1220, y=54)
    time.sleep(6)
    ###########улсын жигсаалт гаргах товч дээр дарах############
    agui.click(x=1017, y=495)
    time.sleep(3)
    ####change country####
    country_change_function()
    ###############
    time.sleep(1)
    ###########впн ыг хаах############
    agui.click(x=1220, y=54)
    time.sleep(1)


def new_tab():
    time.sleep(1)
    agui.hotkey('ctrl', 't')
    time.sleep(1)
    ###########рандомоор бэлтгэгдсэн линк дотроос гаргах############
    agui.write(
        site_links[randint(0, link_range-1)], interval=0)
    time.sleep(1)
    agui.press('enter')
    time.sleep(1)


def link_write():
    time.sleep(1)
    ###########хөтөчийн линк бар хэсгийг сонгох############
    agui.click(x=643, y=56)
    time.sleep(2)
    agui.hotkey('ctrl', 'a')
    agui.write(site_links[randint(0, link_range-1)], interval=0)
    time.sleep(1)
    agui.press('enter')
    time.sleep(1)
    new_tab()
    time.sleep(1)
    new_tab()
    time.sleep(1)
    new_tab()
    time.sleep(1)


def next_start():
    # agui.alert(title="Alert box next",
    #            text="from now don't touch mouse and keyboard a few minutes(1-2min)", button="YES")
    time.sleep(2)
    agui.hotkey('Win', 'd')
    time.sleep(1)
    ###########кромыг сонгох############
    agui.click(x=271, y=753)
    time.sleep(1)
    ###########хоёр кром нээлттэй байх ба баруун гар талыг нь сонгох############
    agui.click(x=309, y=668)
    time.sleep(1)
    ################
    time.sleep(1)

    agui.click(x=1153, y=12)
    agui.hotkey('ctrl', 'w')
    time.sleep(1)
    agui.hotkey('ctrl', 'w')
    time.sleep(1)
    agui.hotkey('ctrl', 'w')
    time.sleep(1)
    agui.click(x=643, y=56)
    time.sleep(2)


def one_time():
    time.sleep(2)
    min_windows_start_chrome()
    # refresh()
    vpn_change_country()
    link_write()
    # agui.alert(title="Alert box", text="now you can touch computer")
    time.sleep(3600)
    next_start()
    time.sleep(1)

################################## next ###################################


# agui.alert(title="Alert box",
#            text="from now don't touch mouse and keyboard a few minutes(1-2min)", button="YES")
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
one_time()
