import pygame as pg
import time
from colors import Color

from hsv_to_rgb import hsv_to_rgb
from Ball import Ball

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Init variables
pg.init()
pg.mixer.init()

running = True
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()
prev_time = time.time()

pg.display.set_caption("Hello World!")

hue = 0
balls = []

# Utility functions
def draw_text(text, x=0, y=0, size=16, color=Color.BLACK):
    font_name = pg.font.match_font("arial")
    font = pg.font.Font(font_name, size)

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    
    screen.blit(text_surface, text_rect)



# MAIN GAME LOOP

while running:
    # Limit framerate
    clock.tick(FPS)

    # Draw background
    (r, g, b) = hsv_to_rgb(hue, 1, 1)
    r = int(255 * r)
    g = int(255 * g)
    b = int(255 * b)

    screen.fill((r, g, b))

    # Handle input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                balls = []

        # Mouse
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()

            ball = Ball(pos)
            balls.append(ball)

    # Update
    if hue < 360:
        hue += 0.001
    else:
        hue = 0

    for ball in balls:
        ball.update()

        if ball.y > WINDOW_HEIGHT:
            balls.remove(ball)

    # Render
    for ball in balls:
        ball.render(screen)

    draw_text("Hello World!", 70, 200, 150, Color.WHITE)

    pg.display.update()

pg.quit()
