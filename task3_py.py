# -*- coding: utf-8 -*-
"""task3.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hza3w61Y34tKg3k1naJZeLyBRCBq4keS
"""

def print_positive_numbers(numbers):
    for n in numbers:
        if n > 0:
            print(n)
x=input("Enter the list of numbers:")
numbers=list(map(int,x.split()))

print("Positive numbers in the list:")
print_positive_numbers(numbers)