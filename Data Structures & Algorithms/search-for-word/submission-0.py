class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0 or len(word)==0:
            return False

        def dfs(i,j,word):
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[0]:
                return False
            
            if len(word)==1:
                return True

            temp = board[i][j]
            board[i][j]='#'
            res= (dfs(i+1,j,word[1:]) or 
                    dfs(i-1,j,word[1:]) or
                    dfs(i,j+1,word[1:]) or
                    dfs(i,j-1,word[1:]))
            board[i][j] = temp
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, word):
                    return True
        return False