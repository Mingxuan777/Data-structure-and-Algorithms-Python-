import time
import random
from random import sample

def look_for(L, left, right):
    if (left >= right):
        return L[left]
    m = random.randint(left, right)
    n = L[left]
    L[left] = L[m]
    L[m] = n

    i = left
    j = right
    key = L[left]
    while i < j:
        while i < j and key <= L[j]:
            j -= 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i += 1
        L[j] = L[i]
    L[i] = key

    if (len(L) % 2 ==0 and i == int(len(L) / 2) - 1):
        return key
    elif (len(L) % 2 != 0 and i == int(len(L) / 2)):
        return key
    if (i > int(len(L) /2) - 1):
        return look_for(L, left, i - 1)
    else:
        return look_for(L, i + 1, right)

def main():

    result = sample([x for x in range(-1000, 1000)], 11)
    print(result)
    start = time.time()
    mid = look_for(result, 0, len(result) - 1)
    end = time.time()
    print("中间值为： " + str(mid))

if __name__ == '__main__':
    main()