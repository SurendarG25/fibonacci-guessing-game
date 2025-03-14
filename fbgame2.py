import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fibonacci Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Timer and score
timer = 30
score = 0

# Fibonacci sequence
fibonacci = [0, 1]
user_input = ""

# Load and resize background image
background_image = pygame.image.load(r"C:\Users\Pavani\Pictures\gamebackground.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to screen dimensions

# Load background music
pygame.mixer.music.load("C:/Users/Pavani/Music/gardens-stylish-chill-303261.mp3")  # Replace with your music file
pygame.mixer.music.play(-1)  # Loop indefinitely

# Animation variables
animation_frames = 0
animation_text = ""

# Game loop
clock = pygame.time.Clock()
running = True
start_time = time.time()

while running:
    # Draw background image
    screen.blit(background_image, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check user input
                try:
                    guess = int(user_input)
                    if guess == fibonacci[-1] + fibonacci[-2]:
                        # Correct guess
                        fibonacci.append(guess)
                        score += 1
                        timer += 5
                        animation_text = "Correct!"
                        animation_frames = 30
                    else:
                        # Incorrect guess
                        timer -= 2
                        animation_text = "Incorrect!"
                        animation_frames = 30
                except ValueError:
                    # Invalid input
                    animation_text = "Invalid Input!"
                    animation_frames = 30
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Update timer
    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:
        timer -= 1
        start_time = time.time()

    # Check for game over
    if timer <= 0:
        running = False

    # Display last two Fibonacci numbers
    fib_text = f"Last two numbers: {fibonacci[-2]}, {fibonacci[-1]}"
    fib_surface = font.render(fib_text, True, BLACK)
    screen.blit(fib_surface, (50, 50))

    # Display timer
    timer_text = f"Time: {timer}"
    timer_surface = font.render(timer_text, True, BLACK)
    screen.blit(timer_surface, (50, 150))

    # Display score
    score_text = f"Score: {score}"
    score_surface = font.render(score_text, True, BLACK)
    screen.blit(score_surface, (50, 250))

    # Display user input
    input_text = f"Your guess: {user_input}"
    input_surface = small_font.render(input_text, True, BLACK)
    screen.blit(input_surface, (50, 350))

    # Display animation
    if animation_frames > 0:
        animation_surface = font.render(animation_text, True, GREEN if animation_text == "Correct!" else RED)
        screen.blit(animation_surface, (WIDTH // 2 - 100, HEIGHT // 2))
        animation_frames -= 1

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Game over screen
screen.blit(background_image, (0, 0))
game_over_text = font.render("Game Over", True, BLACK)
score_final_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
screen.blit(score_final_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))
pygame.display.flip()

# Stop the music
pygame.mixer.music.stop()

# Wait for a few seconds before quitting
pygame.time.wait(4000)

# Quit Pygame
pygame.quit()
sys.exit()