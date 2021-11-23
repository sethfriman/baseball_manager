import random
from game_files.main import *
from player_information.player import *

home_roster = home
away_roster = away

class Lineup(): #based only on batting stats

    def __init__(self, roster):
        """ Constructor for Lineup """
        self.roster = roster
        self.lineup = {}

    def get_pitcher(self): #run for home and away

        pitchers = []
        cleaned_p = []
        for x in self.roster:
            player = x.__dict__
            for a, b in player.items():
                if a == 'position' and b == 'P':
                    pitchers.append(x)

        for p in pitchers:
            pitcher = p.__dict__
            for a, b in pitcher.items():
                if a == 'hand':
                    if b == 'Right' or b == 'Left':
                        cleaned_p.append(pitcher)
                        #print(cleaned_p)
        pitcher_choice = random.choice(cleaned_p)
        pitcher_info = pitcher_choice
        for n, p in pitcher_info.items():
            if n == 'name':
                return pitcher_info

    def get_position(self):

        SS = []
        LF = []
        CF = []
        RF = []
        B1 = []
        B2 = []
        B3 = []
        C = []
        DH = []

        pitcher = self.get_pitcher()
        print(pitcher)

        self.lineup['SS'] = {}
        self.lineup['LF'] = {}
        self.lineup['2B'] = {}
        self.lineup['1B'] = {}
        self.lineup['RF'] = {}
        self.lineup['DH'] = {}
        self.lineup['CF'] = {}
        self.lineup['3B'] = {}
        self.lineup['C'] = {}

        non_pitchers = []

        for x in self.roster:
            player = x.__dict__
            player_items = player.items()
            for a, b in player_items:
                if a == 'position' and b != 'P' and b != 'Unknown':
                        non_pitchers.append(player_items)
                        #print(non_pitchers)

        for c, d in pitcher.items():
            if c == 'hand' and d == 'Right':
                #print(d)
                for player in non_pitchers:
                    #print(player)
                    for a, b in player:
                        #print(a)
                        if a == 'rhp_stats':
                            batting_avg = b['AVG'].mean()
                            print(batting_avg)
                        if a == 'name':
                            name = b
                            #print(name)
                        if a == 'position':
                            if b == 'C':
                                #print(b)
                                C.append((name, batting_avg))
                                print(C)
                            if b == '1B':
                                B1.append((name, batting_avg))
                                print(B1)
                            if b == '2B':
                                B2.append((name, batting_avg))
                                print(B2)
                            if b == '3B':
                                B3.append((name, batting_avg))
                                print(B3)
                            if b == 'SS':
                                SS.append((name, batting_avg))
                                print(SS)
                            if b == 'LF':
                                LF.append((name, batting_avg))
                                print(LF)
                            if b == 'CF':
                                CF.append((name, batting_avg))
                                print(CF)
                            if b == 'RF':
                                RF.append((name, batting_avg))
                                print(RF)
                            if b == 'DH':
                                DH.append((name, batting_avg))
                                print(DH)

            if c == 'hand' and d == 'Left':
                for player in non_pitchers:
                    #print(player)
                    for a, b in player:
                        #print(a)
                        if a == 'lhp_stats':
                            batting_avg = b['AVG'].mean()
                            print(batting_avg)
                        if a == 'name':
                            name = b
                            #print(name)
                        if a == 'position':
                            if b == 'C':
                                #print(b)
                                C.append((name, batting_avg))
                                print(C)
                            if b == '1B':
                                B1.append((name, batting_avg))
                                print(B1)
                            if b == '2B':
                                B2.append((name, batting_avg))
                                print(B2)
                            if b == '3B':
                                B3.append((name, batting_avg))
                                print(B3)
                            if b == 'SS':
                                SS.append((name, batting_avg))
                                print(SS)
                            if b == 'LF':
                                LF.append((name, batting_avg))
                                print(LF)
                            if b == 'CF':
                                CF.append((name, batting_avg))
                                print(CF)
                            if b == 'RF':
                                RF.append((name, batting_avg))
                                print(RF)
                            if b == 'DH':
                                DH.append((name, batting_avg))
                                print(DH)

    def return_lineup(self):
        return self.lineup

LU = Lineup(home_roster)
#LU.get_pitcher()
#Lineup.get_position()
