import pygame

pygame.init()

# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Hello from KBTU')

# Load image
image = pygame.image.load("/Users/roman/Desktop/lectures/pp2/pp2-spring2023/week9/images/img_1.png")
resized_image = pygame.transform.scale(image, (100, 100))

step = 5
x, y = 0, 0
dx, dy = 0, 0
clock = pygame.time.Clock()
rotated_image = pygame.transform.rotate(resized_image, -45)

CUSTOM_EVENT = pygame.USEREVENT + 1
CUSTOM_EVENT_1 = pygame.USEREVENT + 2

running = True
while running:
    screen.fill((0, 0, 0))

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
    screen.blit(rotated_image, (x, y))

    # pressed = pygame.key.get_pressed()
    pygame.display.flip()
    clock.tick(60)
