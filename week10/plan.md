# snake & street racer  
___

#### Pygame colors  
```python
import pygame
color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red
```

#### objects interactions - `collides`
Fixed object boundaries.  
By defining these boundaries, the game is able to detect when two or more boundaries overlap or touch  
This allows it to then handle interaction based on which objects are touching.


#### check for collision objects
```python
import pygame

object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))

print(object1.colliderect(object2)) # collide rectangle

object1 = pygame.Rect((20, 50), (50, 100))
 
print(object1.collidepoint(50, 75))  # collide point
```

#### get object borders
```python
import pygame
# create a rectangle of the same size as the image
image = pygame.image.load('./materials/Player.png')
rect = image.get_rect()  # (x, y, width, height)
rect.center = (160, 520) # set this rectangle starting position
rect.move_ip(5, 0) # move in X and Y direction

def draw(self, surface):
    # on which to draw; what and where;
    surface.blit(self.image, self.rect) # surface and object to draw

```


#### Sprites
```python
import pygame
enemies = pygame.sprite.Group()
enemies.add(enemy)

if pygame.sprite.spritecollideany(player, enemies):
    running = False
```


#### using Fonts
```python
import pygame

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))
```

#### set background
```python
import pygame

background = pygame.image.load("./materials/AnimatedStreet.png")
SCREEN.blit(background, (0, 0))
```