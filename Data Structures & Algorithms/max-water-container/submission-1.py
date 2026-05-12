class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = min(heights[-1],heights[0])*(len(heights)-1)
        point1,point2=0,len(heights)-1
        while point2>point1:
            width = point2-point1
            vol = min(heights[point1],heights[point2])*width
            max_vol = max(max_vol,vol)
            if heights[point1]>heights[point2]:
                point2-=1
            else:
                point1+=1
            
        return max_vol
            
        