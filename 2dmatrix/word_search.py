class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def func(i, j, word):
            if len(word)==0:
                return True
            dirr=[(0,1),(0,-1),(1,0),(-1,0)]

            for d in dirr:
                if 0<=i+d[0]<len(board) and 0<=j+d[1]<len(board[0]) and board[i+d[0]][j+d[1]]==word[0]:
                    temp=board[i+d[0]][j+d[1]]
                    board[i+d[0]][j+d[1]]="*"
                    if func(i+d[0],j+d[1],word[1:]):
                        return True
                    board[i+d[0]][j+d[1]]=temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    temp=board[i][j]
                    board[i][j]="*"
                    if func(i,j,word[1:]):
                        return True
                    board[i][j]=temp
        