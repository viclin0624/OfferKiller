# 二维数组的查找： https://leetcode.cn/problems/search-a-2d-matrix-ii/description/
def search_in_array(arr, target):
    if arr is None:
        return False
    m = len(arr)
    if m == 0:
        return False
    n = len(arr[0])
    if n == 0:
        return False
    
    i = 0
    j = n-1
    while i < m and j > -1:
        if arr[i][j]==target:
            return True
        elif arr[i][j]>target:
            j -= 1
        elif arr[i][j]<target:
            i += 1
    return False