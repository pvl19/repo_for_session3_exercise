import numpy as np
import pandas as pd

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.
<<<<<<< HEAD

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
=======
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
>>>>>>> e860871c99c5e414ca0f70e6ea39c528d9cb5e12
