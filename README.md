# Baseball Player Management System

## What is this?
This project is a warehouse for baseball player management that may be used by a manager or General Manager to inform
decisions related to creating a roster and deciding lineups for a matchup. 

It includes functionality for lineup comparison, matchup customization, dynamic lineup generation, player comparisons,
salary information, and in-depth breakdowns of individual player performance.

Each of these is intended to be used in tandem with each other so that a manager may gain more insight about their own
players and their opponent's players.

## Methodology
The largest unique factors to this project are the weighted game functionality and consequentially the newly calculated 
metrics that get generated from this type of aggregation.

This project uses an inverse distance formula to dynamically weight each player's performance based on the specified
date. This allows us to evaluate a player's current capabilities as a function of their more recent games, while still
acknowledging previous performances.

These weighted statistics are then aggregated to compute new metrics such as a weighted batting average, weighted on 
base percentage, weighted runs created, and weighted runs created per game. The calculations for these metrics can be
found in data_cleaning_and_organization/gen_stats.py.

Recommended lineups are based on the weighted runs created per game statistic because it considers all available
batting stats for each player, and puts all players on a level playing field in regard to the number of games they
played.

The remainder of this project leverages the weighted statistics and other raw data to generate insights about player and
team performance that would be of interest to team executives.

## How to Run
In a terminal, navigate to the game_files folder that houses the main.py file

Run the command 'python main.py' from this directory and the program will execute

Lineup outputs are printed and image outputs are saved to the results_visuals directory

Certain functions are run as individual scripts and are not executed each run in the main.py file. 
Independent files are:
 - player_eval_example.py
 - injury_report_example.py
 - redsox_comps.py
 - wins.py


## Outputs
Outputs include 3 lineups (positional, top9, and random9), lineup visuals, and player comparison visuals. 
The lineups are printed to the console. All generated charts are saved to results_visuals.


## Sources:
1. 2021 Boston Red Sox Schedule. Baseball Reference. (n.d.). Retrieved December 6, 2021, from https://www.baseball-reference.com/teams/BOS/2021-schedule-scores.shtml. 
2. ESPN Internet Ventures. (2021, May 30). Chicago Cubs' David Bote suffered dislocated shoulder on slide vs. Cincinnati Reds. ESPN. Retrieved December 3, 2021, from https://www.espn.com/mlb/story/_/id/31538067/chicago-cubs-david-bote-suffered-dislocated-shoulder-slide-vs-cincinnati-reds. 
3. How to zip two lists of lists in python? GeeksforGeeks. (2020, December 11). Retrieved December 6, 2021, from https://www.geeksforgeeks.org/python-zipping-two-lists-of-lists/. 
4. MLB current rosters. MLB Current Rosters - The Baseball Cube. (n.d.). Retrieved December 3, 2021, from http://www.thebaseballcube.com/mlb/rosters/. 
5. Python: Merging Two dictionaries. GeeksforGeeks. (2020, November 16). Retrieved December 3, 2021, from https://www.geeksforgeeks.org/python-merging-two-dictionaries/. 
6. Splits leaderboards as LHP. FanGraphs. (n.d.). Retrieved December 3, 2021, from https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=97&splitArrPitch=&position=P&autoPt=false&splitTeams=false&statType=player&statgroup=1&startDate=2020-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1%2C1. 
7. Splits leaderboards as RHP. FanGraphs. (n.d.). Retrieved December 3, 2021, from https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=96&splitArrPitch=&position=P&autoPt=false&splitTeams=false&statType=player&statgroup=1&startDate=2020-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1%2C1. 
8. Splits leaderboards vs LHP. FanGraphs. (n.d.). Retrieved December 3, 2021, from https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=1&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=1&startDate=2020-07-23&endDate=2021-10-03&players=&filter=&groupBy=game&sort=-1,1
9. Splits leaderboards vs LHP. FanGraphs. (n.d.). Retrieved December 3, 2021, from https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=2&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=1&startDate=2020-07-23&endDate=2021-10-03&players=&filter=&groupBy=game&sort=-1,1
10. Wikimedia Foundation. (2021, September 29). Runs created. Wikipedia. Retrieved December 3, 2021, from https://en.wikipedia.org/wiki/Runs_created.