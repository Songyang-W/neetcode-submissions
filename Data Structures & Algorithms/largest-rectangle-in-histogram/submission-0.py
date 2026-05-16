class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #brutal force, iterate
        largest_area=0
        for i in range(len(heights)):
            height=heights[i]
            for j in range(i,len(heights)):
                height=min(height,heights[j])
                area=height*(j-i+1)
                largest_area=max(largest_area,area)
        return largest_area