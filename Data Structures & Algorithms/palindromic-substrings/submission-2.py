class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            s="#"+"#".join(s)+"#"
            p=[0 for i in range(len(s))]
            l,r=0,0
            for i in range(len(s)):
                radius = min(p[r-i+l],r-i)
                while i-radius-1>=0 and i+radius+1<len(s) and s[i-radius-1]==s[i+radius+1]:
                    radius+=1
                p[i]=radius
                if i+radius>r:
                    r=i+radius
                    l=i-radius
            return p
        p = manacher(s)
        count=0
        for i in p:
            count+=(i+1)//2
        return count


