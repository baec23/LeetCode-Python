from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        toReturn = [1] * n
        currProduct = 1
        for i in range(1, len(nums)):
            currProduct *= nums[i-1]
            toReturn[i] = currProduct
        currProduct = 1
        for i in reversed(range(0, len(nums)-1)):
            currProduct *= nums[i+1]
            toReturn[i] *= currProduct 
        return toReturn

