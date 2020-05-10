import random
import os
import pygame as pg
import sys

pg.init()

######GAME SETTİNGS####

TITLE = "FLYCAPE"
WIDTH = 900
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

######### SCREEN APPEARANCE #######

the_screen = pg.display.set_mode(SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

########### defining colors #############


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (204, 204, 0)
XXXLIGHTPINK = (255, 204, 229)
XXLIGHTPINK = (255, 153, 204)
XLIGHTPINK = (255, 102, 178)
LIGHTPINK = (255, 0, 127)

#######################################GAME FOLDERS ###########################


game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "images")
voice_folder = os.path.join(game_folder, "voices")
ufo_img_folder = os.path.join(image_folder, "ufo_images")
explosion_anim_folder = os.path.join(image_folder, "explosion")
laserbeam_anim_folder = os.path.join(image_folder, "laserbeam")
player_exp_anim_folder = os.path.join(image_folder, "player_explosion")
powerup_img_folder = os.path.join(image_folder, "powerups")
water_exp_anim_folder = os.path.join(image_folder, "water_explosion")
sounds_folder = os.path.join(voice_folder,"sound effects")
score_filename = "score.txt"


##### musics, sounds#######

pg.mixer.music.load(os.path.join(voice_folder, "gameMusic.mp3"))
pg.mixer.music.set_volume(0.2)

gameOver_sound = pg.mixer.Sound(os.path.join(sounds_folder, "game_over_sound.wav"))
####### CRUSH EFFECT OR EXPLOSİONS
ufo_explosion_sound = pg.mixer.Sound(os.path.join(sounds_folder, "ufo_explosion_sound.wav"))
ufo_explosion_sound.set_volume(0.2)
ship_explosion_sound = pg.mixer.Sound(os.path.join(sounds_folder, "ship_explosion_sound.wav"))
ufo_hit_ship_sound = pg.mixer.Sound(os.path.join(sounds_folder, "is_ship_hit_sound.wav"))
freeze_sound = pg.mixer.Sound(os.path.join(sounds_folder, "freeze_sound.wav"))
ufo_hit_ship_sound.set_volume(0.4)
######SHOOT EFFECTS #########

laser_shoot_sound = pg.mixer.Sound(os.path.join(sounds_folder, "laser.wav"))
rocket_shoot_sound = pg.mixer.Sound(os.path.join(sounds_folder, "rocket_sound.wav"))
balloon_shoot_sound = pg.mixer.Sound(os.path.join(sounds_folder, "balloon_shoot_sound.wav"))
laserbeam_shoot_sound = pg.mixer.Sound(os.path.join(sounds_folder, "laserbeam_sound.wav"))
laserbeam_shoot_sound.set_volume(0.4)

##### POWERUP SOUNDS
life_pow_sound = pg.mixer.Sound(os.path.join(sounds_folder, "life_pow.wav"))
shield_pow_sound = pg.mixer.Sound(os.path.join(sounds_folder, "shield_pow.wav"))
speed_pow_sound = pg.mixer.Sound(os.path.join(sounds_folder, "speed_pow_sound.ogg"))
kill_all_sound = pg.mixer.Sound(os.path.join(sounds_folder, "kill_all_pow_sound.wav"))
########################################## IMAGES #################################

background = pg.image.load(os.path.join(image_folder, "background.png"))
#ship image
ship_image = pg.image.load(os.path.join(image_folder, "ship.png")).convert()
ship_image.set_colorkey(WHITE)
little_ship_image = pg.transform.scale(ship_image, (25, 12))

#laser image
lasershoot_image = pg.image.load(os.path.join(image_folder, "laser.png")).convert()
lasershoot_image.set_colorkey(BLACK)

#rocket image
rocket_basic_image = pg.image.load(os.path.join(image_folder, "rocket.png")).convert()
rocket_basic_image.set_colorkey(WHITE)
rocket_image = pg.transform.scale(rocket_basic_image, (30, 30))

