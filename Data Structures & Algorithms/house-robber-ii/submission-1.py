class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        caches=[-1 for i in range(len(nums)-1)]
        
        def dfs(n,nums_sub):
            if n>len(nums_sub)-1:
                return 0
            if caches[n]>0:
                return caches[n]
            caches[n]=max(dfs(n+1,nums_sub),nums_sub[n]+dfs(n+2,nums_sub))
            return caches[n]
        caches=[-1 for i in range(len(nums)-1)]
        subset1 = dfs(0,nums[:-1])
        caches=[-1 for i in range(len(nums)-1)]
        subset2 = dfs(0,nums[1:])
        return max(subset1,subset2)