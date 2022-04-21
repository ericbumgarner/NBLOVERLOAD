import pygame
import random
from time import asctime
from Ballset import *
from nbloverloaded import *

'''
NBL OVERLOAD FUNCTIONS
'''

'''
Loading Assets
'''
pygame.font.init()
scoring_buttons = Ballset()

UP000 = Player('UP000', 'Unknown Player')
FP000 = Player('FP000', 'Future Player')
GI000 = Player('GP000', 'Gary Imposter')
DD000 = Player('DD000', 'DeMo_DoG')
RG000 = Player('RG000', 'Red_Gekko')
JB000 = Player('JB000', 'Jail_Break')

HB001 = Player('HB001', 'Hale Bumgarner', '2', '2')
MA002 = Player('MA002', 'Masae Aitoku', '3')
# KN003 = Player('KN003','Khanh Ngo')
DW004 = Player('DW004', 'Delbert Wong')
CC005 = Player('CC005', 'Chris Chua')
# AL006 = Player('AL006','Armando Leal')
# FH007 = Player('FH007','Frank Hom')
SW008 = Player('SW008', 'Siara Waseem')
# LB009 = Player('LB009','Louise Barron')
# AP010 = Player('AP010','Anastasia Plotnikova')
KK011 = Player('KK011', 'Kenny Koo')
# RM012 = Player('RM012','Ren Mata')
KS013 = Player('KS013', 'Kevin Su')
KZ014 = Player('KZ014', 'Karen Zeng')
JP015 = Player('JP015', 'Joseph Phillips')
RL016 = Player('RL016', 'Rene Loria')
TS017 = Player('TS017', 'Tom Seymour')
LW018 = Player('LW018', 'Leon Waki')
GB019 = Player('GB019', 'Greg Benitz')
TE020 = Player('TE020', 'Todd Emmel')
WM021 = Player('WM021', 'Wyatt Moss')
# AF022 = Player('AF022','Alan Fung')
# JL023 = Player('JL023','Joina Liao')
ST024 = Player('ST024', 'Sara Thomas')
SW025 = Player('SW025', 'Steve Wong')
YH026 = Player('YH026', 'Yoli Handoko')
AI027 = Player('AI027', 'Andi Iwan')
GF028 = Player('GF028', 'German Frigerio')
PB029 = Player('PB029', 'Pascal Bouchareine')
SA030 = Player('SA030', 'Santiago Alessandri')
TH031 = Player('TH031', 'Thom Haddow')
# WH032 = Player('WH032','Wade Hargrove')
AL033 = Player('AL033', 'Alice Loo')
# RY034 = Player('RY034','Robert Yulo')
# OC035 = Player('OC035','Oliver Cruz')
# CM036 = Player('CM036','Christian Manalastas')
MH037 = Player('MH037', 'Mark Hernandez')
# MB038 = Player('MB038','Mark Butler')
# NP039 = Player('NP039','Nik Pledger')
# JB040 = Player('JB040','Jeff Binkley')
# TM041 = Player('TM041','Tommy Mudd')
# ES042 = Player('ES042','Ed Sinchai')
PN043 = Player('PN043', 'Paulo Naranjo')
# BT044 = Player('BT044','Brian Theberge')
# YP045 = Player('YP045','Yevgeniya Plotnikova')
BY046 = Player('BY046', 'Ben Yu')
JC047 = Player('JC047', 'Juan Cheung')
# DN048 = Player('DN048','David Norris')
# TY049 = Player('TY049','Travis Yalup')
# EJ050 = Player('EJ050','Ell Jackson')
# JL051 = Player('JL051','Julia Landholt')
# EM052 = Player('EM052','Estelle Mays')
AY053 = Player('AY053', 'Art Yee')
# JG054 = Player('JG054','Josh Gomes')
BO055 = Player('BO055', 'Bonnie Ogg')
LJ056 = Player('LJ056', 'Lucy Ji')
TP057 = Player('TP057', 'Tom Passow')
CH058 = Player('CH058', 'Craig Hu')
AI059 = Player('AI059', 'Alexis Iwan')
KS060 = Player('KS060', 'Kevin Scheper')
NL061 = Player('NL061', 'Nicholas Lansdown')
CM062 = Player('CM062', 'Cheryl Morgan')
DS063 = Player('DS063', 'David Sumisaki')
TJ064 = Player('TJ064', 'Taylor Jones')
KH065 = Player('KH065', 'Kirk Habbling')
MS066 = Player('MS066', 'Motoko Siguenza')
OA067 = Player('OA067', 'Olga Azarova')
LD068 = Player('LD068', 'Luyan Ding')
SJ069 = Player('SJ069', 'Shubham Jain')
MA070 = Player('MA070', 'Marcelo Aviles')
NS071 = Player('NS071', 'Noah Snyder')
BS072 = Player('BS072', 'Brandon Seguerre')
TY073 = Player('TY073', 'Tae Yim')

NBLT00 = Team('Substitutes', 'NBLT00', [UP000, GI000, FP000])
NBLT99 = Team('BlitZ', 'NBLT99', [DD000, RG000, JB000])
NBLT01 = Team('Eye Rollers', 'NBLT01', [MA002, DW004, CC005, BO055])
# NBLT02 = Team('HOMicide','02',[])
NBLT03 = Team('Push Out Method', 'NBLT03', [KS013, KZ014, JP015, RL016, SW008, CM062])
NBLT04 = Team('Paladins', 'NBLT04', [TS017, LW018, GB019, TE020, WM021])
NBLT05 = Team('Crazy Pool Asians', 'NBLT05', [ST024, SW025, YH026, AI027, AI059, KS060])
NBLT06 = Team('Breaking Bad', 'NBLT06', [GF028, PB029, SA030, TH031, AY053, LJ056])
NBLT07 = Team('The Screechers', 'NBLT07', [KK011, AL033, DS063, TJ064, KH065, MH037])
# NBLT08 = Team('Marked For Death','08',[])
NBLT09 = Team('Pool Magic', 'NBLT09', [PN043, BY046, JC047, TY073, BS072])
# NBLT10 = Team('Push It Good','10',[])
NBLT11 = Team('The Chainstrokers', 'NBLT11', [HB001, TP057, CH058])
NBLT12 = Team("Moto's Locos", 'NBLT12', [MS066, OA067, LD068, SJ069, MA070, NS071])

team_Master_TUP = (NBLT01, NBLT03, NBLT04, NBLT05, NBLT06, NBLT07, NBLT09, NBLT11, NBLT12)

def conwayATOM(_point, _state):
    test = False
    connectedalive = 0
    if _state[(bordercheckx(_point[0] - 1), borderchecky(_point[1] - 1))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0] - 1), borderchecky(_point[1]))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0] - 1), borderchecky(_point[1] + 1))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0]), borderchecky(_point[1] - 1))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0]), borderchecky(_point[1] + 1))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0] + 1), borderchecky(_point[1] - 1))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0] + 1), borderchecky(_point[1]))]:
        connectedalive += 1
    if _state[(bordercheckx(_point[0] + 1), borderchecky(_point[1] + 1))]:
        connectedalive += 1
    if not _state[(_point[0], _point[1])] and connectedalive < 3:
        test = False
    if _state[(_point[0], _point[1])] and connectedalive < 2:
        test = False
    if _state[(_point[0], _point[1])] and connectedalive == 2:
        test = True
    if _state[(_point[0], _point[1])] and connectedalive == 3:
        test = True
    if _state[(_point[0], _point[1])] and connectedalive > 3:
        test = False
    if not _state[(_point[0], _point[1])] and connectedalive == 3:
        test = True
    return test


def bordercheckx(_point):
    if _point == 81:
        return 1
    if _point == 0:
        return 80
    else:
        return _point


def borderchecky(_point):
    if _point == 49:
        return 1
    if _point == 0:
        return 48
    else:
        return _point


def loadingscreen(win, familylogo_, tableborder_):
    grid = []
    for x in range(1, 81, 1):
        for y in range(1, 49, 1):
            grid.append((x, y))

    state_list = (True, False)

    base = []
    for item in range(3840):
        base.append(random.choice(state_list))

    conway_dict = []
    for idx, item in enumerate(grid):
        conway_dict.append(item)
        conway_dict.append(base[idx])
    it = iter(conway_dict)
    res_dct = dict(zip(it, it))

    conway_dict2 = []
    for idx, item in enumerate(grid):
        conway_dict2.append(item)
        conway_dict2.append(base[idx])
    it = iter(conway_dict2)
    res_dct2 = dict(zip(it, it))

    namelist = []
    for y in range(1, 49, 1):
        for x in range(1, 81, 1):
            namelist.append((x, y))

    square_dict = {}
    for num in namelist:
        square_dict[num] = {'x': 0, 'y': 0, 'w': 10, 'h': 10}

    x = 0
    y = 0
    for item in square_dict:
        square_dict[item]['x'] = x
        square_dict[item]['y'] = y
        x += 10
        if x == 800:
            x = 0
            y += 10

    generation = 0
    ###adjust timing
    while generation < 30:

        for item in res_dct:
            res_dct2[item] = conwayATOM(item, res_dct)

        for item in res_dct2:
            if res_dct2[item]:
                pygame.draw.rect(win, (random.randint(100, 140), random.randint(220, 250), random.randint(80, 120)), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))
            else:
                pygame.draw.rect(win, (15, 139, 68), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))
        win.blit(familylogo_, (300, 100))
        win.blit(tableborder_, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)

        for item in res_dct2:
            res_dct[item] = conwayATOM(item, res_dct2)

        for item in res_dct:
            if res_dct[item]:
                pygame.draw.rect(win, (random.randint(100, 140), random.randint(220, 250), random.randint(80, 120)), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))
            else:
                pygame.draw.rect(win, (15, 139, 68), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))
        win.blit(familylogo_, (300, 100))
        win.blit(tableborder_, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)
        generation += 1


def conwayscreensaver(window_):
    tableborder_ = pygame.image.load('tableborder.png')

    grid = []
    for x in range(1, 81, 1):
        for y in range(1, 49, 1):
            grid.append((x, y))

    state_list = [True, False]

    base = []
    for item in range(3840):
        base.append(random.choice(state_list))

    conway_dict = []
    for idx, item in enumerate(grid):
        conway_dict.append(item)
        conway_dict.append(base[idx])
    it = iter(conway_dict)
    res_dct = dict(zip(it, it))

    conway_dict2 = []
    for idx, item in enumerate(grid):
        conway_dict2.append(item)
        conway_dict2.append(base[idx])
    it = iter(conway_dict2)
    res_dct2 = dict(zip(it, it))

    namelist = []
    for y in range(1, 49, 1):
        for x in range(1, 81, 1):
            namelist.append((x, y))

    square_dict = {}
    for num in namelist:
        square_dict[num] = {'x': 0, 'y': 0, 'w': 10, 'h': 10}

    x = 0
    y = 0
    for item in square_dict:
        square_dict[item]['x'] = x
        square_dict[item]['y'] = y
        x += 10
        if x == 800:
            x = 0
            y += 10

    running_ = True
    while running_:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainmenu(window_)
        for item in res_dct:
            res_dct2[item] = conwayATOM(item, res_dct)

        for item in res_dct2:
            if res_dct2[item]:
                pygame.draw.rect(window_, (random.randint(100, 140), random.randint(220, 250), random.randint(80, 120)),
                                 (square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'],
                                  square_dict[item]['h']))
            else:
                pygame.draw.rect(window_, (15, 139, 68), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)

        for item in res_dct2:
            res_dct[item] = conwayATOM(item, res_dct2)

        for item in res_dct:
            if res_dct[item]:
                pygame.draw.rect(window_, (random.randint(100, 140), random.randint(220, 250), random.randint(80, 120)),
                                 (square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'],
                                  square_dict[item]['h']))
            else:
                pygame.draw.rect(window_, (15, 139, 68), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)


