import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


abv = ['ARI', 'ATL', 'BAL', 'BOS', 'CHW', 'CHC', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD',
                      'MIA', 'MIL', 'MIN', 'NYY', 'NYM', 'OAK', 'PHI', 'PIT', 'SDP', 'SFG', 'SEA', 'STL', 'TBR', 'TEX',
                      'TOR', 'WSN']

list_league = ['NL', 'NL', 'AL', 'AL', 'AL', 'NL', 'NL', 'AL', 'NL', 'AL', 'AL', 'AL', 'AL', 'NL', 'NL', 'NL', 'NL', 'AL',
               'NL', 'AL', 'NL', 'NL', 'NL', 'NL', 'AL', 'NL', 'AL', 'NL', 'AL', 'NL']



# reading necessary data into dataframes
standings_df = pd.read_csv('../data_directory/standings_2021.csv')
stats_df = pd.read_csv('../data_directory/FanGraphs_total.csv')
# changing date column to datetime
stats_df['Date'] = pd.to_datetime(stats_df['Date'], format="%Y/%m/%d")
# only including 2021 stats
stats_2021 = stats_df[stats_df['Date'] > datetime.datetime(2021,1,1)]

#runs created metric for each game
stats_2021['total_bases'] = stats_2021['1B'] + (2 * stats_2021['2B']) + \
                                 (3 * stats_2021['3B']) + (4 * stats_2021['HR'])
stats_2021['Runs Created'] = (((stats_2021['H'] + stats_2021['BB'] -
                                     stats_2021['CS'] + stats_2021['HBP'] -
                                     stats_2021['GDP']) * (
                                            stats_2021['total_bases'] +
                                            (0.26 * (stats_2021['BB'] -
                                                     stats_2021['IBB'] +
                                                     stats_2021['HBP'])) +
                                            0.52 * (stats_2021['SH'] +
                                                    stats_2021['SF'] +
                                                    stats_2021['SB']))) /
                                   (stats_2021['AB'] + stats_2021['BB'] +
                                    stats_2021['HBP'] + stats_2021['SH'] +
                                    stats_2021['SF']))


def get_wins_vs_rc(list_teams, list_leagues):
    """
    returns: scatter plot depicting team's runs created in 2021 vs wins, along with their league
    """
    list_wins = []
    list_rc = []
    df = pd.DataFrame()
    for i in list_teams:
        team_df = standings_df[standings_df['Tm'] == i]
        team_df = team_df.reset_index()
        team_wins = team_df['W'][0]
        team_stats_df = stats_2021[stats_2021['Tm'] == i]
        total_rc = team_stats_df['Runs Created'].sum()
        list_wins.append(team_wins)
        list_rc.append(total_rc)
    dict_wins = {'color': abv, 'wins': list_wins, 'rc': list_rc, 'style': list_leagues}
    df = pd.DataFrame(dict_wins)
    sns.scatterplot(x='rc', y='wins', data=df, hue='color', style='style', legend='full')
    plt.legend(bbox_to_anchor=(1.01, 1),
               borderaxespad=0)
    plt.title("Total Team Runs Created Vs. Wins 2021")
    plt.xlabel("Team Runs Created in 2021")
    plt.ylabel("Wins")
    plt.show()


get_wins_vs_rc(abv, list_league)