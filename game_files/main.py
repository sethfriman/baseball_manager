
import sys

from pos_lineup import *
from random9_lineup import random9Lineup
from top9_lineup import top9Lineup
from gen_matchup import *

sys.path.append('../')
# from player_information.roster import Roster
# from player_information.roster import get_pitcher
# from player_information.player import Player, Batter, Pitcher
# import data_cleaning_and_organization.dataclean as dc
# from data_cleaning_and_organization.gen_stats import gen_stat
from results_visuals.player_comp import player_comp
from results_visuals.lineup_compare import lineup_compare


list_abbrv = ['ARI', 'ATL', 'BAL', 'BOS', 'CHW', 'CHC', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD',
                      'MIA', 'MIL', 'MIN', 'NYY', 'NYM', 'OAK', 'PHI', 'PIT', 'SDP', 'SFG', 'SEA', 'STL', 'TBR', 'TEX',
                      'TOR', 'WSN']

list_cities = ["Arizona", "Atlanta", "Baltimore", "Boston", "Chicago", "Chicago", "Cincinnati", "Cleveland",
                       "Colorado", "Detroit", "Houston", "Kansas City", "Los Angeles", "Los Angeles", "Miami",
                       "Milwaukee", "Minnesota", "New York", "New York", "Oakland", "Philadelphia", "Pittsburgh",
                       "San Diego", "San Francisco", "Seattle", "St. Louis", "Tampa Bay", "Texas", "Toronto",
                       "Washington"]

list_team = ["Diamondbacks", "Braves", "Orioles", "Red Sox", "White Sox", "Cubs", "Reds", "Indians",
                     "Rockies", "Tigers", "Astros", "Royals", "Angels", "Dodgers", "Marlins", "Brewers",
                     "Twins", "Yankees", "Mets", "Athletics", "Phillies", "Pirates", "Padres",
                     "Giants", "Mariners", "Cardinals", "Rays", "Rangers", "Blue Jays", "Nationals"]

list_roster_objects = []