def conwaystats(window_, _mresults, home_lineup_, away_lineup_):
    tableborder_ = pygame.image.load('tableborder.png')

    grid = []
    for x in range(1, 81, 1):
        for y in range(1, 49, 1):
            grid.append((x, y))

    state_list = [True, False]

    base = []
    for item in range(3840):
        base.append(random.choice(state_list))

    conway_dict = []
    for idx, item in enumerate(grid):
        conway_dict.append(item)
        conway_dict.append(base[idx])
    it = iter(conway_dict)
    res_dct = dict(zip(it, it))

    conway_dict2 = []
    for idx, item in enumerate(grid):
        conway_dict2.append(item)
        conway_dict2.append(base[idx])
    it = iter(conway_dict2)
    res_dct2 = dict(zip(it, it))

    namelist = []
    for y in range(1, 49, 1):
        for x in range(1, 81, 1):
            namelist.append((x, y))

    square_dict = {}
    for num in namelist:
        square_dict[num] = {'x': 0, 'y': 0, 'w': 10, 'h': 10}

    x = 0
    y = 0
    for item in square_dict:
        square_dict[item]['x'] = x
        square_dict[item]['y'] = y
        x += 10
        if x == 800:
            x = 0
            y += 10

    if _mresults['15'][1][0] > 7:
        h_ = 'home'
        roster_ = home_lineup_
        eval(_mresults['home']).s_match_score = 0
        eval(_mresults['away']).s_match_score = 0
    if _mresults['15'][1][1] > 7:
        h_ = 'away'
        roster_ = away_lineup_
        eval(_mresults['home']).s_match_score = 0
        eval(_mresults['away']).s_match_score = 0

    running_ = True
    while running_:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                scoresheet_function(window_, _mresults, home_lineup_, away_lineup_, 15)
                mainmenu(window_)
        for item in res_dct:
            res_dct2[item] = conwayATOM(item, res_dct)

        for item in res_dct2:
            if res_dct2[item]:
                pygame.draw.rect(window_, (random.randint(100, 140), random.randint(220, 250), random.randint(80, 120)),
                                 (square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'],
                                  square_dict[item]['h']))
            else:
                pygame.draw.rect(window_, (15, 139, 68), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))

        match_results_screen = pygame.image.load('match_results_screen.png')
        textfont = pygame.font.Font('arialbd.ttf', 28)
        player1_ = textfont.render(roster_[0].firstname, False, (0, 0, 0))
        player2_ = textfont.render(roster_[1].firstname, False, (0, 0, 0))
        player3_ = textfont.render(roster_[2].firstname, False, (0, 0, 0))

        window_.blit(match_results_screen, (75, 60))

        window_.blit(eval(_mresults[h_]).ol_logo, (333, 75))
        window_.blit(player1_, (103, 350))
        window_.blit(player2_, (316, 350))
        window_.blit(player3_, (528, 350))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)

        for item in res_dct2:
            res_dct[item] = conwayATOM(item, res_dct2)

        for item in res_dct:
            if res_dct[item]:
                pygame.draw.rect(window_, (random.randint(100, 140), random.randint(220, 250), random.randint(80, 120)),
                                 (square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'],
                                  square_dict[item]['h']))
            else:
                pygame.draw.rect(window_, (15, 139, 68), (
                square_dict[item]['x'], square_dict[item]['y'], square_dict[item]['w'], square_dict[item]['h']))

        window_.blit(match_results_screen, (75, 60))

        window_.blit(eval(_mresults[h_]).ol_logo, (333, 75))
        window_.blit(player1_, (103, 350))
        window_.blit(player2_, (316, 350))
        window_.blit(player3_, (528, 350))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)


def match_selector(window_):
    tableborder_ = pygame.image.load('tableborder.png')
    background_ = pygame.image.load('bed.png')
    matchbar_ = pygame.image.load('matchbar.png')
    recording_ = pygame.image.load('recording.png')
    table2_ = pygame.image.load('table2.png')
    table34_ = pygame.image.load('table34.png')
    table8_ = pygame.image.load('table8.png')
    table9_ = pygame.image.load('table9.png')

    matches = {'Table 2': {'Home': NBLT00, 'Away': NBLT99},
               'Table 34': {'Home': NBLT00, 'Away': NBLT99},
               'Table 8': {'Home': NBLT99, 'Away': NBLT00},
               'Table 9': {'Home': NBLT99, 'Away': NBLT00}}

    if asctime().split()[1] == 'Apr' and asctime().split()[2] == '1':
        matches = {'Table 2': {'Home': NBLT06, 'Away': NBLT09},
                   'Table 34': {'Home': NBLT12, 'Away': NBLT04},
                   'Table 8': {'Home': NBLT11, 'Away': NBLT05},
                   'Table 9': {'Home': NBLT11, 'Away': NBLT03}}

    if asctime().split()[1] == 'Mar' and asctime().split()[2] == '25':
        matches = {'Table 2': {'Home': NBLT03, 'Away': NBLT05},
                   'Table 34': {'Home': NBLT01, 'Away': NBLT09},
                   'Table 8': {'Home': NBLT07, 'Away': NBLT11},
                   'Table 9': {'Home': NBLT06, 'Away': NBLT12}}

    if asctime().split()[1] == 'Apr' and asctime().split()[2] == '2':
        matches = {'Table 2': {'Home': NBLT11, 'Away': NBLT06},
                   'Table 34': {'Home': NBLT04, 'Away': NBLT05},
                   'Table 8': {'Home': NBLT09, 'Away': NBLT07},
                   'Table 9': {'Home': NBLT03, 'Away': NBLT01}}

    if asctime().split()[1] == 'Mar' and asctime().split()[2] == '24':
        matches = {'Table 2': {'Home': NBLT05, 'Away': NBLT09},
                   'Table 34': {'Home': NBLT11, 'Away': NBLT01},
                   'Table 8': {'Home': NBLT07, 'Away': NBLT04},
                   'Table 9': {'Home': NBLT03, 'Away': NBLT12}}

    if asctime().split()[1] == 'Apr' and asctime().split()[2] == '15':
        matches = {'Table 2': {'Home': NBLT09, 'Away': NBLT06},
                   'Table 34': {'Home': NBLT01, 'Away': NBLT07},
                   'Table 8': {'Home': NBLT05, 'Away': NBLT12},
                   'Table 9': {'Home': NBLT03, 'Away': NBLT04}}

    if asctime().split()[1] == 'Apr' and asctime().split()[2] == '22':
        matches = {'Table 2': {'Home': NBLT04, 'Away': NBLT01},
                   'Table 34': {'Home': NBLT12, 'Away': NBLT11},
                   'Table 8': {'Home': NBLT07, 'Away': NBLT09},
                   'Table 9': {'Home': NBLT06, 'Away': NBLT03}}

    if asctime().split()[1] == 'Mar' and asctime().split()[2] == '28':
        matches = {'Table 2': {'Home': NBLT07, 'Away': NBLT12},
                   'Table 34': {'Home': NBLT05, 'Away': NBLT06},
                   'Table 8': {'Home': NBLT11, 'Away': NBLT04},
                   'Table 9': {'Home': NBLT09, 'Away': NBLT03}}

    if asctime().split()[1] == 'Mar' and asctime().split()[2] == '30':
        matches = {'Table 2': {'Home': NBLT07, 'Away': NBLT06},
                   'Table 34': {'Home': NBLT05, 'Away': NBLT03},
                   'Table 8': {'Home': NBLT12, 'Away': NBLT01},
                   'Table 9': {'Home': NBLT11, 'Away': NBLT09}}

    if asctime().split()[1] == 'Mar' and asctime().split()[2] == '29':
        matches = {'Table 2': {'Home': NBLT03, 'Away': NBLT11},
                   'Table 34': {'Home': NBLT12, 'Away': NBLT09},
                   'Table 8': {'Home': NBLT01, 'Away': NBLT05},
                   'Table 9': {'Home': NBLT06, 'Away': NBLT04}}

    if asctime().split()[1] == 'May' and asctime().split()[2] == '20':
        matches = {'Table 2': {'Home': NBLT04, 'Away': NBLT12},
                   'Table 34': {'Home': NBLT06, 'Away': NBLT11},
                   'Table 8': {'Home': NBLT09, 'Away': NBLT01},
                   'Table 9': {'Home': NBLT07, 'Away': NBLT05}}

    if asctime().split()[1] == 'May' and asctime().split()[2] == '27':
        matches = {'Table 2': {'Home': NBLT05, 'Away': NBLT01},
                   'Table 34': {'Home': NBLT11, 'Away': NBLT05},
                   'Table 8': {'Home': NBLT04, 'Away': NBLT09},
                   'Table 9': {'Home': NBLT03, 'Away': NBLT07}}

    if asctime().split()[1] == 'Mar' and asctime().split()[2] == '26':
        matches = {'Table 2': {'Home': NBLT12, 'Away': NBLT06},
                   'Table 34': {'Home': NBLT11, 'Away': NBLT07},
                   'Table 8': {'Home': NBLT05, 'Away': NBLT04},
                   'Table 9': {'Home': NBLT01, 'Away': NBLT03}}

    # Bar One
    for number in range(-100, 65, 5):
        window_.blit(background_, (0, 0))
        window_.blit(matchbar_, (number, 60))
        window_.blit(matches['Table 2']['Home'].ol_logo, (number + 10, 80))
        window_.blit(matches['Table 2']['Away'].ol_logo, (number + 10, 320))
        window_.blit(recording_, (number + 32, 200))
        window_.blit(table2_, (number + 13, 225))

        window_.blit(tableborder_, (0, 0))
        pygame.display.update()

    # Bar Two
    for number in range(65, 235, 5):
        window_.blit(background_, (0, 0))
        window_.blit(matchbar_, (number, 60))
        window_.blit(matches['Table 34']['Home'].ol_logo, (number + 10, 80))
        window_.blit(matches['Table 34']['Away'].ol_logo, (number + 10, 320))
        window_.blit(table34_, (number + 13, 225))

        window_.blit(matchbar_, (65, 60))
        window_.blit(matches['Table 2']['Home'].ol_logo, (75, 80))
        window_.blit(matches['Table 2']['Away'].ol_logo, (75, 320))
        window_.blit(recording_, (97, 200))
        window_.blit(table2_, (78, 225))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()

    # Bar Three
    for number in range(235, 405, 5):
        window_.blit(background_, (0, 0))
        window_.blit(matchbar_, (number, 60))
        window_.blit(matches['Table 8']['Home'].ol_logo, (number + 10, 80))
        window_.blit(matches['Table 8']['Away'].ol_logo, (number + 10, 320))
        window_.blit(table8_, (number + 13, 225))

        window_.blit(matchbar_, (235, 60))
        window_.blit(matches['Table 34']['Home'].ol_logo, (245, 80))
        window_.blit(matches['Table 34']['Away'].ol_logo, (245, 320))
        window_.blit(table34_, (248, 225))

        window_.blit(matchbar_, (65, 60))
        window_.blit(matches['Table 2']['Home'].ol_logo, (75, 80))
        window_.blit(matches['Table 2']['Away'].ol_logo, (75, 320))
        window_.blit(recording_, (97, 200))
        window_.blit(table2_, (78, 225))

        window_.blit(tableborder_, (0, 0))
        pygame.display.update()

    # Bar Four
    for number in range(405, 575, 5):
        window_.blit(background_, (0, 0))
        window_.blit(matchbar_, (number + 3, 60))
        window_.blit(matches['Table 9']['Home'].ol_logo, (number + 13, 80))
        window_.blit(matches['Table 9']['Away'].ol_logo, (number + 13, 320))
        window_.blit(table9_, (number + 16, 225))

        window_.blit(matchbar_, (405, 60))
        window_.blit(matches['Table 8']['Home'].ol_logo, (415, 80))
        window_.blit(matches['Table 8']['Away'].ol_logo, (415, 320))
        window_.blit(table8_, (418, 225))

        window_.blit(matchbar_, (235, 60))
        window_.blit(matches['Table 34']['Home'].ol_logo, (245, 80))
        window_.blit(matches['Table 34']['Away'].ol_logo, (245, 320))
        window_.blit(table34_, (248, 225))

        window_.blit(matchbar_, (65, 60))
        window_.blit(matches['Table 2']['Home'].ol_logo, (75, 80))
        window_.blit(matches['Table 2']['Away'].ol_logo, (75, 320))
        window_.blit(recording_, (97, 200))
        window_.blit(table2_, (78, 225))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_ = pygame.mouse.get_pos()

                print(click_)

                # match1
                if click_[0] < 220 and click_[0] > 65 and click_[1] < 430 and click_[1] > 60:
                    print('match1')
                    match(window_, matches['Table 2']['Home'], matches['Table 2']['Away'])
                    match1_played = 1

                # match2
                if click_[0] < 390 and click_[0] > 235 and click_[1] < 430 and click_[1] > 60:
                    print('match2')
                    match(window_, matches['Table 34']['Home'], matches['Table 34']['Away'])
                    match2_played = 1

                # match3
                if click_[0] < 560 and click_[0] > 405 and click_[1] < 430 and click_[1] > 60:
                    print('match3')
                    match(window_, matches['Table 8']['Home'], matches['Table 8']['Away'])
                    match3_played = 1

                # match4
                if click_[0] < 730 and click_[0] > 575 and click_[1] < 430 and click_[1] > 60:
                    print('match4')
                    match(window_, matches['Table 9']['Home'], matches['Table 9']['Away'])
                    match4_played = 1


