import random


class Conway:
    """Conway's Game of Life model"""

    board_size = 10

    def __init__(self):
        self.board = self.random_board()
    
    def __str__(self):
        size = self.board_size
        
        string_board = ""
        for i in range(size):
            for j in range(size):
                string_board += str(self.board[i][j]) + " "
            string_board += "\n"
            
        return string_board.rstrip()
    
    def random_board(self):
        size = self.board_size
        return [[random.choice([1, 0]) for _ in range(size)] for _ in range(size)]
    
    def exclusive_grid_sum(self, x, y):
        size = self.board_size
        ex_sum = -self.board[x][y]
        for i in range(-1, 2):
            for j in range(-1, 2):
                ex_sum += self.board[(x + i) % size][(y + j) % size]

        return ex_sum
    
    def update_state(self, x, y):
        neighbors = self.exclusive_grid_sum(x, y)
        
        if self.board[x][y] == 1 and 2 <= neighbors <= 3:
            self.board[x][y] = 1
        elif self.board[x][y] == 0 and neighbors == 3:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0
        
    def update_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.update_state(i, j)
    
conway = Conway()
print(conway)
conway.update_board()
print("\n\n\n")
print(conway)