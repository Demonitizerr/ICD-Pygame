import pygame
import random
#colour cameleon and cli to move
# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Base Protector')
clock = pygame.time.Clock()
running = True

# create variables here
timer = 0

base = pygame.Rect(0,0,50,50)
base.center = (200,150)

def update():
    global timer, r, colour
    


def draw():
  global random, colour, base
  screen.fill((0,0,0))
  pygame.draw.rect(screen,(255,255,0),base)
#   base.center = (200,200)




  
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