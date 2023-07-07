import  os
def swap(arr,i,j):
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]

# 这个函数的解释
#1.亦或满足结果率以及交换律
#2.0^N = N   N^N=0
#3.设a =  甲、b = 乙
#4.a = a^b 此时 a = 甲^乙 b=乙
#5.b = a^b 此时 a = 甲^乙 b=甲^乙^乙=甲
#6.a = a^b 此时 a = 甲^乙^甲 = 乙 b = 甲
#7.至此 a = 乙 b = 甲
#8.注意:a、b应为不同地址空间的value


# 从小到大
def bubble(arr):
    for i in range(len(arr)-1,0,-1): # 第一层循环控制在哪个空间中
        for j in range(0,i):         # 第二个循环控制两两交换
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
    return arr

# 从大到小
def bubble2(arr):
    for i in range(1,len(arr)-1):
        for j in range(i,len(arr)-1):
            if arr[j] < arr[j+1]:
                swap(arr, j, j + 1)

    return arr



if __name__ == '__main__':
    a = [3,5,1,56,5]
    print(bubble(a))
    print(bubble2(a))

