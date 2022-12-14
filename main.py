import pygame, helpers, sys

# game speed
speed = 10
# the size of the initial snake
square_size = 60
# define frame sizes
frame_size_x = 1380
frame_size_y = 840
# using graphics coordinate system (up = 8, down = 4, right = 2, left = 1)
direction = 2
# initialize snake position
head_position = [120, 60]
snake_body = [[120, 60]]
# set food
food_spawn = True
# set score to zero
score = 0
# set food position
food_position= helpers.get_food_postion(frame_size_x, frame_size_y, square_size)
# define colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
# score font
choice = 1
color = white
font = "consolas"
size = 20


# check whether game initialization was successful
check_errors = pygame.init()
if check_errors[1] > 0:
    raise ValueError(f"Failed to initialize: {check_errors[1]}\n")
sys.stdout.write("Launching Snake v1.0 ...\n")


# create game window and elements
pygame.display.set_caption("Snake v1.0")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
frame_controller = pygame.time.Clock()


# gameplay loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord("w") and direction != 4:
                direction = 8
            elif event.key == pygame.K_DOWN or event.key == ord("s") and direction != 8:
                direction = 4
            elif event.key == pygame.K_LEFT or event.key == ord("a") and direction != 2:
                direction = 1
            elif (
                event.key == pygame.K_RIGHT or event.key == ord("d") and direction != 1
            ):
                direction = 2

    if direction == 8:
        head_position[1] -= square_size
    elif direction == 4:
        head_position[1] += square_size
    elif direction == 1:
        head_position[0] -= square_size
    elif direction == 2:
        head_position[0] += square_size

    if head_position[0] < 0:
        head_position[0] = frame_size_x - square_size
    elif head_position[0] > frame_size_x - square_size:
        head_position[0] = 0
    elif head_position[1] < 0:
        head_position[1] = frame_size_y - square_size
    elif head_position[1] > frame_size_y - square_size:
        head_position[1] = 0

    # if the snake eats the food
    snake_body.insert(0, list(head_position))
    if head_position[0] == food_position[0] and head_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # spawn food, if food is eaten
    if not food_spawn:
        food_position = helpers.get_food_postion(
            frame_size_x, frame_size_y, square_size
        )
        food_spawn = True

    # generate game window
    game_window.fill(black)
    for position in snake_body:
        # draw snake
        pygame.draw.rect(
            game_window,
            green,
            pygame.Rect(
                position[0] + 2,
                position[1] + 2,
                square_size - 2,
                square_size - 2,
            ),
        )
    # draw food
    pygame.draw.rect(
        game_window,
        red,
        pygame.Rect(
            food_position[0],
            food_position[1],
            square_size,
            square_size,
        ),
    )

    # game over sequence?
    for block in snake_body[1:]:
        if head_position[0] == block[0] and head_position[1] == block[1]:
            # reset variables (need something much more interesting here!!!)
            direction, head_position, snake_body = 2, [120, 60], [[120, 60]]
            food_position = helpers.get_food_postion(
                frame_size_x, frame_size_y, square_size
            )
            food_spawn, score = False, 0

    # display score
    score_surface, score_rect = helpers.display_score(
        choice, color, font, size, score, frame_size_x, frame_size_y
    )
    game_window.blit(score_surface, score_rect)

    # refresh
    pygame.display.update()
    frame_controller.tick(speed)
