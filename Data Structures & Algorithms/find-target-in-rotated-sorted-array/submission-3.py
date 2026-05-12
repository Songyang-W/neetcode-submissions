class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use two pointer find min
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l
        # find the element 
        if target>nums[-1]:
            l,r=0,pivot-1
        else:
            l,r=pivot,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            else:
                r=m-1

        if nums[l]==target:
            return l
        else:
            return -1

