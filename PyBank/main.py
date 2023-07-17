# Modules
import os
import csv

# Set path for the file
budget_csv = os.path.join("Resources","budget_data.csv")

# Declare initial values for  total months, net total, greatest increase, greatest decrease, and previous profit / loss
months_total = 0
net_total = 0
greatestincrease = 0
greatestdecrease = 0
total_change = 0
lastprofitloss = 0

# Open the CSV
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Declare the header in the csv file
    csv_header = next(csvreader)

    # Search each row in the csv file
    for row in csvreader:

        # Add one to the months total
        months_total += 1

        # Declare the profit/loss as the second column of the current row 
        profitloss = int(row[1])

        # Add the current profit / loss to the net total
        net_total += profitloss

        # Record the change from last month's profit / loss, excluding first month
        if row[0] != "Jan-10":
            change = profitloss - lastprofitloss

            # Check if the current row is the greatest month-over-month increase in profit
            if change > greatestincrease:
                greatestincrease = change
                greatestincreasemonth = row[0]
        
            # Check if the current row is the greatest month-over-month decrease in profit
            if change < greatestdecrease:
                greatestdecrease = change
                greatestdecreasemonth = row[0]
        
            # Add the current change to the total change
            total_change += change
        
        # Record current profit / loss to compare against in next iteration of the loop
        lastprofitloss = profitloss

    #Calculate average change, excluding the first month
    average_change = round(total_change/(months_total-1), 2)

    # Print results to terminal
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {months_total}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})")
    print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})")

    # Set a path for an output txt file
    output_file = os.path.join("Analysis", "output.txt")

    # Write results to txt file
    def write_to_file(output_file, lines):
        with open(output_file,"w") as text:
            for line in lines:
                text.write(f"{line}\n")

    write_to_file(output_file, ("Financial Analysis", "---------------------------",
                  f"Total Months: {months_total}", f"Net Total: ${net_total}", f"Average Change: ${average_change}",
                  f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})",
                  f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})"))