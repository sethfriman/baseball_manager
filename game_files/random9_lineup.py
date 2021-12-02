def random9Lineup(home_df, away_df, home_a, away_a, home, away):

    home_random_9 = home_df.sample(9)
    away_random_9 = away_df.sample(9)

    home_9 = home_random_9[['Name', 'Position', 'weighted_runs_created_per_game']]
    away_9 = away_random_9[['Name', 'Position', 'weighted_runs_created_per_game']]

    # Print the matchup, organizing the data by weighted_runs_created_per_game
    print(home + ' random lineup based on ' + away_a + ' Handed pitcher:')
    print(home_9.head(9))
    home_er = round(home_9.weighted_runs_created_per_game.sum(), 2)
    print('Total Expected Runs: ', home_er)
    print()
    print(away + ' random lineup based on ' + home_a + ' Handed pitcher:')
    print(away_9.head(9))
    away_er = round(away_9.weighted_runs_created_per_game.sum(), 2)
    print('Total Expected Runs: ', away_er)

    return home_er, away_er





