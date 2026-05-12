class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        p=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j]>nums[i]:
                    p[j]=max(p[i]+1,p[j])
                
        return max(p)+1




                    
