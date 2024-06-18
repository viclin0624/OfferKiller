# 数组中重复的数字
def duplicate_in_array(arr):
    if len(arr) == 0:
        return None
    n = len(arr)
    for i in range(n):
        while arr[i] != i:
            if arr[i] == arr[arr[i]]:
                return arr[i]
            else:
                # 左右顺序不能交换！
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
                print(arr)
                #print(arr[i], arr[arr[i]])
    return -1
print(duplicate_in_array([3 , 1 , 2 , 0 , 2 , 5 ,3 ]))

# https://leetcode.cn/problems/find-all-duplicates-in-an-array/description/
# 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

# 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
class Solution:
    def findDuplicates(self, nums):
        res = set()
        if len(nums) == 0:
            return res
        n = len(nums)
        for i in range(n):
            while nums[i]!=i+1:
                if nums[i]==nums[nums[i]-1]:
                    res.add(nums[i])
                    break
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return res
        