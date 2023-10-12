import random


class Conway:
    """Conway's Game of Life model"""

    def __init__(self, size):
        self.size = size
        self.board = self.random_board()

    def __str__(self):
        string_board = ""
        for i in range(self.size):
            for j in range(self.size):
                string_board += str(self.board[i][j]) + " "
            string_board += "\n"

        return string_board.rstrip()

    def random_board(self):
        return [
            [random.choice([1, 0]) for _ in range(self.size)] for _ in range(self.size)
        ]

    def neighbours(self, x, y):
        ex_sum = -self.board[x][y]
        for i in range(-1, 2):
            for j in range(-1, 2):
                ex_sum += self.board[(x + i) % self.size][(y + j) % self.size]

        return ex_sum

    def update_state(self, x, y):
        neighbors = self.neighbours(x, y)

        if self.board[x][y] == 1 and 2 <= neighbors <= 3:
            self.board[x][y] = 1
        elif self.board[x][y] == 0 and neighbors == 3:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0

    def update_board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.update_state(i, j)


def test() -> None:
    conway = Conway(10)
    print(conway)
    conway.update_board()
    print("\n\n\n")
    print(conway)


if __name__ == "__main__":
    test()
