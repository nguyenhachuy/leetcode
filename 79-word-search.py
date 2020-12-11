class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def backtracking(i,j,step):
            if step == len(word) - 1:
                return True
            elif step >= len(word):
                return False
            result = False
            for a,b in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                if a < 0 or a >= m or b < 0 or b >= n or board[a][b] != word[step+1]:
                    continue
                board[a][b] = "#"
                result |= backtracking(a,b,step+1)
                board[a][b] = word[step+1]
                if result:
                    return result
            return result

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = "#"
                    if backtracking(i,j,0):
                        return True
                    board[i][j] = word[0]
        return False
