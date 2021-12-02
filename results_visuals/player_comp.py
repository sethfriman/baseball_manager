import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


def player_comp(players_list, p_hand='Total', start_date='2021-01-01'):
    """Creates a Line plot showing the Runs Created by each player listed against a certain type of pitcher over time"""

    # Select the right dataframe based on the pitcher's hand
    if p_hand == 'Total':
        player_df = pd.read_csv('../data_directory/FanGraphs_total.csv')
    elif p_hand == 'Right':
        player_df = pd.read_csv('../data_directory/FanGraphs_rhp.csv')
    elif p_hand == 'Left':
        player_df = pd.read_csv('../data_directory/FanGraphs_lhp.csv')
    else:
        print('NO FILE FOR PITCHER HAND: ', p_hand)
        return

    # manipulate the DF for the right dates and players. Add Runs Created metric
    filtered_df = player_df[(player_df['Name'].isin(players_list)) & (player_df['Date'] > start_date)]
    filtered_df['NameTm'] = filtered_df['Name'] + '-' + filtered_df['Tm']
    filtered_df['total_bases'] = filtered_df['1B'] + (2 * filtered_df['2B']) + \
                                 (3 * filtered_df['3B']) + (4 * filtered_df['HR'])
    filtered_df['Runs Created'] = (((filtered_df['H'] + filtered_df['BB'] -
                                     filtered_df['CS'] + filtered_df['HBP'] -
                                     filtered_df['GDP']) * (
                                            filtered_df['total_bases'] +
                                            (0.26 * (filtered_df['BB'] -
                                                     filtered_df['IBB'] +
                                                     filtered_df['HBP'])) +
                                            0.52 * (filtered_df['SH'] +
                                                    filtered_df['SF'] +
                                                    filtered_df['SB']))) /
                                   (filtered_df['AB'] + filtered_df['BB'] +
                                    filtered_df['HBP'] + filtered_df['SH'] +
                                    filtered_df['SF']))

    # Visualize the data and save the resulting plot
    fig, ax = plt.subplots()
    #fig.set_size_inches(30, 15)
    dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in filtered_df.Date.values]
    filtered_df['Date'] = dates
    dates.sort()
    date_set = list(set(dates))
    date_set.sort()
    filtered_df = filtered_df.sort_values('Date')
    dates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
    date_set = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in date_set]
    filtered_df['Date'] = dates
    sns.lineplot(x='Date', y='Runs Created', hue='NameTm', data=filtered_df, ax=ax)
    ax.set_xticklabels(date_set, rotation=45, horizontalalignment='right')
    ax.set_title('Runs Created Comparison Chart')
    fig.savefig('../results_visuals/player_comp.png')