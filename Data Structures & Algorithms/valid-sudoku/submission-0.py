class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicate(nine_items):
            checklist=defaultdict(int)
            for item in nine_items:
                if item.isdigit():
                    checklist[item]+=1
                    if checklist[item]>1:
                        return True
            return False

        for r in range(9):
            if has_duplicate(board[r]):
                return False
            for c in range(9):
                if has_duplicate([row[c] for row in board]):
                    return False
                if r%3==0 and c%3==0:
                    matrix = [row[c:c+3] for row in board[r:r+3]]
                    flat_list = [item for sublist in matrix for item in sublist]
                    if has_duplicate(flat_list):
                        return False
        return True

        