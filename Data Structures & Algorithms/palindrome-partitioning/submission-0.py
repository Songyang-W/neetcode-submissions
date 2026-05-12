class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,part=[],[]
        def dfs(s,i,j):
            if i >= len(s):
                if j==i:
                    res.append(part.copy())
                return
            
            if self.is_palindrome(s,j,i):
                part.append(s[j:i+1])
                dfs(s,i+1,i+1)
                part.pop()
            dfs(s,i+1,j)
        dfs(s,0,0)
        return res

    def is_palindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True