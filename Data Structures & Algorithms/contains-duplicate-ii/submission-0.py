class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupset={}
        for i,num in enumerate(nums):
            if num in dupset and i-dupset[num]<=k:
                return True
            else:
                dupset[num]=i
        return False