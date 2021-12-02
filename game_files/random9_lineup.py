#THIS MIGHT STILL NEED TO BE MODIFIED A BIT 
import random
from game_files.main import *
from player_information.player import *
from player_information.roster import *

away_pitcher = get_pitcher(away)
a_p_hand = away_pitcher.get_arm()

home_df = pd.DataFrame()
away_df = pd.DataFrame()

home_pitcher = get_pitcher(home)
h_p_hand = home_pitcher.get_arm()

home_random_9 = []
away_random_9 = []
#def random9Lineup(home_df, away_df, home_a, away_a, home, away):
for player in home:
    try:
        if away_pitcher == 'rhp':
            player_df = player.get_lhp_stats()
        elif away_pitcher == 'lhp':
            player_df = player.get_rhp_stats()
        #else:
            #player_df = player.get_hall_stats()
            #player_df['Position'] = player_df.get_position()
            #home_df = home_df.append(player_df, ignore_index=True)
    except AttributeError as e:
        pass

for player in away:
    try:
        if home_pitcher == 'rhp':
            player_df = player.get_lhp_stats()
        elif home_pitcher == 'lhp':
            player_df = player.get_rhp_stats()
        #else:
            #player_df = player.get_hall_stats()
            #player_df['Position'] = player_df.get_position()
            #away_df = away_df.append(player_df, ignore_index=True)
    except AttributeError as e:
        pass

#home_random_9 = home_df.sort_values('weighted_runs_created_per_game', ascending=False)[:9].reset_index(
            #drop=True)
#away_random_9 = away_df.sort_values('weighted_runs_created_per_game', ascending=False)[:9].reset_index(
            #drop=True)


items = (home_weighted, away_weighted)
home_random_9 = random.choice(items)
away_random_9 = random.choice(items)

home_random_9 = home_random_9[['Name', 'Position', 'weighted_runs_created_per_game']]
away_random_9 = away_random_9[['Name', 'Position', 'weighted_runs_created_per_game']]

# Print the matchup, organizing the data by weighted_runs_created_per_game
print(home_pitcher, ' random lineup based on ', a_p_hand,  ' Handed pitcher:')
print(home_random_9.head(9))
home_er = round(home_random_9.weighted_runs_created_per_game.sum(), 2)
print('Total Expected Runs: ', home_er)
print()
print(away_pitcher, ' random lineup based on ' , h_p_hand,  ' Handed pitcher:')
print(away_random_9.head(9))
away_er = round(away_random_9.weighted_runs_created_per_game.sum(), 2)
print('Total Expected Runs: ', away_er)

    #return home_er, away_er
