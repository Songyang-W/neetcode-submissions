class Solution:
    def getSum(self, a: int, b: int) -> int:
        #a+b=(a&b)<<1+a^b
        mask = 0xFFFFFFFF
        max_int=0x7FFFFFFF

        def sum_bit(a,b):
            if b==0:
                return a
            else:
                carry=(a&b)<<1
                a = (a ^ b) & mask
                b=carry&mask
                return sum_bit(a,b)

        return sum_bit(a,b) if sum_bit(a,b) <= max_int else ~(sum_bit(a,b)^ mask)