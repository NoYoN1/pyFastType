from random import randint
from random import seed
import pyautogui as agui
import time


def country_germany():
    ####Germany####
    time.sleep(1)
    agui.moveTo(x=918, y=227)
    agui.click(x=918, y=227)
    time.sleep(1)
    ###############


def country_romania():
    ####Romania####
    time.sleep(1)
    agui.moveTo(x=910, y=255)
    agui.click(x=910, y=255)
    time.sleep(1)
    ###############


def country_singapore():
    ####Singapore####
    time.sleep(1)
    agui.moveTo(x=920, y=291)
    agui.click(x=920, y=291)
    time.sleep(1)
    ###############


def country_unitedstate():
    ####UnitedState####
    time.sleep(1)
    agui.moveTo(x=929, y=316)
    agui.click(x=929, y=316)
    time.sleep(1)


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
    ###############


def change_country():
    time.sleep(1)
    agui.moveTo(x=1190, y=54)
    agui.click(x=1190, y=54)
    time.sleep(2)
    agui.moveTo(x=1017, y=495)
    agui.click(x=1017, y=495)
    time.sleep(2)
    ####Germany####
    # Driver program
    country_change_function()

    ###############
    time.sleep(2)
    agui.moveTo(x=1190, y=54)
    agui.click(x=1190, y=54)
    time.sleep(2)


site_links = ['viewboxu.blogspot.com/2020/03/blog-post_73.html', 'viewboxu.blogspot.com/2020/03/136-adsbygoogle-window.html', 'viewboxu.blogspot.com/2019/11/opc911-adsbygoogle-window.html', 'viewboxu.blogspot.com/2018/05/full-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/11/ge-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/11/flatliners-2017.html',
              'viewboxu.blogspot.com/2017/09/wo.html', 'viewboxu.blogspot.com/2017/11/tho-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/11/ame-adsbygoogle-window.html', 'viewboxu.blogspot.com/2017/08/hi.html', 'viewboxu.blogspot.com/2017/08/de_26.html', 'viewboxu.blogspot.com/2017/08/pe.html', 'viewboxu.blogspot.com/2017/08/de_27.html']

link_range = len(site_links)


def new_tab():
    print(site_links[randint(0, link_range-1)])


def link_write():
    print(site_links[randint(0, link_range-1)])

    new_tab()

    new_tab()

    new_tab()


link_write()
