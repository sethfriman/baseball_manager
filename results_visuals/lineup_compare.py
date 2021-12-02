# LINEUPS and RESULTS

from matplotlib import pyplot as plt
import seaborn as sns


def lineup_compare(results_df, h_p_hand, a_p_hand, home_name, away_name):

    if h_p_hand == 'Left':
        home_pitcher_hand = 'lhp'
    else:
        home_pitcher_hand = 'rhp'

    if a_p_hand == 'Left':
        away_pitcher_hand = 'lhp'
    else:
        away_pitcher_hand = 'rhp'

    fig, ax = plt.subplots()
    sns.barplot(x='Lineup Type', y='Expected Runs', data=results_df, hue='Location', ax=ax)
    ax.set_title('Expected Runs Lineup Comparison Chart')
    plt.show()
    fig.savefig('../results_visuals/' + away_name + '_' + away_pitcher_hand + '_at_' +
                home_name + '_' + home_pitcher_hand + '.png')
