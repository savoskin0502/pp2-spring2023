import pygame

pygame.init()

# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Hello from KBTU ( Tuesday 14:00 - 16:00 ) ")
radius = 100
start_pos_rect_x = WIDTH // 2 - radius
start_pos_rect_y = HEIGHT // 2 - radius
rf = 100


running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red;green;blue;

    for event in pygame.event.get():  # get all events and iterate over them
        if event.type == pygame.QUIT:  # check if any of these events are a `QUIT`
            running = False  # if `QUIT` detected - set running to false and end the loop

    pygame.draw.circle(screen, color=(127, 127, 127), center=(WIDTH // 2, HEIGHT // 2), radius=radius, width=5)
    pygame.draw.line(screen, color=(255, 0, 0), start_pos=(0, 0), end_pos=(WIDTH, HEIGHT), width=10)
    pygame.draw.line(screen, color=(255, 0, 0), start_pos=(0, HEIGHT), end_pos=(WIDTH, 0), width=10)
    pygame.draw.rect(
        screen,
        color=(0, 0, 255),
        rect=pygame.Rect(
            start_pos_rect_x,
            start_pos_rect_y,
            2 * radius,
            2 * radius,
        ),
        width=5,
    )
    pygame.draw.polygon(
        screen,
        color=(0, 0, 0),
        points=[
            (start_pos_rect_x, start_pos_rect_y),
            (start_pos_rect_x + 2 * radius, start_pos_rect_y),
            (start_pos_rect_x + radius, start_pos_rect_y - rf),
        ],
        width=10,
    )

    pygame.display.flip()

