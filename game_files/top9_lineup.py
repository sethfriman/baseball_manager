
def top9Lineup(home_df, away_df, home_a, away_a, home, away):
    """Creates a Lineup from the top 9 batters overall on a team based on Weighted Runs Created"""

    home_best_9 = home_df.sort_values('weighted_runs_created_per_game', ascending=False)[:9].reset_index(
        drop=True)
    away_best_9 = away_df.sort_values('weighted_runs_created_per_game', ascending=False)[:9].reset_index(
        drop=True)
    home_best_9 = home_best_9[['Name', 'Position', 'weighted_runs_created_per_game']]
    away_best_9 = away_best_9[['Name', 'Position', 'weighted_runs_created_per_game']]

    # Print the matchup, organizing the data by weighted_runs_created_per_game
    print(home + ' top 9 lineup based on ' + away_a + ' Handed pitcher:')
    print(home_best_9)
    home_er = round(home_best_9.weighted_runs_created_per_game.sum(), 2)
    print('Total Expected Runs: ', home_er)
    print()
    print(away + ' top 9 lineup based on ' + home_a + ' Handed pitcher:')
    print(away_best_9)
    away_er = round(away_best_9.weighted_runs_created_per_game.sum(), 2)
    print('Total Expected Runs: ', away_er)
    return home_er, away_er
