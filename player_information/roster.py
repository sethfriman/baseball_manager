# Roster class representing roster for each team
import random


def get_pitcher(roster):  # run for home and away

    pitchers = []
    cleaned_p = []
    for x in roster:
        player = x.__dict__
        for a, b in player.items():
            if a == 'position' and b == 'P':
                pitchers.append(x)

    for p in pitchers:
        pitcher = p.__dict__
        for a, b in pitcher.items():
            if a == 'hand':
                if b == 'Right' or b == 'Left':
                    cleaned_p.append(p)
    pitcher_choice = random.choice(cleaned_p)
    return pitcher_choice


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

    def get_city(self):
        """
        :return: city name
        """
        return self.city

    def add_player(self, player):
        """ Add player to roster """
        self.roster.append(player)

    def get_current_roster(self):
        """
        :return: current roster
        """
        return self.roster
