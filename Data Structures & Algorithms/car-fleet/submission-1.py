class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort first, then calculate the time for each car to reach the target
        #check the time needs for the sorted list, if following number smaller and equal, combine
        pair=[(target-p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=False)
        prev_time=0
        fleet=0
        for d,s in pair:
            cur_time=d/s
            if prev_time<cur_time:
                prev_time=cur_time
                fleet+=1
        return fleet
            