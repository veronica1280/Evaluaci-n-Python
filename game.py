import pygame
import random
import math
import sys
import os

#Inicializamos pygame
pygame.init()

# Establemos el tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Función para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    

asset_background = resource_path('images/fondoMinecraft.webp')
background = pygame.image.load(asset_background)

asset_icon = resource_path('images/ufo.png')
icon = pygame.image.load(asset_icon)

asset_sound = resource_path('images/audio/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

asset_playerimg = resource_path('images/steve.png')
original_playerimg = pygame.image.load(asset_playerimg)
playerimg = pygame.transform.scale(original_playerimg, (60, 60))

asset_bulletimg = resource_path('images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)

asset_over_font = resource_path('images/RAVIE.TTF')
over_font = pygame.font.Font(asset_over_font, 60)  # Reemplaza 'tamaño_del_texto' con el tamaño de fuente deseado

asset_font = resource_path('images/comicbd.ttf')
font = pygame.font.Font(asset_font, 12)  # Reemplaza 'tamaño_del_texto' con el tamaño de fuente deseado

pygame.display.set_caption("Space Invader")

pygame.display.set_icon(icon)

pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

# Posición inicial del jugador
playerX = 370
playerY = 470
playerx_change = 0  
playery_change= 0 

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10  # Número de enemigos

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(no_of_enemies):
    # cargamos enemigo 1
    enemy1_path = resource_path('images/unnamed.png')
    enemy1_img = pygame.image.load(enemy1_path)
    enemy1_img = pygame.transform.scale(enemy1_img, (40, 40))  # Reemplaza 'nuevo_ancho1' y 'nuevo_alto1' con las dimensiones deseadas

    # cargamos enemigo 2 
    enemy2_path = resource_path('images/zombie.jpg')
    enemy2_img = pygame.image.load(enemy2_path)
    enemy2_img = pygame.transform.scale(enemy2_img, (40, 40))  # Reemplaza 'nuevo_ancho2' y 'nuevo_alto2' con las dimensiones deseadas


    enemyimg.append(enemy1_img)
    enemyimg.append(enemy2_img)

    #posición aleatoria del enemigo en X e Y
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))

    #velocidad de movimiento del enemigo en X e Y
    enemyX_change.append(10)
    enemyY_change.append(10)

    #variables para guardar la posion de la bala
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 20
    bullet_state = "ready"
    
# se inicia el juego con puntaje en 0
score = 0

# funcion para mostrar la puntuacion en la pantalla
def show_score():
    score_value = font.render("SCORE " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))

# funcion para dibujar al jugador en la pantalla
def player(x, y):
    screen.blit(playerimg, (x, y))

# funcion para dibujar al enemigo en la pantalla
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

# funcion para disparar la bala
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))
    
# funcion para comprobar si ha habido una colision entre la bala y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# funcion para mostrar el texto de "Game Over" en pantalla
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(
        center=(int(screen_width/2), int(screen_height/2)))
    screen.blit(over_text, text_rect)


# Funcion principal del juego
def gameloop():

    # Declaramos variables globales
    global score
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global collision
    global bullet_state


def gameloop():
    global score
    global playerX
    global playerx_change
    global bulletX
    global bulletY
    global Collision
    global bullet_state
    
    in_game = True
    while in_game:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerx_change = -5
                
                if event.key == pygame.K_RIGHT:
                    playerx_change = 5
                    
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                
            if event.type == pygame.KEYUP:
                    playerx_change = 0
                
        playerX += playerx_change
                
        if playerX <= 0:
            playerX = 0
        
        elif playerX >= 736:
            playerX = 736
            
        for i in range(no_of_enemies):
            if enemyY[i] > 440:
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]
            
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 454
                bullet_state = "ready"
                score += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)
            enemy(enemyX[i], enemyY[i], i)
            
        if bulletY < 0:
            bulletY = 454
            bullet_state = "ready"
            score += 1
        
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        
        player(playerX, playerY)
        show_score()
        
        pygame.display.update()
        
        clock.tick(120)
gameloop()  