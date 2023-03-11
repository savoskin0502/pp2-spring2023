import pygame

pygame.init()
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode(size=(HEIGHT, WIDTH))
clock = pygame.time.Clock()


# why without events pygame hangs
x, y = 10, 10
step = 1
running = True
while running:
    screen.fill((0, 0, 0))  # RGB - red, green, blue; 0 - black; 255 - white
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print('here')

    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_UP]:
    #     y -= step
    # if pressed[pygame.K_DOWN]:
    #     y += step
    # if pressed[pygame.K_LEFT]:
    #     x -= step
    # if pressed[pygame.K_RIGHT]:
    #     x += step
    # print(pygame.K_UP)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 90, 90))
    pygame.display.flip()

    clock.tick(140)
