"""Профилировка затрат памяти"""
# https://pypi.org/project/guppy3/

from guppy import hpy
import copy

h = hpy()

x = list(range(100000))
y = copy.deepcopy(x)

print(h.heap())
