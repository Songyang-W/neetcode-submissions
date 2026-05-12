class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1={}
        set2={}
        for c1 in s:
            if c1 in set1:
                set1[c1]+=1
            else:
                set1[c1]=1
        for c2 in t:
            if c2 in set2:
                set2[c2]+=1
            else:
                set2[c2]=1
        return set1==set2