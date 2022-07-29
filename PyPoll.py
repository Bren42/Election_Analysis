#add the needed dependencies
import csv

import os

#assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")

#assign a variable to write results to
file_to_write=os.path.join("resources", "Election_outcomes.txt")

#Initialize a total vote counter
total_votes=0

#Candidate options list.
candidate_options=[]

#Declare and empty dictionary
candidate_votes={}

#declaring a variable with an empty string value
winning_candidate=('')
winning_count=0
winning_percent=0


#open the election results and read the file. with the reader function
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #read and move past the headers row
    headers=next(file_reader)

    #Print each row in the csv file(use a for loop)
    for row in file_reader:
        #Add the total votes
        total_votes+=1

        #print the candidates name from each row.
        candidate_name=row[2]
        

        #If statement to check for names and write only unique
        if candidate_name not in candidate_options:
            
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            
            #begin tracking the candidates vote count.
            candidate_votes[candidate_name]=0

        #run through the for loop to add a vote to the candidates name
        candidate_votes[candidate_name]+=1 
    
#write results into a text file
with open(file_to_write,'w') as txt_file:

    #Write the election results using an F string literal
    election_results=(f'\nElection Results\n'
    f'-------------------------\n'
    f'Total Votes:{total_votes:,}\n'
    f'-------------------------\n')

    print(election_results,end="")

    #save election results to a txt file.
    txt_file.write(election_results)

    #determine the percentage of votes by candidate
    #1.iterate through the candidate list.

    for candidate_name in candidate_votes:
        
        #retrieve vote count of candidate
        votes=candidate_votes[candidate_name]
        
        #calculate the percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100

    #print candidate information, vote count and percentage
        candidate_results=(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

    #print candidate results to the terminal
        print(candidate_results)

    #write candidate results to a text file
        txt_file.write(candidate_results)
    

        
    #determine if the candidate votes are greater than the winning count
        if (votes>winning_count) and (vote_percentage>winning_percent):
            
            #if true set winning_count and winning percentage
            winning_count=votes

            winning_percent=vote_percentage

            winning_candidate=candidate_name

    winning_candidate_summary=(
    f"--------------------\n"
    f'Winner:{winning_candidate}\n'
    f"Winning Vote Count:{winning_count}\n"
    f"Winning Percentage:{winning_percent:.1f}%\n"
    f"--------------------")
    
    txt_file.write(winning_candidate_summary)
    #print(winning_candidate_summary) commented out as this is no longer needed at this time. remove comment hash to use this code line.


  