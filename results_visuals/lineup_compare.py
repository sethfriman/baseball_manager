# LINEUPS and RESULTS
results_df = pd.DataFrame(columns=['Lineup Type', 'Expected Runs', 'Location'])

top9_h, top9_a = top9Lineup(home_weighted, away_weighted,
                            h_p_hand, a_p_hand,
                            home_name, away_name)
if h_p_hand == 'Left':
    home_pitcher_hand = 'lhp'
else:
    home_pitcher_hand = 'rhp'

if a_p_hand == 'Left':
    away_pitcher_hand = 'lhp'
else:
    away_pitcher_hand = 'rhp'

results_df = results_df.append({'Lineup Type': 'Top9', 'Expected Runs': top9_h, 'Location': 'Home'}, ignore_index=True)
results_df = results_df.append({'Lineup Type': 'Top9', 'Expected Runs': top9_a, 'Location': 'Away'}, ignore_index=True)

fig, ax = plt.subplots()
sns.barplot(x='Lineup Type', y='Expected Runs', data=results_df, hue='Location', ax=ax)
ax.set_title('Expected Runs Lineup Comparison Chart')
fig.savefig('../results_visuals/' + away_name + '_' + away_pitcher_hand + '_at_' +
            home_name + '_' + away_pitcher_hand + '.png')
