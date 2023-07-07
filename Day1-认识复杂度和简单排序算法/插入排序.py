# 时间复杂度指的是按照最差情况估计的时间表现
# 一般情况下只考虑最差情况 至于平均情况 最好情况意义不大


def insert_sort():
    arr = [12, 11, 13, 5, 6]
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(arr)

insert_sort()
