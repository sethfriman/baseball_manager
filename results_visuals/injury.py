import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


def injury_batting_eval(data, column, player):
    injured_df = data[data[column] == player]
    fig = plt.subplots(figsize=(12, 6))

    ABs = list(injured_df['AB'])
    HR = list(injured_df['HR'])
    H = list(injured_df['H'])

    plt.plot(ABs, color='blue', label='Number of At Bats in Game', zorder=2)
    plt.plot(HR, 'k*', label='Number of Home Runs in Game', zorder=3)
    plt.plot(H, color='red', label='Number of Hits in Game')
    plt.title('Post-Injury Batting Evaluation')
    plt.xlabel('Number of Played Game Since Return to Play')
    plt.ylabel('Count of Statistic')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()


player_df = pd.read_csv('../data_directory/FanGraphs_total.csv')
print(injury_batting_eval(player_df, 'Name', 'Salvador Perez'))

