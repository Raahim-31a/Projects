import pygame
from Menu_selection import player_get
import csv
Player = player_get
pygame.init()
WIDTH = 1280
HEIGHT = 720
Display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
Display_surface.fill('gray10')
running = True

player1 = pygame.Surface((100, 200))
player1.fill("white")
player1_rect = player1.get_frect(center = (150, 360))

player2 = pygame.Surface((100, 200))
player2.fill("white")
player2_rect = player2.get_frect(center = (WIDTH - 150, 360))
clock = pygame.time.Clock()
ScoreP1 = 0
ScoreP2 = 0
font = pygame.font.Font("pong-score.ttf", 100)
ScoreSurfP1 = font.render(str(ScoreP1), True, "white")
ScorerectP1 = ScoreSurfP1.get_frect(center = (WIDTH/4, 100))
ScoreSurfP2 = font.render(str(ScoreP2), True, "white")
ScorerectP2 = ScoreSurfP1.get_frect(center = (WIDTH/4 * 3, 100))


Selected = True
Pong = pygame.Surface((50,50))
Pong.fill("white")
Pong_rect = Pong.get_frect(center = (WIDTH/2, HEIGHT/2))
Dash_Height = [36 * i for i in range(0, 20, 2)]
fontSel = pygame.font.SysFont("Helvetica",  50)

Dash = pygame.Surface((20, 36))
Dash.fill("white")
Pong_vel = pygame.math.Vector2(-0.5, 0)
pygame.display.set_caption(f"PONG {Player} Player")
while running:
    pygame.display.set_caption(f"PONG {Player} Player")
    dt = clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    KEYS = pygame.key.get_pressed()
    Display_surface.fill('Gray10')
    if KEYS[pygame.K_w] and player1_rect.top > 0:
        player1_rect.top -= 0.5 * dt
    elif KEYS[pygame.K_s] and player1_rect.bottom < HEIGHT:
        player1_rect.bottom += 0.5 * dt
    if KEYS[pygame.K_ESCAPE]:
        running = False
    if Player == 2:
        if KEYS[pygame.K_UP] and player2_rect.top > 0:
            player2_rect.top -= 0.5 * dt
        elif KEYS[pygame.K_DOWN] and player2_rect.bottom < HEIGHT:
            player2_rect.bottom += 0.5 * dt
    elif Player == 1 and ScoreP2 != 10:
        dist = player2_rect.left - Pong_rect.right
        NewY = Pong_rect.center[1] + ((dist/Pong_vel.x) * Pong_vel.y)
        Newy = round(NewY, 0)
        if player2_rect.center[1] > Newy and Pong_vel.x > 0 and player2_rect.top > 0:
            if (player2_rect.bottom - 50) > Newy > (player2_rect.top + 50):
                pass
            else:
                player2_rect.top -= 0.5 * dt
        elif player2_rect.center[1] < Newy and Pong_vel.x > 0 and player2_rect.bottom < 720:
            if (player2_rect.bottom - 50) > Newy > (player2_rect.top + 50):
                pass
            else:
                player2_rect.bottom += 0.5 * dt


    Pong_rect.center += Pong_vel * dt
    if Pong_rect.colliderect(player1_rect) or Pong_rect.colliderect(player2_rect):
        Pong_vel.x *= -1

        if Pong_rect.colliderect(player1_rect):
            Pong_rect.left = player1_rect.right
            H = player1_rect.center[1] - Pong_rect.center[1]
            L = player1_rect.center[0] - Pong_rect.left
            newy = Pong_vel.x * (H/L)
            Pong_vel.y = newy
        elif Pong_rect.colliderect(player2_rect):
            Pong_rect.right = player2_rect.left
            H = player2_rect.center[1] - Pong_rect.center[1]
            L = player2_rect.center[0] - Pong_rect.right
            newy = Pong_vel.x * (H/L)
            Pong_vel.y = newy
    if Pong_rect.top <= 0 or Pong_rect.bottom >= 720:
        Pong_vel.y *= -1
        if Pong_rect.top < 0:
            Pong_rect.top = 0
        elif Pong_rect.bottom > 720:
            Pong_rect.bottom = 720
    if Pong_rect.right >= 1280:
        ScoreP1 += 1
        Pong_vel.y = 0
        Pong_rect.center = (WIDTH/2, HEIGHT/2)
        if ScoreP1 == 10:
            Pong_vel.x = 0
            font1 = pygame.font.SysFont("Helvetica",  150)
            Win = font1.render("PLAYER 1 WINS"
                              "\nPRESS ESC TO EXIT", True, "darkblue", "black")
            Win_rect = Win.get_frect(center = (WIDTH/2, HEIGHT/2))
    if Pong_rect.right <= 0:
        ScoreP2 += 1
        Pong_vel.y = 0
        Pong_rect.center = (WIDTH/2, HEIGHT/2)
        if ScoreP2 == 10:
            Pong_vel.x = 0
            font1 = pygame.font.SysFont("Helvetica",  150)
            Win = font1.render("PLAYER 2 WINS"
                              "\nPRESS ESC TO EXIT", True, "darkblue", "black")
            Win_rect = Win.get_frect(center=(WIDTH / 2, HEIGHT / 2))

    ScoreSurfP1 = font.render(str(ScoreP1), True, "white")
    ScorerectP1 = ScoreSurfP1.get_frect(center=(WIDTH / 4, 100))
    ScoreSurfP2 = font.render(str(ScoreP2), True, "white")
    ScorerectP2 = ScoreSurfP1.get_frect(center=(WIDTH - WIDTH/4, 100))
    for j in range(10):
        Display_surface.blit(Dash, (WIDTH/2 - 10, Dash_Height[j]))
    Display_surface.blit(ScoreSurfP1, ScorerectP1)
    Display_surface.blit(ScoreSurfP2, ScorerectP2)
    Display_surface.blit(Pong, Pong_rect)
    Display_surface.blit(player1, player1_rect)
    Display_surface.blit(player2, player2_rect)
    if ScoreP1 == 10 or ScoreP2 == 10:
        Display_surface.blit(Win, Win_rect)
    pygame.display.update()

pygame.quit()
