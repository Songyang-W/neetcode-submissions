class Solution:
    def longestPalindrome(self, s: str) -> str:
        res,reslen='',0
        for i in range(len(s)):
            for j in range(i,len(s)):
                l,r=i,j
                while r>l and s[l]==s[r]:
                    l+=1
                    r-=1
                if l>=r and reslen <(j-i+1):
                    reslen=j-i+1
                    res=s[i:j+1]
        return res

