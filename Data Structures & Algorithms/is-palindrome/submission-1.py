class Solution:
    def isPalindrome(self, s: str) -> bool:
        point1 = 0
        point2 = len(s)-1
        while point1<point2:
            while not s[point1].isalnum() and point1<len(s)-1:
                point1+=1
            while not s[point2].isalnum() and point2>0:
                point2-=1
            if point2>point1:
                if s[point1].lower()==s[point2].lower():
                    point1+=1
                    point2-=1
                    continue
                else:
                    return False
        return True

