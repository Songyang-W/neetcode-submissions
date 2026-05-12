class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre,suf=0,0
        n,max_prod=len(nums),nums[0]
        for i in range(n):
            pre=nums[i]*(pre or 1)
            suf=nums[n-i-1]*(suf or 1)
            max_prod=max(max_prod,max(pre,suf))
        return max_prod