import random, pygame

DEAD = False
ALIVE = True
STATE = [DEAD, ALIVE]

YELLOW = (255, 255, 0)
GRAY = (127, 127, 127)


class Conway:
    """Conway's Game of Life model"""

    def __init__(self, size: int):
        self.size = size
        self.board = self.random_board()

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if size < 1:
            raise ValueError("Board size must be a positive integer.")
        else:
            self._size = size

    def __str__(self) -> str:
        string_board = ""
        for i in range(self.size):
            for j in range(self.size):
                string_board += str(self.board[i][j]) + " "
            string_board += "\n"

        return string_board.rstrip()

    def random_board(self):
        return [
            [random.choice(STATE) for _ in range(self.size)] for _ in range(self.size)
        ]

    def neighbours(self, x: int, y: int) -> int:
        if self.board[x][y]:
            neighbour_count = -1
        else:
            neighbour_count = 0
            
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.board[(x + i) % self.size][(y + j) % self.size]:
                    neighbour_count += 1

        return neighbour_count

    def update_state(self, x: int, y: int) -> None:
        neighbors = self.neighbours(x, y)

        if self.board[x][y] == ALIVE and 2 <= neighbors <= 3:
            self.board[x][y] = ALIVE
        elif self.board[x][y] == DEAD and neighbors == 3:
            self.board[x][y] = ALIVE
        else:
            self.board[x][y] = DEAD

    def update_board(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                self.update_state(i, j)

    def render_board(self, screen):
        width, height = screen.get_size()
        cell_width = dx = width / self.size
        cell_height = dy = height / self.size

        x0, y0 = 0, 0

        x, y = x0, y0
        for i in range(self.size):
            for j in range(self.size):
                rect = pygame.Rect(x, y, cell_width, cell_height)
                if self.board[i][j]:
                    pygame.draw.rect(screen, YELLOW, rect)
                else:
                    pygame.draw.rect(screen, GRAY, rect)
                y += dy
            x, y = x + dx, y0

        pygame.display.flip()


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            pass
        else:
            return n
