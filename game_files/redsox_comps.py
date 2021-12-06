
from game_files.gen_matchup import *
from game_files.pos_lineup import *
import pandas as pd
import itertools
from collections import Counter
import matplotlib.pyplot as plt

#ensure game date and retrieve data
rs_sched = pd.read_csv('../data_directory/redsox_schedule.csv')
#print(rs_sched)
gameday_df = rs_sched[(rs_sched['Date'] == "2021-07-18")]
all_batters = pd.read_csv('../data_directory/FanGraphs_total.csv')
batters = all_batters[(all_batters['Date'] == "2021-07-18")]
batters = batters[(batters['Tm'] == "BOS")]
sox_acc = list(batters['Name'])
sox_acc_nosubs = sox_acc[:9]
#print(sox_acc_nosubs)
#print(gameday_df)

game_nums = list(rs_sched['Gm#'])
#print(type(x_axis))

#pull all possible players for specific matchup
#run redsox and nyy through genmatchup
sox_weighted, nyy_weighted, sox_name, nyy_name, sox_p_hand, nyy_p_hand, sox, nyy = genMatchup('BOS', 'NYY', 'Left', 'Right', "2021-07-18")
#print(sox)

#run redsox and nyy through positional lineup generator
pos_sox, pos_nyy = make_pos_lineup(sox, nyy, sox_weighted, nyy_weighted, sox_name, nyy_name)
# print(pos_sox)
# print(pos_nyy)

#create lineup dfs for each team
sox_poslineup_df, sox_weight_num = lineup_df(pos_sox)
nyy_poslineup_df, nyy_weight_num = lineup_df(pos_nyy)
#print(sox_poslineup_df)
#print(nyy_poslineup_df)

#list of players in predicted redsox lineup
sox_pred = list(sox_poslineup_df['Name'])
#print(sox_pred)

#list of player in actual redsox lineup
#sox_acc =

