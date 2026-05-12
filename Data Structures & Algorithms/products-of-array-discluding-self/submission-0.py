class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        suffix=1
        output_list = [1]*len(nums)
        for numind in range(len(nums)):
            if numind==0:
                continue
            else:
                prefix*=nums[numind-1]
                output_list[numind] = prefix
        for numind in range(len(nums)):
            numind_new = len(nums)-numind
            if numind ==0:
                continue
            else:
                suffix*=nums[numind_new]
                output_list[numind_new-1] *= suffix
        return output_list

        