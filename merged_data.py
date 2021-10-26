#imports 
import pandas as pd 
-------
#reading savant left data into a dataframe 
left_data = pd.read_csv('savant_data_left.csv')
left_data

#reading savant right data into a dataframe 
right_data = pd.read_csv('savant_data_right.csv')
right_data 

#reading player teams into a dataframe 
player_teams = pd.read_csv('player_teams.csv')
player_teams 
-------
#gathering all of the files 
files = ['savant_data_right.csv', 'savant_data_left.csv', 'player_teams.csv']

#concating the data 
merged_data = pd.concat([pd.read_csv(f) for f in files])

#naming the new data 
merged_data.to_csv('Merged.csv', index=False, encoding='utf-8-sig')

new_data = pd.read_csv('Merged.csv')
new_data
