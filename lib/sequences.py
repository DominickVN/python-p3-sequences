#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    
    if length >= 1:
        fibonacci_list.append(0)
    
    if length >= 2:
        fibonacci_list.append(1)
    
    if length >= 3:
        for i in range(2, length):
            next_number = fibonacci_list[i-1] + fibonacci_list[i-2]
            fibonacci_list.append(next_number)
    
    print(fibonacci_list)


print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)