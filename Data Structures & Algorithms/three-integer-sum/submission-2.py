class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputlist=[]
        for ind, num in enumerate(nums):
            point1 = ind+1
            point2=len(nums)-1
            while point2>point1:
                current_value = nums[point1]+nums[point2]
                if current_value<-num:
                    point1+=1
                elif current_value>-num:
                    point2-=1
                elif current_value == -num:
                    if [num,nums[point1],nums[point2]] not in outputlist:
                        outputlist.append([num,nums[point1],nums[point2]])
                    point1+=1
                        
                
        return outputlist


        