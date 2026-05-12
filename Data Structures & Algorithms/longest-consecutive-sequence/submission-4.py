class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        unique_nums = list(set(nums))
        unique_nums.sort()
        longest_consecutive=1
        current_consecutive=0
        new_leading=unique_nums[0]
        for num in unique_nums:
            if new_leading+1==num:
                new_leading+=1
                if current_consecutive<longest_consecutive:
                    current_consecutive+=1
                else:
                    current_consecutive+=1
                    longest_consecutive = current_consecutive
            else:
                new_leading=num
                current_consecutive=1
        return longest_consecutive


        