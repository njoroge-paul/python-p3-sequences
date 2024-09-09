#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fib_sequence=[]
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a+b
    print(fib_sequence)
    return fib_sequence

print_fibonacci(5)