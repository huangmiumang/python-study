#!~/.jumbo/bin/python
#coding=utf-8

def find_last_pos(src, tar):
    last_pos = -1
    while True:
        pos = src.find(tar, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos
