import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 400
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
GREEN = (34, 139, 34)

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
gravity = 0.5
velocity = 0

# Pipe settings
pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)
speed = 3

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

def draw_bird():
    pygame.draw.circle(SCREEN, BLUE, (bird_x, int(bird_y)), bird_radius)

def draw_pipes():
    pygame.draw.rect(SCREEN, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    bottom_pipe_y = pipe_height + pipe_gap
    pygame.draw.rect(SCREEN, GREEN, (pipe_x, bottom_pipe_y, pipe_width, HEIGHT - bottom_pipe_y))

def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(text, (10, 10))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -7  # Jump

    # Bird physics
    velocity += gravity
    bird_y += velocity

    # Pipe movement
    pipe_x -= speed

    # Pipe resets
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(80, 400)
        score += 1

    # Collision detection
    if bird_y - bird_radius <= 0 or bird_y + bird_radius >= HEIGHT:
        break

    if bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
        if bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap:
            break

    # Draw everything
    SCREEN.fill((0, 0, 0))
    draw_bird()
    draw_pipes()
    show_score()

    pygame.display.update()
    CLOCK.tick(60)

# Game Over Screen
SCREEN.fill((0, 0, 0))
text = font.render("Game Over!", True, WHITE)
SCREEN.blit(text, (120, 250))
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
