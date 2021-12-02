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
        self.pitcher = pitcher
        self.pos = pos

    def get_position(self):
        """ Returns lineup based on player position and weighted_runs_created_per_game statistic """

        # Initializing position lists to store all players in their respective position list
        SS = []
        LF = []
        CF = []
        RF = []
        B1 = []
        B2 = []
        B3 = []
        C = []
        DH = []

        # Initializing nested position dictionaries in master dictionary self.lineup
        self.lineup['1B'] = {}
        self.lineup['2B'] = {}
        self.lineup['3B'] = {}
        self.lineup['LF'] = {}
        self.lineup['CF'] = {}
        self.lineup['RF'] = {}
        self.lineup['SS'] = {}
        self.lineup['C'] = {}
        self.lineup['DH'] = {}

        # Stores all non-pitcher players
        non_pitchers = []

        # Opens pitcher object
        pitcher = self.pitcher.__dict__

        # Appends non-pitchers to non-pitchers list
        for x in self.roster: #in self.weightedstats?
            player = x.__dict__
            player_items = player.items()
            for a, b in player_items:
                if a == 'position' and b != 'P' and b != 'Unknown':
                    non_pitchers.append(player_items)

        #drop from non-pitchers if not in weighted stats df bc that way avoid nan/empty array for stat


        # Appends player name and weighted_runs_created_per_game statistic to position lists
        weighted_non_pitchers = []
        for player in non_pitchers:
            for a, b in player:
                if a == 'name':
                    name = b

                    for batter in self.weighted_stats['Name']:
                        if batter == name:
                            weighted_non_pitchers.append(player)
        for p in weighted_non_pitchers:
            for a, b in p:
                if a == 'name':
                    name = b
                    for batter in self.weighted_stats:
                        avg_runs = self.weighted_stats.loc[self.weighted_stats['Name'] == name][
                                        'weighted_runs_created_per_game'].values
                if a == 'position' and b == '1B':
                    B1.append((name, avg_runs))
                if a == 'position' and b == '2B':
                    B2.append((name, avg_runs))
                if a == 'position' and b == '3B':
                    B3.append((name, avg_runs))
                if a == 'position' and b == 'LF':
                    LF.append((name, avg_runs))
                if a == 'position' and b == 'CF':
                    CF.append((name, avg_runs))
                if a == 'position' and b == 'RF':
                    RF.append((name, avg_runs))
                if a == 'position' and b == 'SS':
                    SS.append((name, avg_runs))
                if a == 'position' and b == 'C':
                    C.append((name, avg_runs))
                if a == 'position' and b == 'DH':
                    DH.append((name, avg_runs))

        # Inserts 1B player with highest weighted_runs_created_per_game to position dictionary
        B1_stats = []
        for p, stat in B1:
            # if only one player in position list
            if len(B1) == 1:
                self.lineup['1B'] = p
            # if multiple players in position list, pick player with higher statistic
            if len(B1) > 1:
                B1_stats.append(stat)
                best_stat = max(B1_stats)
                for i, s in enumerate(B1_stats):
                    if best_stat == B1_stats[i]:
                        self.lineup['1B'] = (B1[i][0], best_stat[0])

        B2_stats = []
        for p, stat in B2:
            if len(B2) == 1:  # if only one player with this position
                self.lineup['2B'] = p
            if len(B2) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                B2_stats.append(stat)
                best_stat = max(B2_stats)
                for i, s in enumerate(B2_stats):
                    if best_stat == B2_stats[i]:
                        self.lineup['2B'] = (B2[i][0], best_stat[0])

        B3_stats = []
        for p, stat in B3:
            if len(B3) == 1:  # if only one player with this position
                self.lineup['3B'] = p
            if len(B3) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                B3_stats.append(stat)
                best_stat = max(B3_stats)
                for i, s in enumerate(B3_stats):
                    if best_stat == B3_stats[i]:
                        self.lineup['3B'] = (B3[i][0], best_stat[0])

        LF_stats = []
        for p, stat in LF:
            if len(LF) == 1:  # if only one player with this position
                self.lineup['LF'] = p
            if len(LF) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                LF_stats.append(stat)
                best_stat = max(LF_stats)
                for i, s in enumerate(LF_stats):
                    if best_stat == LF_stats[i]:
                        self.lineup['LF'] = (LF[i][0], best_stat[0])

        RF_stats = []
        for p, stat in RF:
            if len(RF) == 1:  # if only one player with this position
                self.lineup['RF'] = p
            if len(RF) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                RF_stats.append(stat)
                best_stat = max(RF_stats)
                for i, s in enumerate(RF_stats):
                    if best_stat == RF_stats[i]:
                        self.lineup['RF'] = (RF[i][0], best_stat[0])

        # If there are no LF or RF players in the position lists, use LF for RF and vice versa if there are enough players in the position lists
        if len(LF) == 0 or len(RF) == 0:
            if len(RF) > 1:
                best_stat = max(RF_stats)
                RF_stats.remove(best_stat)
                sec_best = max(RF_stats)
                for i, s in enumerate(RF_stats):
                    if sec_best == RF_stats[i]:
                        self.lineup['LF'] = (RF[i][0], best_stat[0])
            if len(LF) > 1:
                best_stat = max(LF_stats)
                LF_stats.remove(best_stat)
                sec_best = max(LF_stats)
                for i, s in enumerate(LF_stats):
                    if sec_best == LF_stats[i]:
                        self.lineup['RF'] = (LF[i][0], best_stat[0])

        CF_stats = []
        for p, stat in CF:
            if len(CF) == 1:  # if only one player with this position
                self.lineup['CF'] = p
            if len(CF) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                CF_stats.append(stat)
                best_stat = max(CF_stats)
                for i, s in enumerate(CF_stats):
                    if best_stat == CF_stats[i]:
                        self.lineup['CF'] = (CF[i][0], best_stat[0])

        C_stats = []
        for p, stat in C:
            if len(C) == 1:  # if only one player with this position
                self.lineup['C'] = p
            if len(C) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                C_stats.append(stat)
                best_stat = max(C_stats)
                for i, s in enumerate(C_stats):
                    if best_stat == C_stats[i]:
                        self.lineup['C'] = (C[i][0], best_stat[0])

        SS_stats = []
        for p, stat in SS:
            if len(SS) == 1:  # if only one player with this position
                self.lineup['SS'] = p
            if len(SS) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                SS_stats.append(stat)
                best_stat = max(SS_stats)
                for i, s in enumerate(SS_stats):
                    if best_stat == SS_stats[i]:
                        self.lineup['SS'] = (SS[i][0], best_stat[0])

        DH_stats = []
        for p, stat in DH:
            if len(DH) == 1:  # if only one player with this position
                self.lineup['DH'] = p
            if len(DH) > 1:  # if multiple players with this position, pick player with higher avg runs per game stat
                DH_stats.append(stat)
                best_stat = max(DH_stats)
                for i, s in enumerate(DH_stats):
                    if best_stat == DH_stats[i]:
                        self.lineup['DH'] = (DH[i][0], best_stat[0])
        print(self.lineup)
        lineup_df = pd.DataFrame(list(self.lineup.items()), columns=['a', 'b'])
        lineup_df[['b1', 'b2']] = lineup_df['b'].to_list()
        print(lineup_df)



        reserves = []
        reserves_tuple = []
        for player in weighted_non_pitchers:
            reserves.append(player)
        for sub in reserves:
            for a, b in sub:
                if a == 'name':
                    name = b
                    for batter in self.weighted_stats:
                        avg_runs = self.weighted_stats.loc[self.weighted_stats['Name'] == name][
                            'weighted_runs_created_per_game'].values
                if a == 'position':
                    pos = b
                    reserves_tuple.append((name, pos, avg_runs[0]))

        reserves_tuple_sorted = sorted(reserves_tuple, key=lambda tup: tup[2], reverse=True)

        lineup_names = []
        for k, v in self.lineup.items():
            if len(v) != 0:
                lineup_names.append(v)

        possible_subs = [name for name in reserves_tuple_sorted if p[0] not in lineup_names]

    def pos_lists(self):
        pos_list = []

        # Stores all non-pitcher players
        non_pitchers = []

        # Opens pitcher object
        pitcher = self.pitcher.__dict__

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
hC = Lineup(home, home_weighted, away_pitcher, 'C')
hC_pos_list = hC.pos_lists()
home_C = hC.pos_dict(hC_pos_list)

