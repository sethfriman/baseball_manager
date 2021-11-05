#IMPORTS 
import pandas as pd 

#reading the left hand player data 
lhp = pd.read_csv('FanGraphs_lhp.csv')
#lhp

#reading right hand player data 
rhp = pd.read_csv('FanGraphs_rhp.csv')
#rhp

total = pd.read_csv('FanGraphs_total.csv')
#total

player_teams = pd.read_csv('player_teams.csv')
#player_teams

##############

#gathering all of the files 
files = ['FanGraphs_lhp.csv', 'FanGraphs_rhp.csv', 'FanGraphs_total.csv', 'player_teams.csv']

#concatinating the data 
merged_data = pd.concat([pd.read_csv(f) for f in files])

#saving/naming csv 
merged_data.to_csv('Updated_Merged_Data.csv', index=False, encoding='utf-8-sig')

new_updated_merged_data = pd.read_csv('Updated_Merged_Data.csv')
new_updated_merged_data
