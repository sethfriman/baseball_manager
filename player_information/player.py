# Player class representing player
import pandas as pd

# IMPORTANT:
# NEED TO ADD IN POSITION FOR ALL AND HANDEDNESS (FOR PITCHER)


class Player:

    def __init__(self, name: str, team_name: str):
        """ Constructor for Player"""
        self.name = name
        self.team_name = team_name

    def get_name(self):
        """
        :return: player name
        """
        return self.name

    def get_team(self):
        """
        :return: player position
        """
        return self.team_name


class Batter(Player):

    def __init__(self, name: str, team_name: str, gen_stats: pd.DataFrame, lhp_stats: pd.DataFrame, rhp_stats: pd.DataFrame):
        """ Constructor for Batter class - is a PLayer"""
        # inherits from player
        super().__init__(name, team_name)

        self.gen_stats = gen_stats
        self.rhp_stats = rhp_stats
        self.lhp_stats = lhp_stats

    def get_all_stats(self):
        """
        :return: aggregated batter stats
        """
        return self.gen_stats

    def get_lhp_stats(self):
        """
        :return: batter stats vs lhp
        """
        return self.lhp_stats

    def get_rhp_stats(self):
        """
        :return: batter stats vs rhp
        """
        return self.rhp_stats


class Pitcher(Player):

    def __init__(self, name: str, team_name: str, stats: pd.DataFrame):
        """Constructor for Pitcher class - is a Player"""

        # inherits from Player
        super().__init__(name, team_name)

        self.stats = stats

    def get_stats(self):
        """
        :return: stats for pitcher
        """
        return self.stats

    #def get_arm(self):
        """
        :return: pitcher throwing arm
        """
        #return self.handedness





