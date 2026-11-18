import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

player = pygame.Rect(180, 500, 40, 80)
obstacles = []
score = 0
game_over = False
last_spawn = 0

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    player.x = max(50, player.x - 10)
                elif event.key == pygame.K_RIGHT:
                    player.x = min(310, player.x + 10)

            if event.key == pygame.K_r and game_over:
                player.x = 180
                obstacles.clear()
                score = 0
                game_over = False
                last_spawn = pygame.time.get_ticks()

    if not game_over:
        now = pygame.time.get_ticks()

        if now - last_spawn > 1000:
            x = random.randint(50, 310)
            obstacles.append(pygame.Rect(x, 0, 40, 80))
            last_spawn = now

        for obs in obstacles[:]:
            obs.y += 5

            if player.colliderect(obs):
                game_over = True
            elif obs.top >= 600:
                obstacles.remove(obs)
                score += 1

    screen.fill((0, 150, 0))
    pygame.draw.rect(screen, (50, 50, 50), (50, 0, 300, 600))

    for y in range(0, 600, 100):
        pygame.draw.rect(screen, (255, 255, 255), (195, y, 10, 50))

    pygame.draw.rect(screen, (0, 0, 255), player)

    for obs in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obs)

    screen.blit(font.render("Score: " + str(score), True, (255, 255, 255)), (10, 10))

    if game_over:
        screen.blit(font.render("GAME OVER", True, (255, 255, 0)), (130, 260))
        screen.blit(font.render("Press R to Restart", True, (255, 255, 255)), (100, 300))

    pygame.display.update()

pygame.quit()
