class Solution:
    def isHappy(self, n: int,seen=[]) -> bool:
        slow,fast=n,self.convert_num(n)
        while slow!=fast and fast!=1:
            fast=self.convert_num(fast)
            fast=self.convert_num(fast)
            slow=self.convert_num(slow)
        
        return True if fast==1 else False

    
    def convert_num(self,n:int) -> int:
        n_str=str(n)
        res=0
        for i in n_str:
            res+=int(i)**2
        return res