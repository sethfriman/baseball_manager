import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class PositionLineup():

    def __init__(self):
        """ Constructor for Lineup """
        self.lineup = {}

    def pos_lists(self, roster, pos, w_stats):
        """ Returns list of potential players for inputted position """
        pos_list = []

        # Stores all non-pitcher players
        non_pitchers = []

        # Appends non-pitchers to non-pitchers list
        for x in roster:
            player = x.__dict__
            player_items = player.items()
            for a, b in player_items:
                if a == 'position' and b != 'P' and b != 'Unknown':
                    non_pitchers.append(player_items)

        # Appends player to weighted_non_pitchers to filter out any players with no weighted runs created per game statistic (if player in
        weighted_non_pitchers = []
        for player in non_pitchers:
            for a, b in player:
                if a == 'name':
                    name = b
                    for batter in w_stats['Name']:
                        if batter == name:
                            weighted_non_pitchers.append(player)
        # Appends player name and weighted runs created per game statistic as a tuple to pos_list
        for p in weighted_non_pitchers:
            p = dict(p)
            name = p['name']
            for batter in w_stats:
                avg_runs = w_stats[w_stats['Name'] == name][
                    'weighted_runs_created_per_game'].values[0]
            if p['position'] == pos:
                pos_list.append((name, avg_runs))
        return pos_list

    def pos_dict(self, pos_list, pos):
        """ Returns Lineup for Inputted Position """
        # Inserts player with highest weighted runs created per game to position dictionary
        pos_list = sorted(pos_list, key=lambda t: t[1])
        if len(pos_list) != 0:
            self.lineup[pos] = pos_list[-1]

        return self.lineup

    def if_LF_RF_empty(self, LF_list, RF_list):
        """ Inserts left or right fielder into lineup if more than one is available and the 
        roster does not have a player for one of these positions """
        
        if not bool(self.lineup):
            if LF_list == 0 or RF_list == 0:
                if len(RF_list) > 0:
                    RF_list = sorted(RF_list, key=lambda t: t[1])
                    self.lineup['LF'] = RF_list[-2]
                if len(LF_list) > 0:
                    LF_list = sorted(LF_list, key=lambda t: t[1])
                    self.lineup['RF'] = LF_list[-2]
        else:
            pass
        
def lineup_df(lineup_dict):
    """ Converts dictionary into dataframe and returns dataframe and total runs created by the lineup """
    df = pd.DataFrame(lineup_dict.items(), columns=['Position', 'combo'])
    pd.DataFrame(df['combo'].tolist(), index=df.index)
    df[['Name', 'Weighted runs per game']] = pd.DataFrame(df['combo'].tolist(), index=df.index)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = df.drop(['combo'], 1)
    total_wrpg = round(df['Weighted runs per game'].sum(), 2)
    return df, total_wrpg

