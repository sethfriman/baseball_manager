# Baseball Player Management System
## Motivation:
Baseball is America’s pastime. Collectively, in the MLB alone, the teams are worth around $66 billion. In our group, we have baseball fans and future baseball-professional hopefuls. We believe that the outcome of our project could theoretically be used by baseball front offices to assist in organizing rosters and setting lineups during the season. This could be a helpful project to have to show future recruiters as it shows a combination of our personal interests with our technical skills and knowledge.
## Objectives:
Our code will create a player management system to project rosters and lineups for a randomly generated baseball game. We plan to complete this project in Jupyter Notebook, due namely to the visualizations we hope to produce. Baseball produces a lot of statistics, so the system can always be fine-tuned to take more and more into account and further improve the accuracy of the developer. We hypothesize that we will be able to accurately produce a sufficient, competitive roster of baseball players for any generated matchup.
## Data Sources:
https://www.mlb.com/stats/
This will be our primary data source as it hosts all current and historic game and player stats in the MLB.

https://www.milb.com/stats/ 
This will be our secondary source of data. It shows the same information as the previous source, however, for Minor League (MiLB) teams and players.

https://baseballsavant.mlb.com/statcast_search
This is a site that accesses the previously mentioned MLB data via specific filtering measures so we can more easily and accurately check our data.
## Platform Architecture:
We currently believe that the platform architecture for this project will be a re-usable software library. Our expected deliverables include our finalized game rosters, our starting lineups, and a series of visuals to support these selections. We are also considering running a ‘baseball game’ with the rosters to see who the potential winner would be.

## Component Architecture:
As mentioned in our Status Report 1 slide deck, we plan to have 6 core sections of our component architecture: random game generator, roster createion, line-up genereator, pitcher selector, position selector, and a line-up comparison. Our random game generator will be a function that will randomly generate two unique opponenents for a matchup. From here, we move to roster creation. These will be the resulting dataframes of players and statistics that result from our data and the selected teams. A Player Class will be created in order to make player objects. The Roster class will then be built out of these player objects. Our line-up generator will return starting line-ups similar to the rosted depending on the pitcher selector and the position selector. The pitcher selector will be a function that will randomly select a player object that is an eligible starting pitcher from the roster. The postion selector will then consist of a series of methods to select the teams line-up depending on the opposing teams pitcher, as well as a ranking of the best fielding and batting stats. Finally, we will finish our analysis with a line-up comparison. This will compare our generated lineup to the most recent lineup of the most recent execution of the actual matchup. A series of visualizations will be executed here in order to show our analysis.
