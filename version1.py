import pygame
import helpers

BLACK = (0, 0, 0)


def main() -> None:
    board_size = helpers.get_int("Enter board size: ")
    conway = helpers.Conway(board_size)

    bg_color = BLACK
    pygame.init()

    screen = pygame.display.set_mode()
    screen.fill(bg_color)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        conway.render_board(screen)
        conway.update_board()
        pygame.time.delay(1000 // board_size)

    pygame.quit()


if __name__ == "__main__":
    main()
