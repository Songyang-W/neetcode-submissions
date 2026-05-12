class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        temp_str = ''
        l,r = 0,len(s)-1
        s_set = defaultdict(int)
        have_set=defaultdict(int)
        t_set = defaultdict(int)
        have_set=defaultdict(int)
        for c in t:
            t_set[c]+=1
        while l<=r:
            if s[l] not in t:
                l+=1
            if s[r] not in t:
                r-=1
            if r<0 or l>len(s)-1:
                break
            if s[l] in t and s[r] in t:
                break

        for c in s[l:r+1]:
            if c in t:
                s_set[c]+=1
                have_set[c]= min(s_set[c],t_set[c])
            temp_str+=c
            
            while have_set==t_set:
                if len(res) ==0:
                    res=temp_str
                elif len(res)>len(temp_str):
                    res=temp_str
                if temp_str[0] in t_set:
                    s_set[temp_str[0]]-=1
                    have_set[temp_str[0]]=min(s_set[temp_str[0]],t_set[temp_str[0]])
                temp_str=temp_str[1:]
                
        return res
            
