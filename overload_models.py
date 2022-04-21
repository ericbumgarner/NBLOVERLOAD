import json
import pygame

class Stats:
    s_gamesplayed = 0

    s_gameswon = 0
    s_gameswonstreak = 0
    s_highgameswonstreak = 0
    s_gameswonstreaklist = []

    s_gameslost = 0
    s_gamesloststreak = 0
    s_highgamesloststreak = 0

    s_matcheswon = 0
    s_matcheswonstreak = 0
    s_highmatcheswonstreak = 0

    s_matcheslost = 0
    s_matchesloststreak = 0
    s_highmatchesloststreak = 0

    s_e9 = 0
    s_e9ed = 0
    s_br = 0
    s_bred = 0
    s_tf = 0
    s_tfed = 0
    s_combo = 0

    s_ballsonbreak = 0

    s_highballsonbreak = 0

    s_bihtaken = 0

    s_bihgiven = 0

    s_onemade = 0
    s_twomade = 0
    s_threemade = 0
    s_fourmade = 0
    s_fivemade = 0
    s_sixmade = 0
    s_sevenmade = 0
    s_eightmade = 0
    s_ninemade = 0
    s_ballsmade = 0
    s_ave_ballsmade = 0
    s_ballmadestreak = 0
    s_highballmadestreak = 0

    s_highballfinish = 0

    def __init__(self):
        pass

    def ol_loadstats(self):
        try:
            with open('logs\%s.txt' % self.ID, 'r') as _file:
                data = json.loads(_file.read())
                self.s_gamesplayed = data['s_gamesplayed']

                self.s_gameswon = data['s_gameswon']
                self.s_gameswonstreak = data['s_gameswonstreak']
                self.s_highgameswonstreak = data['s_highgameswonstreak']

                self.s_gameslost = data['s_gameslost']
                self.s_gamesloststreak = data['s_gamesloststreak']
                self.s_highgamesloststreak = data['s_highgamesloststreak']

                self.s_matcheswon = data['s_matcheswon']
                self.s_matcheswonstreak = data['s_matcheswonstreak']
                self.s_highmatcheswonstreak = data['s_highmatcheswonstreak']

                self.s_matcheslost = data['s_matcheslost']
                self.s_matchesloststreak = data['s_matchesloststreak']
                self.s_highmatchesloststreak = data['s_highmatchesloststreak']

                self.s_e9 = data['s_e9']
                self.s_br = data['s_br']
                self.s_tf = data['s_tf']
                self.s_combo = data['s_combo']

                self.s_ballsonbreak = data['s_ballsonbreak']
                self.s_highballsonbreak = data['s_highballsonbreak']

                self.s_bihtaken = data['s_bihtaken']
                self.s_bihgiven = data['s_bihgiven']
                if self.s_gamesplayed != 0 and self.s_bihtaken != 0:
                    self.ave_bih = "{:.2f}".format(data['s_bihtaken'] / data['s_gamesplayed'])

                self.s_bihgiven = data['s_bihgiven']
                if self.s_gamesplayed != 0 and self.s_bihgiven != 0:
                    self.ave_fouls = "{:.2f}".format(data['s_bihgiven'] / data['s_gamesplayed'])

                self.s_onemade = data['s_onemade']
                self.s_twomade = data['s_twomade']
                self.s_threemade = data['s_threemade']
                self.s_fourmade = data['s_fourmade']
                self.s_fivemade = data['s_fivemade']
                self.s_sixmade = data['s_sixmade']
                self.s_sevenmade = data['s_sevenmade']
                self.s_eightmade = data['s_eightmade']
                self.s_ninemade = data['s_ninemade']
                self.s_ballsmade = int(
                    self.s_onemade + self.s_twomade + self.s_threemade + self.s_fourmade + self.s_fivemade + self.s_sixmade + self.s_sevenmade + self.s_eightmade + self.s_ninemade)
                if self.s_ballsmade != 0:
                    self.s_ave_ballsmade = "{:.2f}".format(self.s_ballsmade / self.s_gamesplayed)

                self.s_ballmadestreak = data['s_ballmadestreak']
                self.s_highballmadestreak = data['s_highballmadestreak']

                self.s_highballfinish = data['s_highballfinish']
        except:
            self.ol_savestats()
            print('Nope ' + str(self.ID))

    def ol_gamewon(self):
        self.gamesplayed += 1
        self.gameswon += 1
        self.gameswonstreak += 1

    def ol_gamelost(self):
        self.gamesplayed += 1
        self.gameslost += 1
        self.gameswonstreak = 0

    def ol_savestats(self):
        dict_maker = [a for a in dir(self) if a.startswith('s_')]

        stat_line = [self.__getattribute__(a) for a in dir(self) if a.startswith('s_')]
        dictionarylist = []
        for idx, item in enumerate(dict_maker):
            dictionarylist.append(item)
            dictionarylist.append(stat_line[idx])
        it = iter(dictionarylist)
        res_dct = dict(zip(it, it))
        with open('logs\%s.txt' % self.ID, 'w') as _file:
            _file.write(str(res_dct).replace("\'", "\""))


