#!/usr/bin/env python3
import os.path

def time_string(seconds):
    hours = 0
    minutes = 0

    if seconds >= 3600:
        hours = seconds // 3600
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = seconds // 60
        seconds -= minutes * 60

    return_string = str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s "
    return return_string

def generate_img_tag(src, alt='0', width="200px", height="200px"):

    if alt[0] == '0':
        alt = src

    src += ".jpg"
    path = "./profile_pictures/" + src

    if(os.path.isfile(path)):
        print_string = "<img src='/profile_pictures/" + src + "' alt='" + alt
        print_string += "' style='width:" + width + ";height=" + height + ";'>"
    else:
        print_string = "<img src='/profile_pictures/question-mark.jpg' alt='" + alt
        print_string += "' style='width:25%;height:25%;'> "

    print(print_string)
