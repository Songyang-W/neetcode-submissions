class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=((1+len(nums))*len(nums))/2
        return int(res-sum(nums))
