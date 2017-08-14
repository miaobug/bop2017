#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import copy
import re

def init():
    file = open('./server/lesson_2.txt', 'r')
    data = []
    while 1:
        line = file.readline().strip()
        if not line:
            break
        paras = line.split('\t')
        lesson = {}
        lesson['id'] = paras[0]
        lesson['name'] = paras[1]
        lesson['type'] = paras[2]
        lesson['score'] = paras[3]
        lesson['teacher'] = paras[4]
        places = []
        if not lesson['teacher'].strip():
            continue
        try:
            lesson['info1'] = paras[9]
            places.append(lesson['info1'])
        except Exception, e:
            lesson['info1'] = ''
        try:
            lesson['info2'] = paras[10]
            places.append(lesson['info2'])
        except Exception, e:
            lesson['info2'] = ''
        lesson['place'] = "\t".join(places)
        data.append(lesson)
    return data

def get_lessons(lesson_name):
    data = init()
    res = []
    for k in data:
        if lesson_name in k['name']:
            res.append(k)
    return res

def get_one_lesson(lesson_list, teacher):
    for lesson in lesson_list:
        if teacher in lesson['teacher']:
            return lesson
    return -1

def get_lesson_list(time='周二'):
    data = init()
    res = []
    for lesson in data:
        if time in lesson['place']:
            res.append(lesson)
    for k in res:
        for t in k:
            print t,k[t]
    return res

if __name__ == '__main__':
    file = open('./server/lesson_2.txt', 'r')
    data = []
    while 1:
        line = file.readline().strip()
        if not line:
            break
        paras = line.split('\t')
        lesson = {}
        lesson['id'] = paras[0]
        lesson['name'] = paras[1]
        lesson['type'] = paras[2]
        lesson['score'] = paras[3]
        lesson['teacher'] = paras[4]
        if not lesson['teacher'].strip():
            continue
        try:
            lesson['info1'] = paras[9]
        except Exception, e:
            lesson['info1'] = ''
        try:
            lesson['info2'] = paras[10]
        except Exception, e:
            lesson['info2'] = ''
        for k in lesson:
            print k, lesson[k]
        print ""