def match(window_, home_, away_):
    home_roster = []
    away_roster = []
    for player_ in home_.roster:
        home_roster.append(player_)

    for player_ in away_.roster:
        away_roster.append(player_)

    tableborder_ = pygame.image.load('tableborder.png')
    background_ = pygame.image.load('bed.png')
    scoresheet = pygame.image.load('scoresheet-75.png')
    threefoulbutton = pygame.image.load('largecueball-100.png')
    threefoulantibutton = pygame.image.load('chalk-100.png')
    breaker = pygame.image.load('breakrack-100.png')

    textfont = pygame.font.Font('arialbd.ttf', 26)

    cueball_ = pygame.image.load('cueball-100.png')
    cueball_2 = pygame.image.load('cueball-25.png')

    roundone_text = 'Round One'
    text_title = textfont.render(roundone_text, False, (255, 207, 53))

    window_.blit(background_, (0, 0))
    y = 265
    for square_ in range(3):
        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
        y += 45
    y = 265
    for square_ in range(3):
        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
        y += 45
    window_.blit(text_title, (330, 400))
    window_.blit(cueball_, (350, 265))

    # if click
    '''
    x = 75
    y = 225
    for player_ in home_roster:
        textSurface = textfont.render(player_.name,False,(0,0,0))
        window_.blit(textSurface,(x,y))
        y -= 35
    x = 465
    y = 225
    for player_ in away_roster:
        textSurface = textfont.render(player_.name,False,(0,0,0))
        window_.blit(textSurface,(x,y))
        y-=35
    '''

    '''
    x = 400
    y = 70
    for player_ in away_roster:
        textSurface = textfont.render(player_.name,False,(0,0,0))
        window_.blit(textSurface,(x,y))
        y += 30
    '''
    window_.blit(tableborder_, (0, 0))
    pygame.display.update()

    pick_ = 1
    lineup1 = 0
    lineup2 = 0
    lineup3 = 0
    lineup4 = 0
    lineup5 = 0
    lineup6 = 0
    home_lineup = []
    away_lineup = []
    submit = 0
    submit2 = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_ = pygame.mouse.get_pos()
                print(click_)

                # Player1
                if click_[0] < 340 and click_[0] > 70 and click_[1] < 305 and click_[1] > 265 and lineup1 == 0:
                    x = 75
                    y = 270
                    pygame.draw.rect(window_, (255, 255, 255), (70, 265, 270, 40))
                    pick_ += 1
                    if pick_ + 1 > len(home_roster):
                        pick_ = 0
                    textSurface = textfont.render(home_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (x, y))
                    y -= 35
                    if lineup2 == 0:
                        window_.blit(cueball_, (350, 265))
                        window_.blit(cueball_2, (350, 315))

                    pygame.display.update()
                    lineup2 = 1

                # Player2
                if click_[0] < 340 and click_[0] > 70 and click_[1] < 350 and click_[1] > 310 and lineup2 == 1:
                    if lineup1 == 0:
                        home_lineup.append(home_roster.pop(pick_))
                    pick = 0
                    x = 75
                    y = 270
                    pick_ += 1
                    if pick_ + 1 > len(home_roster):
                        pick_ = 0
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    textSurface = textfont.render(home_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (x, 315))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_, (350, 310))
                    window_.blit(cueball_2, (350, 355))
                    window_.blit(tableborder_, (0, 0))
                    pygame.display.update()
                    lineup1 = 1
                    lineup3 = 1

                # Player3
                if click_[0] < 340 and click_[0] > 70 and click_[1] < 395 and click_[1] > 355 and lineup3 == 1:
                    if lineup2 == 1:
                        home_lineup.append(home_roster.pop(pick_))
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    pygame.draw.rect(window_, (255, 255, 255), (70, 310, 270, 40))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    home_lineup_two = textfont.render(home_lineup[1].name, False, (0, 0, 0))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(home_lineup_two, (75, 315))
                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_2, (350, 310))
                    window_.blit(cueball_, (350, 355))
                    # window_.blit(cueball_2,(410,265))

                    pygame.draw.rect(window_, (255, 0, 0), (70, 200, 90, 50))
                    window_.blit(tableborder_, (0, 0))

                    x = 75
                    y = 270
                    pick_ += 1
                    if pick_ + 1 > len(home_roster):
                        pick_ = 0
                    textSurface = textfont.render(home_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (x, 360))
                    y -= 35
                    pygame.display.update()
                    lineup2 = 0
                    submit = 1

                if click_[0] > 70 and click_[0] < 160 and click_[1] > 200 and click_[1] < 250 and submit == 1:
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    pygame.draw.rect(window_, (255, 255, 255), (70, 310, 270, 40))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    home_lineup_two = textfont.render(home_lineup[1].name, False, (0, 0, 0))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(home_lineup_two, (75, 315))
                    textSurface = textfont.render(home_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (75, 360))

                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_2, (350, 310))
                    window_.blit(cueball_2, (350, 355))
                    window_.blit(cueball_, (410, 265))
                    # window_.blit(cueball_2,(410,310))
                    window_.blit(tableborder_, (0, 0))
                    pygame.draw.rect(window_, (0, 255, 0), (70, 200, 90, 50))
                    lineup4 = 1
                    pygame.display.update()
                    submit = 0
                    lineup3 = 0
                    home_lineup.append(home_roster.pop(pick_))

                # Player4
                if click_[0] < 730 and click_[0] > 460 and click_[1] < 305 and click_[1] > 265 and lineup4 == 1:
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    pygame.draw.rect(window_, (255, 255, 255), (70, 310, 270, 40))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    home_lineup_two = textfont.render(home_lineup[1].name, False, (0, 0, 0))
                    home_lineup_three = textfont.render(home_lineup[2].name, False, (0, 0, 0))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(home_lineup_two, (75, 315))
                    window_.blit(home_lineup_three, (75, 360))

                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_2, (350, 310))
                    window_.blit(cueball_2, (350, 355))
                    window_.blit(cueball_, (410, 265))
                    window_.blit(cueball_2, (410, 310))
                    pygame.draw.rect(window_, (0, 255, 0), (70, 200, 90, 50))
                    window_.blit(tableborder_, (0, 0))

                    pick_ += 1
                    if pick_ + 1 > len(away_roster):
                        pick_ = 0
                    textSurface = textfont.render(away_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (465, 270))
                    pygame.display.update()
                    lineup3 = 0
                    lineup5 = 1

                # Player5
                if click_[0] < 730 and click_[0] > 460 and click_[1] < 350 and click_[1] > 310 and lineup5 == 1:
                    if lineup4 == 1:
                        away_lineup.append(away_roster.pop(pick_))
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    pygame.draw.rect(window_, (255, 255, 255), (70, 310, 270, 40))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    home_lineup_two = textfont.render(home_lineup[1].name, False, (0, 0, 0))
                    home_lineup_three = textfont.render(home_lineup[2].name, False, (0, 0, 0))
                    away_lineup_one = textfont.render(away_lineup[0].name, False, (0, 0, 0))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(home_lineup_two, (75, 315))
                    window_.blit(home_lineup_three, (75, 360))
                    window_.blit(away_lineup_one, (465, 270))

                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_2, (350, 310))
                    window_.blit(cueball_2, (350, 355))
                    window_.blit(cueball_2, (410, 265))
                    window_.blit(cueball_, (410, 310))
                    window_.blit(cueball_2, (410, 355))
                    pygame.draw.rect(window_, (0, 255, 0), (70, 200, 90, 50))

                    window_.blit(tableborder_, (0, 0))

                    pick_ += 1
                    if pick_ + 1 > len(away_roster):
                        pick_ = 0
                    textSurface = textfont.render(away_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (465, 315))
                    y -= 35
                    pygame.display.update()
                    lineup4 = 0
                    lineup6 = 1

                # Player6
                if click_[0] < 730 and click_[0] > 460 and click_[1] < 395 and click_[1] > 355 and lineup6 == 1:
                    if lineup5 == 1:
                        away_lineup.append(away_roster.pop(pick_))
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    pygame.draw.rect(window_, (255, 255, 255), (70, 310, 270, 40))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    home_lineup_two = textfont.render(home_lineup[1].name, False, (0, 0, 0))
                    home_lineup_three = textfont.render(home_lineup[2].name, False, (0, 0, 0))
                    away_lineup_one = textfont.render(away_lineup[0].name, False, (0, 0, 0))
                    away_lineup_two = textfont.render(away_lineup[1].name, False, (0, 0, 0))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(home_lineup_two, (75, 315))
                    window_.blit(home_lineup_three, (75, 360))
                    window_.blit(away_lineup_one, (465, 270))
                    window_.blit(away_lineup_two, (465, 315))

                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_2, (350, 310))
                    window_.blit(cueball_2, (350, 355))
                    window_.blit(cueball_2, (410, 265))
                    window_.blit(cueball_2, (410, 310))
                    window_.blit(cueball_, (410, 355))
                    pygame.draw.rect(window_, (0, 255, 0), (70, 200, 90, 50))
                    pygame.draw.rect(window_, (255, 0, 0), (640, 200, 90, 50))
                    window_.blit(tableborder_, (0, 0))

                    x = 75
                    y = 270
                    pick_ += 1
                    if pick_ + 1 > len(away_roster):
                        pick_ = 0

                    textSurface = textfont.render(away_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (465, 360))
                    y -= 35
                    pygame.display.update()
                    lineup5 = 0
                    submit2 = 1

                if click_[0] > 640 and click_[0] < 730 and click_[1] > 200 and click_[1] < 250 and submit2 == 1:
                    window_.blit(background_, (0, 0))
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (460, y, 270, 40))
                        y += 45
                    y = 265
                    for square_ in range(3):
                        pygame.draw.rect(window_, (255, 255, 255), (70, y, 270, 40))
                        y += 45
                    window_.blit(text_title, (330, 400))
                    pygame.draw.rect(window_, (255, 255, 255), (70, 310, 270, 40))
                    y -= 35
                    home_lineup_one = textfont.render(home_lineup[0].name, False, (0, 0, 0))
                    home_lineup_two = textfont.render(home_lineup[1].name, False, (0, 0, 0))
                    home_lineup_three = textfont.render(home_lineup[2].name, False, (0, 0, 0))
                    away_lineup_one = textfont.render(away_lineup[0].name, False, (0, 0, 0))
                    away_lineup_two = textfont.render(away_lineup[1].name, False, (0, 0, 0))
                    textSurface = textfont.render(away_roster[pick_].name, False, (0, 0, 0))
                    window_.blit(textSurface, (465, 360))
                    window_.blit(home_lineup_one, (75, 270))
                    window_.blit(home_lineup_two, (75, 315))
                    window_.blit(home_lineup_three, (75, 360))
                    window_.blit(away_lineup_one, (465, 270))
                    window_.blit(away_lineup_two, (465, 315))

                    window_.blit(cueball_2, (350, 265))
                    window_.blit(cueball_2, (350, 310))
                    window_.blit(cueball_2, (350, 355))
                    window_.blit(cueball_2, (410, 265))
                    window_.blit(cueball_2, (410, 310))
                    window_.blit(cueball_2, (410, 355))
                    window_.blit(tableborder_, (0, 0))
                    pygame.draw.rect(window_, (0, 255, 0), (70, 200, 90, 50))
                    pygame.draw.rect(window_, (0, 255, 0), (640, 200, 90, 50))
                    pygame.display.update()
                    submit2 = 0
                    lineup6 = 0
                    away_lineup.append(away_roster.pop(pick_))

                    match_path = (
                    (0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0), (0, 2), (1, 0), (2, 1), (0, 0), (1, 1), (2, 2),
                    (0, 1), (1, 2), (2, 0))
                    final_score = {'home': home_.ID, 'away': away_.ID}
                    for idx_, item_ in enumerate(match_path):
                        final_score[str(idx_ + 1)] = match1(window_, home_, away_, home_lineup[item_[0]],
                                                            away_lineup[item_[1]], idx_ + 1, final_score, home_lineup,
                                                            away_lineup)
                        # if idx_+1 == 3:

                    print('match over!')
                    print(final_score)
                    conwaystats(window_, final_score, home_lineup, away_lineup)
                    # scoresheet_function(window_,final_score,home_lineup,away_lineup,15)

                    # mainmenu(window_)


