class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                l,r=i,j
                while l<j and s[l]==s[r]:
                    l+=1
                    r-=1
                count+=(l>=r)
        return count
