import pygame
import random
import time

pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gold = (255, 215, 0)

# screen 

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 20
base_speed = 5

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)


# FOOD SYSTEM 
def generate_food(snake_list):
    """Generate food with type (weight, value, lifetime)"""

    food_types = [
        {"color": red, "value": 1, "lifetime": 10},   # common
        {"color": blue, "value": 3, "lifetime": 7},   # rare
        {"color": gold, "value": 5, "lifetime": 5},   # very rare
    ]

    # Weighted random choice
    weights = [70, 20, 10]
    food_type = random.choices(food_types, weights=weights)[0]

    while True:
        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

        if [foodx, foody] not in snake_list:
            return {
                "x": foodx,
                "y": foody,
                "color": food_type["color"],
                "value": food_type["value"],
                "spawn_time": time.time(),
                "lifetime": food_type["lifetime"]
            }


# DRAW
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def show_score(score, level):
    value = score_font.render(f"Score: {score}   Level: {level}", True, black)
    dis.blit(value, [10, 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 8, dis_height / 3])



def gameLoop():
    game_over = False
    game_close = False

    # Initial position
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Movement
    x1_change = snake_block
    y1_change = 0
    direction = "RIGHT"  # used to block reverse moves

    snake_List = []
    Length_of_snake = 1

    score = 0
    level = 1

    food = generate_food(snake_List)

    while not game_over:

        #  GAME OVER SCREEN 
        while game_close:
            dis.fill(white)
            message("You Lost! SPACE-Play Again | Q-Quit", red)
            show_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            elif event.type == pygame.KEYDOWN:
                # Prevent reverse movement
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

        # MOVEMENT 
        if direction == "LEFT":
            x1_change = -snake_block
            y1_change = 0
        elif direction == "RIGHT":
            x1_change = snake_block
            y1_change = 0
        elif direction == "UP":
            y1_change = -snake_block
            x1_change = 0
        elif direction == "DOWN":
            y1_change = snake_block
            x1_change = 0

        x1 += x1_change
        y1 += y1_change

        #  WALL COLLISION 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        dis.fill(white)

        # FOOD TIMER 
        if time.time() - food["spawn_time"] > food["lifetime"]:
            food = generate_food(snake_List)

        elapsed = time.time() - food["spawn_time"]
        remain = food["lifetime"] - elapsed
        if (remain <= 0):
            food = generate_food(snake_List)
        else:
            draw_food = True
            if (remain < 2):
                if (int(time.time() * 10) % 2 == 0):
                    draw_food = False

        if draw_food:
            pygame.draw.rect(dis, food["color"],
                         [food["x"], food["y"], snake_block, snake_block])

        # SNAKE 
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        show_score(score, level)

        pygame.display.update()

        # EAT FOOD 
        if x1 == food["x"] and y1 == food["y"]:
            Length_of_snake += 1
            score += food["value"]

            level = score // 5 + 1
            food = generate_food(snake_List)

        clock.tick(base_speed + level * 2)

    pygame.quit()
    quit()


gameLoop()