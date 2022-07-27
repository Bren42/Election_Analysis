# The data we need to retrieve
# 1.the total number of votes cast
# 2. A complete list of the candidates that received votes.
# 3. The percentage of votes a candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#Import the datetime class from the datetime module.
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now=dt.datetime.now() 

# Print the present time
print("the time right now is",now)


import csv

import os

#assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")

#open the election results and read the file.
with open(file_to_load) as election_data:

#todo read and analyze the data here.

    #read the file object with the reader function
    file_reader=csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)

    print(headers)
     

#using the with statement open the file as a text file




    #to do: Perform analysis



#create a file name variable to a direct or indirect path to the file


#using the with statement open the file as a text file


#write some data to the file
    
#close the file.



