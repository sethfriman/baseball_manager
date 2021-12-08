import matplotlib.pyplot as plt
import pandas as pd
import warnings
import seaborn as sns
warnings.filterwarnings("ignore")

def player_stat_eval(data, column, player, stat, start_date, end_date):
    """ Pulls Specific Stats for a Player from the desired Data Source """
    data['10game_rolling_avg'] = data.H.rolling(10).mean()
    specific_df = data[data[column] == player]
    specific_df = specific_df[specific_df['Date'] > start_date]
    specific_df = specific_df[specific_df['Date'] < end_date]
    final_df = specific_df[[stat, '10game_rolling_avg']]
    return final_df


# Demo Example: Injury Report
player_df = pd.read_csv('../data_directory/FanGraphs_total.csv')

before_injury = player_stat_eval(player_df, 'Name', 'David Bote', 'H', '2020-07-27', '2021-05-29')
after_injury = player_stat_eval(player_df, 'Name', 'David Bote', 'H', '2021-07-01', '2021-09-30')

sns.set_palette("bright")
plt.figure(figsize=(12, 5))

sns.lineplot(x=range(len(before_injury)),
             y='H',
             data=before_injury,
             label='Hits per Game (Before Injury: 2020 + 2021)',
             linestyle='dashed',
             alpha=0.3)
sns.lineplot(x=range(len(after_injury)),
             y='H',
             data=after_injury,
             label='Hits per Game (After Injury: 2021 Season)',
             linestyle='dashed',
             alpha=0.3)
# plot using rolling average
sns.lineplot(x=range(len(before_injury)),
             y='10game_rolling_avg',
             data=before_injury,
             label='Rolling Average Hits per Game (Before Injury: 2020 + 2021)',
             linewidth=2)
sns.lineplot(x=range(len(after_injury)),
             y='10game_rolling_avg',
             data=after_injury,
             label='Rolling Average Hits per Game (After Injury: 2021)',
             linewidth=2)
plt.xlabel('Number of Games Played in Season')
plt.ylabel('Number of Hits per Game')
plt.title('Post-Injury Batting Evaluation: David Bote')
plt.show()
