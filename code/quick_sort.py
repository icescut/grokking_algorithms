# -*- coding:utf-8 -*-

def quickSort(arr):
    '''
    快速排序
    '''
    # 基线条件
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([5, 3, 6, 2, 10]))
