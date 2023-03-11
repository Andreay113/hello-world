# pygame template

import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables

# Colours
grey = (128, 128, 128, 1)
dark_grey = (105,105,105)
white = (250,250,250)
green = (12, 166, 51)
blue = (135, 206, 235)
yellow = (255,255,0)
moon_grey = (188,188,188)
cloud_white = (255,255,255)
brown = (144, 92, 66)
black = (0,0,0)
star = (240,240,240)

# Dimensions 
above_grass_height = HEIGHT - 100
width_middle = 170
height_middle = 100
middle_position = WIDTH/2
width_side = 175
height_side = 150
left_position = WIDTH/4 - 50
right_position = 3/4 * WIDTH + 50
sun_x = WIDTH + 40
sun_y = 110
moon_x = WIDTH + 40
moon_y = 110
cloud_x_1 = 30
cloud_y_1 = 60
radius_1 = random.randrange(18,23) 
cloud_x_2 = 250
cloud_y_2 = 40
radius_2 = random.randrange(18,23)
cloud_x_3 = 450
cloud_y_3 = 90
radius_3 = random.randrange(18,23)
tree_leaf_width = 40
tree_width = 20
tree_height = 50
tree_middle = tree_width/2 + 30
key_left = False
key_right = False
cloud_speed = 0

# Functions
def draw_cloud(x,y,z):
    pygame.draw.circle(screen, cloud_white, [x, y], z)
    pygame.draw.circle(screen, cloud_white, [x + 25, y - 15], z)
    pygame.draw.circle(screen, cloud_white, [x + 55, y - 5], z)
    pygame.draw.circle(screen, cloud_white, [x + 20, y + 15], z)
    pygame.draw.circle(screen, cloud_white, [x + 45, y + 10], z)

def draw_tree(x,y):
    tree_middle = tree_width/2 + x
    pygame.draw.rect(screen, brown, [x, y, tree_width, tree_height])
    pygame.draw.polygon(screen, green , [[tree_middle, y - 50], [tree_middle + tree_leaf_width, y], [tree_middle - tree_leaf_width, y]])
    pygame.draw.line(screen, black, [x, y], [x + 30, y], 2)
    if key_left == False and key_right == False:
        pygame.draw.polygon(screen, green , [[tree_middle, y - 80], [tree_middle + tree_leaf_width - 5, y - 25], [tree_middle - tree_leaf_width + 5, y - 25]])
        pygame.draw.polygon(screen, green , [[tree_middle, y - 95], [tree_middle + tree_leaf_width - 10, y - 45], [tree_middle - tree_leaf_width + 10, y - 45]])
        pygame.draw.polygon(screen, black, [[x, y], [x, y + tree_height], [x + tree_width,y + tree_height], [x + tree_width, y], [tree_middle + tree_leaf_width, y], [x + 30, y - 25], [tree_middle + tree_leaf_width - 5, y - 25], [tree_middle + 20, y - 45], [tree_middle + tree_leaf_width - 10, y - 45], [tree_middle, y - 95], [tree_middle - tree_leaf_width + 10, y - 45], [tree_middle - 21, y - 45], [tree_middle - tree_leaf_width + 5, y - 25], [tree_middle - 22, y - 25], [tree_middle - tree_leaf_width,y]], 2)
    elif key_left == True: 
        pygame.draw.polygon(screen, green , [[tree_middle -10 , y - 80 + 15], [tree_middle + tree_leaf_width - 5 - 5, y - 25 -5], [tree_middle - tree_leaf_width + 5 - 5, y - 25 +5]])
        pygame.draw.polygon(screen, green , [[tree_middle -15, y - 95 +10], [tree_middle + tree_leaf_width - 10 - 10, y - 45 - 10], [tree_middle - tree_leaf_width + 10 -10, y - 45 +10]])
        pygame.draw.polygon(screen, black, [[x, y], [x, y + tree_height], [x + tree_width,y + tree_height], [x + tree_width, y], [tree_middle + tree_leaf_width, y], [x + 25, y - 29], [tree_middle + tree_leaf_width - 5 - 5, y - 25 - 5], [tree_middle + 20 - 12, y - 45 - 6], [tree_middle + tree_leaf_width - 10 - 9, y - 45 - 8], [tree_middle - 16, y - 95 + 8], [tree_middle - tree_leaf_width + 10 - 11, y - 45 + 9], [tree_middle - 21 - 8, y - 45 +6], [tree_middle - tree_leaf_width + 5 - 5, y - 25 + 7], [tree_middle - 22, y - 25], [tree_middle - tree_leaf_width,y]], 2)

    elif key_right == True: 
        pygame.draw.polygon(screen, green , [[tree_middle +10 , y - 80 + 15], [tree_middle - tree_leaf_width + 5 + 5, y - 25 -5], [tree_middle + tree_leaf_width - 5 + 5, y - 25 +5]])
        pygame.draw.polygon(screen, green , [[tree_middle +15, y - 95 +10], [tree_middle - tree_leaf_width + 10 + 10, y - 45 - 10], [tree_middle + tree_leaf_width - 10 +10, y - 45 +10]])
        pygame.draw.polygon(screen, black, [[x, y], [x, y + tree_height], [x + tree_width,y + tree_height], [x + tree_width, y], [tree_middle + tree_leaf_width, y], [x + 30, y - 25], [tree_middle + tree_leaf_width - 5 + 5, y - 25 + 4], [tree_middle + 20 + 8, y - 45 + 8], [tree_middle + tree_leaf_width - 10 + 9, y - 45 + 8], [tree_middle +14, y - 95 + 8], [tree_middle - tree_leaf_width + 10 +11, y - 45 -11], [tree_middle - 21 + 12, y - 45 - 5], [tree_middle - tree_leaf_width + 5 + 5, y - 25 -4], [tree_middle - 22 + 7, y - 25 - 3], [tree_middle - tree_leaf_width,y]], 2)


