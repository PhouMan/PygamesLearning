import pygame
from sys import exit

def display_score():
    time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"Score: {time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)


pygame.init()

# Creates the window and window caption name
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game Window")

# Clock Object
clock = pygame.time.Clock()

# the font
test_font = pygame.font.Font('Assets/Pixeltype.ttf', 50)

game_active = False
start_time = 0

# Surfaces
# Note: Use .convert() for better optimization. .convert_alpha() for pngs with transparent parts
sky_surface = pygame.image.load('Assets/Sprites/Sky.png').convert()

ground_surface = pygame.image.load('Assets/Sprites/ground.png').convert()


# score_surface = test_font.render("Score: 0", False, "black")
# score_rect = score_surface.get_rect(topleft=(10,10))

snail_surface = pygame.image.load('Assets/Sprites/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))


player_surface = pygame.image.load('Assets/Sprites/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft=(80, 300))
player_gravity = 0

#Intro
player_stand = pygame.image.load('Assets/Sprites/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))

while True:
    # Checks for if the user closes the window, if so quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity -= 20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        # the background images and their positions
        screen.blit(sky_surface,(0, 0))
        screen.blit(ground_surface, (0, 300))

        display_score()
        # pygame.draw.rect(screen, '#FFF44F', score_rect)
        # pygame.draw.rect(screen, '#FFF44F', score_rect, 10)
        # screen.blit(score_surface, score_rect)

        # Snail movement
        if snail_rect.right <= 0:
            snail_rect.left = 800

        snail_rect.x -= 2
        screen.blit(snail_surface, snail_rect)

        # Player movement
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        # Snail Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)


    # Updates the display surface at screen
    pygame.display.update()

    # Caps the while loop at 60 ticks per second
    clock.tick(60)