#baloon image
blue_balloon_img = pg.image.load(os.path.join(image_folder, "blue_baloon.png")).convert()
blue_balloon_img.set_colorkey(WHITE)


####UFO IMAGE DİC###

ufo_images = {}
ufo_images['xsmall'] = []
ufo_images['small'] = []
ufo_images['medium'] = []
ufo_images['large'] = []
ufo_images['xlarge'] = []

ufo_img_sizes = ['xsmall', 'small', 'medium', 'large', 'xlarge']
for i in range(8):
    filename = "smufo{}.png".format(i)
    img = pg.image.load(os.path.join(ufo_img_folder, filename)).convert()
    img.set_colorkey(WHITE)
    img_xsmall = pg.transform.scale(img, (30, 30))
    img_small = pg.transform.scale(img, (40, 40))
    img_medium = pg.transform.scale(img, (50, 50))
    img_large = pg.transform.scale(img, (60, 60))
    img_xlarge = pg.transform.scale(img, (70, 70))

    ufo_images['xsmall'].append(img_xsmall)
    ufo_images['small'].append(img_small)
    ufo_images['medium'].append(img_medium)
    ufo_images['xlarge'].append(img_xlarge)
    ufo_images['large'].append(img_large)



#######EXPLOSİON ANİMATİON ########


explosion_anim = {}
explosion_anim['sm'] = []
explosion_anim['lrg'] = []
explosion_anim['player'] = []

for i in range(14):
    filename = "explosion{}.png".format(i)
    img = pg.image.load(os.path.join(explosion_anim_folder, filename)).convert()
    img.set_colorkey(WHITE)
    img_small = pg.transform.scale(img, (30, 30))
    explosion_anim['sm'].append(img_small)
    img_large = pg.transform.scale(img, (300, 300))
    explosion_anim['lrg'].append(img_large)


#######DİFFERENT EXPLOSİON ANİMATİON İF SHİP DİE ########
for i in range(10):
    filename = "player_explosion{}.png".format(i)
    img = pg.image.load(os.path.join(player_exp_anim_folder, filename)).convert()
    img.set_colorkey(WHITE)
    img_rect = img.get_rect()
    img_small = pg.transform.scale(img, (int(img_rect.size[0]/3) + 10, int(img_rect.size[1] / 3) + 10))
    explosion_anim['player'].append(img_small)



#######LASERBEAM ANİMATİON  IN DIFFERENT COLORS ########

laserbeam_anim = {}
laserbeam_anim['blue'] = []
laserbeam_anim['orange'] = []
laserbeam_anim['purple'] = []
laserbeam_anim['red'] = []
laserbeam_colors = ['blue', 'purple', 'red']
for i in range(7):
    filename_blue = "bluelaser{}.png".format(i)
    filename_purple = "purplelaser{}.png".format(i)
    filename_red = "redlaser{}.png".format(i)

    img_blue = pg.image.load(os.path.join(laserbeam_anim_folder, filename_blue)).convert()
    img_purple = pg.image.load(os.path.join(laserbeam_anim_folder, filename_purple)).convert()
    img_red = pg.image.load(os.path.join(laserbeam_anim_folder, filename_red)).convert()

    img_blue.set_colorkey(WHITE)
    img_purple.set_colorkey(WHITE)
    img_red.set_colorkey(WHITE)

    laserbeam_anim['blue'].append(img_blue)
    laserbeam_anim['purple'].append(img_purple)
    laserbeam_anim['red'].append(img_red)


#######DİFFERENT POWERUP IMAGES ########


powerup_images = {}
powerup_images['death'] = pg.image.load(os.path.join(powerup_img_folder, "death.png")).convert()
powerup_images['killAll'] = pg.image.load(os.path.join(powerup_img_folder, "killAll.png")).convert()
powerup_images['gun'] = pg.image.load(os.path.join(powerup_img_folder, "gun.png")).convert()
powerup_images['life'] = pg.image.load(os.path.join(powerup_img_folder, "life.png")).convert()
powerup_images['speed'] = pg.image.load(os.path.join(powerup_img_folder, "speed.png")).convert()
powerup_images['shield'] = pg.image.load(os.path.join(powerup_img_folder, "shield.png")).convert()


