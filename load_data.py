import numpy as np
import pandas as pd

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.
def fiboroni(num):
    fib = [1,1]
    if num < 1:
        print("Nope.")
    elif num == 1:
        print([1])
    elif num == 2:
        print([1,1])
    else:
        for i in range(2, num):
            fib.append(fib[i-1] + fib[i - 2])
        print(fib)
