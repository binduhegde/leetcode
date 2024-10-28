#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:33:09 2023

@author: bindu
"""
# def solution2(s, t):
#     tlist = [i for i in t]
    
#     for i in range(len(s)):
#         for j in range(len(t)):
#             if s[i] == t[j]:
#                 print(i, j)
#                 tlist.pop(j)
#     return len(tlist) == 0    

# print(solution2('rat', 'tar'))   



def solution2(s, t): 
    if len(s) == len(t):
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    t = t[:j] + ' '+ t[j+1:]
                    break
        t = t.replace(' ','' )
    return len(t) == 0
print(solution2('aacc', 'ccac'))   













