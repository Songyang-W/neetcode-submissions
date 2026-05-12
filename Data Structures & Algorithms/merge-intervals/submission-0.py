class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:[x[0],x[1]])
        res=[intervals[0]]

        for i in range(0,len(intervals)):
            cur=intervals[i]
            if cur[0]<=res[-1][1]:
                res[-1][0]=min(cur[0],res[-1][0])
                res[-1][1]=max(cur[1],res[-1][1])
            else:
                res.append(cur)
        return res
