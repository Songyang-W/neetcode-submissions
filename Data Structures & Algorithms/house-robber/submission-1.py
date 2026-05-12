class Solution:
    def rob(self, nums: List[int]) -> int:

        caches=[0 for i in range(len(nums))]
        def dfs(n):
            if n>len(nums)-1:
                return 0
            if caches[n]>0:
                return caches[n]
            cur=max(nums[n]+dfs(n+2),dfs(n+1))
            caches[n]=cur
            return cur
        return dfs(0)