water_exp_anim = {}
water_exp_anim['sm'] = []
water_exp_anim['lrg'] = []

for i in range(11):
    filename = "{}.png".format(i)
    img = pg.image.load(os.path.join(water_exp_anim_folder, filename)).convert()
    img.set_colorkey(WHITE)
    img_lrg = pg.transform.scale(img, (300, 300))
    img_sm = pg.transform.scale(img, (40, 40))
    water_exp_anim['sm'].append(img_sm)
    water_exp_anim['lrg'].append(img_lrg)



############### MUSİC AND SOUND EFFECTS ##############


###########GLOBAL VARİABLES AND NEEDİNGS #############


constant_xlocation_of_ship = 20


################ DRAW FUNCTİONS #######################


def draw_bar(screen, x_coordinate, y_coordinate, value, bar_type):  #to draw shield
    if value < 0:
        value = 0
    elif value > 100:
        value = 100
    bar_length = 100
    bar_height = 10
    fill = int(value / 100 * bar_length)
    outline_rect = pg.Rect(x_coordinate, y_coordinate, bar_length, bar_height)
    filler_rect = pg.Rect(x_coordinate, y_coordinate, fill, bar_height)
    pg.draw.rect(screen, WHITE, outline_rect, 3)

    if bar_type == 'shield':
        if value > 60:
            pg.draw.rect(screen, GREEN, filler_rect)

        elif value > 30:
            pg.draw.rect(screen, YELLOW, filler_rect)

        elif value < 30:
            pg.draw.rect(screen, RED, filler_rect)

    if bar_type == 'spell':

        if value <= 33:
            pg.draw.rect(screen, XXXLIGHTPINK, filler_rect)

        elif value <= 66:
            pg.draw.rect(screen, XXLIGHTPINK, filler_rect)

        elif value <= 99:
            pg.draw.rect(screen, XLIGHTPINK, filler_rect)

        elif value == 100:
            pg.draw.rect(screen, LIGHTPINK, filler_rect)