fake_pred_list = [['Marwin Gonzalez', 'J.D. Marnez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Refroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Berts', 'Kevin Plawecki', 'Fanchy Cordero', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cero', 'Hunter Refroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian azquez', 'Enrie Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Huer Renfroe', 'Christian Arroyo', 'Alex Verdugo'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Christian Arroyo', 'Alex Vdugo', 'Michael Chavis'], ['Marwin Gonzalez', 'J.D. Mainez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Garrett Richards', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Nick Pivetta', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Christian Arroyo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis'], ['Marwin Gonzalez', 'J.D. Martinez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec', 'Jonathan Arauz'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Martin Perez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Nathan Eovaldi', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Rafael Devers'], ['Marwin Gonzalez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Eduardo Rodriguez', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Danny Santana', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Eduardo Rodriguez', 'Hunter Renfroe', 'Alex Verdugo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Garrett Richards', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Connor Wong'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Connor Wong', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Rafael Devers'], ['J.D. Martinez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Connor Wong'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Michael Chavis'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Alex Verdugo', 'Michael Chavis'], ['J.D. Martinez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Michael Chavis'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Bobby Dalbec', 'Jonathan Arauz', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jonathan Arauz'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['Marwin Gonzalez', 'J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers'], ['Marwin Gonzalez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Jonathan Arauz'], ['Marwin Gonzalez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Jonathan Arauz'], ['Marwin Gonzalez', 'J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Rafael Devers', 'Jarren Duran'], ['Marwin Gonzalez', 'J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Rafael Devers', 'Connor Wong'], ['Marwin Gonzalez', 'J.D. Martinez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Franchy Cordero', 'Hunter Renfroe', 'Rafael Devers', 'Jarren Duran'], ['Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jonathan Arauz'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Franchy Cordero', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Christian Arroyo', 'Kyle Schwarber'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Christian Arroyo', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jarren Duran'], ['Christian Vazquez', 'Xander Bogaerts', 'Yairo Munoz', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jonathan Arauz', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Travis Shaw', 'Xander Bogaerts', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Jonathan Arauz', 'Jarren Duran'], ['J.D. Martinez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Yairo Munoz', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Xander Bogaerts', 'Yairo Munoz', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Yairo Munoz', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Jack Lopez', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Jonathan Arauz', 'Jarren Duran'], ['J.D. Martinez', 'Christian Vazquez', 'Danny Santana', 'Jack Lopez', 'Hunter Renfroe', 'Kyle Schwarber', 'Rafael Devers', 'Bobby Dalbec', 'Jonathan Arauz'], ['J.D. Martinez', 'Danny Santana', 'Travis Shaw', 'Jack Lopez', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Travis Shaw', 'Taylor Motter', 'Jack Lopez', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Travis Shaw', 'Taylor Motter', 'Jack Lopez', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Travis Shaw', 'Taylor Motter', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Danny Santana', 'Enrique Hernandez', 'Travis Shaw', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Jose Iglesias', 'Danny Santana', 'Enrique Hernandez', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['Christian Vazquez', 'Jose Iglesias', 'Danny Santana', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Jack Lopez', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Jack Lopez', 'Kevin Plawecki', 'Hunter Renfroe'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Kyle Schwarber'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Rafael Devers', 'Bobby Dalbec'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Xander Bogaerts', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo', 'Rafael Devers'], ['J.D. Martinez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Kevin Plawecki', 'Hunter Renfroe', 'Kyle Schwarber', 'Alex Verdugo'], ['J.D. Martinez', 'Christian Vazquez', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Eduardo Rodriguez', 'Hunter Renfroe', 'Kyle Schwarber', 'Rafael Devers'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo', 'Kyle Schwarber'], ['J.D. Martinez', 'Christian Vazquez', 'Jose Iglesias', 'Enrique Hernandez', 'Chris Sale', 'Travis Shaw', 'Xander Bogaerts', 'Hunter Renfroe', 'Christian Arroyo']]



def sox_pred():
    """ Runs each game from Red Sox schedule through genMatchup and
    make_pos_lineup to gather the predicted Red Sox lineups for each game in the 2021 season """

    all_sox_preds = []

    for index, row in rs_sched.iterrows():
        date = row['Date']
        opp_abbrev = row['Opp']
        sox_weighted, opp_weighted, sox_name, opp_name, sox_p_hand, opp_p_hand, sox, opp = genMatchup(home='BOS', away=opp_abbrev, h_p_hand=None, a_p_hand=None, before_date=date)
        pos_sox, pos_opp = make_pos_lineup(sox, opp, sox_weighted, opp_weighted, sox_name, opp_name)
        sox_poslineup_df, sox_weight_num = lineup_df(pos_sox)
        #opp_poslineup_df, opp_weight_num = lineup_df(pos_opp)
        sox_pred = list(sox_poslineup_df['Name'])
        all_sox_preds.append(sox_pred)

    return all_sox_preds

def sox_acc():

    all_sox_acc = []
    all_batters = pd.read_csv('../data_directory/FanGraphs_total.csv')

    for index, row in rs_sched.iterrows():
        date = row['Date']
        batters = all_batters[(all_batters['Date'] == date)]
        batters = batters[(batters['Tm'] == "BOS")]
        sox_acc = list(batters['Name'])
        sox_acc_nosubs = sox_acc[:9]
        all_sox_acc.append(sox_acc_nosubs)

    return all_sox_acc

all_sox_acc = sox_acc()
    #what do you want to have outputted? to get each lineup to go through the accuracy function I think a list
    #of lists might make the most sense? that way you only call the accuracy function once (change the accuracy
    #function so it supports this)

    #for each team in the csv do genmatchup against sox
    #then run make_pos_lineup
    #output either the list of predicted player or the df lineups


#sox_games_comp()

def multi_accuracy(lineup_pred, lineup_real):
    """ Compares BOS entire season of games to determine lineup accuracy of predicted lineups """

    #https://www.geeksforgeeks.org/python-zipping-two-lists-of-lists/
    zipped = [list(itertools.chain(*i))
           for i in zip(lineup_pred, lineup_real)]
    all_acc_percentages = []

    for lst in zipped:
        yes_list = []
        no_list = []
        #print(lst)
        counter = Counter(lst)
        #print(counter)
        for k, v in counter.items():
            #print(k, v)
            if v == 2:
                yes_list.append(k)
            else:
                no_list.append(k)
        accuracy = len(yes_list) / ((len(yes_list) + (len(no_list))))
        percent = round((accuracy * 100), 2)
        all_acc_percentages.append(percent)

    return all_acc_percentages

all_acc_percentages = multi_accuracy(fake_pred_list, all_sox_acc)

def single_accuracy(lineup_pred, lineup_real):
    """ Compares predicted and actual lineups for a single game """
    yes_list = []
    no_list = []
    for item in lineup_pred:
        if item in lineup_real:
            yes_list.append(item)
        else:
            no_list.append(item)
    for item in lineup_real:
        if item not in lineup_pred:
            no_list.append(item)
    print('yes', yes_list)
    print('no', no_list)
    accuracy = len(yes_list) / ((len(yes_list) + (len(no_list))))
    percent = round((accuracy * 100), 2)
    return percent

#score = single_accuracy(sox_pred, sox_acc_nosubs)
#perfect = 100

def BOS_lineup_comp_graph():
    #xaxis is game num
    #yaxis is accuracy percentage
    # sns.lineplot(x=range(len(before_injury)),
    #              y='H',
    #              data=before_injury,
    #              label='Hits per Game (Before Injury: 2020 Season)',
    #              linestyle='dashed',
    #              alpha=0.3)
    x_axis = game_nums
    y_axis = all_acc_percentages
    plt.plot(x_axis, y_axis)
    plt.xlabel('Game Number')
    plt.ylabel('Lineup Accuracy (%)')
    plt.title('Lineup Accuracy for all BOS games (2021): Actual vs Predicted Positional Lineups')
    plt.show()

BOS_lineup_comp_graph()
# xaxis = ['Real Lineup', 'Generated Lineup']
# yaxis = []
# yaxis.append(perfect)
# yaxis.append(score)
# plt.bar(xaxis, yaxis)
# plt.title('Comparison of Real vs Generated Lineup for BOS (BOS vs NYY 7/18/21)')
# plt.xlabel('Lineup Type')
# plt.ylabel('Accuracy (%)')
# plt.show()

'''
#game = GameManager('BOS', 'NYY')
roster_rs = GameManager.rosters('BOS', 'NYY')
print(roster_rs)

#build lineups for specific matchup
print('-------------------BEST POSITIONAL BATTERS LINEUPS (RED SOX vs YANKEES 2021-07-18) -------------------')
pos_h, pos_a = make_pos_lineup(home, away, sox_only, opp_only, 'BOS', 'NYY')

'''
