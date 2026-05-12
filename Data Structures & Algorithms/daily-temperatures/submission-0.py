class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brutal force
        
        N=len(temperatures)
        res=[0 for i in range(N)]
        for i in range(N):
            for j in range(i,N):
                if temperatures[i]<temperatures[j]:
                    res[i]=j-i
                    break
        return res
