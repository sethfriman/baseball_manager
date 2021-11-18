import random
import pandas as pd
from player_information.roster import Roster
from player_information.player import Player, Batter, Pitcher

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


class GameManager:

    def __init__(self):

        # Setting up rosters, adding to a list of all rosters:
        for i in range(len(list_team)):
            roster = Roster(list_team[i], list_cities[i], list_abbrv[i])
            list_roster_objects.append(roster)

        lhp = pd.read_csv('../data_directory/FanGraphs_lhp.csv')
        rhp = pd.read_csv('../data_directory/FanGraphs_rhp.csv')
        total = pd.read_csv('../data_directory/FanGraphs_total.csv')
        pitcher_stats = pd.read_csv('../data_directory/pitcher_data.csv')

        # creating player objects and adding to correct team's roster
        # all unique batters
        unique_batters_df = total.drop_duplicates(subset=["playerId"])
        list_player_id = unique_batters_df["playerId"].tolist()

        positions = pd.read_csv("../data_directory/Positional_Data.csv")

        # capitalize positions

        positions['Position'] = positions['Position'].str.upper()

        # for each batter, create a batter object with all stats and team/name
        for i in list_player_id:
            player_total_stats = total[total["playerId"] == i]
            lhp_stats = lhp[lhp["playerId"] == i]
            rhp_stats = rhp[rhp["playerId"] == i]
            player_name = player_total_stats.iloc[0]["Name"]
            player_team = player_total_stats.iloc[-1]["Tm"]
            possible_players = positions[positions['Name'] == player_name]
            correct_player = possible_players[possible_players['Team'] == player_team]

            if correct_player.empty:
                player_position = 'Unknown'
                player_status = 'Unknown'
            else:
                player_position = correct_player.iloc[0]['Position']
                player_status = correct_player.iloc[0]['Status']

            player_obj = Batter(player_name, player_team, player_position, player_total_stats, lhp_stats, rhp_stats)

            # then add created player object to the roster of team that batter plays on
            idx = list_abbrv.index(player_team)
            roster_obj = list_roster_objects[idx]
            roster_obj.add_player(player_obj)

        # doing same for pitchers
        unique_pitchers = pitcher_stats.drop_duplicates(subset=["playerId"])
        list_pitcher_id = unique_pitchers["playerId"].tolist()

        for p in list_pitcher_id:
            pitcher_ind_stats = pitcher_stats[pitcher_stats["playerId"] == p]
            pitcher_name = pitcher_ind_stats.iloc[0]["Name"]
            pitcher_team = pitcher_ind_stats.iloc[-1]["Tm"]
            possible_pitchers = positions[positions['Name'] == pitcher_name]
            correct_pitcher = possible_pitchers[possible_pitchers['Team'] == pitcher_team]

            if correct_pitcher.empty:
                pitcher_position = 'Unknown'
                pitcher_status = 'Unknown'
            else:
                pitcher_position = correct_player.iloc[0]['Position']
                pitcher_status = correct_player.iloc[0]['Status']

            pitcher_obj = Pitcher(pitcher_name, pitcher_team, pitcher_position, pitcher_ind_stats)

            idx = list_abbrv.index(pitcher_team)
            roster_obj = list_roster_objects[idx]
            roster_obj.add_player(pitcher_obj)

    def matchup(self, teams):
        # .sample() does not allow for there to be repeating elements chosen
        matchups = random.sample(teams, 2)
        home_team = matchups[0]
        away_team = matchups[1]


        ## TO DEMONSTRATE ON STATUS REPORT?:

        hi = list_abbrv.index(home_team)
        ai = list_abbrv.index(away_team)

        home_roster = list_roster_objects[hi].get_current_roster()
        away_roster = list_roster_objects[ai].get_current_roster()

        home_list = []
        away_list = []

        for i in home_roster:
            home_list.append((i.get_name(), i.get_position()))

        for i in away_roster:
            away_list.append((i.get_name(), i.get_position()))
        
      
        home_spot = teams.index(home_team)
        away_spot = teams.index(away_team)
        home_team = list_cities[home_spot] + " " + list_team[home_spot]
        away_team = list_cities[away_spot] + " " + list_team[away_spot]
      
        print('Game Matchup:', home_team, '(home) vs', away_team, '(away)')

        print(home_team + " Players:")
        print(home_list)
        print(away_team + " Players:")
        print(away_list)




if __name__ == "__main__":
    # will change this based on dataframes, but keep as list for now
    GameManager().matchup(list_abbrv)





