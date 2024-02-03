import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rock, Paper, Scissors Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Game Variables
rock = 0
paper = 1
scissors = 2
ai_choice = random.randint(0, 2)
user_choice = None
game_state = 'welcome'  # Could be 'welcome', 'game', or 'result'
font = pygame.font.Font(None, 36)
choices = ["Rock", "Paper", "Scissors"]  # Added this line

def draw_text(text, position, color, font=font):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def reset_game():
    global ai_choice, game_state
    ai_choice = random.randint(0, 2)
    game_state = 'game'

def welcome_screen():
    screen.fill(black)
    draw_text("Rock [r], Paper [p], or Scissors [s] ?", (100, 200), white)
    draw_text("Press the corresponding key to choose.", (80, 240), white)

def game_screen():
    global game_state
    screen.fill(black)
    draw_text(f'You chose {choices[user_choice]}', (50, 100), white)
    draw_text(f'Opponent chose {choices[ai_choice]}', (50, 150), white)
    
    if ai_choice == user_choice:
        draw_text("It's a tie!", (50, 200), blue)
    elif (user_choice == rock and ai_choice == scissors) or \
         (user_choice == scissors and ai_choice == paper) or \
         (user_choice == paper and ai_choice == rock):
        draw_text("You win!", (50, 200), green)
    else:
        draw_text("You lose!", (50, 200), red)
    
    #draw_text("Press any key to play again", (50, 250), white)
    game_state = 'welcome'

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_state == 'welcome':
                if event.key == pygame.K_r:
                    user_choice = rock
                    reset_game()
                elif event.key == pygame.K_p:
                    user_choice = paper
                    reset_game()
                elif event.key == pygame.K_s:
                    user_choice = scissors
                    reset_game()
            elif game_state == 'result':
                reset_game()

    if game_state == 'welcome':
        welcome_screen()
    elif game_state == 'game':
        game_screen()

    pygame.display.flip()
    pygame.time.delay(2000)
