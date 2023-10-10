from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            dict[num] = index
        for index, num in enumerate(nums):
            complement = target - num
            if dict.__contains__(complement) and dict[complement] != index:
                return [index, dict[complement]]
        return [-1, -1]


