"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h=[]
        intervals.sort(key=lambda x: x.start)
        count,cur=0,0
        for interval in intervals:
            if not h:
                heapq.heappush(h,interval.end)
                cur=1
                continue
            while h and h[0]<=interval.start:
                heapq.heappop(h)
            heapq.heappush(h,interval.end)
            cur=len(h)
            count=max(count,cur)
        return max(count,cur)
            