class Player(Stats):

    def __init__(self, _playerID, _fullname, ol_card_selection='1', ol_cue_selection='1'):
        super().__init__()

        self.name = _fullname
        self.firstname = _fullname.split(' ')[0]
        self.ID = _playerID
        self.shooting = 'on'
        self.current_foul = 0
        self.card_selection = ol_card_selection
        self.cue_selection = ol_cue_selection
        self.ol_finalscore = {'1': {'on': 1, 'off': 0},
                              '2': {'on': 1, 'off': 0},
                              '3': {'on': 1, 'off': 0},
                              '4': {'on': 1, 'off': 0},
                              '5': {'on': 1, 'off': 0},
                              '6': {'on': 1, 'off': 0},
                              '7': {'on': 1, 'off': 0},
                              '8': {'on': 1, 'off': 0},
                              '9': {'on': 1, 'off': 0}}
        self.ol_card = {
            '1': {'on': pygame.image.load('card_grey_100.png'), 'off': pygame.image.load('card_grey_50.png')},
            '2': {'on': pygame.image.load('card_cali_100.png'), 'off': pygame.image.load('card_cali_50.png')},
            '3': {'on': pygame.image.load('machan-100.png'), 'off': pygame.image.load('machan-50.png')}}
        self.ol_cue = {'1': {'on': pygame.image.load('cue1-100.png'), 'off': pygame.image.load('cue1-25.png')},
                       '2': {'on': pygame.image.load('cue2-100.png'), 'off': pygame.image.load('cue2-25.png')}}
        self.ol_scorecard = {'1': {'on': pygame.image.load('mini1-100.png'), 'off': pygame.image.load('mini1-25.png')},
                             '2': {'on': pygame.image.load('mini2-100.png'), 'off': pygame.image.load('mini2-25.png')},
                             '3': {'on': pygame.image.load('mini3-100.png'), 'off': pygame.image.load('mini3-25.png')},
                             '4': {'on': pygame.image.load('mini4-100.png'), 'off': pygame.image.load('mini4-25.png')},
                             '5': {'on': pygame.image.load('mini5-100.png'), 'off': pygame.image.load('mini5-25.png')},
                             '6': {'on': pygame.image.load('mini6-100.png'), 'off': pygame.image.load('mini6-25.png')},
                             '7': {'on': pygame.image.load('mini7-100.png'), 'off': pygame.image.load('mini7-25.png')},
                             '8': {'on': pygame.image.load('mini8-100.png'), 'off': pygame.image.load('mini8-25.png')},
                             '9': {'on': pygame.image.load('mini9-100.png'), 'off': pygame.image.load('mini9-25.png')}}
        self.ol_threefoul = {
            '1': {'on': pygame.image.load('cueball-100.png'), 'off': pygame.image.load('cueball-25.png')},
            '2': {'on': pygame.image.load('cueball-100.png'), 'off': pygame.image.load('cueball-25.png')},
            '3': {'on': pygame.image.load('cueball-100.png'), 'off': pygame.image.load('cueball-25.png')}}

    def __repr__(self):
        return f'{self.ID} - {self.name}'


class Team(Stats):

    def __init__(self, _teamname, _teamID, _roster=None):
        super().__init__()
        self.teamname = _teamname
        self.ID = _teamID
        self.ol_logo = pygame.image.load(self.ID + '.png')

        self.s_match_score = 0

        self.ol_matchscore = {'0': pygame.image.load('score-0.png'),
                              '1': pygame.image.load('score-1.png'),
                              '2': pygame.image.load('score-2.png'),
                              '3': pygame.image.load('score-3.png'),
                              '4': pygame.image.load('score-4.png'),
                              '5': pygame.image.load('score-5.png'),
                              '6': pygame.image.load('score-6.png'),
                              '7': pygame.image.load('score-7.png'),
                              '8': pygame.image.load('score-8.png'),
                              '9': pygame.image.load('score-9.png'),
                              '10': pygame.image.load('score-10.png'),
                              '11': pygame.image.load('score-11.png'),
                              '12': pygame.image.load('score-12.png'),
                              '13': pygame.image.load('score-13.png'),
                              '14': pygame.image.load('score-14.png'),
                              '15': pygame.image.load('score-15.png')}

        if _roster is None:
            self.roster = []
        else:
            self.roster = _roster

    def __repr__(self):
        return f'{self.ID} - {self.roster}'

class Ballset:
    def __init__(self):
        self.rackofnine = {'1':{'on':pygame.image.load('1-100.png'),'off':pygame.image.load('1-25.png')},
                           '2':{'on':pygame.image.load('2-100.png'),'off':pygame.image.load('2-25.png')},
                           '3':{'on':pygame.image.load('3-100.png'),'off':pygame.image.load('3-25.png')},
                           '4':{'on':pygame.image.load('4-100.png'),'off':pygame.image.load('4-25.png')},
                           '5':{'on':pygame.image.load('5-100.png'),'off':pygame.image.load('5-25.png')},
                           '6':{'on':pygame.image.load('6-100.png'),'off':pygame.image.load('6-25.png')},
                           '7':{'on':pygame.image.load('7-100.png'),'off':pygame.image.load('7-25.png')},
                           '8':{'on':pygame.image.load('8-100.png'),'off':pygame.image.load('8-25.png')},
                           '9':{'on':pygame.image.load('9-100.png'),'off':pygame.image.load('9-25.png')}}

