# Roster class representing roster for each team

class Roster:

    def __init__(self, name: str, city: str, abbreviation: str):
        """ Constructor for Roster """
        self.name = name
        self.city = city
        self.abbreviation = abbreviation
        self.roster = []

    def get_name(self):
        """
        :return: team name
        """
        return self.name

    def get_abbreviation(self):
        """
        :return: team abbreviation
        """
        return self.abbreviation

    # def get_city(self):
    #     """
    #     :return: city name
    #     """
    #     return self.city

    def add_player(self, player):
        """ Add player to roster """
        self.roster.append(player)

    def get_current_roster(self):
        """
        :return: current roster
        """
        return self.roster
