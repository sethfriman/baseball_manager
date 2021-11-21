import random

'''
# from a dictionary
def pitcher_generator(roster):
    pitchers = []
    for x,y in roster.items():
        for a,b in y.items():
            if a == 'pos' and b == 'P':
                pitchers.append(x)
    pitcher = random.choice(pitchers)
    return pitcher

players_h = {'1': {'pos': 'P', 'team': 'ARI', 'hand': 'R', 'stat': 12}, '2': {'pos': 'P', 'team': 'ATL', 'hand': 'L', 'stat': 13}, '3': {'pos': 'RF', 'feel': 'boop', 'hand': 'R', 'stat': 14}}
players_a = {'7': {'pos': 'P', 'team': 'ARI', 'hand': 'R', 'stat': 12}, '6': {'pos': 'P', 'team': 'ATL', 'hand': 'L', 'stat': 13}, '5': {'pos': 'RF', 'feel': 'boop', 'hand': 'R', 'stat': 14}}

game = matchup(list_abbrv)

home_pitcher = pitcher_generator(players_h)
away_pitcher = pitcher_generator(players_a)

print('Home Pitcher:', home_pitcher)
print('Away Pitcher:', away_pitcher)
'''

# # from a list
# def pitcher_generator(roster):
#     pitchers = []
#     for x in roster:
#         for a,b in x.items():
#             if a == 'pos' and b == 'P':
#                 pitchers.append(x)
#     pitcher_choice = random.choice(pitchers)
#     for k,v in pitcher_choice.items():
#         if k == 'name':
#             pitcher = v
#     return pitcher
#
#
# players_h = [{'name': '1','pos': 'P', 'team': 'ARI', 'hand': 'R', 'stat': 12}, {'name': '2', 'pos': 'P', 'team': 'ATL', 'hand': 'L', 'stat': 13}, {'name': '3', 'pos': 'RF', 'feel': 'boop', 'hand': 'R', 'stat': 14}]
# players_a = [{'name': '7', 'pos': 'P', 'team': 'ARI', 'hand': 'R', 'stat': 12}, {'name': '6', 'pos': 'P', 'team': 'ATL', 'hand': 'L', 'stat': 13}, {'name': '5', 'pos': 'RF', 'feel': 'boop', 'hand': 'R', 'stat': 14}]
#
# game = matchup(list_abbrv)
#
#
# home_pitcher = pitcher_generator(players_h)
# away_pitcher = pitcher_generator(players_a)
#
# print('Home Pitcher:', home_pitcher)
# print('Away Pitcher:', away_pitcher)

#make lineup a child class of roster????

# def generate_pitcher():
#     pass

    #get the list of pitchers from the roster of the two teams in the generate game
    #pitcher = random.choice of that list
    #returns one starting pitcher, will be run twice
    #might want player objects too



from game_files.main import *
from player_information.player import *

# print(home)
# print(away)

home_roster = home
away_roster = away

#for player in home:
    #print(player.__dict__)
    #print(type(player))


class Lineup(): #based only on batting stats

    def __init__(self, roster):
        """ Constructor """
        #super().__init__(self, name, city, abbreviation)
        self.roster = roster
        # self.player = player
        # self.pos = pos
        # self.home = home
        # self.away = away
        self.lineup = {}
        #self.name = name
        #self.city = city
        #self.abbreviation = abbreviation

    def get_pitcher(self): #run for home and away

        pitchers = []
        for x in self.roster:
            player = x.__dict__
            for a, b in player.items():
                if a == 'position' and b == 'P':
                    pitchers.append(x)
        pitcher_choice = random.choice(pitchers)
        pitcher_info = pitcher_choice.__dict__
        for n, p in pitcher_info.items():
            if n == 'name':
                return p

    def get_position(self):
        #call for each of the 9 positions (not pitcher)
        #lineup = {}
        #each position is dict in larger lineup dict

        # for player in self.roster:
        #     print(player.__dict__)

            #print(type(player))

        pitcher = self.get_pitcher()

        self.lineup['SS'] = {}
        self.lineup['LF'] = {}
        self.lineup['2B'] = {}
        self.lineup['1B'] = {}
        self.lineup['RF'] = {}
        self.lineup['DH'] = {}
        self.lineup['CF'] = {}
        self.lineup['3B'] = {}
        self.lineup['C'] = {}

        return self.lineup

        # for x, y in roster.items():
        #     for a, b in y.items():
        # # for DH
        #     if a == 'pos' and b == 'DH':
        #         self.lineup['DH'] = x

        # if someone in the roster is DH, then they're automatically the DH
        # if no one, then it's the person who has the best batting stats AND isn't in the lineup

    def return_lineup(self):
        return self.lineup
#
#
LU = Lineup(home_roster)
LU.get_pitcher()
#Lineup.get_position()