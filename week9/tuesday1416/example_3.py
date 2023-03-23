
import pygame

pygame.init()

# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Hello from KBTU ( Tuesday 14:00 - 16:00 ) ")
x, y = 100, 100
step = 3
dx, dy = 0, 0
clock = pygame.time.Clock()


running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red;green;blue;

    for event in pygame.event.get():  # get all events and iterate over them
        if event.type == pygame.QUIT:  # check if any of these events are a `QUIT`
            running = False  # if `QUIT` detected - set running to false and end the loop

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]:
        dx = 1
        dy = 1
    elif pressed[pygame.K_UP]:
        dx = 0
        dy = -1
    elif pressed[pygame.K_DOWN]:
        dx = 0
        dy = 1
    elif pressed[pygame.K_LEFT]:
        dx = -1
        dy = 0
    elif pressed[pygame.K_RIGHT]:
        dx = 1
        dy = 0
    x += dx * step
    y += dy * step

    # x = abs(x + dx * step) % WIDTH
    # y = abs(y + dy * step) % HEIGHT

    pygame.draw.rect(
        screen,
        color=(255, 0, 0),
        rect=pygame.Rect(
            x,
            y,
            40, 40
        )
    )

    pygame.display.flip()

    # 1/60
    clock.tick(60)
