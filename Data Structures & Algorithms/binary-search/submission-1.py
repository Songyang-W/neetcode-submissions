class Solution:
    def search(self, nums: List[int], target: int) -> int:
        started_ind = len(nums)//2
        current_searching_len = len(nums)//2
        if target not in nums:
            return -1
        while nums[started_ind]!=target:
            if current_searching_len == 1:
                current_searching_len = 2 
            current_searching_len=current_searching_len//2
            if nums[started_ind]<target:
                started_ind+= current_searching_len
            if nums[started_ind]>target:
                started_ind-= current_searching_len
        if nums[started_ind] == target:
            return started_ind
        

        