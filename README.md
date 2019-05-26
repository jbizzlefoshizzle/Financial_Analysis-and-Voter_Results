# Financial Analysis and Voter Results
In this repository are two different projects.

### PyBank
I was tasked with creating a Python script for analyzing the financial records of a company.
I was given a set of financial data within budget_data.csv.
The dataset is composed of two columns: `Date` and `Profit/Losses`.

I needed to create a Python script that analyzed the data to calculate:
- the total number of months included in the dataset
- the net total amount of "Profit/Losses" over the entire period
- the average of the changes in "Profit/Losses" over the entire period
- the greatest increase in profits (date and amount) over the entire period
- the greatest decrease in losses (date and amount) over the entire period

Not only does the script print the analysis to the terminal, but it also exports a .txt file with the necessary results.
--------------------------------------------------------------------------------------------------------------------------
### PyPoll
I was tasked with helping a small, rural town modernize its vote-counting process.
(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
I was given a set of poll data within election_data.csv.
The dataset is composed of three columns: Voter ID, County, and Candidate.

I needed to create a Python script that analyzed the votes and calculated:
- the total number of votes cast
- a complete list of candidates who received votes
- the percentage of votes each candidate won
- the total number of votes each candidate won
- the winner of the election based on popular vote.

#### Warning!
The PyPoll directory is missing election_data.csv.
Due to its massive file size, I could not upload it from my local repository to my remote one.
As a result, the script will not properly run.

Not only does the script print the analysis to the terminal, but it also exports a .txt file with the necessary results.
--------------------------------------------------------------------------------------------------------------------------
