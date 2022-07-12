# PyBank Project
import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
save = os.path.join("analysis", "budget_analysis.txt")

# Open csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

# Initialize Variables
    total_months = []
    total_profit = []
    monthly_change = []

    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # total profit/months loop
    for i in range(len(total_profit) - 1):
        monthly_change.append(total_profit[i + 1] - total_profit[i])

# max & min of profits
max_profit = max(monthly_change)
min_profit = min(monthly_change)
max_month = monthly_change.index(max(monthly_change)) + 1
min_month = monthly_change.index(min(monthly_change)) + 1

# write to terminal & txt file
with open(save, "w") as txt_file:
    overall_summary = (
            f"Financial Analysis\n"
            f"-------------------------\n"
            f"Total Months: {len(total_months)}\n"
            f"Total: ${sum(total_profit)}\n"
            f"Average Change: ${round(sum(monthly_change) / len(monthly_change), 2)}\n"
            f"Greatest Increase in Profits: {total_months[max_month]} (${(str(max_profit))})\n"
            f"Greatest Decrease in Profits: {total_months[min_month]} (${(str(min_profit))})\n")
    print(overall_summary)
    txt_file.write(overall_summary)
