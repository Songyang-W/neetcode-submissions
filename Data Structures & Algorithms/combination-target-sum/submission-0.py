class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def count_change(i, cur_target, path):
            # Base Case: Success! (Found a valid combination)
            if cur_target == 0:
                res.append(path.copy())
                return
            
            # Base Case: Failure (Exceeded target or ran out of numbers)
            if cur_target < 0 or i >= len(nums):
                return

            # Decision 1: WITH_BILL (Use nums[i])
            # We stay at index 'i' because we can reuse the same number
            path.append(nums[i])
            count_change(i, cur_target - nums[i], path)
            
            # Decision 2: WITHOUT_BILL (Skip nums[i])
            # We must pop() to clean up the path before the "without" branch
            path.pop() 
            count_change(i + 1, cur_target, path)

        count_change(0, target, [])
        return res