import math

ls1 = [1,8,90,78,6]

def getMax(array,L,R):
    if L == R:
        return array[L]

    mid = L + ((R-L) >> 1)
    left_max = getMax(array,L,mid)
    right_max = getMax(array,mid+1,R)
    print(left_max)
    print(right_max)
    print("------------------- --")
    return left_max if left_max >= right_max else right_max


if __name__ == '__main__':
    print(getMax(ls1,0,len(ls1)-1))

