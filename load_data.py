import numpy as np
import pandas as pd

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.

def fib(input):
    fm2 = 0
    fm1 = 1

    i = 0
    while i < input:
        if i == 0:
            print(0)
        elif i == 1:
            print(1)
        elif i > 1:
            f = fm1 + fm2
            fm2 = fm1
            fm1 = f
            print(f)
        i += 1
        
    return