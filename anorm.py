import pygame
import os
import random
import sys
import time

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
FPS = 50
clock = pygame.time.Clock()
EASY = ['map1.txt', 'map2.txt', 'map3.txt']
MEDIUM = ['map4.txt', 'map5.txt', 'map6.txt']
HARD = ['map7.txt', 'map8.txt', 'map9.txt']


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Добро пожаловать!"]
    fon = pygame.transform.scale(load_image('start.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 35)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        pygame.mixer.music.load('start.mp3')
        pygame.mixer.music.play(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def final_screen():
    intro_text = ["Congratulations", 'You are winner!']
    fi = load_image('final.png')
    final = pygame.transform.scale(fi, (690, 713))
    screen.blit(final, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    pygame.mixer.music.load('final.mp3')
    pygame.mixer.music.play(1)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.flip()
    time.sleep(50)
    terminate()


def lose_screen(width, height):
    lose = pygame.transform.scale(load_image('over.jpg'), (width, height))
    screen.blit(lose, (0, 0))
    font = pygame.font.Font(None, 30)
    pygame.mixer.music.load('game over.mp3')
    pygame.mixer.music.play(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                choose_screen()
                return
        pygame.display.flip()


def info_screen():
    intro_text = ['Правила игры',
                  'В нашей игре вам предстоит стать отважной героиней',
                  'и выбраться из лабиринта. В лабиринте вам нужно',
                  'пройти через ловушки. Будьте аккуратны!',
                  'Если вы попадете в ловушку,', 'вы проиграете.',
                  'Лабиринт состоит из 3 уровней,',
                  'Каждый следующий сложнее предыдущего.',
                  'В долгий путь, дорогой друг!']
    info = pygame.transform.scale(load_image('info.jpg'), (600, 600))
    screen.blit(info, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    x1, y1 = 500, 550
    w = 100
    h = 50
    button('Выйти', x1, y1, w, h)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= x1 and x <= x1 + w and y >= y1 and y <= y1 + h:
                    choose_screen()
                    return
        pygame.display.flip()


def button(text, x, y, w, h):
    font = pygame.font.Font(None, 35)
    text = font.render(text, 1, (100, 255, 100))
    text_x = x + 10
    text_y = y + 10
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, w, h), 1)


def choose_screen():
    pygame.mixer.music.stop()
    ch = load_image('info.jpg')
    fo = pygame.transform.scale(ch, (width, height))
    screen.blit(fo, (0, 0))
    font = pygame.font.Font(None, 43)
    text = font.render('Выберите дейтвие и нажмите на кнопку', 1, (100, 255, 100))
    text_x = 10
    text_y = 90
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 30)
    w = 160
    h = 50
    x1, y1 = 20, 250
    x2, y2 = 210, 250
    x3, y3 = 400, 250
    button('Инструкция', x1, y1, w, h)
    button('Начать', x2, y2, w, h)
    button('Выйти', x3, y3, w, h)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= x1 and x <= x1 + w and y >= y1 and y <= y1 + h:
                    info_screen()
                    return
                elif x >= x2 and x <= x2 + w and y >= y2 and y <= y2 + h:
                    return
                elif x >= x3 and x <= x3 + w and y >= y3 and y <= y3 + h:
                    terminate()
        pygame.display.flip()


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_width = tile_height = 40
r = load_image('rock.png')
rock = pygame.transform.scale(r, (tile_width, tile_height))
e = load_image('lvl1.jpg')
empty = pygame.transform.scale(e, (tile_width, tile_height))
l = load_image('lava.png')
lava = pygame.transform.scale(l, (tile_width, tile_height))
p = load_image('portal.png', -1)
portal = pygame.transform.scale(p, (tile_width, tile_height))
tile_images = {'wall': rock, 'empty': empty, 'lava': lava, 'portal': portal}
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
flower_group = pygame.sprite.Group()
flower2_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()


class Flower(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(flower_group, all_sprites)
        self.image = pygame.transform.scale(image, (tile_width, tile_height))
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)
        self.dx = 1

    def update(self):
        if pygame.sprite.spritecollideany(self, walls_group) or pygame.sprite.spritecollideany(self, lava_group):
            self.dx = -self.dx
        elif self.rect.x < 0 or self.rect.x >= width - tile_width:
            self.dx = -self.dx
        self.rect = self.rect.move(self.dx, 0)

    def attack(self):
        if pygame.sprite.spritecollideany(self, player_group):
            lose_screen(700, 700)


class Flower_vert(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(flower_group, all_sprites)
        self.image = pygame.transform.scale(image, (tile_width, tile_height))
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)
        self.dx = 1

    def update(self):
        if pygame.sprite.spritecollideany(self, walls_group) or pygame.sprite.spritecollideany(self, lava_group):
            self.dx = -self.dx
        elif self.rect.y < 0 or self.rect.y >= height - tile_height:
            self.dx = -self.dx
        self.rect = self.rect.move(0, self.dx)

    def attack(self):
        if pygame.sprite.spritecollideany(self, player_group):
            lose_screen(700, 700)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        if tile_type == 'wall':
            self.add(walls_group)
        elif tile_type == 'portal':
            self.add(portal_group)
        elif tile_type == 'lava':
            self.add(lava_group)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(player_group, all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.scale((sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size))), (tile_width - 3, tile_height - 3)))
        self.frames_right = self.frames[17:24]
        self.frames_left = self.frames[9:16]
        self.frames_down = self.frames[:8]
        self.frames_up = self.frames[25:32]

    def update_left(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames_left)
        self.image = self.frames_left[self.cur_frame]

    def update_right(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames_right)
        self.image = self.frames_right[self.cur_frame]

    def update_up(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames_up)
        self.image = self.frames_up[self.cur_frame]

    def update_down(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames_down)
        self.image = self.frames_down[self.cur_frame]

    def move(self, x, y):
        self.rect = self.image.get_rect().move(self.rect.x + x * tile_width, tile_height * y + self.rect.y)


def generate_level(level):
    new_player, x, y, flower, flower2 = None, None, None, None, None
    for sprite in walls_group:
        sprite.kill()
    for sprite in lava_group:
        sprite.kill()
    for sprite in flower_group:
        sprite.kill()
    for sprite in flower2_group:
        sprite.kill()
    for sprite in portal_group:
        sprite.kill()
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.' or level[y][x] == '*' or level[y][x] == '+':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '~':
                Tile('lava', x, y)
            elif level[y][x] == 'x':
                Tile('portal', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '*':
                x1 = x
                y1 = y
                flower = Flower(load_image("flower.jpg", -1), x1, y1)
            elif level[y][x] == '+':
                x2 = x
                y2 = y
                flower2 = Flower_vert(load_image("flower2.png", -1), x2, y2)
    new_player = AnimatedSprite(load_image("character3.jpg", -1), 8, 4, xx, yy)
    return new_player, xx, yy, flower, flower2


player, level_x, level_y, flower, flower2 = generate_level(load_level(random.choice(EASY)))
u = 'easy'
start_screen()
choose_screen()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)
                player.update_left()
                if (pygame.sprite.spritecollideany(player, walls_group) or
                    player.rect.x <= -tile_width):
                    player.move(1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)
                player.update_right()
                if (pygame.sprite.spritecollideany(player, walls_group)  or
                    player.rect.x >= width):
                    player.move(-1, 0)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
                player.update_down()
                if (pygame.sprite.spritecollideany(player, walls_group) or
                    player.rect.y >= height):
                    player.move(0, -1)
            elif event.key == pygame.K_UP:
                player.move(0, -1)
                player.update_up()
                if (pygame.sprite.spritecollideany(player, walls_group) or
                    player.rect.y <= -tile_height):
                    player.move(0, 1)
        elif pygame.sprite.spritecollideany(player, portal_group) and u == 'easy':
            size = width, height = 700, 700
            screen = pygame.display.set_mode(size)
            tile_width = tile_height = 35
            r = load_image('rock.png')
            rock = pygame.transform.scale(r, (tile_width, tile_height))
            e = load_image('wood.png')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            f = load_image('flower.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            fl = load_image('flower2.png')
            flower = pygame.transform.scale(f, (tile_width, tile_height))
            l = load_image('lava.png')
            lava = pygame.transform.scale(l, (tile_width, tile_height))
            p = load_image('portal.png')
            portal = pygame.transform.scale(p, (tile_width, tile_height))
            tile_images = {'wall': rock, 'empty': empty,
                           'flower': flower, 'lava': lava, 'portal': portal}
            player, level_x, level_y, flower, flower2 = generate_level(load_level(random.choice(MEDIUM)))
            u = 'medium'
        elif pygame.sprite.spritecollideany(player, portal_group) and u == 'medium':
            size = width, height = 690, 713
            screen = pygame.display.set_mode(size)
            tile_width = tile_height = 23
            r = load_image('3lvl.png')
            rock = pygame.transform.scale(r, (tile_width, tile_height))
            e = load_image('carpet.jpeg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            f = load_image('flower.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            fl = load_image('flower2.png')
            flower = pygame.transform.scale(f, (tile_width, tile_height))
            l = load_image('lava.png')
            lava = pygame.transform.scale(l, (tile_width, tile_height))
            p = load_image('portal.png')
            portal = pygame.transform.scale(p, (tile_width, tile_height))
            tile_images = {'wall': rock, 'empty': empty, 'lava': lava, 'portal': portal}
            player, level_x, level_y, flower, flower2 = generate_level(load_level(random.choice(HARD)))
            u = 'hard'
        elif pygame.sprite.spritecollideany(player, portal_group) and u == 'hard':
            final_screen()
        elif (pygame.sprite.spritecollideany(player, flower_group) or
              pygame.sprite.spritecollideany(player, lava_group)):
            lose_screen(width, height)
            size = width, height = 600, 600
            screen = pygame.display.set_mode(size)
            tile_width = tile_height = 40
            r = load_image('rock.png')
            rock = pygame.transform.scale(r, (tile_width, tile_height))
            e = load_image('lvl1.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            f = load_image('flower.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            fl = load_image('flower2.png')
            flower = pygame.transform.scale(f, (tile_width, tile_height))
            l = load_image('lava.png')
            lava = pygame.transform.scale(l, (tile_width, tile_height))
            p = load_image('portal.png')
            portal = pygame.transform.scale(p, (tile_width, tile_height))
            tile_images = {'wall': rock, 'empty': empty, 'lava': lava, 'portal': portal}
            player, level_x, level_y, flower, flower2 = generate_level(load_level(random.choice(EASY)))
            u = 'easy'
    for flower in flower_group:
        flower.update()
        if pygame.sprite.spritecollideany(flower, player_group):
            lose_screen(width, height)
            size = width, height = 600, 600
            screen = pygame.display.set_mode(size)
            tile_width = tile_height = 40
            r = load_image('rock.png')
            rock = pygame.transform.scale(r, (tile_width, tile_height))
            e = load_image('lvl1.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            f = load_image('flower.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            fl = load_image('flower2.png')
            flower = pygame.transform.scale(f, (tile_width, tile_height))
            l = load_image('lava.png')
            lava = pygame.transform.scale(l, (tile_width, tile_height))
            p = load_image('portal.png')
            portal = pygame.transform.scale(p, (tile_width, tile_height))
            tile_images = {'wall': rock, 'empty': empty, 'lava': lava, 'portal': portal}
            player, level_x, level_y, flower, flower2 = generate_level(load_level(random.choice(EASY)))
            u = 'easy'
    for flower in flower2_group:
        flower.update()
        if pygame.sprite.spritecollideany(flower, player_group):
            lose_screen(width, height)
            size = width, height = 600, 600
            screen = pygame.display.set_mode(size)
            tile_width = tile_height = 40
            r = load_image('rock.png')
            rock = pygame.transform.scale(r, (tile_width, tile_height))
            e = load_image('lvl1.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            f = load_image('flower.jpg')
            empty = pygame.transform.scale(e, (tile_width, tile_height))
            fl = load_image('flower2.png')
            flower = pygame.transform.scale(f, (tile_width, tile_height))
            l = load_image('lava.png')
            lava = pygame.transform.scale(l, (tile_width, tile_height))
            p = load_image('portal.png')
            portal = pygame.transform.scale(p, (tile_width, tile_height))
            tile_images = {'wall': rock, 'empty': empty, 'lava': lava, 'portal': portal}
            player, level_x, level_y, flower, flower2 = generate_level(load_level(random.choice(EASY)))
            u = 'easy'
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
