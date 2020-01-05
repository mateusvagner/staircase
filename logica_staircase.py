# -*- coding: utf-8 -*-
"""
StairCase
"""

def staircase(n):
    stairs = list(range(n+1))
    stairs = stairs[1:]
    for i in stairs:
        stair = str(' '*(n-i) + i*'#')
        print(stair)


n = int(input('Informe o número de níveis: '))
staircase(n)
