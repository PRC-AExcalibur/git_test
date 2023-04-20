#coding=utf8

import os

tmp = os.popen('who').readlines()
print(tmp)

tmp = os.popen('git remote -v').readlines()
print(tmp)

tmp = os.popen('git branch -vv').readlines()
print(tmp)

tmp = os.popen('who').readlines()
print(tmp)