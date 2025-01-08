import pygame
pygame.init()
WIDTH = 1280
HIEGHT = 720
Display_surface_menu = pygame.display.set_mode((WIDTH, HIEGHT))
Display_surface_menu.fill("gray10")
running = True
P1 = pygame.image.load("download.png").convert_alpha()
P1_rect = P1.get_frect(center = (WIDTH/4, HIEGHT/2))
P2 = pygame.image.load("images.png").convert_alpha()
P2_rect = P2.get_frect(center = (WIDTH/4 *3, HIEGHT/2))
font = pygame.font.SysFont("Helvetica", 75)
Player = 1
while running:
    pygame.display.set_caption("MENU")
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_ESCAPE]:
        running = False
    click = pygame.mouse.get_pressed()[0]
    pos = pygame.mouse.get_pos()
    if P1_rect.collidepoint(pos) and click:
        Player = 1
        running = False
    if P2_rect.collidepoint(pos) and click:
        Player = 2
        running = False
    MSG = font.render("SELECT THE NUMBER OF PLAYERS", True, "WHITE")
    MSG_rect = MSG.get_frect(center = (WIDTH/2, HIEGHT/4))
    Display_surface_menu.fill("gray10")
    Display_surface_menu.blit(MSG, MSG_rect)
    Display_surface_menu.blit(P1, P1_rect)
    Display_surface_menu.blit(P2, P2_rect)
    pygame.display.update()

pygame.quit()
player_get = Player