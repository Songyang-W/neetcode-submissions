class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=[False for i in range(len(nums))]
        res[-1]=True
        for i in range(len(nums)-1,-1,-1):
            rad= nums[i]
            while (rad+i<len(nums)) and rad>0 and not res[rad+i]:
                rad-=1
            if rad>0:
                res[i]=True
        return res[0]

