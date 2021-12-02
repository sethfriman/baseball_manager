import random
import pandas as pd
from game_files.main import *
from player_information.player import *


class Lineup(): #based only on batting stats

    def __init__(self, roster, weighted_stats, pitcher, pos):
        """ Constructor for Lineup """
        self.roster = roster
        self.lineup = {}
        self.weighted_stats = weighted_stats
        self.pos = pos

    def pos_lists(self):
        pos_list = []

        # Stores all non-pitcher players
        non_pitchers = []

        # Appends non-pitchers to non-pitchers list
        for x in self.roster:  # in self.weightedstats?
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
                    for batter in self.weighted_stats['Name']:
                        if batter == name:
                            weighted_non_pitchers.append(player)
        # Appends player name and weighted runs created per game statistic as a tuple to pos_list
        for p in weighted_non_pitchers:
            p = dict(p)
            name = p['name']
            for batter in self.weighted_stats:
                avg_runs = self.weighted_stats[self.weighted_stats['Name'] == name][
                    'weighted_runs_created_per_game'].values[0]
            if p['position'] == self.pos:
                pos_list.append((name, avg_runs))
        return pos_list

    def pos_dict(self, pos_list):
        # # Inserts player with highest weighted runs created per game to position dictionary
        pos_list = sorted(pos_list, key=lambda t: t[1])
        if len(pos_list) != 0:
            self.lineup[self.pos] = pos_list[-1]

        return self.lineup

    def if_LF_RF_empty(self, LF_list, RF_list):
        RF_stats = []
        LF_stats = []
        for p, stat in LF_list:
            LF_stats.append(stat)
        for p, stat in RF_list:
            RF_stats.append(stat)

        if bool(self.lineup) == False:
            if LF_list == 0 or RF_list == 0:
                if len(RF_list) > 1:
                    best_stat = max(RF_stats)
                    RF_stats.remove(best_stat)
                    sec_best = max(RF_stats)
                    for i, s in enumerate(RF_stats):
                        if sec_best == RF_stats[i]:
                            self.lineup['LF'] = (RF_list[i][0], best_stat[0])
                if len(LF_list) > 1:
                    best_stat = max(LF_stats)
                    LF_stats.remove(best_stat)
                    sec_best = max(LF_stats)
                    for i, s in enumerate(LF_stats):
                        if sec_best == LF_stats[i]:
                            self.lineup['RF'] = (LF_list[i][0], best_stat[0])
        else:
            pass


# Call pos_lists and pos_dict for each position in home team
hC = Lineup(home, home_weighted, 'C')
hC_pos_list = hC.pos_lists()
home_C = hC.pos_dict(hC_pos_list)

hB1 = Lineup(home, home_weighted, '1B')
hB1_pos_list = hB1.pos_lists()
home_B1 = hB1.pos_dict(hB1_pos_list)

hB2 = Lineup(home, home_weighted, '2B')
hB2_pos_list = hB2.pos_lists()
home_B2 = hB2.pos_dict(hB2_pos_list)

hB3 = Lineup(home, home_weighted, '3B')
hB3_pos_list = hB3.pos_lists()
home_B3 = hB3.pos_dict(hB3_pos_list)

hSS = Lineup(home, home_weighted, 'SS')
hSS_pos_list = hSS.pos_lists()
home_SS = hSS.pos_dict(hSS_pos_list)

hLF = Lineup(home, home_weighted, 'LF')
hLF_pos_list = hLF.pos_lists()

hRF = Lineup(home, home_weighted, 'RF')
hRF_pos_list = hRF.pos_lists()

home_LF = hLF.pos_dict(hLF_pos_list)
home_RF = hRF.pos_dict(hRF_pos_list)
LF_RF = hLF.if_LF_RF_empty(hLF_pos_list, hRF_pos_list)

hCF = Lineup(home, home_weighted, 'CF')
hCF_pos_list = hCF.pos_lists()
home_CF = hCF.pos_dict(hCF_pos_list)


hDH = Lineup(home, home_weighted, 'DH')
hDH_pos_list = hDH.pos_lists()
home_DH = hDH.pos_dict(hDH_pos_list)


# Combines all position dictionaries into one master home lineup dictionary
home_lineup = {**home_C, **home_B1, **home_B2, **home_B3, **home_SS, **home_LF, **home_CF, **home_RF, **home_DH}
print('Home Lineup: ', home_lineup)


