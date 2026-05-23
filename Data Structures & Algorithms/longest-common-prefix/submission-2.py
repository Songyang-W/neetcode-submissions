class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(len(prefix)):
            for string in strs:
                if i==len(string) or string[i]!=prefix[i]:
                    return prefix[:i]
        return prefix

