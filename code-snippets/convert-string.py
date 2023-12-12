"""
Problem statement

You are given a string 'STR'. You have to convert the first alphabet
of each word in a string to UPPER CASE.
For example:
If the given string 'STR' = "I am a student of the third year" so you
have to transform this string to "I Am A Student Of The Third Year"

Note:
'STR' will contains only space and alphabets both uppercase and lowercase.
The words will be separated by space.

See https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/651072/offering/10442100?leftPanelTabValue=PROBLEM
"""

from os import *
from sys import *
from collections import *
from math import *


def convertString(str):
    """Converts a string by capitalizing the first letter of each word of `str` argument."""
    string_list = str.split()
    string_list_uppercase = []
    new_str = ""
    for element in string_list:
        string_list_uppercase.append(element.capitalize())

    new_str = " ".join(string_list_uppercase)
    return new_str
