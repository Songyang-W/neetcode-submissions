class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            s="#"+"#".join(s)+"#"
            p=[0 for i in range(len(s))]
            l,r=0,0
            for i in range(len(s)):
                radius = min(p[r-i+l],r-i)
                while i-radius>=0 and i+radius<len(s) and s[i-radius]==s[i+radius]:
                    radius+=1
                p[i]=radius
                if i+radius>r:
                    r=i+radius
                    l=i-radius
            return p
        p = manacher(s)
        count=0
        for i in p:
            count+=(i)//2
        return count