def make_pos_lineup(home_team, away_team, home_w_stats, away_w_stats, home_name, away_name):
    """ Returns home and away lineups using PositionLineup class """
    
    L = PositionLineup()

    hC_pos_list = L.pos_lists(home_team, 'C', home_w_stats)
    home_C = L.pos_dict(hC_pos_list, 'C')

    hB1_pos_list = L.pos_lists(home_team, '1B', home_w_stats)
    home_B1 = L.pos_dict(hB1_pos_list, '1B')

    hB2_pos_list = L.pos_lists(home_team, '2B', home_w_stats)
    home_B2 = L.pos_dict(hB2_pos_list, '2B')

    hB3_pos_list = L.pos_lists(home_team, '3B', home_w_stats)
    home_B3 = L.pos_dict(hB3_pos_list, '3B')

    hSS_pos_list = L.pos_lists(home_team, 'SS', home_w_stats)
    home_SS = L.pos_dict(hSS_pos_list, 'SS')

    hLF_pos_list = L.pos_lists(home_team, 'LF', home_w_stats)

    hRF_pos_list = L.pos_lists(home_team, 'RF', home_w_stats)

    home_LF = L.pos_dict(hLF_pos_list, 'LF')
    home_RF = L.pos_dict(hRF_pos_list, 'RF')
    L.if_LF_RF_empty(hLF_pos_list, hRF_pos_list)

    hCF_pos_list = L.pos_lists(home_team, 'CF', home_w_stats)
    home_CF = L.pos_dict(hCF_pos_list, 'CF')

    hDH_pos_list = L.pos_lists(home_team, 'DH', home_w_stats)
    home_DH = L.pos_dict(hDH_pos_list, 'DH')

    # Combines all position dictionaries into one master home lineup dictionary
    # Research From: https://www.geeksforgeeks.org/python-merging-two-dictionaries/
    home_lineup = {**home_C, **home_B1, **home_B2, **home_B3, **home_SS, **home_LF, **home_CF, **home_RF, **home_DH}

    # Away Team
    aC_pos_list = L.pos_lists(away_team, 'C', away_w_stats)
    away_C = L.pos_dict(aC_pos_list, 'C')

    aB1_pos_list = L.pos_lists(away_team, '1B', away_w_stats)
    away_B1 = L.pos_dict(aB1_pos_list, '1B')

    aB2_pos_list = L.pos_lists(away_team, '2B', away_w_stats)
    away_B2 = L.pos_dict(aB2_pos_list, '2B')

    aB3_pos_list = L.pos_lists(away_team, '3B', away_w_stats)
    away_B3 = L.pos_dict(aB3_pos_list, '3B')

    aSS_pos_list = L.pos_lists(away_team, 'SS', away_w_stats)
    away_SS = L.pos_dict(aSS_pos_list, 'SS')

    aLF_pos_list = L.pos_lists(away_team, 'LF', away_w_stats)

    aCF_pos_list = L.pos_lists(away_team, 'CF', away_w_stats)
    away_CF = L.pos_dict(aCF_pos_list, 'CF')

    aRF_pos_list = L.pos_lists(away_team, 'C', away_w_stats)

    away_LF = L.pos_dict(aLF_pos_list, 'LF')
    away_RF = L.pos_dict(aRF_pos_list, 'RF')
    L.if_LF_RF_empty(aLF_pos_list, aRF_pos_list)

    aDH_pos_list = L.pos_lists(away_team, 'DH', away_w_stats)
    away_DH = L.pos_dict(aDH_pos_list, 'DH')

    # Combines all position dictionaries into one master home lineup dictionary
    # Research From: https://www.geeksforgeeks.org/python-merging-two-dictionaries/
    away_lineup = {**away_C, **away_B1, **away_B2, **away_B3, **away_SS, **away_LF, **away_CF, **away_RF, **away_DH}

    # Creates Position Ratio Bar Graph for each lineup
    get_pos_count(hB1_pos_list, hB2_pos_list, hB3_pos_list, hLF_pos_list, hCF_pos_list, hRF_pos_list, hSS_pos_list,
                  hC_pos_list, hDH_pos_list, home_name)
    get_pos_count(aB1_pos_list, aB2_pos_list, aB3_pos_list, aLF_pos_list, aCF_pos_list, aRF_pos_list, aSS_pos_list,
                  aC_pos_list, aDH_pos_list, away_name)
    return home_lineup, away_lineup

def get_pos_count(B1, B2, B3, LF, RF, CF, SS, C, DH, team):
    """
    Returns bar chart showing player position count for the inputted team.
    X-axis is positions.
    Y-axis is player count.
    """

    positions = ['1B', '2B', '3B', 'LF', 'RF', 'CF', 'SS', 'C', 'DH']
    occurrences = [len(B1), len(B2), len(B3), len(LF), len(RF), len(CF), len(SS), len(C), len(DH)]

    fig, ax = plt.subplots()

    ax.bar(positions, occurrences)
    plt.title('Player Position Count for ' + team)
    plt.xlabel('Positions')
    plt.ylabel('Player Count')
    y_ticks = np.arange(0, 6, 1)
    plt.yticks(y_ticks)
    plt.show()
    fig.savefig(f'../results_visuals/position_ratios_{team}.png')
