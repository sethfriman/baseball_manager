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
    
     def get_pitcher(self): #run for home and away

        pitchers = []
        cleaned_p = []
        for x in self.roster:
            player = x.__dict__
            for a, b in player.items():
                if a == 'position' and b == 'P':
                    pitchers.append(x)

        for p in pitchers:
            pitcher = p.__dict__
            for a, b in pitcher.items():
                if a == 'hand':
                    if b == 'Right' or b == 'Left':
                        cleaned_p.append(pitcher)
                        #print(cleaned_p)
        pitcher_choice = random.choice(cleaned_p)
        pitcher_info = pitcher_choice
        for n, p in pitcher_info.items():
            if n == 'name':
                return pitcher_info
