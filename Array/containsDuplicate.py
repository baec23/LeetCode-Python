from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if seen.__contains__(num):
                return True
            seen.add(num)
        return False