def draw_lives(screen, x_coor, y_coor, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x_coor + (30 * i)
        img_rect.y = y_coor
        screen.blit(img, img_rect)



################ CLASSES #######################


class Ship(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_image
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = constant_xlocation_of_ship
        self.rect.y = int(HEIGHT/2)
        self.shield = 100
        self.spell_power = 0
        self.lives = 3
        self.radius = int(self.rect.width/2)
        self.hidden = False
        self.hidden_timer = pg.time.get_ticks()#when ship hidden

    def update(self, *args):
        #unhide if the ship is hidden
        if self.hidden and pg.time.get_ticks() - self.hidden_timer > 1000:
            self.hidden = False
            self.rect.x = constant_xlocation_of_ship
            self.rect.y = int(HEIGHT / 2)

        up, down = args
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + self.rect.size[1] > HEIGHT:
            self.rect.y = HEIGHT - self.rect.size[1]
        if up:
            self.rect.y -= 5
        if down:
            self.rect.y += 5
        if self.spell_power > 100:
            self.spell_power = 100

    def shoot(self, shoot_type):
        if shoot_type == 'laser':
            laser = Laser(self.rect.size[0], self.rect.size[1], self.rect.y)
            laser_shoot_sound.play()
            all_sprites.add(laser)
            laser_sprites.add(laser)

        elif shoot_type == 'rocket':
            rocket = Rocket(self.rect.size[0], self.rect.size[1], self.rect.y)
            rocket_shoot_sound.play()
            all_sprites.add(rocket)
            rocket_sprites.add(rocket)

        elif shoot_type == 'laserbeam':
            laserbeam = Laserbeam(self.rect.size[0], self.rect.size[1], self.rect.y)
            laserbeam_shoot_sound.play()
            all_sprites.add(laserbeam)
            laserbeam_sprites.add(laserbeam)


        elif shoot_type == 'balloon':
            baloon = WaterBalloon(self.rect.size[0], self.rect.size[1], self.rect.y)
            balloon_shoot_sound.play()
            all_sprites.add(baloon)
            baloon_sprites.add(baloon)


    def hide(self):
        self.hidden = True
        self.hidden_timer = pg.time.get_ticks()
        self.rect.center = (-200, int(HEIGHT / 2))


class Laser(pg.sprite.Sprite):
    def __init__(self, ship_width, ship_height, ship_ycoordinate):
        super().__init__()
        self.image = lasershoot_image
        self.rect = self.image.get_rect()
        self.rect.x = constant_xlocation_of_ship + ship_width
        self.rect.y = ship_ycoordinate + int(ship_height / 2)
        self.speed_x = 10
        self.radius = int((self.rect.size[0] * 0.8) / 2)

    def update(self, *args):
        if self.rect.x > WIDTH:
            self.kill()
        self.rect.x += self.speed_x


class Powerup(pg.sprite.Sprite):
    def __init__(self, ufo):
        super().__init__()
        self.type = random.choice(['death', 'gun', 'killAll', 'life', 'shield', 'speed'])
        self.image = powerup_images[self.type]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.center = ufo.rect.center
        self.speed_x = int(ufo.speed_x / -3)
        self.speed_y = int(ufo.speed_y / -3)
        self.radius = int((self.rect.size[0] * 0.8) / 2)

    def update(self, *args):
        if self.rect.x > WIDTH:
            self.kill()
        if self.rect.y < 0:
            self.rect.y = 0
            self.speed_y = -self.speed_y
        if self.rect.y + self.rect.size[1] > HEIGHT:
            self.rect.y = HEIGHT - self.rect.size[1]
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Rocket(pg.sprite.Sprite):
    def __init__(self, ship_width, ship_height, ship_ycoordinate):
        super().__init__()
        self.image = rocket_image
        self.rect = self.image.get_rect()
        self.rect.x = constant_xlocation_of_ship + ship_width
        self.rect.y = ship_ycoordinate + int(ship_height / 2)
        self.speed_x = 3

    def update(self, *args):
        if self.rect.x > WIDTH:
            self.kill()
        self.rect.x += self.speed_x


class Ufo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.choice = random.choice(ufo_img_sizes)
        self.image = random.choice(ufo_images[self.choice])
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        self.rect.x = random.randrange(WIDTH+70, WIDTH + 200)
        self.speed_x = random.randrange(3, 12)
        self.speed_y = random.randrange(-2, 2)
        self.radius = 20
        pg.draw.circle(self.image, GREEN, self.rect.center, self.radius)
        self.frozen = False
        self.frozen_time = pg.time.get_ticks()

    def update(self, *args):
        if self.frozen:
            if pg.time.get_ticks() - self.frozen_time >= 3000:
                self.frozen = False
        if not self.frozen:
            self.rect.x -= self.speed_x
            self.rect.y += self.speed_y
        if self.rect.x + self.rect.size[0] <= 0:
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.rect.x = random.randrange(WIDTH + 70, WIDTH + 100)
        if self.rect.y + self.rect.size[1] <= 0:
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.rect.x = random.randrange(WIDTH + 70, WIDTH + 100)

    def freeze(self):
        self.frozen = True
        self.frozen_time = pg.time.get_ticks()


class Explosion(pg.sprite.Sprite):
    def __init__(self, center, choice='sm'):
        super().__init__()
        self.choice = choice
        self.image = explosion_anim[self.choice][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pg.time.get_ticks()
        self.frame = 0
        self.frame_rate = 75

    def update(self, *args):
        now = pg.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.choice]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.choice][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class WaterBalloon(pg.sprite.Sprite):
    def __init__(self, ship_width, ship_height, ship_ycoordinate):
        super().__init__()
        self.image = blue_balloon_img
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = constant_xlocation_of_ship + ship_width
        self.rect.y = ship_ycoordinate + int(ship_height / 2)
        self.speed_x = 3
        self.rotate_angle = 0
        self.rotateSpeed = random.randrange(-20, 20)
        self.last_update = pg.time.get_ticks()

    def update(self, *args):
        self.rotate()
        if self.rect.x > WIDTH:
            self.kill()
        self.rect.x += self.speed_x

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.rotate_angle = (self.rotate_angle + self.rotateSpeed) % 360  #getting the rotate angle
            new_img = pg.transform.rotate(self.original_image, self.rotate_angle)
            old_center = self.rect.center
            self.image = new_img
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class WaterExplosion(pg.sprite.Sprite):
    def __init__(self, center, choice='sm'):
        super().__init__()
        self.choice = choice
        self.image = water_exp_anim[self.choice][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pg.time.get_ticks()
        self.frame = 0
        self.frame_rate = 75

    def update(self, *args):
        now = pg.time.get_ticks()

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(water_exp_anim[self.choice]):
                self.kill()
            else:
                center = self.rect.center
                self.image = water_exp_anim[self.choice][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Laserbeam(pg.sprite.Sprite):
    def __init__(self, ship_width, ship_height, ship_ycoordinate):
        super().__init__()
        self.choice = random.choice(laserbeam_colors)
        self.image = laserbeam_anim[self.choice][0]
        self.rect = self.image.get_rect()
        self.rect.x = constant_xlocation_of_ship + ship_width
        self.rect.y = ship_ycoordinate
        self.frame = 0
        self.frame_rate = 50
        self.last_update = pg.time.get_ticks()

    def update(self, *args):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(laserbeam_anim[self.choice]):
                self.kill()
            else:
                x = self.rect.x
                y = self.rect.y
                self.image = laserbeam_anim[self.choice][self.frame]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


##################### FUNCTİONS ############################




###########SHİELD COORDİNATES #################

ship_shieldbar_x = 5
ship_shieldbar_y = 5

ship_spellpowerbar_x = 5
ship_spellpowerbar_y = 20

boss_shield_y = HEIGHT + 5
boss_shield_x = WIDTH - 5

levelWriteFont = pg.font.SysFont("Helvatica", 30)
scoreFont = pg.font.SysFont("Times New Roman", 20)
gameOverFont = pg.font.SysFont("Times New Roman", 50)
level = 1
score = 0
highscore = 0

############## SCREEN FUNCTIONS ###########

game_over = True


def load_score(highscore):
    file_dir = os.path.dirname(__file__)
    with open(os.path.join(file_dir, score_filename), 'r') as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0

    return highscore


def write_score(highscore): ## WRİTE HİGHSCORE TO FİLE TO ALWAYS STORE
    file_dir = os.path.dirname(__file__)
    with open(os.path.join(file_dir, score_filename), 'w') as f:
        f.write(str(highscore))


def show_gameover_screen(is_start_screen):
    control = True
    endstart = pg.image.load(os.path.join(image_folder, "end_start_screen.png"))
    the_screen.blit(endstart, endstart.get_rect())
    the_screen.blit(levelWriteFont.render("High Score = " + str(highscore), 1, BLACK), (25, 25))
    if not is_start_screen:
        gameOverText = gameOverFont.render("GAME OVER!", 1, BLUE)
        the_screen.blit(gameOverText, (300, 250))
    pg.display.update()
    while control:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                write_score(highscore)
                sys.exit()

            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    control = False
                    pg.mixer.music.play(-1)


################ GAME LOOP ##################

running = True
counter_reset = True
is_start_screen = True
highscore = load_score(highscore)
while running:
    if game_over:
        show_gameover_screen(is_start_screen)
        game_over = False

        ############## SPRİTE GROUPS AND SHİP DEFİNİNG ####################
        the_ship = Ship()
        all_sprites = pg.sprite.Group()
        all_sprites.add(the_ship)
        ufo_sprites = pg.sprite.Group()
        laser_sprites = pg.sprite.Group()
        rocket_sprites = pg.sprite.Group()
        laserbeam_sprites = pg.sprite.Group()
        powUp_sprites = pg.sprite.Group()
        baloon_sprites = pg.sprite.Group()
        ###############SUMMONİNG UFOS ################

        ufo_number = 20

        for i in range(ufo_number):
            ufo1 = Ufo()
            all_sprites.add(ufo1)
            ufo_sprites.add(ufo1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            write_score(highscore)
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                the_ship.shoot('laser')

            elif event.key == pg.K_e and the_ship.spell_power >= 30:
                the_ship.shoot('laserbeam')
                the_ship.spell_power -= 30

            elif event.key == pg.K_w and the_ship.spell_power >= 16:
                the_ship.shoot('rocket')
                the_ship.spell_power -= 16

            elif event.key == pg.K_a and the_ship.spell_power >= 10:
                the_ship.shoot('balloon')
                the_ship.spell_power -= 10


    ## update draw functions
    ##the_screen.fill(BLACK)

    the_screen.blit(background, background.get_rect())
    clock.tick(FPS)
    number_of_ufo = len(ufo_sprites)
    ##### ABOUT SCREEN #################

    draw_bar(the_screen, ship_shieldbar_x, ship_shieldbar_y, the_ship.shield, 'shield')
    draw_bar(the_screen, ship_spellpowerbar_x, ship_spellpowerbar_y, the_ship.spell_power, 'spell')
    draw_lives(the_screen, WIDTH - 300, 5, the_ship.lives, little_ship_image)
    text = levelWriteFont.render("Level {}".format(level), 1, RED)
    the_screen.blit(text, (int(WIDTH -100), 6))
    score_text = scoreFont.render("Score {}".format(score), 1, BLUE)
    the_screen.blit(score_text, (int(WIDTH / 2), 10))
    ################ ABOUT KEYS ################
    keys = pg.key.get_pressed() ## turns the boolean values of keys is pressed 1 or not 0
    up, down = keys[pg.K_UP], keys[pg.K_DOWN]


    ####-------- OTHER THİNGS---------------

    is_laser_hit_ufo = pg.sprite.groupcollide(laser_sprites, ufo_sprites, True, True)
    any_ufo_hit_ship = pg.sprite.spritecollide(the_ship, ufo_sprites, False, collided=pg.sprite.collide_circle)
    is_rocket_hit_ufo = pg.sprite.groupcollide(rocket_sprites, ufo_sprites, True, True)
    is_laserbeam_hit_ufo = pg.sprite.groupcollide(laserbeam_sprites, ufo_sprites, False, True)
    is_powerUp_collected = pg.sprite.spritecollide(the_ship, powUp_sprites, False, collided=pg.sprite.collide_circle)
    is_baloon_hit_ufo = pg.sprite.groupcollide(baloon_sprites, ufo_sprites, True, False)

    if is_baloon_hit_ufo:
        for ufos in is_baloon_hit_ufo.values():
            for ufo in ufos:
                #water_exp_sound.play()
                water_exp = WaterExplosion(ufo.rect.center, 'sm')
                all_sprites.add(water_exp)
                is_water_exp_hit = pg.sprite.spritecollide(water_exp, ufo_sprites, False)
                if is_water_exp_hit:
                    for other_ufo in is_water_exp_hit:
                        ufo.freeze()
                        freeze_sound.play()
                        water_exp = WaterExplosion(other_ufo.rect.center, 'sm')
                        all_sprites.add(water_exp)
                        score += 5

    if is_powerUp_collected:
        for pows in is_powerUp_collected:
            score += 100
            if pows.type == 'shield':
                shield_pow_sound.play()
                the_ship.shield = 100
            if pows.type == 'killAll':
                for ufo in ufo_sprites:
                    explosion = Explosion(ufo.rect.center, random.choice(['sm', 'lrg']))
                    ufo_explosion_sound.play()
                    all_sprites.add(explosion)
                    ufo.kill()
            if pows.type == 'gun':
                for ufo in ufo_sprites:
                    explosion = WaterExplosion(ufo.rect.center, random.choice(['sm', 'lrg']))
                    freeze_sound.set_volume(0.6)
                    freeze_sound.play()
                    freeze_sound.set_volume(0.4)
                    all_sprites.add(explosion)
                    ufo.freeze()

            if pows.type == 'life':
                life_pow_sound.play()
                if the_ship.lives >= 5:
                    the_ship.lives = 5
                else:
                    the_ship.lives += 1
            pows.kill()
            if pows.type == 'speed':
                speed_pow_sound.play()
                for ufo in ufo_sprites:
                    ufo.speed_x = int(ufo.speed_x / 2)
                    ufo.speed_y = int(ufo.speed_y / 2)
                    if ufo.speed_x < 4:
                        ufo.speed_x = 3
                    if - 1 < ufo.speed_y < 0:
                            ufo.speed_y = -1
                    if 1 > ufo.speed_y >= 0:
                        ufo.speed_y = 1
            if pows.type == 'death':
                ship_explosion_sound.play()
                death_explosion = Explosion(the_ship.rect.center, 'player')
                all_sprites.add(death_explosion)
                the_ship.hide()
                the_ship.lives -= 1
                the_ship.shield = 100
                score -= 100
    if is_rocket_hit_ufo:

        for ufos in is_rocket_hit_ufo.values():
            for ufo in ufos:
                ufo_explosion_sound.play()
                explosion = Explosion(ufo.rect.center, 'lrg')
                all_sprites.add(explosion)
                is_explode_hit = pg.sprite.spritecollide(explosion, ufo_sprites, True)
                if is_explode_hit:
                    for other_ufo in is_explode_hit:
                        explosion = Explosion(other_ufo.rect.center, 'sm')
                        ufo_explosion_sound.play()
                        all_sprites.add(explosion)
                        score += 40
    if is_laser_hit_ufo:
        for ufos in is_laser_hit_ufo.values():
            for ufo in ufos:
                the_ship.spell_power += int((ufo.rect.size[0]+ufo.rect.size[1]) / 7)
                explosion = Explosion(ufo.rect.center, 'sm')
                ufo_explosion_sound.play()
                all_sprites.add(explosion)
                if random.random() > 0.9:
                    powerUp = Powerup(ufo)
                    all_sprites.add(powerUp)
                    powUp_sprites.add(powerUp)
            score += 30
    for ufo in any_ufo_hit_ship:
        the_ship.shield -= ufo.radius / 3
        explosion = Explosion(the_ship.rect.center, 'sm')
        ufo_hit_ship_sound.play()
        if the_ship.shield <= 0:
            death_explosion = Explosion(the_ship.rect.center, 'player')
            ship_explosion_sound.play()
            all_sprites.add(death_explosion)
            the_ship.hide()
            the_ship.lives -= 1
            the_ship.shield = 100

    if the_ship.lives == 0 and not death_explosion.alive():
        if score > highscore:
            highscore = score
        score = 0
        game_over = True
        pg.mixer.music.stop()
        gameOver_sound.play()
        is_start_screen = False
    if is_laserbeam_hit_ufo:
        for hit in is_laserbeam_hit_ufo.values():
            for ufo in hit:
                explosion = Explosion(ufo.rect.center, 'sm')
                ufo_explosion_sound.play()
                all_sprites.add(explosion)
                score += 30
    if number_of_ufo == 0:
        if counter_reset:
            ending_time = pg.time.get_ticks()
            counter_reset = False

        if pg.time.get_ticks() - ending_time > 3000:
            counter_reset = True
            level += 1
            for i in range(level * 5):
                ufo = Ufo()
                all_sprites.add(ufo)
                ufo_sprites.add(ufo)

    all_sprites.draw(the_screen)
    all_sprites.update(up, down)
    pg.display.update()