# Converts home lineup dictionary to a pandas dataframe
h_lineup_df = pd.DataFrame(home_lineup.items(), columns=['Position', 'combo'])
pd.DataFrame(h_lineup_df['combo'].tolist(), index=h_lineup_df.index)
h_lineup_df[['Name', 'Weighted runs per game']] = pd.DataFrame(h_lineup_df['combo'].tolist(), index=h_lineup_df.index)
pd.set_option("display.max_rows", None, "display.max_columns", None)
h_lineup_df = h_lineup_df.drop(['combo'], 1)
print(h_lineup_df)
total_wrpg = round(h_lineup_df['Weighted runs per game'].sum(), 2)
print("Lineup's projected runs: ", total_wrpg)

# Call pos_lists and pos_dict for each position in home team
aC = Lineup(away, away_weighted, 'C')
aC_pos_list = aC.pos_lists()
away_C = aC.pos_dict(aC_pos_list)

aB1 = Lineup(away, away_weighted, '1B')
aB1_pos_list = aB1.pos_lists()
away_B1 = aB1.pos_dict(aB1_pos_list)

aB2 = Lineup(away, away_weighted, '2B')
aB2_pos_list = aB2.pos_lists()
away_B2 = aB2.pos_dict(aB2_pos_list)

aB3 = Lineup(away, away_weighted, '3B')
aB3_pos_list = aB3.pos_lists()
away_B3 = aB3.pos_dict(aB3_pos_list)

aSS = Lineup(away, away_weighted, 'SS')
aSS_pos_list = aSS.pos_lists()
away_SS = aSS.pos_dict(aSS_pos_list)

aLF = Lineup(away, away_weighted, 'LF')
aLF_pos_list = aLF.pos_lists()

aCF = Lineup(away, away_weighted, 'CF')
aCF_pos_list = aCF.pos_lists()
away_CF = aCF.pos_dict(aCF_pos_list)

aRF = Lineup(away, away_weighted, 'RF')
aRF_pos_list = aRF.pos_lists()

away_LF = aLF.pos_dict(aLF_pos_list)
away_RF = aRF.pos_dict(aRF_pos_list)
LF_RF = aLF.if_LF_RF_empty(aLF_pos_list, aRF_pos_list)

aDH = Lineup(away, away_weighted, 'DH')
aDH_pos_list = aDH.pos_lists()
away_DH = aDH.pos_dict(aDH_pos_list)

# Combines all position dictionaries into one master home lineup dictionary
away_lineup = {**away_C, **away_B1, **away_B2, **away_B3, **away_SS, **away_LF, **away_CF, **away_RF, **away_DH}
print('Away Lineup: ', away_lineup)

# Converts home lineup dictionary to a pandas dataframe
a_lineup_df = pd.DataFrame(away_lineup.items(), columns=['Position', 'combo'])
pd.DataFrame(a_lineup_df['combo'].tolist(), index=a_lineup_df.index)
a_lineup_df[['Name', 'Weighted runs per game']] = pd.DataFrame(a_lineup_df['combo'].tolist(), index=a_lineup_df.index)
pd.set_option("display.max_rows", None, "display.max_columns", None)
a_lineup_df = a_lineup_df.drop(['combo'], 1)
print(a_lineup_df)
total_wrpg = round(a_lineup_df['Weighted runs per game'].sum(), 2)
print("Lineup's projected runs: ", total_wrpg)


def get_pos_count(B1, B2, B3, LF, RF, CF, SS, C, DH, team):
    """
    Returns bar chart showing player position count for the inputted team.
    X-axis is positions.
    Y-axis is player count.
    """
    positions = ['1B', '2B', '3B', 'LF', 'RF', 'CF', 'SS', 'C', 'DH']
    occurrences = [len(B1), len(B2), len(B3), len(LF), len(RF), len(CF), len(SS), len(C), len(DH)]

    plt.bar(positions, occurrences)
    plt.title('Player Position Count for ' + team)
    plt.xlabel('Positions')
    plt.ylabel('Player Count')
    y_ticks = np.arange(0, 6, 1)
    plt.yticks(y_ticks)
    plt.show()



get_pos_count(hB1_pos_list, hB2_pos_list, hB3_pos_list, hLF_pos_list, hCF_pos_list, hRF_pos_list, hSS_pos_list, hC_pos_list, hDH_pos_list, matchup_tuple[0])
get_pos_count(aB1_pos_list, aB2_pos_list, aB3_pos_list, aLF_pos_list, aCF_pos_list, aRF_pos_list, aSS_pos_list, aC_pos_list, aDH_pos_list, matchup_tuple[1])
