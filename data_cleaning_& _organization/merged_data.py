#IMPORTS 
import pandas as pd 

#reading the left hand player data 
lhp = pd.read_csv('../data directory/FanGraphs_lhp.csv')
lhp
#lhp

#reading right hand player data 
#rhp = pd.read_csv('data directory/FanGraphs_rhp.csv')
#rhp

#total = pd.read_csv('data directory/FanGraphs_total.csv')
#total

#player_teams = pd.read_csv('data directory/player_teams.csv')

#pitcher_stats = pd.read_csv('data directory/pitcher_stats.csv')
#player_teams

##############

#gathering all of the files 
#files = ['data directory/FanGraphs_lhp.csv', 'data directory/FanGraphs_rhp.csv', 'data directory/FanGraphs_total.csv', 'data directory/player_teams.csv']

#concatinating the data 
#merged_data = pd.concat([pd.read_csv(f) for f in files])

#saving/naming csv 
#merged_data.to_csv('Updated_Merged_Data.csv', index=False, encoding='utf-8-sig')

#new_updated_merged_data = pd.read_csv('Updated_Merged_Data.csv')
#new_updated_merged_data
