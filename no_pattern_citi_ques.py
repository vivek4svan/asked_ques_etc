#!/usr/bin/env python

arr = [4,35,80,123,12345,44,8,5,24,23,444,66]
column = 5

max_size = len(str(max(arr)))

for elem_index in range(len(arr)):
    if (elem_index)%column == 0:
        for i in range(column):
            print("+"),
            print("-"*max_size),
        print("+")
    print("|"),
    print(str(arr[elem_index]).rjust(max_size," ")),
    if (elem_index+1)%column == 0:
        print("|")

if len(arr)%column != 0:
    print("|")

if len(arr)%column != 0:
    for i in range(len(arr)%column):
        print("+"),
        print("-"*max_size),
    print("+")
else:
    for i in range(column):
        print("+"),
        print("-"*max_size),
    print("+")
