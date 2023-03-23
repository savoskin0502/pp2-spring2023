import pygame

pygame.init()


# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Hello from KBTU')
radius = 50
square_x = WIDTH // 2 - radius
square_y = HEIGHT // 2 - radius
rf = 40


running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red, green, blue; ( 0 - 255 ); R - red; G - green; B - blue;

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.line(screen, (0, 0, 0), (0, 0), (WIDTH, HEIGHT), width=10)
    pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT), (WIDTH, 0), width=10)

    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(square_x, square_x, 2 * radius, 2 * radius), width=5)
    pygame.draw.circle(screen, (122, 122, 122), (WIDTH // 2, HEIGHT // 2), radius=50, width=5)

    pygame.draw.polygon(
        screen,
        color=(0, 0, 0),
        points=[
            (square_x, square_y),
            (square_x + 2 * radius, square_y),
            (WIDTH // 2, HEIGHT // 2 - radius - rf)
        ]
    )
    pygame.display.flip()