hB1 = Lineup(home, home_weighted, away_pitcher, '1B')
hB1_pos_list = hB1.pos_lists()
home_B1 = hB1.pos_dict(hB1_pos_list)

hB2 = Lineup(home, home_weighted, away_pitcher, '2B')
hB2_pos_list = hB2.pos_lists()
home_B2 = hB2.pos_dict(hB2_pos_list)

hB3 = Lineup(home, home_weighted, away_pitcher, '3B')
hB3_pos_list = hB3.pos_lists()
home_B3 = hB3.pos_dict(hB3_pos_list)

hSS = Lineup(home, home_weighted, away_pitcher, 'SS')
hSS_pos_list = hSS.pos_lists()
home_SS = hSS.pos_dict(hSS_pos_list)

hLF = Lineup(home, home_weighted, away_pitcher, 'LF')
hLF_pos_list = hLF.pos_lists()

hRF = Lineup(home, home_weighted, away_pitcher, 'RF')
hRF_pos_list = hRF.pos_lists()

home_LF = hLF.pos_dict(hLF_pos_list)
home_RF = hRF.pos_dict(hRF_pos_list)
LF_RF = hLF.if_LF_RF_empty(hLF_pos_list, hRF_pos_list)

hCF = Lineup(home, home_weighted, away_pitcher, 'CF')
hCF_pos_list = hCF.pos_lists()
home_CF = hCF.pos_dict(hCF_pos_list)


