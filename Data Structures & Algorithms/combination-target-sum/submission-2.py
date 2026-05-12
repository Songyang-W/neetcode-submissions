class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        nums.sort()
        def dfs(total,nums,path):
            if len(nums)==0:
                return
            if total==0:
                res.append(path.copy())
                return
            if total<nums[0]:
                return
            
            path.append(nums[0])
            withbill = dfs(total-nums[0],nums,path)
            path.pop()
            withoutbill = dfs(total,nums[1:],path)
                


        dfs(target,nums,[])
        return res