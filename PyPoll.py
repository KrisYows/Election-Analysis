import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_data:

    # To do: perform analysis
    #print(election_data)

# Assign a variable to save the file from a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file  
with open(file_to_load) as election_data:

    # Read the file object with a reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    