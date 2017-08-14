#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import copy
import re
import os
import random
buildings = ['一教','二教','三教','四教','哲学','国关','政管','文史','理教','电教']
clocks = ['1','2','3','4','5','6','7','8','9','10','11','12']
data = {}

def get_all_buildings():
    return buildings

def init():
    dir_names = ['today','third','tomorrow']
    for dir_name in dir_names:
        temp_dir = {}
        for parent, dirnames, filenames in os.walk(dir_name):
            for filename in filenames:
                temp_file = {}
                with open(dir_name + '/' + filename, 'r') as f:
                    while 1:
                        line1 = f.readline().strip()
                        if not line1:
                            break
                        line2 = f.readline().strip()
                        temp_file[line1] = line2
                temp_dir[filename.split('.')[0]] = temp_file
        data[dir_name] = temp_dir

def get_empty_rooms(building, time='today'):
    init()
    building = random.choice(buildings)
    clock = random.choice(clocks)
    rooms = data[time][building][clock]
    res = rooms.split('\t')
    count = random.choice(range(4,10))
    if len(res) > count:
        return random.sample(res, count)
    else:
        return res

if __name__ == '__main__':
    init()
    print get_empty_rooms('tets')