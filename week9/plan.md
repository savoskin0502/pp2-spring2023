### MidTerm solutions & Intro to PyGame
___

#### What is PyGame
Python library that provides a way to develop 2D games and multimedia applications.  


#### Install PyGame
You can install Pygame using pip  
```shell
pip install pygame
```

#### What the game is?
Game loop ( while ) that continuously
1. capture events
2. do some logic
3. render the game ( update picture again and again until some condition )
4. close game


#### game intro
```python
import pygame

# sets up PyGame, its modules and should be called at the beginning of your program
pygame.init()

# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((500, 500))

```

#### game loop
runs continuously until the user exits  
-- example_1.py
```python
import pygame

pygame.init()

# to display graphics - you need to create a window
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((500, 500))

running = True
while running:
    for event in pygame.event.get():  # get all events and iterate over them
        if event.type == pygame.QUIT: # check if any of these events are a `QUIT`
            running = False  # if `QUIT` detected - set running to false and end the loop
    pygame.display.flip()  # update display/screent to react on changes that have been made
```


#### set window title `pygame window` => `Hello from KBTU`
```python
import pygame

# change pygame window with the title
pygame.display.set_caption("Hello from KBTU")
```

#### filling screen
```python
import pygame
pygame.init()

HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((500, 500))

screen.fill((255, 255, 255))
```


#### axis in pygame
-- excalidraw example of axis



#### creating figures
there are a lot of functions in pygame to draw something

```python
import pygame

# draw a line on some surface
pygame.draw.line(surface, color, start_pos, end_pos, width=1)

# center - (x, y) of circle's center; width - thickness;
# width=0 - fulfilled
pygame.draw.circle(surface, color, center, radius, width=0)

# rect=(x, y, width, height)
pygame.draw.rect(surface, color, rect, width=0)

# points=[(x, y)]; x and y - coordinates of the vertices
pygame.draw.polygon(surface, color, points, width=0)
```

#### practice - drawing
-- example_2.py
![img_1.png](images/img_1.png)
> lines should be green  
> circle - red  
> square - blue  
> roof - black  


#### to move object continuously
> held key and use pygame.key.get_pressed() instead of iteration over pygame.event.get()  

```python
import pygame

x, y = 30, 30
dx, dy = 1, 0
step = 5

pressed = pygame.key.get_pressed() # capture pressed key 
if pressed[pygame.K_UP]:
    dx, dy = 0, -1 
elif pressed[pygame.K_DOWN]:
    dx, dy = 0, +1
elif pressed[pygame.K_LEFT]:
    dx, dy = -1, 0
elif pressed[pygame.K_RIGHT]:
    dx, dy = +1, 0

x += dx * step
y += dy * step
```

#### practice - fast & furious square 10.
-- example_3.py
> create game with cool square that move faster than YOU  


#### Clock - control the framerate of the game loop
game loop - game logic is executed and the graphics are updated at regular intervals.
The clock is used to ensure that the game runs at a consistent speed, regardless of the performance of the computer running the game.  

main methods  
1. Clock.tick(fps) - run at the end of each frame to ensure that the game runs at a consistent speed.  
The fps argument specifies the desired framerate of the game. The method returns the number of milliseconds that have elapsed since the previous call to tick(). This value can be used to control the speed of game objects.  
2. Clock.get_time() - returns the number of milliseconds that have elapsed since the previous call to tick()
3. Clock.get_fps() -  returns the current framerate of the game, calculated based on the time elapsed between calls to tick()  

-- example_4.py
> add framerate control of the game loop
```python
import pygame


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

```

#### work with images
Before working with an image, you need to load it into your program.  
pygame.image.load(fpath) - load from file into pygame image object (Surface object)  
screen.blit(Surface, position=(x, y)) - display image on the screen.    


```python
import pygame

screen = pygame.display.set_mode((500, 500))
# Load image  
image = pygame.image.load("images/img_1.png")

# Resize image  
resized_image = pygame.transform.scale(image, (400, 300))

# Rotate image  
rotated_image = pygame.transform.rotate(image, 45)

screen.blit(resized_image, (0, 0))


```


#### Work with audio

```python
import pygame

# Load audio file
sound_effect = pygame.mixer.Sound("my_sound_effect.wav")
music = pygame.mixer.Sound("my_music.mp3")

# Play sound effect
sound_effect.play()

# Play music in a loop
music.play(loops=-1)  # infinite
sound_effect.play(loops=3)

# Set volume of sound effect to 50%
sound_effect.set_volume(0.5)

```

#### Timer & custom events

**simple timer**  
pygame.time - to handle timing and timing events such as timers.
pygame.time.wait() - function to pause the program for a specified number of milliseconds.  
This can be useful for creating simple timers.  


**repeating timer**  

pygame.time.set_timer() - to create a timer that repeats at a specified interval.  
This function takes two arguments: the event type to use for the timer, and the number of milliseconds between timer events


```python
import pygame

# Wait for 3 seconds
pygame.time.wait(3000)
print("3 seconds have passed")

# Define custom event type
CUSTOM_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(CUSTOM_EVENT, 1000)

while True:
    for event in pygame.event.get():
        if event.type == CUSTOM_EVENT:
            print('again custom event')
        if event.type == pygame.QUIT:
            break

```


#### custom actions - create and call

```python
import pygame
# Define custom event type
CUSTOM_EVENT = pygame.USEREVENT + 1


# Using pygame.event.post() method.
# Using pygame.time.set_timer() method.

# Trigger custom event
custom_event = pygame.event.Event(CUSTOM_EVENT, {"data": "custom data"})
pygame.event.post(custom_event)


```

