import pygame
import random
import time
import sys

pygame.init()
pygame.font.init()

running = True
update = pygame.USEREVENT
UPDATE_TIMER = 150
pygame.time.set_timer(update, UPDATE_TIMER)

menu = True
play = False
pause = False
game_over = False

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480

EDGE_LEFT = 40
EDGE_RIGHT = 600
EDGE_TOP = 80
EDGE_BOTTOM = 420
WIDTH = 3

WHITE = (255, 255, 255)
LIGHT_GREEN = (140, 217, 7)
DARK_GREEN = (2, 48, 32)
RED = (255, 0, 0)

SCORE_BAR = 60
SCORE_SIZE = 45
SOCRE_POS_X = EDGE_LEFT
SCORE_POS_Y = SCORE_BAR - 40
font = pygame.font.SysFont('Arial Rounded MT Bold', SCORE_SIZE)
score = 0
best = 0

TITLE_SIZE = 100
TITLE_POS_X = 195
TITLE_POS_Y = 190
title_font = pygame.font.SysFont('Arial Rounded MT Bold', TITLE_SIZE)

GAME_STATE_SIZE = 70
game_state_font = pygame.font.SysFont('Arial Rounded MT Bold', GAME_STATE_SIZE)
 
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

BLOCK_SIZE = 20
STEP = 20
STARTING_POSITION_X = 400
STARTING_POSITION_Y = 300
change_direction = RIGHT
INITIAL_LENGTH = 4

pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
SCREEN_COLOR = LIGHT_GREEN
screen.fill(SCREEN_COLOR)

all_sprites = pygame.sprite.Group()
tail = pygame.sprite.Group()

