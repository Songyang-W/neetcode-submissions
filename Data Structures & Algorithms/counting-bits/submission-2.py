class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0 for i in range(n+1)]
        start=1
        for i in range(1,n+1):
            if i ==2*start:
                start*=2
                dp[i]=1
            
            dp[i]=dp[i-start]+1

        return dp