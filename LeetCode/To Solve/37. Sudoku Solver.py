class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        sqr1:list = [board[0][0,1,2],
                     board[1][0,1,2],
                     board[2][0,1,2]]
        sqr2:list = [board[0][3,4,5],
                     board[1][3,4,5],
                     board[2][3,4,5]]
        sqr3:list = [board[0][6,7,8],
                     board[1][6,7,8],
                     board[2][6,7,8]]
        
        sqr4:list = [board[3][0,1,2],
                     board[4][0,1,2],
                     board[5][0,1,2]]
        sqr5:list = [board[3][3,4,5],
                     board[4][3,4,5],
                     board[5][3,4,5]]
        sqr6:list = [board[3][6,7,8],
                     board[4][6,7,8],
                     board[5][6,7,8]]
        
        sqr7:list = [board[6][0,1,2],
                     board[7][0,1,2],
                     board[8][0,1,2]]
        sqr8:list = [board[6][3,4,5],
                     board[7][3,4,5],
                     board[8][3,4,5]]
        sqr9:list = [board[6][6,7,8],
                     board[7][6,7,8],
                     board[8][6,7,8]]
        


        