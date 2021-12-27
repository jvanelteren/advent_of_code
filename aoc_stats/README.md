This small project is meant for when you are doing past years of Advent of Code and want to see how fast you are solving the puzzles.

'Performance' is defined as how fast you are completing the puzzles compared to the number 100 finisher on the leaderboard. It's a pretty narrow definition, in the end it's just about if you are enjoying yourself solving the puzzles. So if you decide you don't care about completion times that's 100% fine!

But if you like the competitive side of things, just do this:

1) Mark your start time when you start the puzzle, just on a piece of paper. Make sure to note the time again when you finish part 1 and part 2. Then calculate the time to star 1 and both stars in your personal file:

2) Fill your scores in scores_personal_YEAR.txt, where YEAR is the year you are competing
   The format is DAY, TIME TO STAR 1, TIME TO BOTH STARS. The times are in minutes.

3) (Only needed if the global scores text file is not in the global_scores directory). Adjust the year in populate_db_with_results.py and run it

4) Adjust the year in interpret_scores.py and run it. You do need to have numpy, pandas and altair installed (pip install ...)

5) A chart.html file will be generated plotting your scores vs the LB

6) Open the html file and see your performance

Hope you enjoy it! Jesse