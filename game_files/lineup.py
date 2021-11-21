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




#from player_information.roster import Roster
from game_files.main import *
from game_files.main import home

print(home)


#make lineup a child class of roster????

# def generate_pitcher():
#     pass

    #get the list of pitchers from the roster of the two teams in the generate game
    #pitcher = random.choice of that list
    #returns one starting pitcher, will be run twice
    #might want player objects too




# class Lineup(Roster): #based only on batting stats
#
#     def __init__(self, player, pos, name, city, abbreviation):
#         """ Constructor """
#         super().__init__(self, name, city, abbreviation)
#         #self.roster = roster
#         self.player = player
#         self.pos = pos
#         #self.name = name
#         #self.city = city
#         #self.abbreviation = abbreviation
#
#
#     def get_home_pitcher(self, pos, name, city, abbreviation):
#         pass
#
#         # pitchers = []
#         # roster = r.get_current_roster()
#         # print(roster)
#
#         # for player in roster:
#         #     if pos == 'P':
#         #         pitchers.append(player)
#         #
#         # return pitchers
#
#     # def get_away_pitcher(self, pos, team, abbrv, player, roster):
#     #     pass
#     #
#     # def get_position(self, pos, team, abbrv, player, roster):
#     #     pass
#     #     #call for each of the 8 positions (not pitcher)
#     #
#     #     # for DH
#     #     # if someone in the roster is DH, then they're automatically the DH
#     #     # if no one, then it's the person who has the best batting stats AND isn't in the lineup
#     #
#     # def return_lineup(self):
#     #     pass #return as pd dataframe
#
#
# Lineup.get_home_pitcher('P', 'Diamondbacks', 'Arizona', 'ARI')