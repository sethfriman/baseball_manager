
from game_files.gen_matchup import *
import pandas as pd


rs_sched = pd.read_csv('../data_directory/red_sox_schedul.csv')
print(rs_sched)

sox_stats = genMatchup('BOS', 'NYY', '2021-10-03')
print(sox_stats)