import pygame #this is python gaming module
from pygame.locals import *
import time
import random  # Import random for generating the apple's position randomly

SIZE = 11 #size of the snake

class Apple: #this class is for making the apple image and it's position
    def __init__(self, parent_screen):
        self.image = pygame.image.load("G:\\py class\\pyproject\\snakefoo1.png").convert() #Apple image location
        self.parent_screen = parent_screen # initializin the screen
        self.x = random.randint(0, 90) * SIZE  # Generate a random x position
        self.y = random.randint(0, 60) * SIZE # Generate a random y position

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))  # Fixed the image variable name
        pygame.display.flip()

    def move_apple(self):
        self.x = random.randint(0, 90) * SIZE
        self.y = random.randint(0, 60) * SIZE

class Snake:# This is class for snake's shape and movemnet
    def __init__(self, parent_screen, length):# function for snake shape
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("G:\\py class\\pyproject\\block1.jpg").convert() # snake image file
        self.x = [SIZE] * length #snake size
        self.y = [SIZE] * length
        self.direction = 'down' # when the game will start it will go for down

    def increasing_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self): #function for snake position in window
        self.parent_screen.fill((0, 0, 0)) # Background color setting property
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):#snake body movement
        for i in range(self.length -1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()

    def move_left(self): #function for moving it up down right left
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 700)) #making the windows size
        self.snake = Snake(self.surface, 5) # initilizing the size of snake
        self.snake.draw()
        self.apple = Apple(self.surface) # Positioning the Apple in windows
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial', 15)
        score = font.render(f"Score: {self.snake.length}", True, (250,250,250))
        self.surface.blit(score,(0, 0))

    def play(self):
        self.snake.walk() # making the snake moveable
        self.apple.draw() # making the snake moveable
        self.display_score()
        pygame.display.flip()

        if self.main_logic(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increasing_length()
            self.apple.move_apple()
    
    def main_logic(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True
            return False

    def run(self): #This function is for making snake moveable using keys of keyboard
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.05) # It will make the snake movable after .1 secend

if __name__ == "__main__": # this is main function and the game will run in this function
    game = Game()
    game.run()