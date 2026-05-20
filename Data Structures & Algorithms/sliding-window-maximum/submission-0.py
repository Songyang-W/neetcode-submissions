class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output_list=[]
        for i in range(len(nums)-k+1):
            output_list.append(max(nums[i:i+k]))
        return output_list
