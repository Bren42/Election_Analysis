# Election_Analysis

## Project Overview
In this project we were given election data from a recent election in Colorado. We were asked to audit the results using the CSV data given to us and compile it into readable outcomes.

 ### 1. Produce the total number of votes cast
 ### 2. A complete list of the candidates that received votes.
 ### 3. The percentage of votes a candidate won.
 ### 4. The total number of votes each candidate won.
 ### 5. The winner of the election based on popular vote.

## Resources
-Data Source: election_results.csv
-Software: Python 3.9.12, Visual Studio Code 1.69.2, windows notepad, Git Bash.

## Summary
The analysis of the election shows:
-There were 369712 total votes cast
- There were three candidates in the election
   -Charles Casper Stockham,
   -Diana DeGette
   -Raymon Anthony Doane
-The candidates overall results are as follows:
   -Charles Casper Stockham received 23% of the vote with (85,213) votes.
   -Diana DeGette received 73.8% of the vote with (272,892) votes.
   -Raymon Anthony Doane received 3.1% of the vote with (11,606) votes.
-The winner of the Election was Diana Degette with 73.8% of the vote and a total vote count of 272,892

## Challenge overview
The election audit allowed us to create a python program that could go through each candidate to tally the number of unique votes cast, we could then use this to build a total number of votes cast and then mathematically compare that to each candidates totals, as well as each county. We could then use the total counts and based on the outcomes for each candidate we were able to show the percentage of vote totals, as well as the percentage of votes going to each candidate and county. 
## Challenge Summary
The nice part of this code is that it can be utlized in other elections by merely pointing it to another csv file with a similar data structure. As we used a lot of open lists and variables that assigned outputs based on the counts they pulled from iterating(looping) through the data we would not need to refactor the code much beyond pointing it towards an updated csv file. It should also be noted that if more variables were added to future election analsyis it would not be hard to add into this code to output, for instance we could add a percentage of vote per candidate by county if we wanted to see the data in that format. So this is a relatively versatile, simple, piece of code that can serve multiple purposes for future data analysis.
