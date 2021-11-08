import random
import pandas as pd


class GameManager:

    def __init__(self):
        lhp = pd.read_csv('data directory/FanGraphs_lhp.csv')
        rhp = rhp = pd.read_csv('data directory/FanGraphs_rhp.csv')
        total = pd.read_csv('data directory/FanGraphs_total.csv')
        player_teams = pd.read_csv('data directory/player_teams.csv')
        pitcher_stats = pd.read_csv('data directory/pitcher_data.csv')

        """
        ADD THESE TO THE ROSTERS:
        for each player in player player_teams:
        if player exists in total stats:
            create batter object with them and their stats and team name 
        if player exists in pitcher stats:
            create pitcher object with them and their stats and team name
        if they don't exist in either:
            create player object with team acronym and name
        
        """





def matchup(teams):
    #.sample() does not allow for there to be repeating elements chosen
    matchup = random.sample(teams, 2)
    return print('Game Matchup:', matchup[0], '(home) vs', matchup[1], '(away)')

# will change this based on dataframes, but keep as list for now
bb_teams = ['Atlanta Braves', 'Miami Marlins', 'New York Mets', 'Philadelphia Phillies', 'Washington Nationals', 'Chicago Cubs', 'Cincinnati Reds', 'Milwaukee Brewers', 'Pittsburgh Pirates', 'St. Louis Cardinals', 'Arizona Diamondbacks', 'Colorado Rockies', 'Los Angeles Dodgers', 'San Diego Padres', 'San Francisco Giants', 'Baltimore Orioles', 'Boston Red Sox', 'New York Yankees', 'Tampa Bay Rays', 'Toronto Blue Jays', 'Chicago White Sox', 'Cleveland Indians',
'Detroit Tigers', 'Kansas City Royals', 'Minnesota Twins', 'Houston Astros', 'Los Angeles Angels', 'Oakland Athletics', 'Seattle Mariners', 'Texas Rangers']

matchup(bb_teams)
