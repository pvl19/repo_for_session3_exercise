import numpy as np

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.


def fibSequence(n):
    sequence = []
    if n<=0:
        return print("Please specify a whole number!")
    else:
        sequence.append(0)
        if n==2:
            sequence.append(1)
        else:
            sequence.append(1)
            for i in range(n-2):
                sequence.append(sequence[-1]+sequence[-2])
    return sequence

