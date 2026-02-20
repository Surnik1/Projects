import pygame
import sys
from random import randint,shuffle
pygame.init()
pygame.mixer.init()
h,w = 600,400
icon = pygame.image.load('DINO_ICON.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((h,w))
pygame.display.set_caption("Dino")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
#модельки
#моделька дино
dino = pygame.image.load("DINO_STAY.png")
dino_stay = pygame.transform.scale(dino, (50, 50))
dino_pos = [50, 350]
dino_size = [50, 50]
# моделька кактуса
dino_run = [pygame.image.load("DINO_RUNNING1.png"), pygame.image.load("DINO_RUNNING2.png")]
dino_run = [pygame.transform.scale(img, (50,50)) for img in dino_run]
dino_cac = [pygame.image.load(f"DINO_CAC{i}.png") for i in range(1,6)]
cac1, cac2, cac3, cac4, cac5 = [pygame.transform.scale(img, (randint(25,40),50)) for img in dino_cac]
#модель смерти
dino_dead = pygame.image.load("DINO_DEAD.png")
dino_dead = pygame.transform.scale(dino_dead, (50, 50))
#моделька дороги
ground = pygame.image.load("DINO_PATH.png")
ground = pygame.transform.scale(ground, (600, 100))
ground_width = ground.get_width()
x1 = 0
x2 = ground_width

speed = 5
# кактуcы
dist = 600
cac_width = 600 * 5
c1, c2, c3, c4, c5 = [i * dist - 200 for i in range(1,6)]
#гравити
gravity = 0.9
on_ground = True
jump_power = -17
velocity_y = 0
#Музыка
playlist = ["1.mp3", "2.mp3", "3.mp3"]
shuffle(playlist)  # Перемешали один раз при запуске
current_track_index = 0

def play_next():
    global current_track_index
    pygame.mixer.music.load(playlist[current_track_index])
    pygame.mixer.music.play()
    current_track_index += 1
    if current_track_index >= len(playlist):
        shuffle(playlist)
        current_track_index = 0
play_next()
pygame.mixer.music.set_volume(0.2)
jump_sound = pygame.mixer.Sound("jump.mp3")
death_sound = pygame.mixer.Sound("death.mp3")
#мигалка
blink_active = False      
blink_timer = 0            
blink_interval = 200     
blink_count = 0           
blink_max = 6             
text_visible = True 

font = pygame.font.Font(None, 30)#тексст
st = pygame.font.Font('PressStart2P-Regular.ttf', 15)#тексст
dead = False
#очки
cnt = 0
run = False
score = 0
best_score = 0
count_jump = 0
#restard
def restart():
    
    
    global speed, cac_width, c1, c2, c3, c4, c5, cnt, run, score, dead, dino, dino_pos,on_ground,count_jump
    
    speed = 5
    cac_width = dist * 5
    c1,c2,c3,c4,c5 = [i * dist - 200 for i in range(1,6)]
    cnt = 0
    run = False
    score = 0
    count_jump = 0
    dead = False
    dino = dino_stay
    dino_pos = [50, 350]
    on_ground = False
def fill():
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, h, w))
    screen.blit(ground, (x1, 300))
    screen.blit(ground, (x2, 300))
    screen.blit(cac1,(c1, 290))
    screen.blit(cac2,(c2, 290))
    screen.blit(cac3,(c3, 290))
    screen.blit(cac4,(c4, 290))
    screen.blit(cac5,(c5, 290))
    screen.blit(name, (dino_pos[0], dino_pos[1] -20))
    if text_visible:
        screen.blit(text_score, (10, 10))
    screen.blit(text_best_score, (10, 30))
    screen.blit(jumps, (10, 50))
    
    screen.blit(dino, (dino_pos[0], dino_pos[1]))
start = True
death_play = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    #система прыжка
    velocity_y += gravity
    dino_pos[1] += velocity_y
    
    if not pygame.mixer.music.get_busy():
        play_next()
    if (keys[pygame.K_UP] or pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE] or keys[pygame.K_w])   and on_ground :
        dino_pos[1] -= 5
        velocity_y = jump_power
        count_jump += 1
        on_ground = False
        run = True
        start = False
        jump_sound.play()
    if keys[pygame.K_r] and not run:
        if count_jump != 0:
            print(f'You jumped {count_jump} times.')
        death_play = True
        restart()
    #если на земле
    if dino_pos[1] >= 300 and not dead:
        velocity_y = 0
        on_ground = True
    #чтоб не упал под карту
    if dino_pos[1] > 300:
        dino_pos[1] = 300
     
    #поз кактусов
    cac_pos = [c1, c2, c3, c4, c5]
    #поз дино
    player = pygame.Rect(*dino_pos, *dino_size)
    # есть столк
    enemies = [pygame.Rect(i, 290, 20, 40) for i in cac_pos if 0 < i < 400]
    for enemy in enemies:
        if player.colliderect(enemy):   
            run = False
            dead = True
            if death_play:
                death_sound.play()
                death_play = False
     
        
    if run:
        #дорожка идущяя
        x1 -= speed
        x2 -= speed
        if x1 <= -ground_width:
            x1 = x2 + ground_width
        
        if x2 <= -ground_width:
            x2 = x1 + ground_width
            
        #моделька когда идет
        if on_ground and cnt % 5 == 0:
            if dino == dino_stay or dino == dino_run[1]:
                dino = dino_run[0]
            else:
                dino = dino_run[1]
        #кактусы двигающие
        c1 -= speed
        c2 -= speed
        c3 -= speed
        c4 -= speed
        c5 -= speed
        if c1 <= -cac_width + dist:
            c1 += cac_width
        if c2 <= -cac_width + dist:
            c2 +=  cac_width
        if c3 <= -cac_width + dist:
            c3 +=  cac_width
        if c4 <= -cac_width + dist:
            c4 +=  cac_width
        if c5 <= -cac_width + dist:
            c5 += cac_width        
        cnt += 1# очки
        if cnt % 4 == 0:
            score += 1
        #моделька если в воздухе
        if not on_ground:
            dino = dino_stay
    if not run:
        dino = dino_stay
        
    if score %400 == 0 and score != 0:
    
        speed += 0.1
    if dead:
        dino = dino_dead
        
    #мигание счетчика
    if score %100 == 3 and score != 0 and not blink_active:
        blink_active = True
        blink_timer = pygame.time.get_ticks()
        blink_count = 0
        text_visible = True
    if blink_active:
        now = pygame.time.get_ticks()

        if now - blink_timer >= blink_interval:
            blink_timer = now
            text_visible = not text_visible 
            blink_count += 1

            if blink_count >= blink_max:
                blink_active = False
                text_visible = True
    
    text_score = font.render(f"Score : {score:,}", True, (0, 0, 0))
    jumps = font.render(f"Jumps : {count_jump:,}", True, (0, 0, 0))

    text_best_score = font.render(f"Best score : {best_score:,}", True, (0, 0, 0))
    if best_score < score and run == False:
        best_score = score
    name = font.render("", True, (0, 0, 0))
    fill()
    if start:
        screen.fill((255,255,255))
        start_text = st.render('For beginning press UP or W or SPACE', True, (0, 0, 0))
        screen.blit(start_text, (h//2 - start_text.get_width() // 2,w//2 - start_text.get_height() // 2))
    if dead:
        screen.fill((255,255,255))
        restart_text = st.render('For restart press R', True, (0, 0, 0))
        screen.blit(restart_text, (h//2 - restart_text.get_width() // 2,w//2 - restart_text.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)