import pygame

pygame.init()


# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Hello from KBTU')
radius = 50
rf = 40
x, y = 40, 50
step = 10
dx, dy = 0, 0
clock = pygame.time.Clock()


running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red, green, blue; ( 0 - 255 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()  # list[int]
    # pygame.K_UP, pygame.K_DOWN, K_LEFT, K_RIGHT

    if pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]:
        dx = -1
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
    # else:
    #     dx, dy = 0, 0
    # print(pressed, 'pressed')
    x = x + dx * step
    y = y + dy * step

    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, 40, 40), width=5)
    pygame.display.flip()

    # 1/60
    clock.tick(100)
