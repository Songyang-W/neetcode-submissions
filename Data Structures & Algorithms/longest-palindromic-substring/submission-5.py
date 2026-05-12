class Solution:
    def longestPalindrome(self, s: str) -> str:
        def man(s):
            new_s="#"+"#".join(s)+"#"
            new_l=len(new_s)
            p=[0 for i in range(new_l)]
            l,r=0,0
            for i in range(new_l):
                if r>i:
                    #start counting from mirror p[i']=p[l+r-i]
                    p[i]=min(r-i,p[l+r-i])
                else:
                    p[i]=0
                while i-p[i]-1>=0 and i+p[i]+1<new_l and new_s[i-p[i]-1]==new_s[i+p[i]+1]:
                    p[i]+=1
                #update l and r
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p
        p=man(s)
        reslen,center_idx=max((c,i)for i,c in enumerate(p))
        start_ind = (center_idx-reslen)//2
        end_ind = (center_idx+reslen)//2
        return s[start_ind:end_ind]

                        