def scoresheet_function(win_, final_score, home_lineup, away_lineup, round_):
    print('scoresheet')
    tableborder_ = pygame.image.load('tableborder.png')
    bigscoresheet_ = pygame.image.load('bigscoresheet.png')
    background_ = pygame.image.load('bed.png')
    win_.blit(background_, (0, 0))
    win_.blit(bigscoresheet_, (0, 0))

    textSurface_ = pygame.font.SysFont('arial', 14)
    h_team_name = textSurface_.render(eval(final_score['home']).teamname, False, (0, 0, 0))
    a_team_name = textSurface_.render(eval(final_score['away']).teamname, False, (0, 0, 0))
    gamewin_ = textSurface_.render('W', False, (0, 255, 0))
    gameloss_ = textSurface_.render('L', False, (255, 0, 0))
    h_player_1 = textSurface_.render(home_lineup[0].name, False, (0, 0, 0))
    h_player_2 = textSurface_.render(home_lineup[1].name, False, (0, 0, 0))
    h_player_3 = textSurface_.render(home_lineup[2].name, False, (0, 0, 0))
    a_player_1 = textSurface_.render(away_lineup[0].name, False, (0, 0, 0))
    a_player_2 = textSurface_.render(away_lineup[1].name, False, (0, 0, 0))
    a_player_3 = textSurface_.render(away_lineup[2].name, False, (0, 0, 0))

    win_.blit(h_team_name, (200, 100))

    win_.blit(h_player_1, (170, 137))

    if '1' in final_score:
        if final_score['1'][1][2] == 1:
            win_.blit(gamewin_, (380, 138))
            win_.blit(textSurface_.render(str(final_score['1'][1][0]), False, (0, 0, 0)), (407, 138))
        if final_score['1'][1][2] == 0:
            win_.blit(gameloss_, (382, 138))
            win_.blit(textSurface_.render(str(final_score['1'][1][0]), False, (0, 0, 0)), (407, 138))

    win_.blit(h_player_2, (170, 156))

    if '2' in final_score:
        if final_score['2'][1][2] == 1:
            win_.blit(gamewin_, (380, 157))
            win_.blit(textSurface_.render(str(final_score['2'][1][0]), False, (0, 0, 0)), (407, 157))
        if final_score['2'][1][2] == 0:
            win_.blit(gameloss_, (382, 157))
            win_.blit(textSurface_.render(str(final_score['2'][1][0]), False, (0, 0, 0)), (407, 157))

    win_.blit(h_player_3, (170, 175))

    if '3' in final_score:
        if final_score['3'][1][2] == 1:
            win_.blit(gamewin_, (380, 176))
            win_.blit(textSurface_.render(str(final_score['3'][1][0]), False, (0, 0, 0)), (407, 176))
        if final_score['3'][1][2] == 0:
            win_.blit(gameloss_, (382, 176))
            win_.blit(textSurface_.render(str(final_score['3'][1][0]), False, (0, 0, 0)), (407, 176))

    # if
    win_.blit(h_player_1, (170, 196))

    if '4' in final_score:
        if final_score['4'][1][2] == 1:
            win_.blit(gamewin_, (380, 197))
            win_.blit(textSurface_.render(str(final_score['4'][1][0]), False, (0, 0, 0)), (407, 197))
        if final_score['4'][1][2] == 0:
            win_.blit(gameloss_, (382, 197))
            win_.blit(textSurface_.render(str(final_score['4'][1][0]), False, (0, 0, 0)), (407, 197))

    win_.blit(h_player_2, (170, 215))

    if '5' in final_score:
        if final_score['5'][1][2] == 1:
            win_.blit(gamewin_, (380, 216))
            win_.blit(textSurface_.render(str(final_score['5'][1][0]), False, (0, 0, 0)), (407, 216))
        if final_score['5'][1][2] == 0:
            win_.blit(gameloss_, (382, 216))
            win_.blit(textSurface_.render(str(final_score['5'][1][0]), False, (0, 0, 0)), (407, 216))

    win_.blit(h_player_3, (170, 234))

    if '6' in final_score:
        if final_score['6'][1][2] == 1:
            win_.blit(gamewin_, (380, 235))
            win_.blit(textSurface_.render(str(final_score['6'][1][0]), False, (0, 0, 0)), (407, 235))
        if final_score['6'][1][2] == 0:
            win_.blit(gameloss_, (382, 235))
            win_.blit(textSurface_.render(str(final_score['6'][1][0]), False, (0, 0, 0)), (407, 235))

    win_.blit(h_player_1, (170, 255))

    if '7' in final_score:
        if final_score['7'][1][2] == 1:
            win_.blit(gamewin_, (380, 256))
            win_.blit(textSurface_.render(str(final_score['7'][1][0]), False, (0, 0, 0)), (407, 256))
        if final_score['7'][1][2] == 0:
            win_.blit(gameloss_, (382, 256))
            win_.blit(textSurface_.render(str(final_score['7'][1][0]), False, (0, 0, 0)), (407, 256))

    win_.blit(h_player_2, (170, 274))

    if '8' in final_score:
        if final_score['8'][1][2] == 1:
            win_.blit(gamewin_, (380, 275))
            win_.blit(textSurface_.render(str(final_score['8'][1][0]), False, (0, 0, 0)), (407, 275))
        if final_score['8'][1][2] == 0:
            win_.blit(gameloss_, (382, 275))
            win_.blit(textSurface_.render(str(final_score['8'][1][0]), False, (0, 0, 0)), (407, 275))

    win_.blit(h_player_3, (170, 293))

    if '9' in final_score:
        if final_score['9'][1][2] == 1:
            win_.blit(gamewin_, (380, 294))
            win_.blit(textSurface_.render(str(final_score['9'][1][0]), False, (0, 0, 0)), (407, 294))
        if final_score['9'][1][2] == 0:
            win_.blit(gameloss_, (382, 294))
            win_.blit(textSurface_.render(str(final_score['9'][1][0]), False, (0, 0, 0)), (407, 294))

    win_.blit(h_player_1, (170, 315))

    if '10' in final_score:
        if final_score['10'][1][2] == 1:
            win_.blit(gamewin_, (380, 316))
            win_.blit(textSurface_.render(str(final_score['10'][1][0]), False, (0, 0, 0)), (407, 316))
        if final_score['10'][1][2] == 0:
            win_.blit(gameloss_, (382, 316))
            win_.blit(textSurface_.render(str(final_score['10'][1][0]), False, (0, 0, 0)), (407, 316))

    win_.blit(h_player_2, (170, 333))

    if '11' in final_score:
        if final_score['11'][1][2] == 1:
            win_.blit(gamewin_, (380, 334))
            win_.blit(textSurface_.render(str(final_score['11'][1][0]), False, (0, 0, 0)), (407, 334))
        if final_score['11'][1][2] == 0:
            win_.blit(gameloss_, (382, 334))
            win_.blit(textSurface_.render(str(final_score['11'][1][0]), False, (0, 0, 0)), (407, 334))

    win_.blit(h_player_3, (170, 352))

    if '12' in final_score:
        if final_score['12'][1][2] == 1:
            win_.blit(gamewin_, (380, 353))
            win_.blit(textSurface_.render(str(final_score['12'][1][0]), False, (0, 0, 0)), (407, 353))
        if final_score['12'][1][2] == 0:
            win_.blit(gameloss_, (382, 353))
            win_.blit(textSurface_.render(str(final_score['12'][1][0]), False, (0, 0, 0)), (407, 353))

    win_.blit(h_player_1, (170, 374))

    if '13' in final_score:
        if final_score['13'][1][2] == 1:
            win_.blit(gamewin_, (380, 375))
            win_.blit(textSurface_.render(str(final_score['13'][1][0]), False, (0, 0, 0)), (407, 375))
        if final_score['13'][1][2] == 0:
            win_.blit(gameloss_, (382, 375))
            win_.blit(textSurface_.render(str(final_score['13'][1][0]), False, (0, 0, 0)), (407, 375))

    win_.blit(h_player_2, (170, 392))

    if '14' in final_score:
        if final_score['14'][1][2] == 1:
            win_.blit(gamewin_, (380, 393))
            win_.blit(textSurface_.render(str(final_score['14'][1][0]), False, (0, 0, 0)), (407, 393))
        if final_score['14'][1][2] == 0:
            win_.blit(gameloss_, (382, 393))
            win_.blit(textSurface_.render(str(final_score['14'][1][0]), False, (0, 0, 0)), (407, 393))

    win_.blit(h_player_3, (170, 411))

    if '15' in final_score:
        if final_score['15'][1][2] == 1:
            win_.blit(gamewin_, (380, 412))
            win_.blit(textSurface_.render(str(final_score['15'][1][0]), False, (0, 0, 0)), (407, 412))
        if final_score['15'][1][2] == 0:
            win_.blit(gameloss_, (382, 412))
            win_.blit(textSurface_.render(str(final_score['15'][1][0]), False, (0, 0, 0)), (407, 412))

    win_.blit(a_team_name, (480, 100))

    win_.blit(a_player_1, (450, 137))

    if '1' in final_score:
        if final_score['1'][1][3] == 1:
            win_.blit(gamewin_, (660, 138))
            win_.blit(textSurface_.render(str(final_score['1'][1][1]), False, (0, 0, 0)), (687, 138))
        if final_score['1'][1][3] == 0:
            win_.blit(gameloss_, (662, 138))
            win_.blit(textSurface_.render(str(final_score['1'][1][1]), False, (0, 0, 0)), (687, 138))

    win_.blit(a_player_2, (450, 156))

    if '2' in final_score:
        if final_score['2'][1][3] == 1:
            win_.blit(gamewin_, (660, 157))
            win_.blit(textSurface_.render(str(final_score['2'][1][1]), False, (0, 0, 0)), (687, 157))
        if final_score['2'][1][3] == 0:
            win_.blit(gameloss_, (662, 157))
            win_.blit(textSurface_.render(str(final_score['2'][1][1]), False, (0, 0, 0)), (687, 157))

    win_.blit(a_player_3, (450, 175))

    if '3' in final_score:
        if final_score['3'][1][3] == 1:
            win_.blit(gamewin_, (660, 176))
            win_.blit(textSurface_.render(str(final_score['3'][1][1]), False, (0, 0, 0)), (687, 176))
        if final_score['3'][1][3] == 0:
            win_.blit(gameloss_, (662, 176))
            win_.blit(textSurface_.render(str(final_score['3'][1][1]), False, (0, 0, 0)), (687, 176))

    # if
    win_.blit(a_player_2, (450, 196))

    if '4' in final_score:
        if final_score['4'][1][3] == 1:
            win_.blit(gamewin_, (660, 197))
            win_.blit(textSurface_.render(str(final_score['4'][1][1]), False, (0, 0, 0)), (687, 197))
        if final_score['4'][1][3] == 0:
            win_.blit(gameloss_, (662, 197))
            win_.blit(textSurface_.render(str(final_score['4'][1][1]), False, (0, 0, 0)), (687, 197))

    win_.blit(a_player_3, (450, 215))

    if '5' in final_score:
        if final_score['5'][1][3] == 1:
            win_.blit(gamewin_, (660, 216))
            win_.blit(textSurface_.render(str(final_score['5'][1][1]), False, (0, 0, 0)), (687, 216))
        if final_score['5'][1][3] == 0:
            win_.blit(gameloss_, (662, 216))
            win_.blit(textSurface_.render(str(final_score['5'][1][1]), False, (0, 0, 0)), (687, 216))

    win_.blit(a_player_1, (450, 234))

    if '6' in final_score:
        if final_score['6'][1][3] == 1:
            win_.blit(gamewin_, (660, 235))
            win_.blit(textSurface_.render(str(final_score['6'][1][1]), False, (0, 0, 0)), (687, 235))
        if final_score['6'][1][3] == 0:
            win_.blit(gameloss_, (662, 235))
            win_.blit(textSurface_.render(str(final_score['6'][1][1]), False, (0, 0, 0)), (687, 235))

    win_.blit(a_player_3, (450, 255))

    if '7' in final_score:
        if final_score['7'][1][3] == 1:
            win_.blit(gamewin_, (660, 256))
            win_.blit(textSurface_.render(str(final_score['7'][1][1]), False, (0, 0, 0)), (687, 256))
        if final_score['7'][1][3] == 0:
            win_.blit(gameloss_, (662, 256))
            win_.blit(textSurface_.render(str(final_score['7'][1][1]), False, (0, 0, 0)), (687, 256))

    win_.blit(a_player_1, (450, 274))

    if '8' in final_score:
        if final_score['8'][1][3] == 1:
            win_.blit(gamewin_, (660, 275))
            win_.blit(textSurface_.render(str(final_score['8'][1][1]), False, (0, 0, 0)), (687, 275))
        if final_score['8'][1][3] == 0:
            win_.blit(gameloss_, (662, 275))
            win_.blit(textSurface_.render(str(final_score['8'][1][1]), False, (0, 0, 0)), (687, 275))

    win_.blit(a_player_2, (450, 293))

    if '9' in final_score:
        if final_score['9'][1][3] == 1:
            win_.blit(gamewin_, (660, 294))
            win_.blit(textSurface_.render(str(final_score['9'][1][1]), False, (0, 0, 0)), (687, 294))
        if final_score['9'][1][3] == 0:
            win_.blit(gameloss_, (662, 294))
            win_.blit(textSurface_.render(str(final_score['9'][1][1]), False, (0, 0, 0)), (687, 294))

    win_.blit(a_player_1, (450, 315))

    if '10' in final_score:
        if final_score['10'][1][3] == 1:
            win_.blit(gamewin_, (660, 316))
            win_.blit(textSurface_.render(str(final_score['10'][1][1]), False, (0, 0, 0)), (687, 316))
        if final_score['10'][1][3] == 0:
            win_.blit(gameloss_, (662, 316))
            win_.blit(textSurface_.render(str(final_score['10'][1][1]), False, (0, 0, 0)), (687, 316))

    win_.blit(a_player_2, (450, 333))

    if '11' in final_score:
        if final_score['11'][1][3] == 1:
            win_.blit(gamewin_, (660, 334))
            win_.blit(textSurface_.render(str(final_score['11'][1][1]), False, (0, 0, 0)), (687, 334))
        if final_score['11'][1][3] == 0:
            win_.blit(gameloss_, (662, 334))
            win_.blit(textSurface_.render(str(final_score['11'][1][1]), False, (0, 0, 0)), (687, 334))

    win_.blit(a_player_3, (450, 352))

    if '12' in final_score:
        if final_score['12'][1][3] == 1:
            win_.blit(gamewin_, (660, 353))
            win_.blit(textSurface_.render(str(final_score['12'][1][1]), False, (0, 0, 0)), (687, 353))
        if final_score['12'][1][3] == 0:
            win_.blit(gameloss_, (662, 353))
            win_.blit(textSurface_.render(str(final_score['12'][1][1]), False, (0, 0, 0)), (687, 353))

    win_.blit(a_player_2, (450, 374))

    if '13' in final_score:
        if final_score['13'][1][3] == 1:
            win_.blit(gamewin_, (660, 375))
            win_.blit(textSurface_.render(str(final_score['13'][1][1]), False, (0, 0, 0)), (687, 375))
        if final_score['13'][1][3] == 0:
            win_.blit(gameloss_, (662, 375))
            win_.blit(textSurface_.render(str(final_score['13'][1][1]), False, (0, 0, 0)), (687, 375))

    win_.blit(a_player_3, (450, 392))

    if '14' in final_score:
        if final_score['14'][1][3] == 1:
            win_.blit(gamewin_, (660, 393))
            win_.blit(textSurface_.render(str(final_score['14'][1][1]), False, (0, 0, 0)), (687, 393))
        if final_score['14'][1][3] == 0:
            win_.blit(gameloss_, (662, 393))
            win_.blit(textSurface_.render(str(final_score['14'][1][1]), False, (0, 0, 0)), (687, 393))

    win_.blit(a_player_1, (450, 411))

    if '15' in final_score:
        if final_score['15'][1][3] == 1:
            win_.blit(gamewin_, (660, 412))
            win_.blit(textSurface_.render(str(final_score['15'][1][1]), False, (0, 0, 0)), (687, 412))
        if final_score['15'][1][3] == 0:
            win_.blit(gameloss_, (662, 412))
            win_.blit(textSurface_.render(str(final_score['15'][1][1]), False, (0, 0, 0)), (687, 412))

    win_.blit(tableborder_, (0, 0))
    pygame.display.update()
    if round_ == 15:
        pygame.image.save(win_,
                          eval(final_score['home']).teamname + '-vs-' + eval(final_score['away']).teamname + '.png')
    scoring = True
    while scoring:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                scoring = False


