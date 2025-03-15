import pygame
import time

# Sprite declaration
playerSprite = pygame.image.load('images/player_image.png')
groundSprite = pygame.image.load('images/ground.png')
rainSprite = pygame.image.load('images/rain.png')

# Initialize pygame
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RainyDay")
pygame.display.set_icon(playerSprite)

# Size the images
playerSprite = pygame.transform.scale(playerSprite, (100, 100))
groundSprite = pygame.transform.scale(groundSprite, (SCREEN_WIDTH, 80))

# Define the objects
player = pygame.Rect(150, 100, playerSprite.get_width(), playerSprite.get_height())
ground = pygame.Rect(0, SCREEN_HEIGHT - groundSprite.get_height(), groundSprite.get_width(), groundSprite.get_height())
rain = pygame.Rect(player.x + 35, player.y + 40, rainSprite.get_width() * 1.5, rainSprite.get_height() * 1.5)

# Define the speed
speed = 2
gravity = 4

# Rain collision tracking
has_collided = False
collision_time = None
reset_delay = 0.25  # seconds after collision before reset

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
run = True
while run:
    current_time = time.time()

    # Fill the background with a color
    screen.fill((200, 200, 255))

    # Always make the rain fall
    rain.y += gravity

    # Check if rain has collided with the ground for the first time
    if not has_collided and rain.bottom >= ground.top:
        has_collided = True
        collision_time = current_time

    # Check if 1 second has passed since collision
    if has_collided and current_time - collision_time >= reset_delay:
        # Reset rain position to player's position
        rain.x = player.x + 35
        rain.y = player.y + 40
        has_collided = False  # Reset collision state

    # Draw sprites (always draw rain regardless of collision)
    screen.blit(rainSprite, rain.topleft)
    screen.blit(playerSprite, player.topleft)
    screen.blit(groundSprite, ground.topleft)

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
        if player.bottom > SCREEN_HEIGHT - 200:
            player.bottom = SCREEN_HEIGHT - 200  # Prevent moving out of the bottom boundary

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