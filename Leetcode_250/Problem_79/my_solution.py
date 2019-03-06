class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:   return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, m, n, word):    return True
        return False
    
    def helper(self, board, i, j, m, n, word):
        if len(word) == 0:  return True
        if i<0 or j<0 or i==m or j==n or board[i][j]!= word[0]: return False
        
        tmp = board[i][j]
        board[i][j] = '#'
        flag = self.helper(board, i-1, j, m, n, word[1:]) or self.helper(board, i+1, j, m, n, word[1:]) or self.helper(board, i, j-1, m, n, word[1:]) or self.helper(board, i, j+1, m, n, word[1:])
        board[i][j] = tmp
        return flag
        
            
        
        