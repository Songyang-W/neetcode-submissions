class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputlist = defaultdict(list)
        for string in strs:
            count = [0]*26
            for letter in string:
                count[ord(letter)-ord("a")]+=1
            outputlist[tuple(count)].append(string)
        
        return list(outputlist.values())

            

