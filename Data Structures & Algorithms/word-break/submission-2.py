class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_l=max([len(word) for word in wordDict])
        min_l=min([len(word) for word in wordDict])
        caches={}
        def dfs(s,wordDict=wordDict,max_l=max_l,min_l=min_l):
            if len(s)==0:
                return True
            if len(s)<min_l:
                caches[s]=False
                return False
            if s in caches:
                return caches[s]
            for i in range(min_l,max_l+1):
                if s[0:i] in wordDict:
                    if dfs(s[i:]):
                        caches[s[i:]]=True
                        return True
            caches[s]=False
            return False
        return dfs(s)



        