def match1(window_, home_, away_, home_player, away_player, round_, score_, home_lineup, away_lineup):
    home_player.ol_loadstats()
    away_player.ol_loadstats()

    soneb = 'on'
    stwob = 'on'
    sthreeb = 'on'
    sfourb = 'on'
    sfiveb = 'on'
    ssixb = 'on'
    ssevenb = 'on'
    seightb = 'on'
    snineb = 'on'

    honeb = 'off'
    htwob = 'off'
    hthreeb = 'off'
    hfourb = 'off'
    hfiveb = 'off'
    hsixb = 'off'
    hsevenb = 'off'
    heightb = 'off'
    hnineb = 'off'

    h1f = 'off'
    h2f = 'off'
    h3f = 'off'

    aoneb = 'off'
    atwob = 'off'
    athreeb = 'off'
    afourb = 'off'
    afiveb = 'off'
    asixb = 'off'
    asevenb = 'off'
    aeightb = 'off'
    anineb = 'off'

    a1f = 'off'
    a2f = 'off'
    a3f = 'off'

    tableborder_ = pygame.image.load('tableborder.png')
    background_ = pygame.image.load('bed.png')
    scoresheet = pygame.image.load('scoresheet-75.png')
    threefoulbutton = pygame.image.load('largecueball-100.png')
    threefoulantibutton = pygame.image.load('chalk-100.png')
    breaker = pygame.image.load('breakrack-100.png')

    textfont = pygame.font.Font('arialbd.ttf', 26)

    cueball_ = pygame.image.load('cueball-100.png')
    cueball_2 = pygame.image.load('cueball-25.png')
    home_breaking_rounds = (1, 2, 3, 7, 8, 9, 13, 14, 15)
    if round_ in home_breaking_rounds:
        home_player.shooting = 'on'
        home_break = True
        away_player.shooting = 'off'
    else:
        home_player.shooting = 'off'
        away_player.shooting = 'on'
        away_break = True

    gameover = True
    turn_ = 0

    while gameover:
        checking_ = True
        window_.blit(background_, (0, 0))

        window_.blit(scoring_buttons.rackofnine['1'][soneb], (95, 375))
        window_.blit(scoring_buttons.rackofnine['2'][stwob], (165, 375))
        window_.blit(scoring_buttons.rackofnine['3'][sthreeb], (235, 375))
        window_.blit(scoring_buttons.rackofnine['4'][sfourb], (305, 375))
        window_.blit(scoring_buttons.rackofnine['5'][sfiveb], (375, 375))
        window_.blit(scoring_buttons.rackofnine['6'][ssixb], (445, 375))
        window_.blit(scoring_buttons.rackofnine['7'][ssevenb], (515, 375))
        window_.blit(scoring_buttons.rackofnine['8'][seightb], (585, 375))
        window_.blit(scoring_buttons.rackofnine['9'][snineb], (655, 375))

        ##HOME
        window_.blit(home_player.ol_card[home_player.card_selection][home_player.shooting], (60, 45))
        window_.blit(home_player.ol_cue[home_player.cue_selection][home_player.shooting], (70, 55))

        window_.blit(home_player.ol_scorecard['1'][honeb], (65, 337))
        window_.blit(home_player.ol_scorecard['2'][htwob], (88, 337))
        window_.blit(home_player.ol_scorecard['3'][hthreeb], (111, 337))
        window_.blit(home_player.ol_scorecard['4'][hfourb], (134, 337))
        window_.blit(home_player.ol_scorecard['5'][hfiveb], (156, 337))
        window_.blit(home_player.ol_scorecard['6'][hsixb], (179, 337))
        window_.blit(home_player.ol_scorecard['7'][hsevenb], (202, 337))
        window_.blit(home_player.ol_scorecard['8'][heightb], (225, 337))
        window_.blit(home_player.ol_scorecard['9'][hnineb], (248, 337))

        window_.blit(home_player.ol_threefoul['1'][h1f], (100, 55))
        window_.blit(home_player.ol_threefoul['2'][h2f], (145, 55))
        window_.blit(home_player.ol_threefoul['3'][h3f], (190, 55))

        ##AWAY
        window_.blit(away_player.ol_card[away_player.card_selection][away_player.shooting], (515, 45))
        window_.blit(away_player.ol_cue[away_player.cue_selection][away_player.shooting], (525, 55))

        window_.blit(away_player.ol_scorecard['1'][aoneb], (519, 337))
        window_.blit(away_player.ol_scorecard['2'][atwob], (542, 337))
        window_.blit(away_player.ol_scorecard['3'][athreeb], (565, 337))
        window_.blit(away_player.ol_scorecard['4'][afourb], (588, 337))
        window_.blit(away_player.ol_scorecard['5'][afiveb], (610, 337))
        window_.blit(away_player.ol_scorecard['6'][asixb], (633, 337))
        window_.blit(away_player.ol_scorecard['7'][asevenb], (656, 337))
        window_.blit(away_player.ol_scorecard['8'][aeightb], (679, 337))
        window_.blit(away_player.ol_scorecard['9'][anineb], (702, 337))

        window_.blit(away_player.ol_threefoul['1'][a1f], (555, 55))
        window_.blit(away_player.ol_threefoul['2'][a2f], (600, 55))
        window_.blit(away_player.ol_threefoul['3'][a3f], (645, 55))

        window_.blit(home_.ol_matchscore[str(home_.s_match_score)], (310, 145))
        # dash = pygame.image.load('dash.png')
        # window_.blit(dash,(375,165))
        window_.blit(away_.ol_matchscore[str(away_.s_match_score)], (420, 145))

        # fix this
        mine = pygame.font.SysFont('Trebuchet', 30)
        mine1 = pygame.font.SysFont('arial', 16)
        textSurface = mine.render(home_player.name, False, (0, 0, 0))
        textSurface1 = mine1.render(home_.teamname, False, (0, 0, 0))
        window_.blit(textSurface, (70, 295))
        window_.blit(textSurface1, (70, 313))
        textSurface = mine.render(away_player.name, False, (0, 0, 0))
        textSurface1 = mine1.render(away_.teamname, False, (0, 0, 0))
        window_.blit(textSurface, (530, 295))
        window_.blit(textSurface1, (530, 313))

        mine1 = pygame.font.SysFont('arial', 16)
        home_stats_view = mine1.render('Record: ' + str(home_player.s_gameswon) + ' / ' + str(home_player.s_gameslost),
                                       False, (0, 0, 0))
        home_stats_view2 = mine1.render('Winstreak: ' + str(home_player.s_gameswonstreak), False, (0, 0, 0))
        home_stats_view3 = mine1.render('Career Balls Made: ' + str(home_player.s_ballsmade), False, (0, 0, 0))
        home_stats_view4 = mine1.render('Ave. Balls/Game: ' + str(home_player.s_ave_ballsmade), False, (0, 0, 0))
        home_stats_view5 = mine1.render('High Winstreak: ' + str(home_player.s_highgameswonstreak), False, (0, 0, 0))
        if home_player.s_bihgiven != 0 and home_player.s_gamesplayed != 0:
            home_stats_view6 = mine1.render(
                'Foul/Game: ' + str("{:.2f}".format(home_player.s_bihgiven / home_player.s_gamesplayed)), False,
                (0, 0, 0))
            window_.blit(home_stats_view6, (90, 175))
        window_.blit(home_stats_view, (90, 100))
        window_.blit(home_stats_view2, (90, 115))
        window_.blit(home_stats_view5, (90, 130))
        window_.blit(home_stats_view4, (90, 145))
        window_.blit(home_stats_view3, (90, 160))
        away_stats_view = mine1.render('Record: ' + str(away_player.s_gameswon) + ' / ' + str(away_player.s_gameslost),
                                       False, (0, 0, 0))
        away_stats_view2 = mine1.render('Winstreak: ' + str(away_player.s_gameswonstreak), False, (0, 0, 0))
        away_stats_view3 = mine1.render('Career Balls Made: ' + str(away_player.s_ballsmade), False, (0, 0, 0))
        away_stats_view4 = mine1.render('Ave. Balls/Game: ' + str(away_player.s_ave_ballsmade), False, (0, 0, 0))
        away_stats_view5 = mine1.render('High Winstreak: ' + str(away_player.s_highgameswonstreak), False, (0, 0, 0))
        if away_player.s_bihgiven != 0 and away_player.s_gamesplayed != 0:
            away_stats_view6 = mine1.render(
                'Foul/Game: ' + str("{:.2f}".format(away_player.s_bihgiven / away_player.s_gamesplayed)), False,
                (0, 0, 0))
            window_.blit(away_stats_view6, (545, 175))
        window_.blit(away_stats_view, (545, 100))
        window_.blit(away_stats_view2, (545, 115))
        window_.blit(away_stats_view5, (545, 130))
        window_.blit(away_stats_view4, (545, 145))
        window_.blit(away_stats_view3, (545, 160))

        window_.blit(threefoulbutton, (310, 55))

        window_.blit(threefoulantibutton, (410, 55))

        window_.blit(scoresheet, (308, 215))

        if round_ in home_breaking_rounds:
            window_.blit(breaker, (190, 205))
        else:
            window_.blit(breaker, (650, 205))

        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_ = pygame.mouse.get_pos()
                print(click_)

                '''
                Foul
                '''
                if click_[0] > 310 and click_[0] < 385 and click_[1] > 55 and click_[
                    1] < 125 and home_player.shooting == 'on':
                    checking_ = True
                    check_window = pygame.image.load('confirmationwindow_foul.png')
                    while checking_:
                        window_.blit(check_window, (0, 0))
                        font_setup = pygame.font.SysFont('arial', 16)
                        home_name_text = font_setup.render(home_player.firstname + ' Fouled?', False, (0, 0, 0))
                        window_.blit(home_name_text, (395, 113))
                        pygame.display.update()
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_ESCAPE]:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_ = pygame.mouse.get_pos()
                                print(click_)
                                if click_[0] > 435 and click_[0] < 540 and click_[1] > 215 and click_[1] < 275:
                                    home_player.current_foul += 1
                                    home_player.s_bihgiven += 1
                                    away_player.s_bihtaken += 1
                                    if home_player.current_foul == 1:
                                        h1f = 'on'
                                        checking_ = False
                                    if home_player.current_foul == 2:
                                        h2f = 'on'
                                        checking_ = False
                                    if home_player.current_foul == 3:
                                        h3f = 'on'
                                        home_player.current_foul = 0
                                        away_player.current_foul = 0

                                        home_player.s_gamesplayed += 1
                                        home_.s_gamesplayed += 1

                                        home_player.s_gameslost += 1
                                        home_.s_gameslost += 1

                                        home_player.s_gameswonstreaklist.append(int(home_player.s_gameswonstreak))
                                        home_player.s_gameswonstreak = 0
                                        home_.wonstreak = 0

                                        home_player.s_gamesloststreak += 1
                                        home_.s_gamesloststreak += 1

                                        home_player.s_onemade += home_player.ol_finalscore['1'][honeb]
                                        home_player.s_twomade += home_player.ol_finalscore['2'][htwob]
                                        home_player.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                        home_player.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                        home_player.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                        home_player.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                        home_player.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                        home_player.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                        home_player.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                        home_.s_onemade += home_player.ol_finalscore['1'][honeb]
                                        home_.s_twomade += home_player.ol_finalscore['2'][htwob]
                                        home_.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                        home_.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                        home_.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                        home_.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                        home_.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                        home_.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                        home_.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                        away_player.s_gamesplayed += 1
                                        away_.s_gamesplayed += 1

                                        away_player.s_gameswon += 1
                                        away_.s_gameswon += 1
                                        away_.s_match_score += 1

                                        away_player.s_gameswonstreak += 1
                                        away_.s_gameswonstreak += 1
                                        if away_player.s_gameswonstreak > away_player.s_highgameswonstreak:
                                            away_player.s_highgameswonstreak = int(away_player.s_gameswonstreak)

                                        away_player.s_gamesloststreak = 0
                                        away_.s_gamesloststreak = 0

                                        away_player.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                        away_player.s_twomade += away_player.ol_finalscore['2'][atwob]
                                        away_player.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                        away_player.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                        away_player.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                        away_player.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                        away_player.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                        away_player.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                        away_player.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                        away_.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                        away_.s_twomade += away_player.ol_finalscore['2'][atwob]
                                        away_.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                        away_.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                        away_.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                        away_.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                        away_.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                        away_.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                        away_.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                        if round_ == 15 and away_.s_match_score > 7:
                                            home_.s_matcheslost += 1
                                            home_.s_matchesloststreak += 1
                                            home_.s_matcheswonstreak = 0

                                            away_.s_matcheswon += 1
                                            away_.s_matcheswonstreak += 1
                                            away_.s_matchesloststreak = 0

                                        else:
                                            home_.s_matcheswon += 1
                                            home_.s_matcheswonstreak += 1
                                            home_.s_matchesloststreak = 0

                                            away_.s_matcheslost += 1
                                            away_.s_matchesloststreak += 1
                                            away_.s_matcheswonstreak = 0

                                        home_player.ol_savestats()
                                        home_player.ol_loadstats()

                                        away_player.ol_savestats()
                                        away_player.ol_loadstats()

                                        home_.ol_savestats()
                                        home_.ol_loadstats()

                                        away_.ol_savestats()
                                        away_.ol_loadstats()

                                        match_score = ((home_player.ID, away_player.ID),
                                                       (home_.s_match_score, away_.s_match_score, 0, 1),
                                                       (1, home_player.ol_finalscore['1'][honeb]),
                                                       (1, away_player.ol_finalscore['1'][aoneb]),
                                                       (2, home_player.ol_finalscore['2'][htwob]),
                                                       (2, away_player.ol_finalscore['2'][atwob]),
                                                       (3, home_player.ol_finalscore['3'][hthreeb]),
                                                       (3, away_player.ol_finalscore['3'][athreeb]),
                                                       (4, home_player.ol_finalscore['4'][hfourb]),
                                                       (4, away_player.ol_finalscore['4'][afourb]),
                                                       (5, home_player.ol_finalscore['5'][hfiveb]),
                                                       (5, away_player.ol_finalscore['5'][afiveb]),
                                                       (6, home_player.ol_finalscore['6'][hsixb]),
                                                       (6, away_player.ol_finalscore['6'][asixb]),
                                                       (7, home_player.ol_finalscore['7'][hsevenb]),
                                                       (7, away_player.ol_finalscore['7'][asevenb]),
                                                       (8, home_player.ol_finalscore['8'][heightb]),
                                                       (8, away_player.ol_finalscore['8'][aeightb]),
                                                       (9, home_player.ol_finalscore['9'][hnineb]),
                                                       (9, away_player.ol_finalscore['9'][anineb]))

                                        return match_score

                                if click_[0] > 265 and click_[0] < 375 and click_[1] > 215 and click_[1] < 275:
                                    checking_ = False

                if click_[0] > 310 and click_[0] < 385 and click_[1] > 55 and click_[
                    1] < 125 and away_player.shooting == 'on':
                    checking_ = True
                    check_window = pygame.image.load('confirmationwindow_foul.png')
                    while checking_:
                        window_.blit(check_window, (0, 0))
                        font_setup = pygame.font.SysFont('arial', 16)
                        away_name_text = font_setup.render(away_player.firstname + ' Fouled?', False, (0, 0, 0))
                        window_.blit(away_name_text, (395, 113))
                        pygame.display.update()
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_ESCAPE]:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_ = pygame.mouse.get_pos()
                                print(click_)
                                if click_[0] > 435 and click_[0] < 540 and click_[1] > 215 and click_[1] < 275:
                                    away_player.current_foul += 1
                                    away_player.s_bihgiven += 1
                                    home_player.s_bihtaken += 1
                                    if away_player.current_foul == 1:
                                        a1f = 'on'
                                        checking_ = False
                                    if away_player.current_foul == 2:
                                        a2f = 'on'
                                        checking_ = False
                                    if away_player.current_foul == 3:
                                        a3f = 'on'
                                        home_player.current_foul = 0
                                        away_player.current_foul = 0

                                        home_player.s_gamesplayed += 1
                                        home_.s_gamesplayed += 1

                                        home_player.s_gameswon += 1
                                        home_.s_gameswon += 1
                                        home_.s_match_score += 1

                                        home_player.s_gameswonstreak += 1
                                        home_.s_gameswonstreak += 1
                                        if home_player.s_gameswonstreak > home_player.s_highgameswonstreak:
                                            home_player.s_highgameswonstreak = int(home_player.s_gameswonstreak)

                                        home_player.s_gamesloststreak = 0
                                        home_.s_gamesloststreak = 0

                                        home_player.s_onemade += home_player.ol_finalscore['1'][honeb]
                                        home_player.s_twomade += home_player.ol_finalscore['2'][htwob]
                                        home_player.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                        home_player.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                        home_player.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                        home_player.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                        home_player.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                        home_player.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                        home_player.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                        home_.s_onemade += home_player.ol_finalscore['1'][honeb]
                                        home_.s_twomade += home_player.ol_finalscore['2'][htwob]
                                        home_.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                        home_.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                        home_.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                        home_.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                        home_.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                        home_.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                        home_.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                        away_player.s_gamesplayed += 1
                                        away_.s_gamesplayed += 1

                                        away_player.s_gameslost += 1
                                        away_.s_gameslost += 1
                                        away_player.s_gameswonstreaklist.append(int(away_player.s_gameswonstreak))
                                        away_player.s_gameswonstreak = 0
                                        away_.s_gameswonstreak = 0

                                        away_player.s_gamesloststreak += 1
                                        away_.s_gamesloststreak += 1

                                        away_player.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                        away_player.s_twomade += away_player.ol_finalscore['2'][atwob]
                                        away_player.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                        away_player.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                        away_player.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                        away_player.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                        away_player.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                        away_player.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                        away_player.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                        away_.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                        away_.s_twomade += away_player.ol_finalscore['2'][atwob]
                                        away_.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                        away_.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                        away_.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                        away_.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                        away_.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                        away_.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                        away_.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                        if round_ == 15 and away_.s_match_score > 7:
                                            home_.s_matcheslost += 1
                                            home_.s_matchesloststreak += 1
                                            home_.s_matcheswonstreak = 0

                                            away_.s_matcheswon += 1
                                            away_.s_matcheswonstreak += 1
                                            away_.s_matchesloststreak = 0

                                        else:
                                            home_.s_matcheswon += 1
                                            home_.s_matcheswonstreak += 1
                                            home_.s_matchesloststreak = 0

                                            away_.s_matcheslost += 1
                                            away_.s_matchesloststreak += 1
                                            away_.s_matcheswonstreak = 0

                                        home_player.ol_savestats()
                                        home_player.ol_loadstats()

                                        away_player.ol_savestats()
                                        away_player.ol_loadstats()

                                        home_.ol_savestats()
                                        home_.ol_loadstats()

                                        away_.ol_savestats()
                                        away_.ol_loadstats()

                                        match_score = ((home_player.ID, away_player.ID),
                                                       (home_.s_match_score, away_.s_match_score, 1, 0),
                                                       (1, home_player.ol_finalscore['1'][honeb]),
                                                       (1, away_player.ol_finalscore['1'][aoneb]),
                                                       (2, home_player.ol_finalscore['2'][htwob]),
                                                       (2, away_player.ol_finalscore['2'][atwob]),
                                                       (3, home_player.ol_finalscore['3'][hthreeb]),
                                                       (3, away_player.ol_finalscore['3'][athreeb]),
                                                       (4, home_player.ol_finalscore['4'][hfourb]),
                                                       (4, away_player.ol_finalscore['4'][afourb]),
                                                       (5, home_player.ol_finalscore['5'][hfiveb]),
                                                       (5, away_player.ol_finalscore['5'][afiveb]),
                                                       (6, home_player.ol_finalscore['6'][hsixb]),
                                                       (6, away_player.ol_finalscore['6'][asixb]),
                                                       (7, home_player.ol_finalscore['7'][hsevenb]),
                                                       (7, away_player.ol_finalscore['7'][asevenb]),
                                                       (8, home_player.ol_finalscore['8'][heightb]),
                                                       (8, away_player.ol_finalscore['8'][aeightb]),
                                                       (9, home_player.ol_finalscore['9'][hnineb]),
                                                       (9, away_player.ol_finalscore['9'][anineb]))

                                        return match_score

                                if click_[0] > 265 and click_[0] < 375 and click_[1] > 215 and click_[1] < 275:
                                    checking_ = False

                if click_[0] > 410 and click_[0] < 485 and click_[1] > 55 and click_[
                    1] < 125 and home_player.shooting == 'on':
                    checking_ = True
                    check_window = pygame.image.load('confirmationwindow_foul.png')
                    while checking_:
                        window_.blit(check_window, (0, 0))
                        font_setup = pygame.font.SysFont('arial', 16)
                        home_name_text = font_setup.render('Clear ' + home_player.firstname + "'s Fouls?", False,
                                                           (0, 0, 0))
                        window_.blit(home_name_text, (395, 113))
                        pygame.display.update()
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_ESCAPE]:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_ = pygame.mouse.get_pos()
                                print(click_)
                                if click_[0] > 435 and click_[0] < 540 and click_[1] > 215 and click_[1] < 275:
                                    home_player.current_foul = 0
                                    h1f = 'off'
                                    h2f = 'off'
                                    checking_ = False

                                if click_[0] > 265 and click_[0] < 375 and click_[1] > 215 and click_[1] < 275:
                                    checking_ = False

                if click_[0] > 410 and click_[0] < 485 and click_[1] > 55 and click_[
                    1] < 125 and away_player.shooting == 'on':
                    checking_ = True
                    check_window = pygame.image.load('confirmationwindow_foul.png')
                    while checking_:
                        window_.blit(check_window, (0, 0))
                        font_setup = pygame.font.SysFont('arial', 16)
                        away_name_text = font_setup.render('Clear ' + away_player.firstname + "'s Fouls?", False,
                                                           (0, 0, 0))
                        window_.blit(away_name_text, (395, 113))
                        pygame.display.update()
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_ESCAPE]:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_ = pygame.mouse.get_pos()
                                print(click_)
                                if click_[0] > 435 and click_[0] < 540 and click_[1] > 215 and click_[1] < 275:
                                    away_player.current_foul = 0
                                    a1f = 'off'
                                    a2f = 'off'
                                    checking_ = False

                                if click_[0] > 265 and click_[0] < 375 and click_[1] > 215 and click_[1] < 275:
                                    checking_ = False

                '''
                Scoresheet
                '''

                if click_[0] > 310 and click_[0] < 490 and click_[1] > 240 and click_[1] < 350 and checking_ == True:
                    scoresheet_function(window_, score_, home_lineup, away_lineup, round_)

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 95 and click_[0] < 155 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and aoneb == 'off':
                    if honeb == 'off':
                        honeb = 'on'
                        soneb = 'off'
                    elif honeb == 'on':
                        honeb = 'off'
                        soneb = 'on'

                if click_[0] > 95 and click_[0] < 155 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and honeb == 'off':
                    if aoneb == 'off':
                        aoneb = 'on'
                        soneb = 'off'
                    elif aoneb == 'on':
                        aoneb = 'off'
                        soneb = 'on'
                '''
                TWO BALL BUTTON
                '''
                if click_[0] > 165 and click_[0] < 225 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and atwob == 'off':
                    if htwob == 'off':
                        htwob = 'on'
                        stwob = 'off'
                    elif htwob == 'on':
                        htwob = 'off'
                        stwob = 'on'

                if click_[0] > 165 and click_[0] < 225 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and htwob == 'off':
                    if atwob == 'off':
                        atwob = 'on'
                        stwob = 'off'
                    elif atwob == 'on':
                        atwob = 'off'
                        stwob = 'on'

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 235 and click_[0] < 295 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and athreeb == 'off':
                    if hthreeb == 'off':
                        hthreeb = 'on'
                        sthreeb = 'off'
                    elif hthreeb == 'on':
                        hthreeb = 'off'
                        sthreeb = 'on'
                if click_[0] > 235 and click_[0] < 295 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and hthreeb == 'off':
                    if athreeb == 'off':
                        athreeb = 'on'
                        sthreeb = 'off'
                    elif athreeb == 'on':
                        athreeb = 'off'
                        sthreeb = 'on'

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 305 and click_[0] < 365 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and afourb == 'off':
                    if hfourb == 'off':
                        hfourb = 'on'
                        sfourb = 'off'
                    elif hfourb == 'on':
                        hfourb = 'off'
                        sfourb = 'on'
                if click_[0] > 305 and click_[0] < 365 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and hfourb == 'off':
                    if afourb == 'off':
                        afourb = 'on'
                        sfourb = 'off'
                    elif afourb == 'on':
                        afourb = 'off'
                        sfourb = 'on'

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 375 and click_[0] < 435 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and afiveb == 'off':
                    if hfiveb == 'off':
                        hfiveb = 'on'
                        sfiveb = 'off'
                    elif hfiveb == 'on':
                        hfiveb = 'off'
                        sfiveb = 'on'
                if click_[0] > 375 and click_[0] < 435 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and hfiveb == 'off':
                    if afiveb == 'off':
                        afiveb = 'on'
                        sfiveb = 'off'
                    elif afiveb == 'on':
                        afiveb = 'off'
                        sfiveb = 'on'

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 445 and click_[0] < 505 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and asixb == 'off':
                    if hsixb == 'off':
                        hsixb = 'on'
                        ssixb = 'off'
                    elif hsixb == 'on':
                        hsixb = 'off'
                        ssixb = 'on'
                if click_[0] > 445 and click_[0] < 505 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and hsixb == 'off':
                    if asixb == 'off':
                        asixb = 'on'
                        ssixb = 'off'
                    elif asixb == 'on':
                        asixb = 'off'
                        ssixb = 'on'

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 515 and click_[0] < 575 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and asevenb == 'off':
                    if hsevenb == 'off':
                        hsevenb = 'on'
                        ssevenb = 'off'
                    elif hsevenb == 'on':
                        hsevenb = 'off'
                        ssevenb = 'on'
                if click_[0] > 515 and click_[0] < 575 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and hsevenb == 'off':
                    if asevenb == 'off':
                        asevenb = 'on'
                        ssevenb = 'off'
                    elif asevenb == 'on':
                        asevenb = 'off'
                        ssevenb = 'on'

                '''
                ONE BALL BUTTON
                '''
                if click_[0] > 585 and click_[0] < 645 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on' and aeightb == 'off':
                    if heightb == 'off':
                        heightb = 'on'
                        seightb = 'off'
                    elif heightb == 'on':
                        heightb = 'off'
                        seightb = 'on'
                if click_[0] > 585 and click_[0] < 645 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on' and heightb == 'off':
                    if aeightb == 'off':
                        aeightb = 'on'
                        seightb = 'off'
                    elif aeightb == 'on':
                        aeightb = 'off'
                        seightb = 'on'

                '''
                Player Change BUTTON
                '''
                if click_[0] > 60 and click_[0] < 280 and click_[1] > 50 and click_[1] < 360 and checking_ == True:
                    home_player.shooting = 'on'
                    away_player.shooting = 'off'

                if click_[0] > 515 and click_[0] < 740 and click_[1] > 50 and click_[1] < 360 and checking_ == True:
                    away_player.shooting = 'on'
                    home_player.shooting = 'off'

                ## NINE BALL
                if click_[0] > 655 and click_[0] < 745 and click_[1] > 375 and click_[
                    1] < 425 and home_player.shooting == 'on':
                    checking_ = True
                    check_window = pygame.image.load('confirmationwindow_9ball.png')
                    while checking_:
                        window_.blit(check_window, (0, 0))
                        font_setup = pygame.font.SysFont('arial', 16)
                        home_name_text = font_setup.render(home_player.firstname + ' Won?', False, (0, 0, 0))
                        window_.blit(home_name_text, (395, 113))
                        pygame.display.update()
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_ESCAPE]:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_ = pygame.mouse.get_pos()
                                print(click_)
                                if click_[0] > 450 and click_[0] < 520 and click_[1] > 205 and click_[1] < 275:
                                    hnineb = 'on'
                                    snineb = 'off'
                                    home_player.current_foul = 0
                                    away_player.current_foul = 0

                                    home_player.s_gamesplayed += 1
                                    home_.s_gamesplayed += 1

                                    home_player.s_gameswon += 1
                                    home_.s_gameswon += 1
                                    home_.s_match_score += 1

                                    home_player.s_gameswonstreak += 1
                                    home_.s_gameswonstreak += 1
                                    if home_player.s_gameswonstreak > home_player.s_highgameswonstreak:
                                        home_player.s_highgameswonstreak = int(home_player.s_gameswonstreak)

                                    home_player.s_gamesloststreak = 0
                                    home_.s_gamesloststreak = 0

                                    home_player.s_onemade += home_player.ol_finalscore['1'][honeb]
                                    home_player.s_twomade += home_player.ol_finalscore['2'][htwob]
                                    home_player.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                    home_player.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                    home_player.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                    home_player.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                    home_player.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                    home_player.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                    home_player.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                    home_.s_onemade += home_player.ol_finalscore['1'][honeb]
                                    home_.s_twomade += home_player.ol_finalscore['2'][htwob]
                                    home_.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                    home_.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                    home_.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                    home_.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                    home_.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                    home_.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                    home_.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                    away_player.s_gamesplayed += 1
                                    away_.s_gamesplayed += 1

                                    away_player.s_gameslost += 1
                                    away_.s_gameslost += 1
                                    away_player.s_gameswonstreaklist.append(int(away_player.s_gameswonstreak))
                                    away_player.s_gameswonstreak = 0
                                    away_.s_gameswonstreak = 0

                                    away_player.s_gamesloststreak += 1
                                    away_.s_gamesloststreak += 1

                                    away_player.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                    away_player.s_twomade += away_player.ol_finalscore['2'][atwob]
                                    away_player.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                    away_player.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                    away_player.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                    away_player.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                    away_player.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                    away_player.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                    away_player.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                    away_.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                    away_.s_twomade += away_player.ol_finalscore['2'][atwob]
                                    away_.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                    away_.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                    away_.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                    away_.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                    away_.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                    away_.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                    away_.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                    if round_ == 15 and away_.s_match_score > 7:
                                        home_.s_matcheslost += 1
                                        home_.s_matchesloststreak += 1
                                        home_.s_matcheswonstreak = 0

                                        away_.s_matcheswon += 1
                                        away_.s_matcheswonstreak += 1
                                        away_.s_matchesloststreak = 0

                                    else:
                                        home_.s_matcheswon += 1
                                        home_.s_matcheswonstreak += 1
                                        home_.s_matchesloststreak = 0

                                        away_.s_matcheslost += 1
                                        away_.s_matchesloststreak += 1
                                        away_.s_matcheswonstreak = 0

                                    home_player.ol_savestats()
                                    home_player.ol_loadstats()

                                    away_player.ol_savestats()
                                    away_player.ol_loadstats()

                                    home_.ol_savestats()
                                    home_.ol_loadstats()

                                    away_.ol_savestats()
                                    away_.ol_loadstats()

                                    match_score = (
                                    (home_player.ID, away_player.ID), (home_.s_match_score, away_.s_match_score, 1, 0),
                                    (1, home_player.ol_finalscore['1'][honeb]),
                                    (1, away_player.ol_finalscore['1'][aoneb]),
                                    (2, home_player.ol_finalscore['2'][htwob]),
                                    (2, away_player.ol_finalscore['2'][atwob]),
                                    (3, home_player.ol_finalscore['3'][hthreeb]),
                                    (3, away_player.ol_finalscore['3'][athreeb]),
                                    (4, home_player.ol_finalscore['4'][hfourb]),
                                    (4, away_player.ol_finalscore['4'][afourb]),
                                    (5, home_player.ol_finalscore['5'][hfiveb]),
                                    (5, away_player.ol_finalscore['5'][afiveb]),
                                    (6, home_player.ol_finalscore['6'][hsixb]),
                                    (6, away_player.ol_finalscore['6'][asixb]),
                                    (7, home_player.ol_finalscore['7'][hsevenb]),
                                    (7, away_player.ol_finalscore['7'][asevenb]),
                                    (8, home_player.ol_finalscore['8'][heightb]),
                                    (8, away_player.ol_finalscore['8'][aeightb]),
                                    (9, home_player.ol_finalscore['9'][hnineb]),
                                    (9, away_player.ol_finalscore['9'][anineb]))

                                    return match_score

                                if click_[0] > 265 and click_[0] < 375 and click_[1] > 215 and click_[1] < 275:
                                    checking_ = False
                                    hnineb = 'off'
                                    snineb = 'on'

                if click_[0] > 655 and click_[0] < 745 and click_[1] > 375 and click_[
                    1] < 425 and away_player.shooting == 'on':
                    checking_ = True
                    check_window = pygame.image.load('confirmationwindow_9ball.png')
                    while checking_:
                        window_.blit(check_window, (0, 0))
                        font_setup = pygame.font.SysFont('arial', 16)
                        away_name_text = font_setup.render(away_player.firstname + ' Won?', False, (0, 0, 0))
                        window_.blit(away_name_text, (395, 113))
                        pygame.display.update()
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False
                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_ESCAPE]:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_ = pygame.mouse.get_pos()
                                print(click_)
                                if click_[0] > 450 and click_[0] < 520 and click_[1] > 205 and click_[1] < 275:
                                    anineb = 'on'
                                    snineb = 'off'
                                    home_player.current_foul = 0
                                    away_player.current_foul = 0

                                    home_player.s_gamesplayed += 1
                                    home_.s_gamesplayed += 1

                                    home_player.s_gameslost += 1
                                    home_.s_gameslost += 1
                                    home_player.s_gameswonstreaklist.append(int(home_player.s_gameswonstreak))
                                    home_player.s_gameswonstreak = 0
                                    home_.wonstreak = 0

                                    home_player.s_gamesloststreak += 1
                                    home_.s_gamesloststreak += 1

                                    home_player.s_onemade += home_player.ol_finalscore['1'][honeb]
                                    home_player.s_twomade += home_player.ol_finalscore['2'][htwob]
                                    home_player.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                    home_player.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                    home_player.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                    home_player.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                    home_player.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                    home_player.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                    home_player.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                    home_.s_onemade += home_player.ol_finalscore['1'][honeb]
                                    home_.s_twomade += home_player.ol_finalscore['2'][htwob]
                                    home_.s_threemade += home_player.ol_finalscore['3'][hthreeb]
                                    home_.s_fourmade += home_player.ol_finalscore['4'][hfourb]
                                    home_.s_fivemade += home_player.ol_finalscore['5'][hfiveb]
                                    home_.s_sixmade += home_player.ol_finalscore['6'][hsixb]
                                    home_.s_sevenmade += home_player.ol_finalscore['7'][hsevenb]
                                    home_.s_eightmade += home_player.ol_finalscore['8'][heightb]
                                    home_.s_ninemade += home_player.ol_finalscore['9'][hnineb]

                                    away_player.s_gamesplayed += 1
                                    away_.s_gamesplayed += 1

                                    away_player.s_gameswon += 1
                                    away_.s_gameswon += 1
                                    away_.s_match_score += 1

                                    away_player.s_gameswonstreak += 1
                                    away_.s_gameswonstreak += 1
                                    if away_player.s_gameswonstreak > away_player.s_highgameswonstreak:
                                        away_player.s_highgameswonstreak = int(away_player.s_gameswonstreak)

                                    away_player.s_gamesloststreak = 0
                                    away_.s_gamesloststreak = 0

                                    away_player.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                    away_player.s_twomade += away_player.ol_finalscore['2'][atwob]
                                    away_player.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                    away_player.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                    away_player.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                    away_player.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                    away_player.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                    away_player.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                    away_player.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                    away_.s_onemade += away_player.ol_finalscore['1'][aoneb]
                                    away_.s_twomade += away_player.ol_finalscore['2'][atwob]
                                    away_.s_threemade += away_player.ol_finalscore['3'][athreeb]
                                    away_.s_fourmade += away_player.ol_finalscore['4'][afourb]
                                    away_.s_fivemade += away_player.ol_finalscore['5'][afiveb]
                                    away_.s_sixmade += away_player.ol_finalscore['6'][asixb]
                                    away_.s_sevenmade += away_player.ol_finalscore['7'][asevenb]
                                    away_.s_eightmade += away_player.ol_finalscore['8'][aeightb]
                                    away_.s_ninemade += away_player.ol_finalscore['9'][anineb]

                                    if round_ == 15 and away_.s_match_score > 7:
                                        home_.s_matcheslost += 1
                                        home_.s_matchesloststreak += 1
                                        home_.s_matcheswonstreak = 0

                                        away_.s_matcheswon += 1
                                        away_.s_matcheswonstreak += 1
                                        away_.s_matchesloststreak = 0

                                    else:
                                        home_.s_matcheswon += 1
                                        home_.s_matcheswonstreak += 1
                                        home_.s_matchesloststreak = 0

                                        away_.s_matcheslost += 1
                                        away_.s_matchesloststreak += 1
                                        away_.s_matcheswonstreak = 0

                                    home_player.ol_savestats()
                                    home_player.ol_loadstats()

                                    away_player.ol_savestats()
                                    away_player.ol_loadstats()

                                    home_.ol_savestats()
                                    home_.ol_loadstats()

                                    away_.ol_savestats()
                                    away_.ol_loadstats()

                                    match_score = (
                                    (home_player.ID, away_player.ID), (home_.s_match_score, away_.s_match_score, 0, 1),
                                    (1, home_player.ol_finalscore['1'][honeb]),
                                    (1, away_player.ol_finalscore['1'][aoneb]),
                                    (2, home_player.ol_finalscore['2'][htwob]),
                                    (2, away_player.ol_finalscore['2'][atwob]),
                                    (3, home_player.ol_finalscore['3'][hthreeb]),
                                    (3, away_player.ol_finalscore['3'][athreeb]),
                                    (4, home_player.ol_finalscore['4'][hfourb]),
                                    (4, away_player.ol_finalscore['4'][afourb]),
                                    (5, home_player.ol_finalscore['5'][hfiveb]),
                                    (5, away_player.ol_finalscore['5'][afiveb]),
                                    (6, home_player.ol_finalscore['6'][hsixb]),
                                    (6, away_player.ol_finalscore['6'][asixb]),
                                    (7, home_player.ol_finalscore['7'][hsevenb]),
                                    (7, away_player.ol_finalscore['7'][asevenb]),
                                    (8, home_player.ol_finalscore['8'][heightb]),
                                    (8, away_player.ol_finalscore['8'][aeightb]),
                                    (9, home_player.ol_finalscore['9'][hnineb]),
                                    (9, away_player.ol_finalscore['9'][anineb]))

                                    return match_score

                                if click_[0] > 265 and click_[0] < 375 and click_[1] > 215 and click_[1] < 275:
                                    checking_ = False
                                    anineb = 'off'
                                    snineb = 'on'


