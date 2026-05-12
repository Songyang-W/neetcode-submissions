class Solution:
    def numDecodings(self, s: str) -> int:
        #valid num>0 and num<27 and if two_digit>9
        #ways count the way to solve 1+2+1 (stair question)
        #and check how many are valid
        if len(s)==0 or s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        count1=1
        count2=1
        for i in range(1,len(s)):
            if int(s[i-1:i+1])==0:
                return 0
            if int(s[i-1:i+1])>9 and int(s[i-1:i+1])<27:
                temp=count1
            else:
                temp=0
            if int(s[i])<10 and int(s[i])>0:
                temp+=count2
            count1=count2
            count2=temp
        return count2


              


        
        