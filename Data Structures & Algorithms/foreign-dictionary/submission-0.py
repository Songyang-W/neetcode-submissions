class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nei={c: set() for w in words for c in w}
        for i in range(len(words)-1):
            min_len=min(len(words[i]),len(words[i+1]))
            if words[i][:min_len]==words[i+1][:min_len] and len(words[i])>len(words[i+1]):
                return ""
            for j in range(min_len):
                if words[i][j]!=words[i+1][j]:
                    nei[words[i][j]].add(words[i+1][j])
                    break
        visited={}
        reversed_list=[]
        def dfs(letter):
            if letter in visited:
                return visited[letter]

            visited[letter]=True

            for n in nei[letter]:
                if dfs(n):
                    return True

            visited[letter]=False
            reversed_list.append(letter)

        for char in nei:
            if dfs(char):
                return ""
        reversed_list.reverse()
        return "".join(reversed_list)
                