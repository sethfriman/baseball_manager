import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def player_stat_eval(data, column, player, stat):
    """ Pulls Specific Stats for a Player from the desired Data Source """
    injured_df = data[data[column] == player]
    stat_list = list(injured_df[stat])
    return stat_list

# demo scenario
player_df = pd.read_csv('../data_directory/FanGraphs_total.csv')
demo1 = injury_batting_eval(player_df, 'Name', 'Salvador Perez', 'AB')
demo2 = injury_batting_eval(player_df, 'Name', 'Salvador Perez', 'HR')
demo3 = injury_batting_eval(player_df, 'Name', 'Salvador Perez', 'H')

fig = plt.subplots(figsize=(12, 6))
plt.plot(demo1, color='blue', label='Number of At Bats in Game', zorder=2)
plt.plot(demo2, 'k*', label='Number of Home Runs in Game', zorder=3)
plt.plot(demo3, color='red', label='Number of Hits in Game')
plt.title('Post-Injury Batting Evaluation')
plt.xlabel('Number of Played Game Since Return to Play')
plt.ylabel('Count of Statistic')
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.show()
