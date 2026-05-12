class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        p=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                k=i
                while k <=j:
                    if nums[j]>nums[k]:
                        p[j]=max(p[k]+1,p[j])
                    k+=1
        return max(p)+1




                    
