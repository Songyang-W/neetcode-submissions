class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N=len(temperatures)
        res=[0 for i in range(N)]
        for i in range(N-2,-1,-1):
            j=i+1
            while j<N and temperatures[j]<=temperatures[i]:
                j=j+res[j]
                if res[j]==0:
                    break
            if temperatures[j]>temperatures[i]:
                res[i]=j-i
        return res