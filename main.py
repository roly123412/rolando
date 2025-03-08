import pygame, sys
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from pygame.draw import circle
from PIL import Image

# Initialize Pygame
pygame.init()

# Set up the display
pygame.display.set_caption('Hello World!')
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
paused = False

#variables for managing
score = 0
score_length = len(str(score))
font = pygame.font.SysFont("Courier New", 150)
text = font.render(str(score), True, (0, 0, 0))
text_center_x = 200
text_rect = text.get_rect(center=(text_center_x, 150))

# shop text
font_shop = pygame.font.SysFont("Courier New", 75)
text_shop = font_shop.render("Shop", True, (0, 0, 0))
text_shop_rect = text.get_rect(center=(160, 75))


# Function to check if mouse click is inside the circle
def distance_function(x, y, h, k, radius):
    distance = (x - h)**2 + (y - k)**2
    return distance <= radius**2


# Colors
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#button coordinates
button_x = 300
button_y = 250
button_rect = pygame.Rect(button_x, button_y, 100, 50)

bbutton_x = 40
bbutton_y = 89
bbutton_rect = pygame.Rect(bbutton_x, bbutton_y, 100, 50)

cbutton_x = 250
cbutton_y = 89
cbutton_rect = pygame.Rect(cbutton_x, cbutton_y, 100, 50)

# Random position for the circle
rx = random.randint(0, 400)
ry = random.randint(0, 300)

# Main game loop
while True:
    screen.fill(WHITE)

    # Draw the circle at a random position (rx, ry)
    if not paused:
        text = font.render(str(score), True, (0, 0, 0))
        screen.blit(text, text_rect)
        pygame.draw.circle(screen, GREY, (rx, ry), 50)
    else:
        #draw buttons for the shop
        screen.blit(text_shop, text_shop_rect)
        pygame.draw.rect(screen, RED, bbutton_rect)
        pygame.draw.rect(screen, GREY, cbutton_rect)
    pygame.draw.rect(screen, RED, button_rect)  #draw button

    # Event handling
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:

            print("Someone clicked somewhere")
            print(event.pos)

            if button_rect.collidepoint(event.pos):
                paused = not paused

            if bbutton_rect.collidepoint(event.pos) and score >= 10:
                score -= 10
                
                

            # Check if the mouse click is inside the circle
            inside_circle = distance_function(event.pos[0], event.pos[1], rx,ry, 50)
            if inside_circle:
                #update score
                score += 1
                text = font.render(str(score), True, (0, 0, 0))
                if len(str(score)) > score_length:
                    score_length += 1
                    text_center_x -= 10
                    text_rect = text.get_rect(center=(text_center_x, 150))
                print("Clicked inside the circle")
                # Move the circle to a new random position after clicking inside it
                rx = random.randint(0, 400)
                ry = random.randint(0, 300)

            else:
                print("Clicked outside the circle")

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)
