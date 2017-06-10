#!/usr/bin/env python3
import os.path

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
