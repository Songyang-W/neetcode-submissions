class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=0,max(piles)+1
        last_num_works = r
        while l<=r and (l+r)//2>=1:
            print(l,r)
            try_k=(l+r)//2
            total_time = 0
            for pile in piles:
                total_time+=pile//try_k+bool(pile%try_k)
            if total_time<=h:
                r=try_k-1
                last_num_works=try_k
            elif total_time>h:
                l=try_k+1
        if total_time>h:
            return last_num_works
        else:
            return try_k


        