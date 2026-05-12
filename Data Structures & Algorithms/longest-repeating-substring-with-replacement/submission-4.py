class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output_dict = defaultdict(int)
        high_f = 0
        l=0
        current_max = 0
        for r,c in enumerate(s):
            output_dict[c]+=1
            most_frequent_char = max(output_dict, key=output_dict.get)
            high_f = max(high_f,output_dict[most_frequent_char])
            print(output_dict)
            while (r-l+1)-high_f>k:
                
                output_dict[s[l]]-=1
                l+=1
            current_max = max(current_max,r-l+1)

        return min(current_max,len(s))



