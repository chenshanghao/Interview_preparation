class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkCol(board) and self.checksquare(board)
    
    def checkRow(self, board):
        for i in range(len(board)):
            val_dict = {}
            for val in board[i]:
                if val != "." and val in val_dict:
                    return False
                elif val != "." and val not in val_dict:
                    val_dict[val] = 1
        return True
    
    def checkCol(self, board):
        for i in range(len(board[0])):
            val_dict = {}
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in val_dict:
                    return False
                elif board[j][i] != "." and board[j][i] not in val_dict:
                    val_dict[board[j][i]] = 1
        return True
                    
    def checksquare(self, board):
        for si in range(0, 9, 3):
            for sj in range(0, 9, 3):
                val_dict = {}
                for i in range(3):
                    for j in range(3):
                        if board[si+i][sj+j] != "." and board[si+i][sj+j] in val_dict:
                            return False
                        elif board[si+i][sj+j] != "." and board[si+i][sj+j] not in val_dict:
                            val_dict[board[si+i][sj+j]] = 1
        return True
                
        