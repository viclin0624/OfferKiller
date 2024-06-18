# 替换空格 字符串题目 本质是数组题目
# 参考合并两个有序数组： https://leetcode.cn/problems/merge-sorted-array/description/

def merge_sorted_arr(arr1, m, arr2, n):
    if arr1 is None or arr1 == []:
        return arr2
    if arr2 is None or arr2 == []:
        return arr1

    arr1_index = m-1
    arr2_index = n-1
    merge_index = m+n-1
    while arr1_index>=0 and arr2_index>=0:
        if arr1[arr1_index]>=arr2[arr2_index]:
            arr1[merge_index] = arr1[arr1_index]
            arr1_index -= 1
        else:
            arr1[merge_index] = arr2[arr2_index]
            arr2_index -= 1
        merge_index -= 1
    if arr2_index >=0:
        arr1[:arr2_index] = arr2[:arr2_index]
