# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:28:48 2017

@author: twschen
"""

class Solution:
    def BinarySearch(self,A,value,low,high):
        if low > high:
            return None
        mid = int((high + low)/2)
        if A[mid] > value:
            return self.BinarySearch(A, value, low, mid-1)
        elif A[mid] < value:
            return self.BinarySearch(A, value, mid+1, high)
        else:
            return A[mid]
    def twoSum(self, nums, target):
        arrays = sorted(nums)
        for index, num in enumerate(arrays):
            ans = self.BinarySearch(arrays,target-num,index+1,len(arrays)-1)
            if ans != None:
                if num == ans:
                    return [i for i, j in enumerate(nums) if j == num][0:2]
                else:
                    return [nums.index(num),nums.index(ans)]
                
                
x = Solution()
print(x.twoSum([2,5,5,11],10))

""" Solution
class Solution(object):
    def twoSum(self, numbers, target):
        d = {}
        for i,num in enumerate(numbers):
            if target - num in d:
                return [d[target-num]+1,i+1]
            d[num]=i
        return []

nums = {2, 7, 11, 15}
target = 26
sol = Solution()
print(sol.twoSum(nums,target))
"""