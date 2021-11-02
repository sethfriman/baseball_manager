# Player class representing player

class Player:

    def __init__(self, name: str, position: str):
        """ Constructor for Player"""
        self.name = name
        self.position = position

    def get_name(self):
        """
        :return: player name
        """
        return self.name

    def get_position(self):
        """
        :return: player position
        """
        return self.position


class Batter(Player):

    def __init__(self,name: str, position: str, gen_stats: dict, lhp_stats: dict, rhp_stats: dict):
        """ Constructor for Batter class - is a PLayer"""
        # inherits from player
        super().__init__(self, name, position)

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

    def __init__self(self, name: str, position: str, stats: dict, handedness: str):
        """Constructor for Pitcher class - is a Player"""

        # inherits from Player
        super().__init__(self, name, position)

        self.stats = stats
        self.handedness = handedness

    def get_stats(self):
        """
        :return: stats for pitcher
        """
        return self.stats

    def get_arm(self):
        """
        :return: pitcher throwing arm
        """
        return self.handedness





