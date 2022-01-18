
import sys

from pos_lineup import *
from random9_lineup import random9Lineup
from top9_lineup import top9Lineup
from gen_matchup import *

sys.path.append('../')
from results_visuals.player_comp import player_comp
from results_visuals.lineup_compare import lineup_compare


# Initial Visualizations using raw dataframes
player_comp(['Anthony Rizzo', 'Kyle Seager', 'Willson Contreras'], p_hand='Right', start_date='2021-09-01')


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
