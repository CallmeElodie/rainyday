import pygame

# Initialize pygame
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sigma")

# Load the player image (Make sure you have a player_image.png file in the same directory)
player_image = pygame.image.load('images/player_image.png')  # Replace with your image file path

# Resize the image to a smaller size (e.g., 50x50)
player_image = pygame.transform.scale(player_image, (100, 100))

# Define the player object (position and size based on the resized image)
player = pygame.Rect(175, 300, player_image.get_width(), player_image.get_height())

# Define the speed (slower movement using pixels per frame)
speed = 2  # Move 1 pixel per frame, adjust as needed

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
run = True
while run:

    # Fill the background with a color
    screen.fill((200, 200, 255))

    # Draw the resized player image onto the screen at the player's position
    screen.blit(player_image, player.topleft)

    # Get key states
    key = pygame.key.get_pressed()

    # Move the player and check boundaries
    if key[pygame.K_a]:  # Move left
        player.move_ip(-speed, 0)
        if player.left < 0:
            player.left = 0  # Prevent moving out of the left boundary
    if key[pygame.K_d]:  # Move right
        player.move_ip(speed, 0)
        if player.right > SCREEN_WIDTH:
            player.right = SCREEN_WIDTH  # Prevent moving out of the right boundary
    if key[pygame.K_w]:  # Move up
        player.move_ip(0, -speed)
        if player.top < 0:
            player.top = 0  # Prevent moving out of the top boundary
    if key[pygame.K_s]:  # Move down
        player.move_ip(0, speed)
        if player.bottom > SCREEN_HEIGHT:
            player.bottom = SCREEN_HEIGHT  # Prevent moving out of the bottom boundary

    # Sprint
    # Sprint
    if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:  # Check for either left or right shift
        speed = 5  # Sprint speed (5x normal speed)
    else:
        speed = 2  # Normal speed

    # Event handling (e.g., quit event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the screen
    pygame.display.update()

    # Control the frame rate (e.g., 60 frames per second)
    clock.tick(60)

# Quit pygame
pygame.quit()