import pandas as pd
import random
import time
import sys
import os

limit_number = 100000
sys.setrecursionlimit(limit_number)

swapCounter = 0
compareCounter = 0

def quick_sort_1(array):
    return quick_sort_a(array, 0, len(array)-1)

def quick_sort_a(array, start, end):
    global compareCounter
    global swapCounter
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            compareCounter += 1
            left += 1
        while(right > start and array[right] >= array[pivot]):
            compareCounter += 1
            right -= 1
        if(left > right):
            compareCounter += 1
            swapCounter += 1
            array[right], array[pivot] = array[pivot], array[right]
        else:
            swapCounter += 1
            array[left], array[right] = array[right], array[left]
    quick_sort_a(array, start, right - 1)
    quick_sort_a(array, right + 1, end)

def quick_sort_2(array):
    return quick_sort_b(array, 0, len(array)-1)

def quick_sort_b(array, start, end):
    global compareCounter
    global swapCounter
    if start >= end:
        return
    pivot = random.randint(start,end-1)
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            compareCounter += 1
            left += 1
        while(right > start and array[right] >= array[pivot]):
            compareCounter += 1
            right -= 1
        if(left > right):
            compareCounter += 1
            swapCounter += 1
            array[right], array[pivot] = array[pivot], array[right]
        else:
            swapCounter += 1
            array[left], array[right] = array[right], array[left]
    quick_sort_b(array, start, right - 1)
    quick_sort_b(array, right + 1, end)

def quick_sort_3(array):
    return quick_sort_c(array, 0, len(array)-1)

def quick_sort_c(array, start, end):
    global compareCounter
    global swapCounter
    if start >= end:
        return
    pivot = 0
    a,b,c=array[start],array[start+(end-start)//2],array[end]
    if a>b:
        if b>c: pivot = start+(end-start)//2
    else:
        if a>c: pivot = start
    if a>c:
        if c>b: pivot = end
    else:
        if a>b: pivot = start
    compareCounter += 2
    
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            compareCounter += 1
            left += 1
        while(right > start and array[right] >= array[pivot]):
            compareCounter += 1
            right -= 1
        if(left > right):
            compareCounter += 1
            swapCounter += 1
            array[right], array[pivot] = array[pivot], array[right]
        else:
            swapCounter += 1
            array[left], array[right] = array[right], array[left]
    quick_sort_c(array, start, right - 1)
    quick_sort_c(array, right + 1, end)

def heap_sort(array):
    global compareCounter
    global swapCounter
    
    n = len(array)
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2
            if (array[r] < array[c]):
                compareCounter += 1
                swapCounter += 1
                array[r], array[c] = array[c], array[r]
            c = r
    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]
        r = 0
        c = 1
        while c<j:
            c = 2*r +1
            if (c<j-1) and (array[c] < array[c+1]):
                compareCounter += 1
                c += 1
            if (c<j) and (array[r] < array[c]):
                compareCounter += 1
                swapCounter += 1
                array[r], array[c] = array[c], array[r]
            r=c
    return array

sortFunc = [quick_sort_1, quick_sort_2, quick_sort_3, heap_sort]

N_list=[100,200,500,1000,2000,3000,4000,5000]
for n_value in N_list:
    print(n_value)
    ListNum=n_value
    TestNum=1000
    result = [[[],[],[]] for _ in range(len(sortFunc))]
    progressChecker=time.time()
    processStart=time.time()

    for i in range(TestNum):
        if time.time()-progressChecker>=5: print(100.0*i/TestNum,"%"); progressChecker = time.time()
        l=[x for x in range(ListNum)]
        random.shuffle(l)
        for j in range(len(sortFunc)):
            temp=l.copy()
            swapCounter = 0
            compareCounter = 0
            
            start=time.perf_counter()
            sortFunc[j](temp)
            end=time.perf_counter()
            
            result[j][0].append(end-start)
            result[j][1].append(swapCounter)
            result[j][2].append(compareCounter)
    processEnd=time.time()

    print("100 %")
    print("Total Time",processEnd-processStart)
    print()

    for i in range(len(result)):
        if not os.path.isdir(os.getcwd()+"/N"+str(ListNum)):
            os.mkdir("N"+str(ListNum))
        df = pd.DataFrame({'Time':result[i][0],'Swap':result[i][1],'Compare':result[i][2]})
        df.to_csv("N"+str(ListNum)+"/SortType"+str(i)+".csv", index = False)

    sumList = [[],[],[]]
    for i in range(len(sortFunc)):
        for j in range(3):
            sumList[j].append(sum(result[i][j]) / len(result[i][j]))

    df = pd.DataFrame({'AvrTime':sumList[0],'AvrSwap':sumList[1],'AvrCompare':sumList[2]})
    df.to_csv("N"+str(ListNum)+"/Result.csv", index = True)