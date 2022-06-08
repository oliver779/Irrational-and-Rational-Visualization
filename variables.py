# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:12:37 2022

@author: Oliver
"""
import json
import os
import math
import subprocess
import random
from mpmath import mp
import numpy as np
import turtle as t
from tkinter import *
from decimal import *
from turtle import *
skk = t.Turtle()


t.screensize(canvwidth=1920, canvheight=1080)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'turtle.json')
with open(my_file) as f:
    m_data = json.load(f)
    
# for i in range(4):
#     skk.forward(50)
#     skk.right(20)

# t.done()

# def split_number(number):
#     number_as_string = str(number)
#     for character in number_as_string:
#         if not character.isdigit():
#             continue
#         yield int(character)
# print(list(split_number(mp.pi)))
# # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
