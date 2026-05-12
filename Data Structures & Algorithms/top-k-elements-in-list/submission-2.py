class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            output[n]+=1
        for n,c in output.items():
            freq[c].append(n)
        freq_list = freq
        freq_list_combine=[]
        for items in freq_list:
            freq_list_combine.extend(items)
        return freq_list_combine[-k:]

        
