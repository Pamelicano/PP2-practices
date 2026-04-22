import pygame
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Screen size
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake settings
snake_block = 20
base_speed = 5

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)


def draw_snake(snake_block, snake_list):
    """Draw snake on screen"""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def show_score(score, level):
    """Display score and level"""
    value = score_font.render(f"Score: {score}   Level: {level}", True, black)
    dis.blit(value, [10, 10])


def message(msg, color):
    """Display message in center"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 8, dis_height / 3])


def generate_food(snake_list):
    """Generate food not inside snake"""
    while True:
        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

        if [foodx, foody] not in snake_list:
            return foodx, foody


def gameLoop():
    game_over = False
    game_close = False

    # Initial position
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Score and level
    score = 0
    level = 1

    # Generate first food
    foodx, foody = generate_food(snake_List)

    while not game_over:

        # Game over screen
        while game_close:
            dis.fill(white)
            message("You Lost! Press SPACE-Play Again or Q-Quit", red)
            show_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check wall collision
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Move snake
        x1 += x1_change
        y1 += y1_change

        # Draw background
        dis.fill(white)

        # Draw food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Snake head
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        # Remove tail if too long
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check self collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake
        draw_snake(snake_block, snake_List)

        # Show score and level
        show_score(score, level)

        pygame.display.update()

        # Check if food eaten
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List)
            Length_of_snake += 1
            score += 1

            # Level increases every 3 points
            level = score // 3 + 1

        # Increase speed with level
        clock.tick(base_speed + level * 2)

    pygame.quit()
    quit()


gameLoop()