hDH = Lineup(home, home_weighted, away_pitcher, 'DH')
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
aC = Lineup(away, away_weighted, home_pitcher, 'C')
aC_pos_list = aC.pos_lists()
away_C = aC.pos_dict(aC_pos_list)

aB1 = Lineup(away, away_weighted, home_pitcher, '1B')
aB1_pos_list = aB1.pos_lists()
away_B1 = aB1.pos_dict(aB1_pos_list)

aB2 = Lineup(away, away_weighted, home_pitcher, '2B')
aB2_pos_list = aB2.pos_lists()
away_B2 = aB2.pos_dict(aB2_pos_list)

aB3 = Lineup(away, away_weighted, home_pitcher, '3B')
aB3_pos_list = aB3.pos_lists()
away_B3 = aB3.pos_dict(aB3_pos_list)

aSS = Lineup(away, away_weighted, home_pitcher, 'SS')
aSS_pos_list = aSS.pos_lists()
away_SS = aSS.pos_dict(aSS_pos_list)

aLF = Lineup(away, away_weighted, home_pitcher, 'LF')
aLF_pos_list = aLF.pos_lists()

aCF = Lineup(away, away_weighted, home_pitcher, 'CF')
aCF_pos_list = aCF.pos_lists()
away_CF = aCF.pos_dict(aCF_pos_list)

aRF = Lineup(away, away_weighted, home_pitcher, 'RF')
aRF_pos_list = aRF.pos_lists()

away_LF = aLF.pos_dict(aLF_pos_list)
away_RF = aRF.pos_dict(aRF_pos_list)
LF_RF = aLF.if_LF_RF_empty(aLF_pos_list, aRF_pos_list)

aDH = Lineup(away, away_weighted, home_pitcher, 'DH')
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
