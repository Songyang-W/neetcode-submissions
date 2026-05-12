class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        cur_max=0
        for i in range(len(nums)):
            cur_max=nums[i]+max(cur_max,0)
            res=max(res,cur_max)
        return res