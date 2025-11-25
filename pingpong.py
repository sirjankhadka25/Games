import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 16
PADDLE_SPEED = 6
BALL_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 48)

class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0
    def move(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
        self.vx = random.choice([-1, 1]) * BALL_SPEED
        self.vy = random.choice([-1, 1]) * BALL_SPEED
    def reset(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.vx = random.choice([-1, 1]) * BALL_SPEED
        self.vy = random.choice([-1, 1]) * BALL_SPEED
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy = -self.vy
    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

left = Paddle(20)
right = Paddle(WIDTH - 20 - PADDLE_WIDTH)
ball = Ball()
score_left = 0
score_right = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left.speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left.speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                right.speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right.speed = PADDLE_SPEED
            if event.key == pygame.K_r:
                score_left = 0
                score_right = 0
                ball.reset()
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                left.speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                right.speed = 0

    left.move()
    right.move()
    ball.move()

    if ball.rect.colliderect(left.rect):
        ball.vx = abs(ball.vx)
        offset = (ball.rect.centery - left.rect.centery) / (PADDLE_HEIGHT/2)
        ball.vy = BALL_SPEED * offset
    if ball.rect.colliderect(right.rect):
        ball.vx = -abs(ball.vx)
        offset = (ball.rect.centery - right.rect.centery) / (PADDLE_HEIGHT/2)
        ball.vy = BALL_SPEED * offset

    if ball.rect.left <= 0:
        score_right += 1
        ball.reset()
    if ball.rect.right >= WIDTH:
        score_left += 1
        ball.reset()

    SCREEN.fill(BLACK)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    left.draw(SCREEN)
    right.draw(SCREEN)
    ball.draw(SCREEN)

    text_left = FONT.render(str(score_left), True, WHITE)
    text_right = FONT.render(str(score_right), True, WHITE)
    SCREEN.blit(text_left, (WIDTH//4 - text_left.get_width()//2, 20))
    SCREEN.blit(text_right, (3*WIDTH//4 - text_right.get_width()//2, 20))

    pygame.display.flip()
    CLOCK.tick(FPS)
