# Assign a variable for the file to load and the path


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/codyjennings/Desktop/Module3/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/codyjennings/Desktop/Module3/Resources/election_analysis.txt'

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Print the header row
    headers = next(file_reader) 
    print(headers)

#Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

# Print the candidate name from each row
        candidate_name = row[2]

#Add the cndidate name to the candidate list
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)  

# Begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0           

# Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)

# determine the percentage of votes for each candidate by looping the counts
# Iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100 
    

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning percent =
        # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
        # And, set the winning_candidate
            winning_candidate = candidate_name
        # To do: dprint out each candidate's name, vote count, and percentage of
        #votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
    # Print the candidate list. 
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage {winning_percentage:.1f}%\n"
        F"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning Candidate's results to the text file
    txt_file.write(winning_candidate_summary)
# 3. Print the total votes
#print(total_votes)
#
# The data we need to retreive 

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won


# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Close the file.