def draw_star(x,y):
    pygame.draw.rect(screen, star, [x, y, 50, 20])


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                key_left = True
                cloud_speed = -1
            elif event.key == pygame.K_RIGHT:
                key_right = True  
                cloud_speed = 1 
            else:
                cloud_speed = 0

        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        key_left = True
    elif keys[pygame.K_RIGHT]:
        key_right = True
    else:
        key_right = False
        key_left = False
    
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill(blue)  # always the first drawing command

# background
    pygame.draw.rect(screen, white, [0, HEIGHT - 100 , WIDTH, HEIGHT])

# sun / day
    pygame.draw.circle(screen, yellow, [sun_x, sun_y], 40)
    pygame.draw.circle(screen, moon_grey, [moon_x, moon_y], 30)
    pygame.draw.circle(screen, blue, [moon_x + 15, moon_y], 20)
    if sun_x >= WIDTH/4 * 3:
        sun_x -= 2
        sun_y -= 1/2
        grey = (128, 128, 128, 1)
        dark_grey = (105,105,105)
        blue = (135, 206, 235)
        white = (250,250,250)
        cloud_white = (255,255,255)
        green = (12, 166, 51)
        brown = (144, 92, 66)
    elif sun_x >= WIDTH/2:
        sun_x -= 2
        sun_y -= 1/4
    elif sun_x >= WIDTH/4:
        sun_x -= 2
        sun_y += 1/4
    elif sun_x > -50:
        sun_x -= 2
        sun_y += 1/2
    elif sun_x == -50:
        moon_x = WIDTH + 40
        moon_y = 110
        sun_x += 1
    # moon / night
    elif moon_x >= WIDTH/4 * 3:
        moon_x -= 2
        moon_y -= 1/2
        blue = (25, 25, 112)
        grey = (82,82,82)
        dark_grey = (59, 59, 59)
        white = (200,200,200)
        cloud_white = (140,140,140)
        green = (20, 51, 6)
        brown = (92, 64, 51)
    elif moon_x >= WIDTH/2:
        moon_x -= 2
        moon_y -= 1/4
    elif moon_x >= WIDTH/4:
        moon_x -= 2
        moon_y += 1/4
    elif moon_x >= -40:
        moon_x -= 2
        moon_y += 1/2
    else:
        sun_x = WIDTH + 40
        sun_y = 110
        moon_x = WIDTH + 40
        moon_y = 110


