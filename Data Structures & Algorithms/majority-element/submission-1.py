class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uniset={}
        for num in nums:
            if num not in uniset:
                uniset[num]=1
            else:
                uniset[num]+=1
                if uniset[num]>len(nums)//2:
                    return num
        return nums[0]
        

