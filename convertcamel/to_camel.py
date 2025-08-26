# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

import re

def to_camel_case(text):
    text = re.split("[-_]", text)
    camel = ""
    for index, word in enumerate(text):
        if index == 0:
            camel += word
        else:
            camel += word.title()
    return camel

# Community Solution
# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
