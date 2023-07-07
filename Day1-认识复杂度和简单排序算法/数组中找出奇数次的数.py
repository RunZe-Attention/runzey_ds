import os


def find_jishu_number():
    arr = [1, 1, 2, 2, 3, 3, 3, 3, 2]
    eof = 0
    for i in range(0,len(arr)):
        eof = eof ^ arr[i]

    print(eof)

#find_jishu_number()


def find_2jishu_number():
    arr = [1, 1,1, 2, 2, 2]
    eof = 0
    for i in range(0,len(arr)):
        eof = eof ^ arr[i]

    right_one = eof & (~eof+1)

    only_one = 0
    for cur in range(0, len(arr)):
        if (cur & right_one) == 1:
            only_one ^= cur

    print(only_one)
    print(eof ^ only_one)

find_2jishu_number()






