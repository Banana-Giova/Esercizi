def checkUpRow(board, i, letter):
    if i != 0\
    and i != 4:
        pass

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        lord:list[str] = list(word)
        lord = lord.append(None)
        row1 = board[0]
        row2 = board[1]
        row3 = board[2]
        n:int = 0

        for i in range(5):
            if row1[i] == lord[n]:
                while True:
                    n += 1
                    pass