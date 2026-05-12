class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point2=len(numbers)-1
        for point1 in range(len(numbers)):
            while target<(numbers[point1]+numbers[point2]):
                point2-=1
            if target==(numbers[point1]+numbers[point2]):
                return[point1+1,point2+1]
        