#
# def genMatchup(home=None, away=None, h_p_hand=None, a_p_hand=None, before_date='2021-10-03'):
#     matchup_tuple = init_players.matchup(list_abbrv, home, away)
#     rosters = init_players.rosters(matchup_tuple[0], matchup_tuple[1])
#
#     home_name = matchup_tuple[0]
#     away_name = matchup_tuple[1]
#
#     home = rosters[0]
#     away = rosters[1]
#
#     if h_p_hand is None:
#         home_pitcher = get_pitcher(home)
#         h_p_hand = home_pitcher.get_arm()
#         print(matchup_tuple[0] + ' pitcher: ' + home_pitcher.get_name() + ', Hand: ' + home_pitcher.get_arm())
#     else:
#         print(matchup_tuple[0] + ' pitcher: ' + h_p_hand + 'y, Hand: ' + h_p_hand)
#
#     if a_p_hand is None:
#         away_pitcher = get_pitcher(away)
#         a_p_hand = away_pitcher.get_arm()
#         print(matchup_tuple[1] + ' pitcher: ' + away_pitcher.get_name() + ', Hand: ' + away_pitcher.get_arm())
#     else:
#         print(matchup_tuple[1] + ' pitcher: ' + a_p_hand + 'y, Hand: ' + a_p_hand)
#
#     if h_p_hand == 'Left':
#         home_pitcher_hand = 'lhp'
#     else:
#         home_pitcher_hand = 'rhp'
#
#     if a_p_hand == 'Left':
#         away_pitcher_hand = 'lhp'
#     else:
#         away_pitcher_hand = 'rhp'
#
#     home_df = pd.DataFrame()
#     away_df = pd.DataFrame()
#
#     # Add all batters from each team to a batters dataframe containing their batting stats
#     for player in home:
#         try:
#             if away_pitcher_hand == 'rhp':
#                 player_df = player.get_rhp_stats()
#             elif away_pitcher_hand == 'lhp':
#                 player_df = player.get_lhp_stats()
#             else:
#                 player_df = player.get_hall_stats()
#             player_df['Position'] = player.get_position()
#             home_df = home_df.append(player_df, ignore_index=True)
#         except AttributeError as e:
#             pass
#
#     for player in away:
#         try:
#             if home_pitcher_hand == 'rhp':
#                 player_df = player.get_rhp_stats()
#             elif home_pitcher_hand == 'lhp':
#                 player_df = player.get_lhp_stats()
#             else:
#                 player_df = player.get_hall_stats()
#             player_df['Position'] = player.get_position()
#             away_df = away_df.append(player_df, ignore_index=True)
#         except AttributeError as e:
#             pass
#
#     # The list of columns that will be either preserved or weighted in the final DataFrame
#     stat_cols = ['Name', 'Tm', 'Date', 'Position', 'G',
#                  'PA', 'AB', 'H', '1B', '2B', '3B',
#                  'HR', 'R', 'RBI', 'BB', 'IBB', 'SO',
#                  'HBP', 'SF', 'SH', 'GDP', 'SB', 'CS']
#
#     # Weight the batting stats based on recency of games
#     home_weighted = dc.weight_stats_df(home_df, stat_cols, before_date=before_date)
#     home_weighted['Tm'] = matchup_tuple[0]
#
#     away_weighted = dc.weight_stats_df(away_df, stat_cols, before_date=before_date)
#     away_weighted['Tm'] = matchup_tuple[1]
#
#     # Filter batters with less than 10 weighted at bats to reduce '1-game-wonders' type of results
#     home_weighted = home_weighted[home_weighted['AB_vs_total'] > 10]
#     away_weighted = away_weighted[away_weighted['AB_vs_total'] > 10]
#
#     # Add the new aggregate stats to the DataFrame from the weighted stats
#     home_weighted = gen_stat(home_weighted, p_hand=away_pitcher_hand)
#     away_weighted = gen_stat(away_weighted, p_hand=home_pitcher_hand)
#
#     return home_weighted, away_weighted, home_name, away_name, h_p_hand, a_p_hand, home, away
#
#
# class GameManager:
#
#     def __init__(self):
#
#         # Setting up rosters, adding to a list of all rosters:
#         for i in range(len(list_team)):
#             roster = Roster(list_team[i], list_cities[i], list_abbrv[i])
#             list_roster_objects.append(roster)
#
#         lhp = pd.read_csv('../data_directory/FanGraphs_lhp.csv')
#         rhp = pd.read_csv('../data_directory/FanGraphs_rhp.csv')
#         total = pd.read_csv('../data_directory/FanGraphs_total.csv')
#         stats_lhp = pd.read_csv('../data_directory/lhp_stats.csv')
#         stats_rhp = pd.read_csv('../data_directory/rhp_stats.csv')
#
#         # creating player objects and adding to correct team's roster
#         # all unique batters
#         unique_batters_df = total.drop_duplicates(subset=["playerId"])
#         list_player_id = unique_batters_df["playerId"].tolist()
#
#         positions = pd.read_csv("../data_directory/Positional_Data.csv")
#
#         # capitalize positions
#
#         positions['Position'] = positions['Position'].str.upper()
#
#         # for each batter, create a batter object with all stats and team/name
#         for i in list_player_id:
#             player_total_stats = total[total["playerId"] == i]
#             lhp_stats = lhp[lhp["playerId"] == i]
#             rhp_stats = rhp[rhp["playerId"] == i]
#             player_name = player_total_stats.iloc[0]["Name"]
#             player_team = player_total_stats.iloc[-1]["Tm"]
#             possible_players = positions[positions['Name'] == player_name]
#             correct_player = possible_players[possible_players['Team'] == player_team]
#
#             if correct_player.empty:
#                 continue
#             else:
#                 player_position = correct_player.iloc[0]['Position']
#                 player_status = correct_player.iloc[0]['Status']
#
#             player_obj = Batter(player_name, player_team, player_position, player_total_stats, lhp_stats, rhp_stats)
#
#             # then add created player object to the roster of team that batter plays on
#             idx = list_abbrv.index(player_team)
#             roster_obj = list_roster_objects[idx]
#             roster_obj.add_player(player_obj)
#
#         # doing same for left handed pitchers
#         unique_pitchers = stats_lhp.drop_duplicates(subset=["playerId"])
#         list_pitcher_id = unique_pitchers["playerId"].tolist()
#
#         for p in list_pitcher_id:
#             pitcher_ind_stats = stats_lhp[stats_lhp["playerId"] == p]
#             pitcher_name = pitcher_ind_stats.iloc[0]["Name"]
#             pitcher_team = pitcher_ind_stats.iloc[-1]["Tm"]
#             possible_pitchers = positions[positions['Name'] == pitcher_name]
#             correct_pitcher = possible_pitchers[possible_pitchers['Team'] == pitcher_team]
#             pitcher_hand = 'Left'
#
#             if correct_pitcher.empty:
#                 continue
#             else:
#                 pitcher_position = correct_player.iloc[0]['Position']
#                 pitcher_status = correct_player.iloc[0]['Status']
#
#             pitcher_obj = Pitcher(pitcher_name, pitcher_team, pitcher_position, pitcher_hand, pitcher_ind_stats)
#
#             idx = list_abbrv.index(pitcher_team)
#             roster_obj = list_roster_objects[idx]
#             roster_obj.add_player(pitcher_obj)
#
#         # doing same for left handed pitchers
#         unique_pitchers_r = stats_rhp.drop_duplicates(subset=["playerId"])
#         list_pitcher_id_r = unique_pitchers_r["playerId"].tolist()
#
#         for p in list_pitcher_id_r:
#             pitcher_ind_stats = stats_rhp[stats_rhp["playerId"] == p]
#             pitcher_name = pitcher_ind_stats.iloc[0]["Name"]
#             pitcher_team = pitcher_ind_stats.iloc[-1]["Tm"]
#             possible_pitchers = positions[positions['Name'] == pitcher_name]
#             correct_pitcher = possible_pitchers[possible_pitchers['Team'] == pitcher_team]
#             pitcher_hand = 'Right'
#
#             if correct_pitcher.empty:
#                 continue
#             else:
#                 pitcher_position = correct_player.iloc[0]['Position']
#                 pitcher_status = correct_player.iloc[0]['Status']
#
#             pitcher_obj = Pitcher(pitcher_name, pitcher_team, pitcher_position, pitcher_hand, pitcher_ind_stats)
#
#             idx = list_abbrv.index(pitcher_team)
#             roster_obj = list_roster_objects[idx]
#             roster_obj.add_player(pitcher_obj)
#
#     def matchup(self, teams, home, away):
#         """ Randomly selects two MLB teams from list of teams without repeating """
#         # .sample() does not allow for there to be repeating elements chosen
#         if (home is None) & (away is None):
#             matchups = random.sample(teams, 2)
#             home_team = matchups[0]
#             away_team = matchups[1]
#         elif home is None:
#             new_team = False
#             while not new_team:
#                 matchups = random.sample(teams, 1)
#                 new_team = matchups[0] != away
#             home_team = matchups[0]
#             away_team = away
#         elif away is None:
#             new_team = False
#             while not new_team:
#                 matchups = random.sample(teams, 1)
#                 new_team = matchups[0] != home
#             home_team = home
#             away_team = matchups[0]
#         else:
#             home_team = home
#             away_team = away
#
#         home_spot = teams.index(home_team)
#         away_spot = teams.index(away_team)
#         home = list_cities[home_spot] + " " + list_team[home_spot]
#         away = list_cities[away_spot] + " " + list_team[away_spot]
#         #
#         print('Game Matchup:', home, '(home) vs', away, '(away)')
#         return home_team, away_team
#
#     def rosters(self, home, away):
#         """ Returns rosters of matchup teams as lists of player objects """
#
#         hi = list_abbrv.index(home)
#         ai = list_abbrv.index(away)
#
#         home_roster = list_roster_objects[hi].get_current_roster()
#         away_roster = list_roster_objects[ai].get_current_roster()
#         return home_roster, away_roster


