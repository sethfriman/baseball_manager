import pandas as pd
import numpy as np
import datetime


def create_roster_df(team, df):
    """Filers the larger dataframe down to a single team to make the data easier to work with"""
    return df[df['team'] == team]


def weight_stats(player_df, stat_cols, pitcher_handedness='both'):
    """Helper function for weight_stats_df that does the actual weighting of each stat"""
    if pitcher_handedness == 'both':
        filtered_player_df = player_df.groupby(['player_name', 'team', 'position', 'game_date', 'months_ago']).sum()
        col_tag = '_vs_total'
    else:
        filtered_player_df = player_df[player_df['pitcher_handedness'] == pitcher_handedness]
        if pitcher_handedness == 'right':
            col_tag = '_vs_rhp'
        else:
            col_tag = '_vs_lhp'

    total_months = filtered_player_df.months_ago.sum()
    filtered_player_df['weight_effect'] = ((total_months - filtered_player_df['months_ago']) / total_months)\
        .astype(float)

    player_dict = {}
    for col in stat_cols:
        filtered_player_df[col+'weighted'] = filtered_player_df[col] * filtered_player_df['weight_effect']
        player_dict[col+col_tag] = [filtered_player_df[col+'weighted'].sum()]

    return pd.DataFrame(player_dict)


def weight_stats_df(team_df, stat_columns):
    """Creates a dataframe for the given team that aggregates each of the players' stats against each
       type of pitcher they face, and weighs the number based on how recent the game was"""
    final_day = datetime.datetime.strptime('2021-10-03', '%Y-%m-%d')  # last day of 2021 regular season

    roster = list(set(team_df.player_name.values))
    using_stat_columns = []
    for col in stat_columns:
        if col in ['player_name', 'team', 'position']:
            using_stat_columns.append(col)
        else:
            using_stat_columns.append(col + '_vs_rhp')
            using_stat_columns.append(col + '_vs_lhp')
            using_stat_columns.append(col + '_vs_total')

    agg_roster_df = pd.DataFrame(columns=using_stat_columns)

    for player in roster:
        player_df = team_df[team_df['player_name'] == player]
        player_df = player_df.sort_values('game_date', ascending=False)
        player_df['months_ago'] = (final_day.year - player_df['game_date'].year) * 12 + \
                                  (final_day.month - player_df['game_date'].month)
        player_df_right = weight_stats(player_df, stat_columns, 'right')
        player_df_left = weight_stats(player_df, stat_columns, 'left')
        player_df_total = weight_stats(player_df, stat_columns)
        total_player_df = player_df_right.merge(player_df_left, on='player_name', how='outer')
        total_player_df = total_player_df.merge(player_df_total, on='player_name', how='outer')
        total_player_df = total_player_df[using_stat_columns]
        agg_roster_df = agg_roster_df.append(total_player_df, ignore_index=True)

