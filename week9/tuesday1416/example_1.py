import pygame

pygame.init()

# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hello from KBTU ( Tuesday 14:00 - 16:00 ) ")


running = True
while running:
    screen.fill((0, 255, 0))  # RGB - red;green;blue;

    for event in pygame.event.get():  # get all events and iterate over them
        if event.type == pygame.QUIT:  # check if any of these events are a `QUIT`
            running = False  # if `QUIT` detected - set running to false and end the loop
    pygame.display.flip()
