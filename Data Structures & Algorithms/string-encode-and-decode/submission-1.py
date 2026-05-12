class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ''
        for word in strs:
            output_str+=f"#{len(word):0{3}d}"
            output_str+=word
        return output_str

    def decode(self, s: str) -> List[str]:
        output_list=[]
        for c_i in range(len(s)-1):
            if s[c_i] == '#':
                if s[c_i+1:c_i+4].isdigit():
                    letters_num = int(s[c_i+1:c_i+4])
                    output_list.append(s[c_i+4:c_i+4+letters_num])
                else:
                    continue
            

        return output_list


