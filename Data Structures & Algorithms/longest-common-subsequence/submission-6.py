class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)>=len(text2):
            longtext,shorttext=text1,text2
        else:
            longtext,shorttext=text2,text1
        pre=[0]*(len(longtext)+1)

        for i in range(len(longtext)-1,-1,-1):
            cur=[0]*(len(longtext)+1)
            for j in range(len(shorttext)-1,-1,-1):
                if longtext[i]==shorttext[j]:
                    cur[j]=1+pre[j+1]
                else:
                    cur[j]=max(pre[j],cur[j+1])
            pre=cur
        return cur[0]