class Snake_head(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        super().__init__()
        self.image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.direction = direction

    def move(self):
        if(self.direction) == RIGHT:
            self.rect.x += STEP

        if(self.direction) == LEFT:
            self.rect.x -= STEP

        if(self.direction) == UP:
            self.rect.y -= STEP

        if(self.direction) == DOWN:
            self.rect.y += STEP

    def change_direction(self, change_direction):
        if(self.direction != LEFT) and change_direction == RIGHT:
            self.direction = RIGHT

        if(self.direction != RIGHT) and change_direction == LEFT:
            self.direction = LEFT

        if(self.direction != DOWN) and change_direction == UP:
            self.direction = UP

        if(self.direction != UP) and change_direction == DOWN:
            self.direction = DOWN

class Snake_tail(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.direction = direction

    def move(self):
        if(self.direction) == RIGHT:
            self.rect.x += STEP

        if(self.direction) == LEFT:
            self.rect.x -= STEP

        if(self.direction) == UP:
            self.rect.y -= STEP

        if(self.direction) == DOWN:
            self.rect.y += STEP

class Apple(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.correct_position = False

    def generate(self):
        self.correct_position = False
        while(self.correct_position == False):
            apple.rect.x = random.randint(EDGE_LEFT // BLOCK_SIZE, EDGE_RIGHT // BLOCK_SIZE) * BLOCK_SIZE
            apple.rect.y = random.randint(EDGE_TOP // BLOCK_SIZE, EDGE_BOTTOM // BLOCK_SIZE) * BLOCK_SIZE
            self.correct_position = True

            for segment in tail:
                if self.rect.center == segment.rect.center or check_out_of_bounds(apple):
                    self.correct_position = False
                    break

            if(self.rect.center == snake_head.rect.center):
                    self.correct_position = False

def follow(tail:pygame.sprite.Group, snake_head:Snake_head):
    tail_list = tail.sprites()
    tail_length = len(tail_list)

    for i in reversed(range(tail_length)):
        current_segment:Snake_tail = tail_list[i]
        next_segment:Snake_tail = tail_list[i-1]
        
        if(i == 0):
            current_segment.direction = snake_head.direction
        else:
            current_segment.direction = next_segment.direction

def check_snake_apple_collision():
    if apple.rect.center == snake_head.rect.center:
        apple.generate()
        return True
    return False

def increase_snake_length():
    last_segment:Snake_tail = tail.sprites()[-1]

    if last_segment.direction == RIGHT:
        tail_segment = Snake_tail(last_segment.rect.x - BLOCK_SIZE, last_segment.rect.y, last_segment.direction)

    if last_segment.direction == LEFT:
        tail_segment = Snake_tail(last_segment.rect.x + BLOCK_SIZE, last_segment.rect.y, last_segment.direction)

    if last_segment.direction == UP:
        tail_segment = Snake_tail(last_segment.rect.x, last_segment.rect.y + BLOCK_SIZE, last_segment.direction)

    if last_segment.direction == DOWN:
        tail_segment = Snake_tail(last_segment.rect.x, last_segment.rect.y - BLOCK_SIZE, last_segment.direction)

    all_sprites.add(tail_segment)
    tail.add(tail_segment)            

def check_head_tail_collision():
    for segment in tail:
        if segment.rect.center == snake_head.rect.center:
            return True
    return False

def check_out_of_bounds(object):
    if object.rect.left < EDGE_LEFT:
        return True
    
    if object.rect.right > EDGE_RIGHT:
        return True
    
    if object.rect.top < EDGE_TOP:
        return True
    
    if object.rect.bottom > EDGE_BOTTOM:
        return True
    
    return False

def draw_text(text, font, color, pos_x, pos_y):
    image = font.render(text, True, color)
    screen.blit(image, (pos_x, pos_y))

def draw_border():
    pygame.draw.line(screen, DARK_GREEN, (EDGE_RIGHT, EDGE_BOTTOM), (EDGE_RIGHT, EDGE_TOP), WIDTH)
    pygame.draw.line(screen, DARK_GREEN, (EDGE_RIGHT, EDGE_TOP), (EDGE_LEFT, EDGE_TOP), WIDTH)
    pygame.draw.line(screen, DARK_GREEN, (EDGE_LEFT, EDGE_BOTTOM), (EDGE_LEFT, EDGE_TOP), WIDTH)
    pygame.draw.line(screen, DARK_GREEN, (EDGE_RIGHT, EDGE_BOTTOM), (EDGE_LEFT, EDGE_BOTTOM), WIDTH)
    pygame.draw.line(screen, DARK_GREEN, (EDGE_LEFT, SCORE_BAR), (EDGE_RIGHT, SCORE_BAR), WIDTH)

snake_head = Snake_head(STARTING_POSITION_X, STARTING_POSITION_Y, RIGHT)
all_sprites.add(snake_head)

for segment in range(1, INITIAL_LENGTH):
    tail_segment = Snake_tail((snake_head.rect.x - segment * BLOCK_SIZE), snake_head.rect.y, snake_head.direction)
    all_sprites.add(tail_segment)
    tail.add(tail_segment)

apple = Apple(random.randint(EDGE_LEFT // BLOCK_SIZE, EDGE_RIGHT // BLOCK_SIZE) * BLOCK_SIZE, random.randint(EDGE_TOP // BLOCK_SIZE, EDGE_BOTTOM // BLOCK_SIZE) * BLOCK_SIZE)
apple.generate()
all_sprites.add(apple)

while running:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if play:
                if event.key == pygame.K_RIGHT:
                    change_direction = RIGHT

                if event.key == pygame.K_LEFT:
                    change_direction = LEFT

                if event.key == pygame .K_UP:
                    change_direction = UP

                if event.key == pygame.K_DOWN:
                    change_direction = DOWN

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RETURN and menu:
                play = True
                menu = False

            if event.key == pygame.K_SPACE and menu == False:
                if pause:
                    pause = False
                    play = True
                else:
                    pause = True
                    play = False

        if event.type == pygame.QUIT:
            running = False

        if event.type == update and play:
            if(change_direction == RIGHT):
                snake_head.change_direction(RIGHT)
            
            if(change_direction == LEFT):
                snake_head.change_direction(LEFT)

            if(change_direction == UP):
                snake_head.change_direction(UP)

            if(change_direction == DOWN):
                snake_head.change_direction(DOWN)

            for segment in tail:
                segment.move()
            follow(tail, snake_head)
            snake_head.move()

    screen.fill(SCREEN_COLOR)
    draw_border()

    if menu:
        draw_text("SNAKE", title_font, DARK_GREEN, TITLE_POS_X, TITLE_POS_Y)
        draw_text("Press ENTER to start", font, DARK_GREEN, TITLE_POS_X - 30, TITLE_POS_Y + 80)

    if play:
        if check_snake_apple_collision():
            increase_snake_length()
            score += 1

        if check_head_tail_collision() or check_out_of_bounds(snake_head):
            game_over = True
            play = False

        all_sprites.draw(screen)
        draw_border()
        draw_text("Score: " + str(score), font, DARK_GREEN, SOCRE_POS_X, SCORE_POS_Y)
        draw_text("Best: " + str(best), font, DARK_GREEN, EDGE_RIGHT - 100, SCORE_POS_Y)
        draw_text("Press SPACE to pause", font, DARK_GREEN, EDGE_LEFT + 115, EDGE_BOTTOM + 20)

    if pause:
        draw_text("Game Paused", game_state_font, DARK_GREEN, EDGE_LEFT + 115, EDGE_TOP + 110)
        draw_text("Press SPACE to unpause", font, DARK_GREEN, EDGE_LEFT + 100, EDGE_TOP + 170)
        draw_text("Score: " + str(score), font, DARK_GREEN, SOCRE_POS_X, SCORE_POS_Y)
        draw_text("Best: " + str(best), font, DARK_GREEN, EDGE_RIGHT - 100, SCORE_POS_Y)

    if game_over:
        time.sleep(1)

        screen.fill(SCREEN_COLOR)
        draw_border()
        draw_text("Game Over", game_state_font, DARK_GREEN, EDGE_LEFT + 145, EDGE_TOP + 110)
        draw_text("Score: " + str(score), font, DARK_GREEN, SOCRE_POS_X, SCORE_POS_Y)
        draw_text("Best: " + str(best), font, DARK_GREEN, EDGE_RIGHT - 100, SCORE_POS_Y)
        pygame.display.update()

        time.sleep(2)

        for sprite in all_sprites:
            sprite.kill()

        change_direction = RIGHT
        snake_head = Snake_head(STARTING_POSITION_X, STARTING_POSITION_Y, RIGHT)
        all_sprites.add(snake_head)

        for segment in range(1, INITIAL_LENGTH):
            tail_segment = Snake_tail((snake_head.rect.x - segment * BLOCK_SIZE), snake_head.rect.y, snake_head.direction)
            all_sprites.add(tail_segment)
            tail.add(tail_segment)
        
        apple = Apple(random.randint(EDGE_LEFT // BLOCK_SIZE, EDGE_RIGHT // BLOCK_SIZE) * BLOCK_SIZE, random.randint(EDGE_TOP // BLOCK_SIZE, EDGE_BOTTOM // BLOCK_SIZE) * BLOCK_SIZE)
        apple.generate()
        all_sprites.add(apple)

        if score > best:
            best = score
        score = 0

        game_over = False
        menu = True

    pygame.display.update()

pygame.quit()