# Initial Visualizations using raw dataframes
player_comp(['Anthony Rizzo', 'Kyle Seager', 'Willson Contreras'], p_hand='Right', start_date='2021-09-01')

# Initialize all of the rosters with player stats
#init_players = GameManager()

# Change the parameters here to customize the matchup
# home/away: abbreviations for teams
# h_p_hand/a_p_hand: 'Left' or 'Right'
# Unspecified values are chosen randomly
home_weighted, away_weighted, home_name, away_name, h_p_hand, a_p_hand, home, away = genMatchup()

#home_weighted, away_weighted, home_name, away_name, h_p_hand, a_p_hand, home, away = genMatchup('MIA', 'TOR', 'Left', 'Right')
#home_weighted, away_weighted, home_name, away_name, h_p_hand, a_p_hand, home, away = genMatchup(home='OAK', a_p_hand='Right', before_date='2021-09-01')

# Start Accumulating Results
results_df = pd.DataFrame(columns=['Lineup Type', 'Expected Runs', 'Location'])

print()
# Top 9 Batter Lineup
print('------------------------TOP 9 BATTERS LINEUPS------------------------')
top9_h, top9_a = top9Lineup(home_weighted, away_weighted, h_p_hand, a_p_hand, home_name, away_name)
results_df = results_df.append({'Lineup Type': 'Top9', 'Expected Runs': top9_h, 'Location': 'Home'}, ignore_index=True)
results_df = results_df.append({'Lineup Type': 'Top9', 'Expected Runs': top9_a, 'Location': 'Away'}, ignore_index=True)
print('\n')

