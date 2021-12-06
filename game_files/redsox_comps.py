
from game_files.gen_matchup import *
from game_files.pos_lineup import *
import pandas as pd

#ensure game date and retrieve data
rs_sched = pd.read_csv('../data_directory/redsox_schedule.csv')
gameday_df = rs_sched[(rs_sched['Date'] == "2021-07-18")]
print(gameday_df)

#pull all possible players for specific matchup
sox_stats = genMatchup('BOS', 'NYY', 'Left', 'Right', "2021-07-18")
sox_only = sox_stats[0]
opp_only = sox_stats[1]
#print(sox_only)
sox_list = list(sox_only['Name'])
#print(sox_list)
sox_2 = sox_list.copy()
sox_list.append('Grace')
print(sox_2)
print(sox_list)
#print(sox_2)
#print(type(sox_2))

def accuracy(lineup_pred, lineup_real):
    yes_list = []
    no_list = []
    for item in lineup_pred:
        if item in lineup_real:
            yes_list.append(item)
        else:
            no_list.append(item)
    accuracy = len(yes_list) / ((len(yes_list) + (len(no_list))))
    percent = round((accuracy * 100), 2)
    return percent

score = accuracy(sox_list, sox_2)
perfect = 100

xaxis = ['Real Lineup', 'Generated Lineup']
yaxis = []
yaxis.append(perfect)
yaxis.append(score)
plt.bar(xaxis, yaxis)
plt.title('Comparison of Real vs Generated Lineup')
plt.xlabel('Lineup Type')
plt.ylabel('Accuracy (%)')
plt.show()

'''
#game = GameManager('BOS', 'NYY')
roster_rs = GameManager.rosters('BOS', 'NYY')
print(roster_rs)

#build lineups for specific matchup
print('-------------------BEST POSITIONAL BATTERS LINEUPS (RED SOX vs YANKEES 2021-07-18) -------------------')
pos_h, pos_a = make_pos_lineup(home, away, sox_only, opp_only, 'BOS', 'NYY')

'''
