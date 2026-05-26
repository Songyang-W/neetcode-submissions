class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n-1):
                    for l in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target and [nums[i],nums[j],nums[k],nums[l]] not in res:
                            res.append([nums[i],nums[j],nums[k],nums[l]])
        return res