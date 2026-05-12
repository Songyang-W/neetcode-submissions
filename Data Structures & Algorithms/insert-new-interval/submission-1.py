class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        res=[]
        if newInterval[1]<intervals[0][0]:
            res.append(newInterval)
        start,end=newInterval[0],newInterval[1]
        i=0
        while i<len(intervals):
            interval=intervals[i]
            if i>0 and intervals[i-1][1]<newInterval[0] and interval[0]>newInterval[1]:
                res.append(newInterval)

            if newInterval[0]>interval[1] or newInterval[1]<interval[0]:
                res.append(interval)
                i+=1
            else:
                i+=1
                start=min(interval[0],start)
                end=max(interval[1],end)
                if i==len(intervals) or intervals[i][0]>newInterval[1]:
                    res.append([start,end])
        if newInterval[0]>interval[1]:
            res.append(newInterval)
        return res

