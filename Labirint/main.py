import pygame
import random
import sys
import os
import time

pygame.init()

# initializam culorile folosite
player_color = (57, 255, 20)
exit_color = (144, 0, 0)
wall_color = (0, 0, 144)
game_background = (0, 144, 144)

text_color = (255, 255, 255)
menu_highlight = (83, 45, 45)
background = (45, 45, 83)

# initializam marimea initiala a peretilor si a coridorului
wall_size = 5
corridor_size = 45 + wall_size

# initializam viteza(FPS) jocului, dificultatea
speed = 60
dificulty = 2
timp = ""

# cream fisierul unde se afla scorulul daca nu exista, iar daca este gol initializam scorulu in el
fscor = open("Scor labirint.txt", 'a')
if os.stat("Scor labirint.txt").st_size == 0:
    fscor.write("Foarte Usor:\n0\nUsor:\n0\nMediu:\n0\nGreu:\n0\nFoarte Greu:\n0\n")
fscor.close()

# initializam marimea jocului
WIDTH = 800 + wall_size
HEIGHT = 600 + wall_size

# initializam marimea jucatorului si a iesiti, si pozitia acestora
player_size = corridor_size - wall_size
player_posx = 0 + wall_size
player_posy = 0 + wall_size
end_size = corridor_size - wall_size
end_posx = corridor_size * (WIDTH // corridor_size - 1) + wall_size
end_posy = corridor_size * (HEIGHT // corridor_size - 1) + wall_size

# intializam screen-ul unde v-om putea vedea ce se intampla in joc
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# initializam conditia de oprire a meniului principal
MENU_OVER = False

# initializam un "clock" pt a controla framerate-ul jocului
clock = pygame.time.Clock()

# punem numele jocului
pygame.display.set_caption('Labirint')

# initializam marimea butoanelor din meniul principal
button_w = 190
button_h = 40

# initializam conditile de aparitie a unor parti din meniul principal
show_dificulty = False
show_instructions = True
show_timer = True
show_scor = True

# initializam fontul folosit de textul din aplicatie
font = pygame.font.SysFont('roboto bold', 40)

# initializam textul folosit de aplicatie
instructions_line1 = font.render('Jucatorul incepe in coltul din stanga sus', True, text_color)
instructions_line2 = font.render('si trebuie sa ajunga la iesirea din coltul', True, text_color)
instructions_line3 = font.render('din dreapta jos a labirintului in cel mai', True, text_color)
instructions_line4 = font.render('scurt timp', True, text_color)
instructions_line5 = font.render('Deplasarea se face cu ajutorul sagetilor', True, text_color)
instructions_line6 = font.render('Puteti sa parasiti labirintul prin apasarea', True, text_color)
instructions_line7 = font.render('iesiri cu mausul(clic dreapta)', True, text_color)

start_text = font.render('Start', True, text_color)

dificulty_text = font.render('Dificultate', True, text_color)
dificulty_very_easy = font.render('Foarte Usor', True, text_color)
dificulty_easy = font.render('Usor', True, text_color)
dificulty_medium = font.render('Mediu', True, text_color)
dificulty_hard = font.render('Greu', True, text_color)
dificulty_very_hard = font.render('Foarte Greu', True, text_color)
dificulty_back = font.render('Inapoi', True, text_color)

timer_text = font.render('Arata timp #', True, text_color)
scor_text1 = font.render('Arata cel mai', True, text_color)
scor_text2 = font.render('bun timp #', True, text_color)
sterge_text = font.render('Sterge  scor', True, text_color)
exit_text = font.render('Iesire', True, text_color)

# initializam matricea folosita in crearea labirintului
MAZE = []


# functia salveaza timpul cel mai mic obtinut de utilizator in fisier
def save_timp():
    global dificulty, timp
    with open("Scor labirint.txt", 'r') as score_file:
        get_all = score_file.readlines()
    score_file.close()
    with open("Scor labirint.txt", 'w') as score_file:
        for i, line in enumerate(get_all, 1):
            if i == dificulty and (timp < line or line == "0\n"):
                score_file.writelines(timp + "\n")
            else:
                score_file.writelines(line)
    score_file.close()


# functia creaza labirintul
def create_maze(show_t):
    for i in range(0, HEIGHT // corridor_size + 1):
        LINE = []
        for j in range(0, WIDTH // corridor_size + 1):
            if i == 0:
                p = 0
            elif j == 0:
                p = 1
            elif show_t and j >= (WIDTH - wall_size - 1.25 * button_w) // corridor_size \
                    and i <= (wall_size + 0.5 * button_h) // corridor_size:
                p = 2
            else:
                p = random.randint(0, 1)
            LINE.append(int(p))
        MAZE.append(LINE)


# functia deseneaza labirintul
def draw_maze():

    h = HEIGHT // corridor_size
    w = WIDTH // corridor_size

    for i in range(1, h):
        for j in range(1, w):
            if MAZE[i][j] == 0:
                pygame.draw.rect(screen, wall_color, (j * corridor_size, i * corridor_size,
                                                      wall_size * (corridor_size // wall_size) + wall_size, wall_size))
            elif MAZE[i][j] == 1:
                pygame.draw.rect(screen, wall_color, (j * corridor_size, i * corridor_size,
                                                      wall_size, wall_size * (corridor_size // wall_size) + wall_size))


# functia afiseaza timpul jucatorului
def show_time(t0):
    global timp
    t = int(time.time() - t0)
    if t < 60:
        time_str = str(t) + " sec"
        time_text = font.render(time_str, True, text_color)
        screen.blit(time_text, (WIDTH - wall_size - 0.75 * button_w, wall_size))
    else:
        secunde = t % 60
        minute = t // 60
        time_str = str(minute) + " min"
        if secunde != 0:
            time_str = time_str + " si " + str(secunde) + " sec"
        time_text = font.render(time_str, True, text_color)
        screen.blit(time_text, (WIDTH - wall_size - 1.25 * button_w, wall_size))
    timp = time_str


# funtia contine jocul propriu zis
def GAME(player_px, player_py, end_px, end_py, show_t):

    # initalizam conditile de miscare
    MOVE_LEFT = False
    MOVE_RIGHT = False
    MOVE_UP = False
    MOVE_DOWN = False
    GAME_OVER = False

    # initializam timpul initial
    t0 = time.time()

    # pornim jocul
    while not GAME_OVER:

        # cautam actiunile facute de utilizator
        for event in pygame.event.get():

            # daca apasam pe x inchidem jocul complet
            if event.type == pygame.QUIT:
                sys.exit()

            # salvam pozitia curenta a mouse-ului, iar daca facem click dreapta unde se afla pozitia iesiri din
            # labirint terminam jocul si ne intoarcem la meniul principal
            mice = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_px < mice[0] < WIDTH and end_py < mice[1] < HEIGHT:
                    GAME_OVER = True

            # facem miscarea cubului controlat de utilizator atat timp cat tasta corespunzatoare e apasata
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    MOVE_LEFT = True
                if event.key == pygame.K_RIGHT:
                    MOVE_RIGHT = True
                if event.key == pygame.K_UP:
                    MOVE_UP = True
                if event.key == pygame.K_DOWN:
                    MOVE_DOWN = True

            # cand ridicam degetul de pe tasta miscarea se opreste
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    MOVE_LEFT = False
                if event.key == pygame.K_RIGHT:
                    MOVE_RIGHT = False
                if event.key == pygame.K_UP:
                    MOVE_UP = False
                if event.key == pygame.K_DOWN:
                    MOVE_DOWN = False

        # verificam daca e posibile miscarea in fiecare directie si daca utilizatorul doreste sa faca deplasarea
        if MOVE_RIGHT \
                and player_px < WIDTH - player_size - wall_size \
                and (MAZE[player_py // corridor_size][(player_px + corridor_size) // corridor_size] != 1
                     or (player_px + player_size) % corridor_size != 0) \
                and player_py % corridor_size == wall_size:
            player_px += 1
        if MOVE_LEFT \
                and player_px > wall_size \
                and (MAZE[player_py // corridor_size][player_px // corridor_size] != 1
                     or player_px % corridor_size != wall_size) \
                and player_py % corridor_size == wall_size:
            player_px -= 1
        if MOVE_UP \
                and player_py > wall_size \
                and (MAZE[player_py // corridor_size][player_px // corridor_size] != 0
                     or player_py % corridor_size != wall_size) \
                and player_px % corridor_size == wall_size:
            player_py -= 1
        if MOVE_DOWN \
                and player_py < HEIGHT - player_size - wall_size \
                and (MAZE[(player_py + corridor_size) // corridor_size][player_px // corridor_size] != 0
                     or (player_py + player_size) % corridor_size != 0) \
                and player_px % corridor_size == wall_size:
            player_py += 1

        # daca cubul controlat de utilizator ajunge la coordonatele iesiri se salveaza timpul jucatorului si se termina
        # jocul revenind la meniul principal
        if (player_px <= end_px + end_size and player_px + player_size >= end_px and player_py == end_py) \
                or (player_py <= end_py + end_size and player_px == end_px and player_py + player_size >= end_py):
            save_timp()
            GAME_OVER = True

        # afisarea la ecran a fundalului, a cubului controlat de jucator, a iesiri si a peretilor labirintului
        screen.fill(game_background)

        pygame.draw.rect(screen, player_color, (player_px, player_py, player_size, player_size))

        pygame.draw.rect(screen, exit_color, (end_px, end_py, end_size, end_size))

        pygame.draw.rect(screen, wall_color, (0, 0, wall_size, HEIGHT))
        pygame.draw.rect(screen, wall_color, (WIDTH - wall_size, 0, wall_size, HEIGHT))
        pygame.draw.rect(screen, wall_color, (0, 0, WIDTH, wall_size))
        pygame.draw.rect(screen, wall_color, (0, HEIGHT - wall_size, WIDTH, wall_size))

        draw_maze()
        if show_t:
            show_time(t0)

        # limita FPS
        clock.tick(speed)

        # updatam imaginea prezentata la ecran
        pygame.display.update()


# meniul principal
while not MENU_OVER:

    # cautam actiunile facute de utilizator
    for ev in pygame.event.get():

        # daca apasam pe x inchidem jocul complet
        if ev.type == pygame.QUIT:
            sys.exit()

        # salvam pozitia curenta a mouse-ului, iar daca facem click dreapta unde se afla pozitia unuia dintre butoane
        # se efectueaza comenzle respective
        mouse = pygame.mouse.get_pos()
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # apasarea butonului Start, incepe jocul de labirint si
            if 0 < mouse[0] < button_w and 0 < mouse[1] < button_h:
                MAZE.clear()
                create_maze(show_timer)
                player_size = corridor_size - wall_size
                player_posx = 0 + wall_size
                player_posy = 0 + wall_size

                end_size = corridor_size - wall_size
                end_posx = corridor_size * (WIDTH // corridor_size - 1) + wall_size
                end_posy = corridor_size * (HEIGHT // corridor_size - 1) + wall_size

                GAME(player_posx, player_posy, end_posx, end_posy, show_timer)

            # butonul de selectare a dificultati, face sa apara butoanele cu dificultatisi  sa dispara instuctiunile
            # jocului sau invers
            if 0 < mouse[0] < button_w and button_h < mouse[1] < button_h * 2 and not show_dificulty:
                show_dificulty = True
                show_instructions = False
            else:
                show_dificulty = False
                show_instructions = True

            # butoanele cu dificultati, schimba dificultatea jocului
            if button_w < mouse[0] < button_w * 2 and button_h < mouse[1] < button_h * 2:
                corridor_size = 45 + wall_size
                dificulty = 2
                show_dificulty = False
                show_instructions = True
            if button_w < mouse[0] < button_w * 2 and button_h * 2 < mouse[1] < button_h * 3:
                corridor_size = 35 + wall_size
                dificulty = 4
                show_dificulty = False
                show_instructions = True
            if button_w < mouse[0] < button_w * 2 and button_h * 3 < mouse[1] < button_h * 4:
                corridor_size = 20 + wall_size
                dificulty = 6
                show_dificulty = False
                show_instructions = True
            if button_w < mouse[0] < button_w * 2 and button_h * 4 < mouse[1] < button_h * 5:
                corridor_size = 15 + wall_size
                dificulty = 8
                show_dificulty = False
                show_instructions = True
            if button_w < mouse[0] < button_w * 2 and button_h * 5 < mouse[1] < button_h * 6:
                corridor_size = 5 + wall_size
                dificulty = 10
                show_dificulty = False
                show_instructions = True

            # butonul inapoi, face sa dispara butoanele cu dificultati si sa apara instructiunile
            if button_w < mouse[0] < button_w * 2 and button_h * 6 < mouse[1] < button_h * 7:
                show_dificulty = False
                show_instructions = True

            # butonul arata timp, shimba starea de aparitie a conometru din coltul din dreapta sus a labirintului
            # conumetrul inital apare acest lucru find marcat prin #
            if 0 <= mouse[0] <= button_w and button_h * 2 <= mouse[1] <= button_h * 3:
                if show_timer:
                    timer_text = font.render('Arata timp', True, text_color)
                    show_timer = False
                else:
                    timer_text = font.render('Arata timp #', True, text_color)
                    show_timer = True

            # butonul arata cel mai bun timp, shimba starea de aparitie highscore-ului din dagina principala
            # highscore-ului inital apare acest lucru find marcat prin #
            if 0 <= mouse[0] <= button_w and button_h * 3 <= mouse[1] <= button_h * 5:
                if show_scor:
                    scor_text2 = font.render('bun timp', True, text_color)
                    show_scor = False
                else:
                    scor_text2 = font.render('bun timp #', True, text_color)
                    show_scor = True

            # butonul sterge scor, sterge highscore-ul salva in fisier
            if 0 <= mouse[0] <= button_w and button_h * 5 <= mouse[1] <= button_h * 6:
                fscor = open("Scor labirint.txt", 'w')
                fscor.write("Foarte Usor:\n0\nUsor:\n0\nMediu:\n0\nGreu:\n0\nFoarte Greu:\n0\n")
                fscor.close()

            # butonul iesire, inchide programul
            if 0 <= mouse[0] <= button_w and button_h * 6 <= mouse[1] <= button_h * 7:
                sys.exit()
        # afisam fundalul
        screen.fill(background)

        # salvam pozitia curenta a mouse-lui, iar daca se afla la coordonatele unuia dintre butoane ii schimbam culoarea
        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[0] <= button_w and 0 <= mouse[1] <= button_h:
            pygame.draw.rect(screen, menu_highlight, [0, 0, button_w, button_h])

        if 0 <= mouse[0] <= button_w and button_h <= mouse[1] <= button_h * 2:
            pygame.draw.rect(screen, menu_highlight, [0, button_h, button_w, button_h])
        if button_w < mouse[0] < button_w * 2 and button_h <= mouse[1] <= button_h * 2 and show_dificulty:
            pygame.draw.rect(screen, menu_highlight, [button_w, button_h, button_w, button_h])
        if button_w < mouse[0] < button_w * 2 and button_h * 2 <= mouse[1] <= button_h * 3 and show_dificulty:
            pygame.draw.rect(screen, menu_highlight, [button_w, button_h * 2, button_w, button_h])
        if button_w < mouse[0] < button_w * 2 and button_h * 3 <= mouse[1] <= button_h * 4 and show_dificulty:
            pygame.draw.rect(screen, menu_highlight, [button_w, button_h * 3, button_w, button_h])
        if button_w < mouse[0] < button_w * 2 and button_h * 4 <= mouse[1] <= button_h * 5 and show_dificulty:
            pygame.draw.rect(screen, menu_highlight, [button_w, button_h * 4, button_w, button_h])
        if button_w < mouse[0] < button_w * 2 and button_h * 5 <= mouse[1] <= button_h * 6 and show_dificulty:
            pygame.draw.rect(screen, menu_highlight, [button_w, button_h * 5, button_w, button_h])
        if button_w < mouse[0] < button_w * 2 and button_h * 6 <= mouse[1] <= button_h * 7 and show_dificulty:
            pygame.draw.rect(screen, menu_highlight, [button_w, button_h * 6, button_w, button_h])

        if 0 <= mouse[0] <= button_w and button_h * 2 <= mouse[1] <= button_h * 3:
            pygame.draw.rect(screen, menu_highlight, [0, button_h * 2, button_w, button_h])

        if 0 <= mouse[0] <= button_w and button_h * 3 <= mouse[1] <= button_h * 5:
            pygame.draw.rect(screen, menu_highlight, [0, button_h * 3, button_w, button_h * 2])

        if 0 <= mouse[0] <= button_w and button_h * 5 <= mouse[1] <= button_h * 6:
            pygame.draw.rect(screen, menu_highlight, [0, button_h * 5, button_w, button_h])

        if 0 <= mouse[0] <= button_w and button_h * 6 <= mouse[1] <= button_h * 7:
            pygame.draw.rect(screen, menu_highlight, [0, button_h * 6, button_w, button_h])

        # afisam textul butoanelor si instructiunile jocului in pozitiile corespunzatoare
        screen.blit(start_text, (0, 0))
        if show_instructions:
            screen.blit(instructions_line1, (button_w + 50, 0))
            screen.blit(instructions_line2, (button_w + 50, button_h))
            screen.blit(instructions_line3, (button_w + 50, button_h * 2))
            screen.blit(instructions_line4, (button_w + 50, button_h * 3))
            screen.blit(instructions_line5, (button_w + 50, button_h * 4))
            screen.blit(instructions_line6, (button_w + 50, button_h * 5))
            screen.blit(instructions_line7, (button_w + 50, button_h * 6))

        screen.blit(dificulty_text, (0, button_h))
        if show_dificulty:
            screen.blit(dificulty_very_easy, (button_w, button_h))
            screen.blit(dificulty_easy, (button_w, button_h * 2))
            screen.blit(dificulty_medium, (button_w, button_h * 3))
            screen.blit(dificulty_hard, (button_w, button_h * 4))
            screen.blit(dificulty_very_hard, (button_w, button_h * 5))
            screen.blit(dificulty_back, (button_w, button_h * 6))

        screen.blit(timer_text, (0, button_h * 2))

        screen.blit(scor_text1, (0, button_h * 3))
        screen.blit(scor_text2, (0, button_h * 4))
        if show_scor:
            with open("Scor labirint.txt", 'r') as f:
                high_score = f.read().splitlines()
                timp_fu1_text = font.render(high_score[0], True, text_color)
                timp_fu2_text = font.render(high_score[1], True, text_color)
                timp_u1_text = font.render(high_score[2], True, text_color)
                timp_u2_text = font.render(high_score[3], True, text_color)
                timp_m1_text = font.render(high_score[4], True, text_color)
                timp_m2_text = font.render(high_score[5], True, text_color)
                timp_g1_text = font.render(high_score[6], True, text_color)
                timp_g2_text = font.render(high_score[7], True, text_color)
                timp_fg1_text = font.render(high_score[8], True, text_color)
                timp_fg2_text = font.render(high_score[9], True, text_color)

                screen.blit(timp_fu1_text, (WIDTH // 2 - button_w, button_h * 9))
                screen.blit(timp_fu2_text, (WIDTH // 2, button_h * 9))
                screen.blit(timp_u1_text, (WIDTH // 2 - button_w, button_h * 10))
                screen.blit(timp_u2_text, (WIDTH // 2, button_h * 10))
                screen.blit(timp_m1_text, (WIDTH // 2 - button_w, button_h * 11))
                screen.blit(timp_m2_text, (WIDTH // 2, button_h * 11))
                screen.blit(timp_g1_text, (WIDTH // 2 - button_w, button_h * 12))
                screen.blit(timp_g2_text, (WIDTH // 2, button_h * 12))
                screen.blit(timp_fg1_text, (WIDTH // 2 - button_w, button_h * 13))
                screen.blit(timp_fg2_text, (WIDTH // 2, button_h * 13))
            f.close()

        screen.blit(sterge_text, (0, button_h * 5))

        screen.blit(exit_text, (0, button_h * 6))

        # updatam imaginea prezentata la ecran
        pygame.display.update()