# Top Batter in Every Position Lineup
print('-------------------BEST POSITIONAL BATTERS LINEUPS-------------------')
pos_h, pos_a = make_pos_lineup(home, away, home_weighted, away_weighted, home_name, away_name)
home_poslineup_df, home_weight = lineup_df(pos_h)
away_poslineup_df, away_weight = lineup_df(pos_a)
print(home_name + ' Positional Lineup: ')
print(home_poslineup_df[['Name', 'Position', 'Weighted runs per game']])
print("Total Expected Runs: ", home_weight)
print()
print(away_name + ' Positional Lineup: ')
print(away_poslineup_df[['Name', 'Position', 'Weighted runs per game']])
print("Total Expected Runs: ", away_weight)
results_df = results_df.append({'Lineup Type': 'Positional', 'Expected Runs': home_weight, 'Location': 'Home'}, ignore_index=True)
results_df = results_df.append({'Lineup Type': 'Positional', 'Expected Runs': away_weight, 'Location': 'Away'}, ignore_index=True)
print('\n')

# Randomly Selected 9 Batters Lineup
print('------------------------RANDOM BATTERS LINEUPS------------------------')
ran9_h, ran9_a = random9Lineup(home_weighted, away_weighted, h_p_hand, a_p_hand, home_name, away_name)
results_df = results_df.append({'Lineup Type': 'Rand9', 'Expected Runs': ran9_h, 'Location': 'Home'}, ignore_index=True)
results_df = results_df.append({'Lineup Type': 'Rand9', 'Expected Runs': ran9_a, 'Location': 'Away'}, ignore_index=True)

# Visualize the lineups on one chart
lineup_compare(results_df, h_p_hand, a_p_hand, home_name, away_name)
