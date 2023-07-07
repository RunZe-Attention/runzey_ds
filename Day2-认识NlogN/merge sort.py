import os



def merge_sort(arr,L,R):
    if L == R:
        return
    mid = L+(R-L) >> 1
    merge_sort(arr, L, mid)
    merge_sort(arr, mid+1, R)
    merge(arr,L,mid,R)

def merge(arr, L, mid, R):
    help = []
    p1 = L
    p2 = mid+1
    i = 0
    while (p1 <= mid) and (p2 <= R):
        if arr[p1] <= arr[p2]:
            print(i)
            print(p1)
            help[i] = arr[p1]
            p1+=1
        else:
            help[i] = arr[p2]
            p2+=1
        i += 1
    while (p1 <=mid):
        help[i] = arr[p1]
        i+=1
        p1+=1
    while (p2 <= R):
        help[i] = arr[p2]
        i += 1
        p2 += 1
    for j in range(0,len(help)):
        arr[L+j] = help[j]





if __name__ == '__main__':
    array = [1,3,2,6,5,9]
    merge_sort(array,0,len(array)-1)
    for i in range(0,len(array)):
        print(array[i])












