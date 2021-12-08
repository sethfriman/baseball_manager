from game_files.gen_matchup import *
from game_files.pos_lineup import *
import pandas as pd
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns


# Convert BOS 2021 schedule to pandas df
rs_sched = pd.read_csv('../data_directory/redsox_schedule.csv')


def team_pred(team_schedule, team_abbrev):
    """ Runs each game from Red Sox schedule through genMatchup and
        make_pos_lineup to gather the predicted Red Sox lineups for each game in the 2021 season.
        Returns a list of lists, where each list is the predicted player names for each game. """

    all_team_preds = []

    for index, row in team_schedule.iterrows():
        date = row['Date']
        opp_abbrev = row['Opp']
        team_weighted, opp_weighted, team_name, opp_name, team_p_hand, opp_p_hand, team, opp = genMatchup(home=team_abbrev, away=opp_abbrev, h_p_hand=None, a_p_hand=None, before_date=date)
        pos_team, pos_opp = make_pos_lineup(team, opp, team_weighted, opp_weighted, team_name, opp_name)
        team_poslineup_df, team_weight_num = lineup_df(pos_team)
        team_pred = list(team_poslineup_df['Name'])
        all_team_preds.append(team_pred)

    return all_team_preds

def team_acc(team_schedule, team_abbrev):
    """ Pulls all players that actually played during each game throughout the season.
        Each game lineup is stored as a list of player names in a master list, which is returned. """

    all_team_acc = []
    all_batters = pd.read_csv('../data_directory/FanGraphs_total.csv')

    for index, row in team_schedule.iterrows():
        date = row['Date']
        batters = all_batters[(all_batters['Date'] == date)]
        batters = batters[(batters['Tm'] == team_abbrev)]
        team_acc = list(batters['Name'])

        # Removed subs as our data does not account for them
        team_acc_nosubs = team_acc[:9]
        all_team_acc.append(team_acc_nosubs)

    return all_team_acc


def multi_accuracy(lineup_pred, lineup_real):
    """ Compares entire team's season of games to determine lineup accuracy of predicted lineups """

    # https://www.geeksforgeeks.org/python-zipping-two-lists-of-lists/
    zipped = [list(itertools.chain(*i))
           for i in zip(lineup_pred, lineup_real)]

    all_acc_percentages = []

    for lst in zipped:
        # if appended to yes_list, actual = predicted for that player
        yes_list = []
        # if appended to no_list, actual != predicted for that player
        no_list = []

        counter = Counter(lst)

        for k, v in counter.items():
            if v == 2:
                yes_list.append(k)
            else:
                no_list.append(k)

        # Calculates accuracy of predicted positional lineup compared to actual lineup
        accuracy = len(yes_list) / ((len(yes_list) + (len(no_list))))
        percent = round((accuracy * 100), 2)
        all_acc_percentages.append(percent)

    return all_acc_percentages


def single_accuracy(lineup_pred, lineup_real):
    """ Compares predicted and actual lineups for a single game """
    # if appended to yes_list, actual = predicted for that player
    yes_list = []
    # if appended to no_list, actual != predicted for that player
    no_list = []

    for item in lineup_pred:
        if item in lineup_real:
            yes_list.append(item)
        else:
            no_list.append(item)
    for item in lineup_real:
        if item not in lineup_pred:
            no_list.append(item)

    # Calculates accuracy of predicted positional lineup compared to actual lineup
    accuracy = len(yes_list) / ((len(yes_list) + (len(no_list))))
    percent = round((accuracy * 100), 2)
    return percent


def lineup_comp_graph(team_abbrev):
    """ Outputs line graph showing the lineup accuracy for each game over the course of the season.
        Calculates rolling average for every 10 games throughout the season and plots. """

    x_axis = list(rs_sched['Gm#'])
    acc_df = pd.DataFrame(all_acc_percentages, columns=['Acc'])
    acc_df['10game_rolling_avg'] = acc_df.Acc.rolling(10).mean()

    sns.set_palette('bright')
    plt.figure(figsize=(12,5))

    sns.lineplot(x=x_axis, y='Acc', data=acc_df, label='Accuracy of Lineup Recommendation', linestyle='dashed', alpha=.3)
    sns.lineplot(x=x_axis, y='10game_rolling_avg', data=acc_df, label='Rolling Average of Accuracies', linewidth=2)

    plt.xlabel('Game Number')
    plt.ylabel('Lineup Accuracy (%)')
    plt.title(f'Lineup Accuracy for all {team_abbrev} games: Actual vs Recommended Positional Lineups')
    plt.savefig(f'../results_visuals/{team_abbrev}_season_lineup_accuracy.png')
    plt.show()


# Comparison of all actual vs predicted positional lineups for BOS 2021 season games

# All actual lineups
all_team_acc = team_acc(rs_sched, 'BOS')

# All predicted lineups
all_team_preds = team_pred(rs_sched, 'BOS')

# Calculates all accuracy percentages for all lineup comparisons
all_acc_percentages = multi_accuracy(all_team_preds, all_team_acc)

# Outputs line graph showcasing accuracy percentages over entire season
lineup_comp_graph('BOS')



# Magnifies into single game - Shows comparison on a smaller scale

def lineup_comp_single(data, date, team):
    """ Returns lineup of 9 players who actually played in specified game. """
    batters = data[(data['Date'] == date)]
    batters = batters[(batters['Tm'] == team)]
    team_acc = list(batters['Name'])

    # Removed subs as our data does not account for them
    # List of players in actual BOS lineup for specified game
    acc_nosubs = team_acc[:9]

    return acc_nosubs

def lineup_comp_graph_single(home_abv, away_abv, home_hand, away_hand, date, actual):
    """ Outputs bar graph showing the lineup accuracy for a specified game based on teams, pitcher arms, and game date. """

    # Call genMatchup for this game
    home_weighted, away_weighted, home_name, away_name, home_p_hand, away_p_hand, home, away = genMatchup(home_abv, away_abv, home_hand, away_hand, date,)

    # Run teams through positional lineup generator
    pos_home, pos_away = make_pos_lineup(home, away, home_weighted, away_weighted, home_name, away_name)

    # Create lineup dataframe for BOS
    team_poslineup_df, team_weight_num = lineup_df(pos_home)

    # List of players in predicted BOS lineup for specified game
    pred = list(team_poslineup_df['Name'])
    score = single_accuracy(pred, actual)
    perfect = 100

    # Example output of individual game accuracy as a bar chart
    fig, ax = plt.subplots()
    xaxis = ['Real Lineup', 'Generated Lineup']
    yaxis = []
    yaxis.append(perfect)
    yaxis.append(score)
    ax.bar(xaxis, yaxis)
    plt.title('Comparison of Real vs Generated Lineup for BOS (BOS vs NYY 7/18/21)')
    plt.xlabel('Lineup Type')
    plt.ylabel('Accuracy (%)')
    fig.savefig(f'../results_visuals/BOS_single_game_accuracy.png')
    plt.show()

# Convert all batters data to pandas df and filters down to BOS vs NYY 7/18/21 game
all_batters = pd.read_csv('../data_directory/FanGraphs_total.csv')

# Example output of individual game accuracy as a bar chart
actual_lineup = lineup_comp_single(all_batters, "2021-07-18", "BOS")
lineup_comp_graph_single('BOS', 'NYY', 'Left', 'Right', '2021-07-18', actual_lineup)
