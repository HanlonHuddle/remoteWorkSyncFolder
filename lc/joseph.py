#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:20:42 2017

@author: Yuchen
"""

def findnext(people, i):
    while True:
        i+=1
        if i >= len(people):
            i = 0
        if people[i] == 1:
            break
    return i

def joseph(n, e):       
    people = [1] * n
    R = n
    cur = 0
    while R>1:
        for i in range(0, e-1):
            cur = findnext(people, cur)
        people[cur] = 0;
        print(cur+1)
        R -= 1
        cur = findnext(people, cur)
    
joseph(21, 3)