def mainmenu(window_):
    tableborder_ = pygame.image.load('tableborder.png')
    background_ = pygame.image.load('bed.png')
    nblleague_ = pygame.image.load('nblleague.png')
    challengeleague_ = pygame.image.load('challengeleague.png')
    conway_ = pygame.image.load('conway.png')
    halecorner_ = pygame.image.load('halecorner.png')
    leaderboards_ = pygame.image.load('leaderboards.png')
    lessons_ = pygame.image.load('lessons.png')

    for item_ in range(-90, 65, 5):
        window_.blit(background_, (0, 0))
        window_.blit(nblleague_, (80, item_))
        window_.blit(leaderboards_, (435, item_))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
    for item_ in range(80, 190, 5):
        window_.blit(background_, (0, 0))
        window_.blit(challengeleague_, (80, item_))
        window_.blit(conway_, (435, item_))
        window_.blit(nblleague_, (80, 65))
        window_.blit(leaderboards_, (435, 65))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()
    for item_ in range(200, 320, 5):
        window_.blit(background_, (0, 0))
        window_.blit(lessons_, (80, item_))
        window_.blit(halecorner_, (435, item_))
        window_.blit(challengeleague_, (80, 190))
        window_.blit(conway_, (435, 190))
        window_.blit(nblleague_, (80, 65))
        window_.blit(leaderboards_, (435, 65))
        window_.blit(tableborder_, (0, 0))
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_ = pygame.mouse.get_pos()
                print(click_)

                # nbl league
                if click_[0] < 360 and click_[0] > 80 and click_[1] < 155 and click_[1] > 60:
                    match_selector(window_)

                # challenge league
                if click_[0] < 360 and click_[0] > 80 and click_[1] < 285 and click_[1] > 190:
                    print('challenge league')

                # lessons
                if click_[0] < 360 and click_[0] > 80 and click_[1] < 415 and click_[1] > 320:
                    print('lessons')

                # leaderboards
                if click_[0] < 715 and click_[0] > 435 and click_[1] < 155 and click_[1] > 60:
                    print('leaderboards')

                # conway
                if click_[0] < 715 and click_[0] > 435 and click_[1] < 285 and click_[1] > 190:
                    conwayscreensaver(window_)

                # hales corner
                if click_[0] < 715 and click_[0] > 435 and click_[1] < 415 and click_[1] > 320:
                    print('hales corner')



