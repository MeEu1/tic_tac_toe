import pygame
from pdb import line_prefix
from prop import *

pygame.init()
screen = pygame.display.set_mode((600, 600))

x_img = pygame.image.load('images/x.png')
o_img = pygame.image.load('images/o.png')

player_round = 1 #1 - P1; 2 - P2
player_color = (255, 0, 0) #red if P1 and blue if P2

line_color = (0, 0, 0)

spaces = Prop()

game_font = pygame.font.Font('font/ShareTechMono-Regular.ttf', 20)
won_font = pygame.font.Font('font/ShareTechMono-Regular.ttf', 40)
restart_font = pygame.font.Font('font/ShareTechMono-Regular.ttf', 15)

game_spaces = [pygame.Rect(0, 0, 200, 200), pygame.Rect(200, 0, 200, 200), pygame.Rect(400, 0, 200, 200), #fist row squares
 pygame.Rect(0, 200, 200, 200), pygame.Rect(200, 200, 200, 200), pygame.Rect(400, 200, 200, 200), #second row squares
 pygame.Rect(0, 400, 200, 200), pygame.Rect(200, 400, 200, 200), pygame.Rect(400, 400, 200, 200)] #last row squares
 #0 - x; 1 - y; 2 - width/height

game_board_index = 0
game_spaces_index = 0

canRestart = False

running = True
while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            for game_space in game_spaces:
                if game_space.collidepoint(mouse_x, mouse_y):
                    spaces.board[game_spaces.index(game_space)] = True #spaces.board and game_spaces have the same length
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and canRestart:
                spaces.restart()
                canRestart = False

    pygame.draw.line(screen, line_color, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), 5)
    #vertical lines

    pygame.draw.line(screen, line_color, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), 5)
    #horizontal lines

    if not spaces.is_aligned():
        for i in range(len(spaces.board)):
            if spaces.board[i] == True:
                if i <= 2:
                    game_board_index = 0
                elif i >= 3 and i <= 5:
                    game_board_index = 1
                elif i >= 6 and i <= 8:
                    game_board_index = 2
                if spaces.game[game_board_index][i % 3] == None:
                    if player_round == 1 and spaces.game[game_board_index][i % 3] == None:
                        spaces.game[game_board_index][i % 3] = x_img
                    elif player_round == 2 and spaces.game[game_board_index][i % 3] == None:
                        spaces.game[game_board_index][i % 3] = o_img
                    player_round = 1 if player_round == 2 else 2

        for i in range(len(spaces.game)):
            for j in range(len(spaces.game[i])):
                if spaces.game[i][j] != None:
                    if i == 0:
                        game_spaces_index = i + j
                    elif i == 1:
                        game_spaces_index = i + j + 2
                    elif i == 2:
                        game_spaces_index = i + j + 4

                    screen.blit(spaces.game[i][j], (game_spaces[game_spaces_index].x, game_spaces[game_spaces_index].y))        

        player_round_text = game_font.render(f'Player {player_round}', False, (0, 0, 0))
        screen.blit(player_round_text, (500, 10))    
    else:
        canRestart = True
        won_text = won_font.render(f'Player {player_round} won!', False, (0, 255, 0))
        restart_text = restart_font.render('For restarting press R', False, (120, 120, 120))

        screen.blit(won_text, (150, 280))
        screen.blit(restart_text, (150, 330))

    pygame.display.update()