# left montain
    pygame.draw.polygon(screen, dark_grey , [[left_position, height_side], [left_position + width_side, above_grass_height], [left_position - width_side, above_grass_height]])
    pygame.draw.polygon(screen, white , [[left_position, height_side], [left_position + 35, height_side + 50], [left_position - 65, height_side + 85]])
    pygame.draw.polygon(screen, white , [[left_position, height_side], [left_position - 35, height_side + 50], [left_position + 65, height_side + 85]])
    pygame.draw.polygon(screen, white , [[left_position, height_side + 80], [left_position - 35, height_side + 60], [left_position, height_side + 50], [left_position + 35, height_side +60]])

# right montain
    pygame.draw.polygon(screen, dark_grey , [[right_position, height_side], [right_position + width_side, above_grass_height], [right_position - width_side, above_grass_height]])
    pygame.draw.polygon(screen, white , [[right_position, height_side], [right_position + 35, height_side + 50], [right_position - 65, height_side + 85]])
    pygame.draw.polygon(screen, white , [[right_position, height_side], [right_position - 35, height_side + 50], [right_position + 65, height_side + 85]])
    pygame.draw.polygon(screen, white , [[right_position, height_side + 80], [right_position - 35, height_side + 60], [right_position, height_side + 50], [right_position + 35, height_side +60]])

# middle montain
    pygame.draw.polygon(screen, grey , [[middle_position, height_middle], [middle_position + width_middle, above_grass_height], [middle_position - width_middle, above_grass_height]])
    pygame.draw.polygon(screen, white , [[middle_position, height_middle], [middle_position + 25, 142], [middle_position - 47, 175]])
    pygame.draw.polygon(screen, white , [[middle_position, height_middle], [middle_position - 25, 142], [middle_position + 47, 175]])
    pygame.draw.polygon(screen, white , [[middle_position, 175], [middle_position - 25, 160], [middle_position, height_middle], [middle_position + 25, 160]])

# cloud 1
    draw_cloud(cloud_x_1, cloud_y_1, radius_1)
    if cloud_speed == 0:
        print ("Press left or right arrow keys to act as wind")
    elif cloud_speed == -1:
        if cloud_x_1 <= -80:
            cloud_x_1 = WIDTH + 40
            cloud_y_1 = random.randrange(30, 110)
            radius_1 = random.randrange(18,23)
    elif cloud_speed == 1:
          if cloud_x_1 >= WIDTH + 80:
            cloud_x_1 = 0 - 40
            cloud_y_1 = random.randrange(30, 110)
            radius_1 = random.randrange(18,23)    
    cloud_x_1 += cloud_speed
 
    


# cloud 2

    draw_cloud(cloud_x_2, cloud_y_2, radius_2)
    if cloud_speed == 0:
        print ("Press left or right arrow keys to act as wind")
    elif cloud_speed == -1:
        if cloud_x_2 <= -80:
            cloud_x_2 = WIDTH + 40
            cloud_y_2 = random.randrange(30, 110)
            radius_2 = random.randrange(18,23)
    elif cloud_speed == 1:
          if cloud_x_2 >= WIDTH + 80:
            cloud_x_2 = 0 - 40
            cloud_y_2 = random.randrange(30, 110)
            radius_2 = random.randrange(18,23)    
    cloud_x_2 += cloud_speed

# cloud 3
    draw_cloud(cloud_x_3, cloud_y_3, radius_3)
    if cloud_speed == 0:
        print ("Press left or right arrow keys to act as wind")
    elif cloud_speed == -1:
        if cloud_x_3 <= -80:
            cloud_x_3 = WIDTH + 40
            cloud_y_3 = random.randrange(30, 110)
            radius_3 = random.randrange(18,23)
    elif cloud_speed == 1:
          if cloud_x_3 >= WIDTH + 80:
            cloud_x_3 = 0 - 40
            cloud_y_3 = random.randrange(30, 110)
            radius_3 = random.randrange(18,23)    
    cloud_x_3 += cloud_speed

# tree
    draw_tree(30, HEIGHT - 75)
    draw_tree(460, HEIGHT - 90)
    draw_tree(569, HEIGHT - 95)
    draw_tree(145,HEIGHT - 95)
    draw_tree(285,HEIGHT - 90)
    draw_tree(411,HEIGHT - 70)
    draw_tree(520,HEIGHT - 65)
    draw_tree(622,HEIGHT - 80)
    draw_tree(80,HEIGHT - 60)
    draw_tree(200,HEIGHT - 60)
    draw_tree(350,HEIGHT - 60)



    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    #---------------------------


pygame.quit()
