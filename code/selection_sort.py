# -*- coding:utf-8 -*-

def findSmallest(arr):
    '''
    找出一个列表中最小的元素
    '''
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    '''
    选择排序
    '''
    newArr = []
    for i in range(len(arr)):
        # 从剩下的元素中找出最小的元素
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
