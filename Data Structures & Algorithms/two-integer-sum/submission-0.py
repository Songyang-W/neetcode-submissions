class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for index,n in enumerate(nums):
            new_target = target-n
            if n in hashset:
                return [hashset[n],index]
            hashset[new_target]=index
        return