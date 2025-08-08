import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 40
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        head = self.body[0]
        x, y = self.direction
        new_head = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        if new_head in self.body[1:] or not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            return False
        self.body.insert(0, new_head)
        return True

    def change_direction(self, direction):
        if (direction[0]*-1, direction[1]*-1) != self.direction:
            self.direction = direction

    def eat_food(self):
        self.body.append(self.body[-1])

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

    def respawn(self, snake):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
        while self.position in snake.body:
            self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        if not snake.move():
            break

        if snake.body[0] in [food.position]:
            food.respawn(snake)
            score += 10
            snake.eat_food()

        screen.fill(WHITE)
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (food.position[0]*GRID_SIZE, food.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()
        clock.tick(10)

# Run the game
main()
