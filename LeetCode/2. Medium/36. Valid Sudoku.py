class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        #To load from home
        flag:bool = True

        sqr1:list = [board[0][0],board[0][1],board[0][2],
                     board[1][0],board[1][1],board[1][2],
                     board[2][0],board[2][1],board[2][2]]
        sqr2:list = [board[0][3],board[0][4],board[0][5],
                     board[1][3],board[1][4],board[1][5],
                     board[2][3],board[2][4],board[2][5]]
        sqr3:list = [board[0][6],board[0][7],board[0][8],
                     board[1][6],board[1][7],board[1][8],
                     board[2][6],board[2][7],board[2][8]]

        sqr4:list = [board[3][0],board[3][1],board[3][2],
                     board[4][0],board[4][1],board[4][2],
                     board[5][0],board[5][1],board[5][2]]
        sqr5:list = [board[3][3],board[3][4],board[3][5],
                     board[4][3],board[4][4],board[4][5],
                     board[5][3],board[5][4],board[5][5]]
        sqr6:list = [board[3][6],board[3][7],board[3][8],
                     board[4][6],board[4][7],board[4][8],
                     board[5][6],board[5][7],board[5][8]]
        
        sqr7:list = [board[6][0],board[6][1],board[6][2],
                     board[7][0],board[7][1],board[7][2],
                     board[8][0],board[8][1],board[8][2]]
        sqr8:list = [board[6][3],board[6][4],board[6][5],
                     board[7][3],board[7][4],board[7][5],
                     board[8][3],board[8][4],board[8][5]]
        sqr9:list = [board[6][6],board[6][7],board[6][8],
                     board[7][6],board[7][7],board[7][8],
                     board[8][6],board[8][7],board[8][8]]
        
        all_squares:dict = {1:sqr1, 2:sqr2, 3: sqr3,
                              4: sqr4, 5:sqr5, 6:sqr6,
                              7:sqr7, 8:sqr8, 9:sqr9}
        
        for li in all_squares.values():
            lick:list = li.copy()
            for i in lick[:]:
                if i == '.':
                    lick.remove(i)
            lock:set = set(lick)
            lock = list(lock)
            lick.sort()
            lock.sort()
            if lick != lock:
                flag:bool = False

        for i in range(9):
            column_check:list = [board[0][i], board[1][i], board[2][i],
                               board[3][i], board[4][i], board[5][i],
                               board[6][i], board[7][i], board[8][i]]
            
            for i in column_check[:]:
                if i == '.':
                    column_check.remove(i)

            lick:list = column_check.copy()
            lock:set = set(lick)
            lock = list(lock)

            if sorted(column_check) != sorted(lock):
                flag:bool = False

        for i in range(9):
            row_check:list = [board[i][0], board[i][1], board[i][2],
                               board[i][3], board[i][4], board[i][5],
                               board[i][6], board[i][7], board[i][8]]
        
            for i in row_check[:]:
                if i == '.':
                    row_check.remove(i)
            lick:list = row_check.copy()
            lock:set = set(lick)
            lock = list(lock)
            
            lick.sort()
            lock.sort()
            if lick != lock:
                flag:bool = False

        if flag == False:
            return False
        else:
            return True

solution:Solution = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(solution.valid_sudoku(board))