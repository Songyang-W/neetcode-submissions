class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_str=''
        current_longest=0
        l,r=0,0
        while r<len(s):
            
            if not s[r].isascii():
                continue
            
            if s[r] not in s[l:r]:
                r+=1
                current_longest=max(current_longest,len(s[l:r]))
                print(l,r)
                print(s[l:r])
            elif s[r] in s[l:r]:
                l+=1

                print(l)
        return current_longest

