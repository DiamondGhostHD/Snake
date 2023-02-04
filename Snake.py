import pygame
import random
import array as arr

pygame.init()
pygame.font.init()


# display resolution
edge_left = 0
edge_right = 720
edge_top = 0
edge_bottom = 480
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Snake')


# display color
color_display = (140, 217, 7)
screen.fill(color_display)


# initial render of the snake
color_snake = (12, 36, 1)
pos_head_x = 360
pos_head_y = 240
snake_head = [pos_head_x, pos_head_y]
snake_block_unit = 15
snake_size = (snake_block_unit, snake_block_unit)



# initial snake position
snake_body_length = 4
pos_body1_x = pos_head_x - 1 * snake_block_unit
pos_body2_x = pos_head_x - 2 * snake_block_unit
pos_body3_x = pos_head_x - 3 * snake_block_unit
pos_body4_x = pos_head_x - 4 * snake_block_unit
snake_body_x = [pos_body1_x, pos_body2_x, pos_body3_x, pos_body4_x]

pos_body1_y = pos_head_y
pos_body2_y = pos_head_y
pos_body3_y = pos_head_y
pos_body4_y = pos_head_y
snake_body_y = [pos_body1_y, pos_body2_y, pos_body3_y, pos_body4_y]

for i in range(snake_body_length):
    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))



# direction
direction = "right"
change_to = direction


# score
my_font = pygame.font.SysFont('Arial Rounded MT Bold', 40)
text_surface = my_font.render('Score:', False, (12, 36, 1))
screen.blit(text_surface, (0, 0))


# color & random position of the apple
color_apple = (255, 0, 0)
random_pos_apple_x = random.randrange(48) * 15
random_pos_apple_y = random.randrange(32) * 15
apple_size = (15, 15)
pygame.draw.rect(screen, color_apple, pygame.Rect((random_pos_apple_x, random_pos_apple_y), apple_size))


# game speed
fps = pygame.time.Clock()
snake_speed = 10
running = True


# game difficulty
difficulty = "easy"
change_difficulty_to = "easy"



while running:

    screen.fill(color_display)  # erease what's been before

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            # changing direction based on which key is touched
            if event.key == pygame.K_LEFT:
                change_to = "left"

            if event.key == pygame.K_RIGHT:
                change_to = "right"

            if event.key == pygame.K_UP:
                change_to = "up"

            if event.key == pygame.K_DOWN:
                change_to = "down"


            # changing difficulty
            if event.key == pygame.K_SPACE:
                if (difficulty == "easy"):
                    change_difficulty_to = "hard"
                else:
                    change_difficulty_to = "easy"


        if event.type == pygame.QUIT:
            running = False



    # changing directions
    if direction != "right" and change_to == "left":  # change to left
        direction = "left"

    if direction != "left" and change_to == "right":  # change to right
        direction = "right"

    if direction != "up" and change_to == "down":  # change to down
        direction = "down"

    if direction != "down" and change_to == "up":  # change to up
        direction = "up"



    # changing difficulty
    if (change_difficulty_to == "hard"):
        difficulty = "hard"
    elif (change_difficulty_to == "easy"):
        difficulty = "easy"


    #gameplay based on difficulty
    if(difficulty == "easy"):

        # movement to left
        if (direction == "left"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[0] -= snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[0] < 0):  # infinite display
                snake_head[0] = 705


        # movement to right
        if (direction == "right"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[0] += snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[0] > 705):  # infinite display
                snake_head[0] = 0


        # down movement
        if (direction == "down"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[1] += snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[1] > 465):  # infinite display
                snake_head[1] = 0


        # up movement
        if (direction == "up"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[1] -= snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[1] < 0):  # infinite display
                snake_head[1] = 465




    if (difficulty == "hard"):

        # movement to left
        if (direction == "left"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[0] -= snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[0] < 0):
                running = False

        # movement to right
        if (direction == "right"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[0] += snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[0] > 705):
                running = False

        # down movement
        if (direction == "down"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[1] += snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[1] > 465):
                running = False

        # up movement
        if (direction == "up"):
            for i in reversed(range(snake_body_length)):
                if (i == 0):
                    snake_body_x[i] = snake_head[0]
                    snake_body_y[i] = snake_head[1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))
                else:
                    snake_body_x[i] = snake_body_x[i - 1]
                    snake_body_y[i] = snake_body_y[i - 1]
                    pygame.draw.rect(screen, color_snake, pygame.Rect((snake_body_x[i], snake_body_y[i], snake_size[0], snake_size[1])))

            snake_head[1] -= snake_block_unit
            pygame.draw.rect(screen, color_snake, pygame.Rect((snake_head[0], snake_head[1], snake_size[0], snake_size[1])))
            if (snake_head[1] < 0):
                running = False





    # eating the apple
    pygame.draw.rect(screen, color_apple, pygame.Rect((random_pos_apple_x, random_pos_apple_y), apple_size))
    if (snake_head[0] == random_pos_apple_x and snake_head[1] == random_pos_apple_y):
        random_pos_apple_x = random.randrange(48) * 15
        random_pos_apple_y = random.randrange(32) * 15
        pygame.draw.rect(screen, color_apple, pygame.Rect((random_pos_apple_x, random_pos_apple_y), apple_size))

        # increse the snake's length after eating apple
        snake_body_x.append(snake_body_x[snake_body_length - 1])
        snake_body_y.append(snake_body_y[snake_body_length - 1])
        snake_body_length += 1



    # snake-snake interaction
    for i in range(snake_body_length):
        if (snake_head[0] == snake_body_x[i] and snake_head[1] == snake_body_y[i]):
            running = False


    # refreshing the display
    screen.blit(text_surface, (0, 0))
    pygame.display.update()
    fps.tick(snake_speed)

pygame.quit()