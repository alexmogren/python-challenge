import csv
import os


#Define Variables
total_votes = 0

candidates = {
}
#Extract Files
file_to_load = os.path.join("PyPoll", "Solution2", "Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

#Calculate Total Votes & Print Results
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)


    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        name = row[2]
        if name not in candidates:
            candidates[name] = 1
        else:
            candidates[name] = candidates[name] + 1
print(total_votes)

for candidate_name, vote_count in candidates.items():
    percentage = vote_count / total_votes * 100
    print(f"{candidate_name}: {vote_count}, {percentage}")

