# Player class representing player
import pandas as pd

class Player:

    def __init__(self, name: str, team_name: str, position: str):
        """ Constructor for Player"""
        self.name = name
        self.team_name = team_name
        self.position = position

    def get_name(self):
        """
        :return: player name
        """
        return self.name

    def get_team(self):
        """
        :return: player team
        """
        return self.team_name

    def get_position(self):
        """
        return: player position
        """
        return self.position


class Batter(Player):

    def __init__(self, name: str, team_name: str, position: str, gen_stats: pd.DataFrame, lhp_stats: pd.DataFrame, rhp_stats: pd.DataFrame):
        """ Constructor for Batter class - is a PLayer"""
        # inherits from player
        super().__init__(name, team_name, position)

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

    def __init__(self, name: str, team_name: str, position: str, hand: str, stats: pd.DataFrame):
        """Constructor for Pitcher class - is a Player"""

        # inherits from Player
        super().__init__(name, team_name, position)

        self.stats = stats
        self.hand = hand

    def get_stats(self):
        """
        :return: stats for pitcher
        """
        return self.stats

    def get_arm(self):
        """
        :return: pitcher throwing arm
        """
        return self.hand





