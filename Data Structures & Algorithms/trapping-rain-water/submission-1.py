class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        l_m,r_m=0,0
        res=0
        while l<=r:
            while height[l]<height[r]:
                if height[l]<l_m:
                    res+=l_m-height[l]
                else:
                    l_m=height[l]
                l+=1
            if height[r]<r_m:
                res+=r_m-height[r]
            else:
                r_m=height[r]
            r-=1
        return res


