class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,part=[],[]
        n=len(s)
        dp=[[False]*len(s) for i in range(len(s))]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and
                                    (i + 1 > (i + l - 2) or
                                    dp[i + 1][i + l - 2]))
        def dfs(s,i,j):
            if i>=len(s):
                if j==i:
                    res.append(part.copy())
                return
            if dp[j][i]:
                part.append(s[j:i+1])
                dfs(s,i+1,i+1)
                part.pop()
            dfs(s,i+1,j)
        dfs(s,0,0)
        return res

    def is_palindromes(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True

        