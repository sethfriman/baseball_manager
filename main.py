import random

def matchup(teams):
    #.sample() does not allow for there to be repeating elements chosen
    matchup = random.sample(teams, 2)
    return print('Game Matchup:', matchup[0], '(home) vs', matchup[1], '(away)')

# will change this based on dataframes, but keep as list for now
bb_teams = ['Atlanta Braves', 'Miami Marlins', 'New York Mets', 'Philadelphia Phillies', 'Washington Nationals', 'Chicago Cubs', 'Cincinnati Reds', 'Milwaukee Brewers', 'Pittsburgh Pirates', 'St. Louis Cardinals', 'Arizona Diamondbacks', 'Colorado Rockies', 'Los Angeles Dodgers', 'San Diego Padres', 'San Francisco Giants', 'Baltimore Orioles', 'Boston Red Sox', 'New York Yankees', 'Tampa Bay Rays', 'Toronto Blue Jays', 'Chicago White Sox', 'Cleveland Indians',
'Detroit Tigers', 'Kansas City Royals', 'Minnesota Twins', 'Houston Astros', 'Los Angeles Angels', 'Oakland Athletics', 'Seattle Mariners', 'Texas Rangers']

matchup(bb_teams)
