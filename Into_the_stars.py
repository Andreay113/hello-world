import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random
import time
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import math

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables
# Title Screen
# Astronaut
astronaut_x = 25
astronaut_y = 320
astronaut_body_x = 50
astronaut_body_y = 370
astronaut_speed = 0.25

# Rocket
rocket_x = 540
rocket_y = 100
rocket_width = 100
rocket_height = 200
rocket_bottom_height = 50
flame_height = 80
rocket_speed = 0.25


# Stage 1 code
tile_size = WIDTH/20
# Maze
tiles = ["empty", "wall", "start", "goal", "key_1", "locked_door_1", "key_2", "locked_door_2", "key_3", "locked_door_3", "key_inventory_1", "key_inventory_2", "key_inventory_1"]
maze = [
[10,11,12,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 6, 0, 0, 1, 0, 8, 1, 3, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 9, 1],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 7, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 5, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 2, 1, 0, 1, 0, 0, 4, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
key_1 = False
lock_1 = False
key_1_inventory = False
key_2 = False
lock_2 = False
key_2_inventory = False
key_3 = False
lock_3 = False
key_3_inventory = False

# Colors
white = (255,255,255)
black = (0,0,0)
red = (224, 16, 0)
gold = (255,215,0)
blue = (32, 0, 224)
green = (0, 255, 0)
light_blue = (0, 150, 255)
dark_blue = (0, 16, 176)
grey = (100,100,100)
light_green = (0, 100, 30)

# Move Variables
x_cord = 1
y_cord = 13
player_x = (x_cord + 0.5) * tile_size
player_y = (y_cord + 0.5) * tile_size
player_size = tile_size/2 * (5/6)
x_move = 0
y_move = 0

# Functions
def draw_key(colour, background):
    pygame.draw.rect(screen, colour, [x + 13, y + 16, 16, 3])
    pygame.draw.rect(screen, colour, [x + 19, y + 10, 3, 7])
    pygame.draw.rect(screen, colour, [x + 24, y + 10, 3, 7])
    pygame.draw.circle(screen, colour, (x + 8, y + tile_size/2), 7)
    pygame.draw.circle(screen, background, (x + 5, y + tile_size/2), 2)

def draw_lock(colour):
    pygame.draw.rect(screen, grey, [x, y, tile_size, tile_size])
    pygame.draw.circle(screen, colour, (x + tile_size/2, y + 12), 8)
    pygame.draw.polygon(screen, colour, [[x + tile_size/2, y + 10], [x + tile_size/2 - 8, y + 25], [x + tile_size/2 + 8, y + 25]])

def draw_text(message, font_size, cords, colour):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(message, True, colour)
    textRect = text.get_rect()
    textRect.center = cords
    screen.blit(text, textRect)

# stage 2 code
#Stars 
stars = []
for n in range(100):
    star_x = random.randrange(0, WIDTH)
    star_y = random.randrange(0, HEIGHT)
    star_r = random.randrange(1, 4)

    star = [star_x, star_y, star_r]
    stars.append(star)

def draw_stars():
	for star in stars:
		star_x = star[0]
		star_y = star[1]
		radius = star[2]
		pygame.draw.circle(screen, (255, 255, 255), (star_x, star_y), radius)
                
def draw_astronaut(x,y):
    astronaut_x = 70
    astronaut_y = 270
    astronaut_body_x = 95
    astronaut_body_y = 320
    pygame.draw.rect(screen, (217, 217, 217), (astronaut_body_x + x, astronaut_body_y+y, 75, 120))
    pygame.draw.rect(screen, (239, 239, 239), (astronaut_body_x+5 +x, astronaut_body_y+y+30, 65, 15))
    pygame.draw.rect(screen, (255, 0, 0), (astronaut_body_x+5 + x, astronaut_body_y+52+y, 5, 5))
    pygame.draw.rect(screen, (255, 255, 0), (astronaut_body_x+12 + x, astronaut_body_y+52+y, 5, 5))
    pygame.draw.rect(screen, (0, 255, 0), (astronaut_body_x+19+x, astronaut_body_y+52+y, 5, 5))
    # astronaut_x = 70  astronaut_y = 270
    pygame.draw.polygon(screen, (217, 217, 217), [(astronaut_x+x, astronaut_y+y,), (astronaut_x+10+x, astronaut_y+y), (astronaut_x+10+x, astronaut_y-10+y), (astronaut_x+110+x, astronaut_y-10+y), (astronaut_x+110+x, astronaut_y-10+y), (astronaut_x+110+x, astronaut_y+y), (astronaut_x+120+x, astronaut_y+y), (astronaut_x+120+x, astronaut_y+70+y), (astronaut_x+110+x, astronaut_y+70+y), (astronaut_x+110+x, astronaut_y+80+y), (astronaut_x+10+x, astronaut_y+80+y), (astronaut_x+10+x, astronaut_y+70+y), (astronaut_x+x, astronaut_y+70+y)])
    pygame.draw.rect(screen, (7, 55, 99), (astronaut_x+10+x, astronaut_y+5+y, 100, 60))
    pygame.draw.polygon(screen, (4, 25, 45), [(astronaut_x+10+x, astronaut_y+30+y), (astronaut_x+25+x, astronaut_y+30+y), (astronaut_x+25+x, astronaut_y+40+y), (astronaut_x+110+x, astronaut_y+40+y), (astronaut_x+110+x, astronaut_y+65+y), (astronaut_x+10+x, astronaut_y+65+y)])
    pygame.draw.rect(screen, (255, 255, 255), (astronaut_x+70+x, astronaut_y+10+y, 35, 10))

#For astronaut

meteorites = []
meteorite_speed_list = []

# For Meteorite
meteorite_diameter = 100

#For score
score = 0

for n in range(5):
    meteorite_x_speed = random.randrange(1, 5)
    meteorite_y_speed = random.randrange(1, 5)
    meteorite_x = random.randrange(0, 200)
    meteorite_y = random.randrange(0, 200)
    meteorite_r = random.randrange(1, 50)

    meteorite = [
        meteorite_x, meteorite_y, meteorite_r, meteorite_x_speed,
        meteorite_y_speed
    ]
    meteorites.append(meteorite)

# stage 3 code
# Object rects
box_side = 55
box1 = pygame.Rect(565, 310, box_side, box_side)
box2 = pygame.Rect(150, 100, box_side, box_side)
box3 = pygame.Rect(565, 70, box_side, box_side)
box4 = pygame.Rect(390, 250, box_side, box_side)
box5 = pygame.Rect(200, 260, box_side, box_side)
box6 = pygame.Rect(10, 60, box_side, box_side)
box7 = pygame.Rect(400, 5, box_side, box_side)
box8 = pygame.Rect(50, 300, box_side, box_side)

# Variable to see if dragging box or not
box1_dragging = False
box2_dragging = False
box3_dragging = False
box4_dragging = False
box5_dragging = False
box6_dragging = False
box7_dragging = False
box8_dragging = False

# Inventory slots
def draw_inventory(colour, slot_number):
    pygame.draw.rect(screen, colour, slot_number, 3)
inventory_slot1 = pygame.Rect(22, HEIGHT-75, 70, 70)
inventory_slot2 = pygame.Rect(97, HEIGHT-75, 70, 70)
inventory_slot3 = pygame.Rect(172, HEIGHT-75, 70, 70)
inventory_slot4 = pygame.Rect(247, HEIGHT-75, 70, 70)
inventory_slot5 = pygame.Rect(322, HEIGHT-75, 70, 70)
inventory_slot6 = pygame.Rect(397, HEIGHT-75, 70, 70)
inventory_slot7 = pygame.Rect(472, HEIGHT-75, 70, 70)
inventory_slot8 = pygame.Rect(547, HEIGHT-75, 70, 70)

# Level Stage Variables
title_screen = True
start_level_1 = False
level_1 = False
finish_level_1 = False
start_level_2 = False
level_2 = False
finish_level_2 = False
start_level_3 = False
level_3 = False
finish_level_3 = False
end_screen = False

# ---------------------------


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            # Stages in game
            if event.key == pygame.K_RETURN:
                if title_screen == True:
                    start_level_1 = True
                    title_screen = False

                elif start_level_1 == True:  
                    start_level_1 = False
                    level_1 = True

                elif finish_level_1 == True:
                    finish_level_1 = False
                    start_level_2 = True

                elif start_level_2 == True:
                    level_2 = True
                    start_level_2 = False

                elif finish_level_2 == True:
                    start_level_3 = True
                    finish_level_2 = False
                
                elif start_level_3 == True:
                    level_3 = True
                    start_level_3 = False

            if level_1 == True:
                # Stage 1 inputs
                if event.key == pygame.K_LEFT:
                    x_move = -1
                if event.key == pygame.K_RIGHT:
                    x_move = 1
                if event.key == pygame.K_UP:
                    y_move = -1
                if event.key == pygame.K_DOWN:
                    y_move = 1

        if event.type == pygame.KEYUP:
            if level_1 == True:
                # Stage 1 inputs
                if event.key == pygame.K_UP and y_move == -1:
                    y_move = 0
                elif event.key == pygame.K_DOWN and y_move == 1:
                    y_move = 0
                elif event.key == pygame.K_LEFT and x_move == -1:
                    x_move = 0
                elif event.key == pygame.K_RIGHT and x_move == 1:
                    x_move = 0
            
        
        if event.type == MOUSEBUTTONDOWN:
            if level_2 == True:
                x, y = event.pos
                for n in range(len(meteorites)):
                    a = meteorites[n][0] - x
                    b = meteorites[n][1] - y
                    distance = math.sqrt(a**2 + b**2)
                    if distance < meteorites[n][2]:
                        score += 1        
                
            if level_3 == True:
                if box1.collidepoint(event.pos):
                    box1_dragging = True
                if box2.collidepoint(event.pos):
                    box2_dragging = True
                if box3.collidepoint(event.pos):
                    box3_dragging = True
                if box4.collidepoint(event.pos):
                    box4_dragging = True
                if box5.collidepoint(event.pos):
                    box5_dragging = True
                if box6.collidepoint(event.pos):
                    box6_dragging = True
                if box7.collidepoint(event.pos):
                    box7_dragging = True
                if box8.collidepoint(event.pos):
                    box8_dragging = True

        if event.type == MOUSEBUTTONUP:
            if level_3 == True:
                # if we were dragging and we moved the box over
                # the "inventory slot", then we move the box to
                # the center of the item slot.
                if box1_dragging == True and inventory_slot1.colliderect(box1):
                    box1.center = inventory_slot1.center
                if box2_dragging == True and inventory_slot2.colliderect(box2):
                    box2.center = inventory_slot2.center
                if box3_dragging == True and inventory_slot3.colliderect(box3):
                    box3.center = inventory_slot3.center
                if box4_dragging == True and inventory_slot4.colliderect(box4):
                    box4.center = inventory_slot4.center
                if box5_dragging == True and inventory_slot5.colliderect(box5):
                    box5.center = inventory_slot5.center
                if box6_dragging == True and inventory_slot6.colliderect(box6):
                    box6.center = inventory_slot6.center
                if box7_dragging == True and inventory_slot7.colliderect(box7):
                    box7.center = inventory_slot7.center
                if box8_dragging == True and inventory_slot8.colliderect(box8):
                    box8.center = inventory_slot8.center
                    
                # Toggle off dragging when the mouse button comes up
                box1_dragging = False
                box2_dragging = False
                box3_dragging = False
                box4_dragging = False
                box5_dragging = False
                box6_dragging = False
                box7_dragging = False
                box8_dragging = False

    # Get proposed new cords
    x_proposed = x_cord + x_move
    y_proposed = y_cord + y_move

    # Stage 1 Intro screen
    if title_screen == True:
        astronaut_y -= astronaut_speed
        if astronaut_y == 315:
            astronaut_speed = -0.25
        elif astronaut_y == 320:
            astronaut_speed = 0.25

        rocket_y += rocket_speed
        if rocket_y == 110:
            rocket_speed = -0.25
        elif rocket_y == 100:
            rocket_speed = 0.25
                
        # DRAWING
        screen.fill((0, 0, 42))  # always the first drawing command

        # Astronaut Intro
        #astronaut_body_x = 45   astronaut_body_y = 370
        pygame.draw.rect(screen, (217, 217, 217), (astronaut_body_x, astronaut_body_y, 75, 120))
        pygame.draw.rect(screen, (239, 239, 239), (astronaut_body_x+5, astronaut_body_y+30, 65, 15))
        pygame.draw.rect(screen, (255, 0, 0), (astronaut_body_x+5, astronaut_body_y+52, 5, 5))
        pygame.draw.rect(screen, (255, 255, 0), (astronaut_body_x+12, astronaut_body_y+52, 5, 5))
        pygame.draw.rect(screen, (0, 255, 0), (astronaut_body_x+19, astronaut_body_y+52, 5, 5))
        # astronaut_x = 20  astronaut_y = 320
        pygame.draw.polygon(screen, (217, 217, 217), [(astronaut_x, astronaut_y,), (astronaut_x+10, astronaut_y), (astronaut_x+10, astronaut_y-10), (astronaut_x+110, astronaut_y-10), (astronaut_x+110, astronaut_y-10), (astronaut_x+110, astronaut_y), (astronaut_x+120, astronaut_y), (astronaut_x+120, astronaut_y+70), (astronaut_x+110, astronaut_y+70), (astronaut_x+110, astronaut_y+80), (astronaut_x+10, astronaut_y+80), (astronaut_x+10, astronaut_y+70), (astronaut_x, astronaut_y+70)])
        pygame.draw.rect(screen, (7, 55, 99), (astronaut_x+10, astronaut_y+5, 100, 60))
        pygame.draw.polygon(screen, (4, 25, 45), [(astronaut_x+10, astronaut_y+30), (astronaut_x+25, astronaut_y+30), (astronaut_x+25, astronaut_y+40), (astronaut_x+110, astronaut_y+40), (astronaut_x+110, astronaut_y+65), (astronaut_x+10, astronaut_y+65)])
        pygame.draw.rect(screen, (255, 255, 255), (astronaut_x+70, astronaut_y+10, 35, 10))

        # ROCKET
        #--Side triangles--
        pygame.draw.polygon(screen, (255, 0, 0), [(rocket_x, rocket_y + 50), (rocket_x, rocket_y + 150), (rocket_x - 50, rocket_y + 150)])
        pygame.draw.polygon(screen, (255, 0, 0), [(rocket_x + rocket_width, rocket_y + 50), (rocket_x + rocket_width, rocket_y + 150), (rocket_x + rocket_width + 50, rocket_y + 150)])
        #--Body--
        pygame.draw.rect(screen, (239, 239, 239), (rocket_x, rocket_y, rocket_width, rocket_height))
        pygame.draw.polygon(screen, (153, 0, 0), [(rocket_x, rocket_y), (rocket_x + rocket_width, rocket_y), (rocket_x + (rocket_width/2), rocket_y - 80)])
        #--Bottom--
        pygame.draw.polygon(screen, (153, 0, 0), [(rocket_x, rocket_y + rocket_height), (rocket_x + rocket_width, rocket_y + rocket_height), (rocket_x + rocket_width + 30, rocket_y + rocket_height + rocket_bottom_height), (rocket_x - 30, rocket_y + rocket_height + rocket_bottom_height)])
        #--Window--
        pygame.draw.circle(screen, (207, 226, 243), (rocket_x + rocket_width/2, rocket_y + 80), 30)
        pygame.draw.circle(screen, (111, 168, 220), (rocket_x + rocket_width/2, rocket_y + 80), 30, 30 > 1)
        #--Flame--
        #flame_height = 80
        flame_y = rocket_y + rocket_height + rocket_bottom_height + 10
        pygame.draw.polygon(screen, (255, 0, 0), [(rocket_x, flame_y), (rocket_x + rocket_width, flame_y), (rocket_x + rocket_width/2, flame_y + flame_height)])
        pygame.draw.polygon(screen, (255, 153, 0), [(rocket_x + 15, flame_y), (rocket_x + rocket_width - 15, flame_y), (rocket_x + rocket_width/2, flame_y + flame_height - 15)])
        pygame.draw.polygon(screen, (255, 255, 0), [(rocket_x + 30, flame_y), (rocket_x + rocket_width - 30, flame_y), (rocket_x + rocket_width/2, flame_y + flame_height - 30)])

        # TEXT
        draw_text("Welcome to...", 30, (WIDTH/2, HEIGHT/2 - 70), (185, 235, 255))
        draw_text("Into the Stars", 50, (WIDTH/2, HEIGHT/2), (255, 255, 255))
        draw_text("Press ENTER to begin Level 1", 20, (WIDTH/2, HEIGHT/2 + 120), (185, 235, 255))
        
    
    
    elif start_level_1 == True:
        screen.fill(black)
        draw_stars()
        draw_text("Help the Astronaut get to the Engine Room", 25, (WIDTH//2,HEIGHT//2 - 60), white)
        draw_text("Escape the Maze", 25, (WIDTH//2,HEIGHT//2), white)
        draw_text("Press ENTER to continue", 25, (WIDTH//2,HEIGHT//2 + 60), white)

    # Stage 1 
    elif level_1 == True:
        # DRAWING
        screen.fill((white))

        # Draw Maze
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                x = col * tile_size
                y = row * tile_size

                if (maze[row])[col] == 1 or (maze[row])[col] == 10 or (maze[row])[col] == 11 or (maze[row])[col] == 12:
                    pygame.draw.rect(screen, black, [x, y, tile_size, tile_size])
                    # Inventory keys
                    if (maze[row])[col] == 10 and key_1_inventory == True:
                        draw_key(light_blue, black)
                    if (maze[row])[col] == 11 and key_2_inventory == True:
                        draw_key(gold, black)
                    if (maze[row])[col] == 12 and key_3_inventory == True:
                        draw_key(light_green, black)

                # Start and goal
                if (maze[row])[col] == 2:
                    pygame.draw.rect(screen, blue, [x, y, tile_size, tile_size])
                if (maze[row])[col] == 3:
                    pygame.draw.rect(screen, red, [x, y, tile_size, tile_size])

                # Keys and Locked Doors
                if (maze[row])[col] == 4 and key_1 == False:
                    draw_key(light_blue, white)
                if (maze[row])[col] == 5 and lock_1 == False:
                    draw_lock(light_blue)

                if (maze[row])[col] == 6 and key_2 == False:
                    draw_key(gold, white)
                if (maze[row])[col] == 7 and lock_2 == False:
                    draw_lock(gold)

                if (maze[row])[col] == 8 and key_3 == False:
                    draw_key(light_green, white)
                if (maze[row])[col] == 9 and lock_3 == False:
                    draw_lock(light_green)

        # Restrict Movement
        if maze[y_proposed][x_proposed] == 0 or maze[y_proposed][x_proposed] == 2 or maze[y_proposed][x_proposed] == 3 or maze[y_proposed][x_proposed] == 4 or (maze[y_proposed][x_proposed] == 5 and key_1 == True) or maze[y_proposed][x_proposed] == 6 or (maze[y_proposed][x_proposed] == 7 and key_2 == True) or maze[y_proposed][x_proposed] == 8 or (maze[y_proposed][x_proposed] == 9 and key_3) == True:
            player_x += x_move * tile_size
            player_y += y_move * tile_size
            x_cord += x_move
            y_cord += y_move

        # Player
        player_location = (player_x, player_y)
        pygame.draw.circle(screen, red, player_location, player_size)

        # Location Updates - Keys, Doors, Finish
        if x_cord == 7 and y_cord == 13:
            key_1 = True
            key_1_inventory = True
        if x_cord == 18 and y_cord == 5 and key_1 == True:
            lock_1 = True
            key_1_inventory = False
            
        if x_cord == 11 and y_cord == 1:
            key_2 = True
            key_2_inventory = True
        if x_cord == 18 and y_cord == 4 and key_2 == True:
            lock_2 = True
            key_2_inventory = False

        if x_cord == 16 and y_cord == 1:
            key_3 = True
            key_3_inventory = True
        if x_cord == 18 and y_cord == 2 and key_3 == True:
            lock_3 = True
            key_3_inventory = False
            
        # Stage Complete
        if x_cord == 18 and y_cord == 1:
            level_1 = False
            finish_level_1 = True

        # Delay for movement
        time.sleep(0.1)

    # Stage 1 Finish Screen
    elif finish_level_1 == True:
        screen.fill(black)
        draw_stars()
        draw_text("YAY!!", 25, (WIDTH//2,HEIGHT//2 - 60), white)
        draw_text("You Completed the Maze", 25, (WIDTH//2,HEIGHT//2), white)
        draw_text("Press ENTER to continue", 25, (WIDTH//2,HEIGHT//2 + 60), white)

    elif start_level_2 == True:
        screen.fill((20, 20, 20)) 
        
        draw_text ("Welcome to Level 2:", 25, (WIDTH//2,HEIGHT//2 - 60), "white")
        draw_text ("Incoming Meteorites", 25, (WIDTH//2,HEIGHT//2 - 30), "white")
        draw_text("Press ENTER", 25, (WIDTH//2,HEIGHT//2 + 60), "white")
        draw_text("to continue", 25, (WIDTH//2,HEIGHT//2 + 90), "white")

        #Draw stars in the background

        draw_stars()
            
        # Astronaut Intro
        draw_astronaut(0,0)

        #Draw Meteorite (big)
        pygame.draw.circle(screen, (77, 78, 79), (660, 0), 200)
        pygame.draw.circle(screen, (90, 90, 90), (660, 0), 200, 5)

    elif level_2 == True:
        #background
        screen.fill((20, 20, 20))
        # Draw stars
        draw_stars()
        #Draw meteorites and change speed and location

        for n in range(len(meteorites)):
            pygame.draw.circle(screen, (77, 78, 79),
                            (meteorites[n][0], meteorites[n][1]),
                            meteorites[n][2])
            #Outline of the meteorites
            pygame.draw.circle(screen, (90, 90, 90),
                            (meteorites[n][0], meteorites[n][1]),
                            meteorites[n][2], 2)

            meteorites[n][0] += meteorites[n][3]
            meteorites[n][1] += meteorites[n][4]

            if meteorites[n][0] + meteorites[n][2] > WIDTH + meteorite_diameter:
                meteorites[n][0] = 0

            elif meteorites[n][1] + meteorites[n][2] > HEIGHT + meteorite_diameter:
                meteorites[n][1] = 0

        draw_text(f"{score}", 25, (30,20), white)

        if score == 20:
            level_2 = False
            finish_level_2 = True


    elif finish_level_2 == True:
        screen.fill((20, 20, 20)) 
        
        draw_text ("Congratulations!", 25, (WIDTH//2,HEIGHT//2 - 60), "white")
        draw_text ("You have completed Level 2", 25, (WIDTH//2,HEIGHT//2 - 30), "white")
        draw_text("Press ENTER", 25, (WIDTH//2,HEIGHT//2 + 60), "white")
        draw_text("to continue", 25, (WIDTH//2,HEIGHT//2 + 90), "white")

        #Draw stars in the background
        draw_stars()
            
        # Astronaut Intro
        draw_astronaut(0,0)

    elif start_level_3 == True:
        screen.fill((0, 0, 42))
        # Stars
        draw_stars()

        # Text
        draw_text("Help the Astronaut clean up outer space!", 25, (WIDTH/2,HEIGHT/2 - 60), white)
        draw_text("Drag and drop each box into its corresponding colour", 20, (WIDTH/2,HEIGHT/2), white)
        draw_text("Press ENTER to continue", 25, (WIDTH/2,HEIGHT/2 + 60), (185, 235, 255))

        # Astronaut
        draw_astronaut(190,70)

    elif level_3 == True:
        # GAME STATE UPDATES
        # The center of the box is at the mouse location when dragging is on
        if box1_dragging == True:
            box1.center = pygame.mouse.get_pos()
        if box2_dragging == True:
            box2.center = pygame.mouse.get_pos()
        if box3_dragging == True:
            box3.center = pygame.mouse.get_pos()
        if box4_dragging == True:
            box4.center = pygame.mouse.get_pos()
        if box5_dragging == True:
            box5.center = pygame.mouse.get_pos()
        if box6_dragging == True:
            box6.center = pygame.mouse.get_pos()
        if box7_dragging == True:
            box7.center = pygame.mouse.get_pos()
        if box8_dragging == True:
            box8.center = pygame.mouse.get_pos()

        # Win Condition
        if box1_dragging == False and inventory_slot1.colliderect(box1) and box2_dragging == False and inventory_slot2.colliderect(box2) and box3_dragging == False and inventory_slot3.colliderect(box3) and box4_dragging == False and inventory_slot4.colliderect(box4) and box5_dragging == False and inventory_slot5.colliderect(box5) and box6_dragging == False and inventory_slot6.colliderect(box6) and box7_dragging == False and inventory_slot7.colliderect(box7) and box8_dragging == False and inventory_slot8.colliderect(box8):
            level_3 = False
            end_screen = True
            #ROCKET
            rocket_x = 270
            rocket_y = HEIGHT + 80
            rocket_width = 100
            rocket_height = 200
            rocket_bottom_height = 50
            flame_height = 80
    
        # DRAWING
        screen.fill((0, 0, 42))
        
        # Stars
        draw_stars()
        
        # Inventory
        draw_inventory((181, 232, 144), inventory_slot1)
        draw_inventory((255, 122, 133), inventory_slot2)
        draw_inventory((105, 187, 255), inventory_slot3)
        draw_inventory((255, 214, 138), inventory_slot4)
        draw_inventory((228, 138, 255), inventory_slot5)
        draw_inventory((102, 217, 232), inventory_slot6)
        draw_inventory((207, 215, 230), inventory_slot7)
        draw_inventory((239, 114, 21), inventory_slot8)

        # Boxes
        def draw_box(colour, box_number):
            pygame.draw.rect(screen, colour, box_number)

        draw_box((181, 232, 144), box1)
        draw_box((255, 122, 133), box2)
        draw_box((105, 187, 255), box3)
        draw_box((255, 214, 138), box4)
        draw_box((228, 138, 255), box5)
        draw_box((102, 217, 232), box6)
        draw_box((207, 215, 230), box7)
        draw_box((239, 114, 21), box8)


    elif end_screen == True:
        rocket_y -= 6
        
        # DRAWING
        screen.fill((0, 0, 42))  # always the first drawing command

        # End Screen
        # STARS
        draw_stars()
        
        # ROCKET
        #--Side triangles--
        pygame.draw.polygon(screen, (255, 0, 0), [(rocket_x, rocket_y + 50), (rocket_x, rocket_y + 150), (rocket_x - 50, rocket_y + 150)])
        pygame.draw.polygon(screen, (255, 0, 0), [(rocket_x + rocket_width, rocket_y + 50), (rocket_x + rocket_width, rocket_y + 150), (rocket_x + rocket_width + 50, rocket_y + 150)])
        #--Body--
        pygame.draw.rect(screen, (239, 239, 239), (rocket_x, rocket_y, rocket_width, rocket_height))
        pygame.draw.polygon(screen, (153, 0, 0), [(rocket_x, rocket_y), (rocket_x + rocket_width, rocket_y), (rocket_x + (rocket_width/2), rocket_y - 80)])
        #--Bottom--
        pygame.draw.polygon(screen, (153, 0, 0), [(rocket_x, rocket_y + rocket_height), (rocket_x + rocket_width, rocket_y + rocket_height), (rocket_x + rocket_width + 30, rocket_y + rocket_height + rocket_bottom_height), (rocket_x - 30, rocket_y + rocket_height + rocket_bottom_height)])
        #--Window--
        pygame.draw.circle(screen, (207, 226, 243), (rocket_x + rocket_width/2, rocket_y + 80), 30)
        pygame.draw.circle(screen, (111, 168, 220), (rocket_x + rocket_width/2, rocket_y + 80), 30, 30 > 1)
        #--Flame--
        #flame_height = 80
        flame_y = rocket_y + rocket_height + rocket_bottom_height + 10

        pygame.draw.polygon(screen, (255, 0, 0), [(rocket_x, flame_y), (rocket_x + rocket_width, flame_y), (rocket_x + rocket_width/2, flame_y + flame_height)])
        pygame.draw.polygon(screen, (255, 153, 0), [(rocket_x + 15, flame_y), (rocket_x + rocket_width - 15, flame_y), (rocket_x + rocket_width/2, flame_y + flame_height - 15)])
        pygame.draw.polygon(screen, (255, 255, 0), [(rocket_x + 30, flame_y), (rocket_x + rocket_width - 30, flame_y), (rocket_x + rocket_width/2, flame_y + flame_height - 30)])

        # TEXT
        draw_text("You beat the game.", 30, (WIDTH/2, HEIGHT/2 - 40), (255, 229, 180))
        draw_text("GREAT WORK!", 40, (WIDTH/2, HEIGHT/2 + 40), (185, 235, 255))
    


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    #---------------------------
pygame.quit()
