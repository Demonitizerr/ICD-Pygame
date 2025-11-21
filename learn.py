import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('???')
clock = pygame.time.Clock()
running = True

# create variables here


def update():
    ...


def draw():
    screen.fill((0,0,0))
    # draw stuff here

    pygame.display.flip() # should be last line


def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update()
        draw()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
