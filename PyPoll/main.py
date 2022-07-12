# PyPoll Project
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
save = os.path.join("analysis", "election_analysis.txt")

# Open/read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Initialize Variables
    total_votes = 0
    list_candidate = []
    votes_for_candidate = {}
    candidate_winner = ""
    winning_count = 0
    winning_perc = 0
    winning_candidate_perc = 0

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate = row[2]

        # Unique candidate list & votes per candidate
        if candidate not in list_candidate:
            list_candidate.append(candidate)
            votes_for_candidate[candidate] = 0
        votes_for_candidate[candidate] += 1

    # Print to terminal & text file
    with open(save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n")
        print(election_results, end="")
        txt_file.write(election_results)

        for candidate in votes_for_candidate:
            # votes & percent of overall votes
            votes = votes_for_candidate.get(candidate)
            perc_votes = float(votes) / float(total_votes) * 100
            candidate_results= (f"{candidate}: {perc_votes:.3f}% ({votes:})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            # Winner
            if (votes > winning_count) and (perc_votes > winning_perc):
                winning_count = votes
                candidate_winner = candidate
                winning_perc = perc_votes

        winner_summary = (
            f"-------------------------\n"
            f"Winner: {candidate_winner}\n"
            f"-------------------------\n")
        print(winner_summary)
        txt_file.write(winner_summary)