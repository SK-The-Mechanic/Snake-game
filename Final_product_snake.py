import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (237, 29, 36)
green = (127, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
init_velocity = 7

# Creating window
screen_width = 1200
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

background_img = pygame.image.load("G:/py class/pyproject/main_bg_3.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height)).convert_alpha()

gameover_img = pygame.image.load("G:/py class/pyproject/game_over_1.jpg")
gameover_img = pygame.transform.scale(gameover_img, (screen_width, screen_height)).convert_alpha()

home_img = pygame.image.load("G:/py class/pyproject/homescreen_bg_2.jpg")
home_img = pygame.transform.scale(home_img, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Snake XanXie")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.Font("G:/py class/pyproject/nexa_rust_slab/NexaRustSans-Trial-BlackShadow1.ttf", 15)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, black, white)
    gameWindow.blit(screen_text, [x, y])

# def plot_snake(gameWindow, color, snk_list, snake_size):
#     for x, y in snk_list:
#         pygame.draw.rect(gameWindow, green, [x, y, snake_size, snake_size])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.circle(gameWindow, green, (x + snake_size // 2, y + snake_size // 2), snake_size // 2)

def welcome():
    global init_velocity
    init_velocity = 7
    exit_game = False

    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(home_img, (0, 0))
        # text_screen("Welcome to Snake XanXie", green, 475, 350)
        # text_screen("For easy mode press 'e'", green, 500, 450)
        # text_screen("For medium mode press 'm'", green, 500, 500)
        # text_screen("For hard mode press 'h'", green, 500, 550)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE:
                #     gameloop()

                if event.key == pygame.K_e:
                    init_velocity -= 5
                    gameloop()

                if event.key == pygame.K_m:
                    init_velocity -= 4
                    gameloop()

                if event.key == pygame.K_h:
                    init_velocity += 1
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    global init_velocity
    exit_game = False
    game_over = False
    pause = False  # Add a pause flag
    snake_x = 45
    snake_y = 45
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    if not os.path.exists("G:/py class/pyproject/high_score.txt"):
        with open("G:/py class/pyproject/high_score.txt", "w") as file:
            file.write("0")

    with open("G:/py class/pyproject/high_score.txt", "r") as file:
        high_score = file.read()

    food_x = random.randint(35, screen_width - 50)
    food_y = random.randint(35, screen_height - 50)
    score = 0
    snake_size = 21
    food_size = 15
    fps = 120

    while not exit_game:
        if game_over:
            with open("G:/py class/pyproject/high_score.txt", "w") as file:
                file.write(str(high_score))

            gameWindow.fill(white)
            gameWindow.blit(gameover_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                    if event.key == pygame.K_SPACE:
                        # Toggle pause when the space bar is pressed
                        pause = not pause

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                    if event.key == pygame.K_c:
                        score += 5

                    if event.key == pygame.K_r:
                        init_velocity -= 1

                    if event.key == pygame.K_q:
                        init_velocity += 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Toggle pause when the space bar is pressed
                        pause = not pause

            if not pause:  # Only update the game when it's not paused
                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                    score += 5
                    food_x = random.randint(25, screen_width - 50)
                    food_y = random.randint(25, screen_height - 50)
                    snk_length += 7
                    pygame.mixer.music.load('G:/py class/pyproject/eating_sound.mp3')
                    pygame.mixer.music.play()
                    if score > int(high_score):
                        high_score = score

                gameWindow.fill(black)
                gameWindow.blit(background_img, (0, 0))
                text_screen("Your Score is: " + str(score), red, 15, 1)
                text_screen("The High Score is: " + str(high_score), red, 975, 1)
                text_screen("Press Space Bar to pause the game", green, 400, 1)
                # pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size]) # food design
                pygame.draw.circle(gameWindow, red, (food_x + food_size // 2, food_y + food_size // 2), food_size // 2)


                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_over = True
                    pygame.mixer.music.load('G:/py class/pyproject/Game_over.mp3')
                    pygame.mixer.music.play()

                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    game_over = True
                    pygame.mixer.music.load('G:/py class/pyproject/Game_over.mp3')
                    pygame.mixer.music.play()

                plot_snake(gameWindow, black, snk_list, snake_size)

            else:
                font = pygame.font.Font("G:/py class/pyproject/campus/CAMPUS PERSONAL USE.ttf", 25)  # Choose a font size (e.g., 36) and style
                text = font.render("The Game Is Paused! To Continue Press Space Bar", True, black, white)
                gameWindow.blit(text, (300, 350))
                # text_screen("The Game Is Paused! To Continue Press Space Bar", black, 300, 35)
                # gameWindow.blit(text,(400, 35))



            # else:
            #     font = pygame.font.Font(None, 25)  # Choose a font size and style
            #     text = font.render("The Game Is Paused! To Continue Press 'Space Bar'", True, green)
            #     gameWindow.blit(text, (400, 25))

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
gameloop()