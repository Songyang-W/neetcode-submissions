class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_table=[0 for i in range(26)]
        s2_table=[0 for i in range(26)]
        for c in s1:
            s1_table[ord(c)-ord('a')]+=1
        for c in s2[:len(s1)-1]:
            s2_table[ord(c)-ord('a')]+=1
        for c_ind in range(len(s2)-len(s1)+1):
            s2_table[ord(s2[c_ind+len(s1)-1])-ord('a')]+=1
            if s2_table==s1_table:
                return True
            s2_table[ord(s2[c_ind])-ord('a')]-=1
        return False