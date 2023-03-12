#Importing 
import os

# Module for reading CSV files
import csv
import statistics
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first 
    csv_header = next(csvreader)
   
       # Read each row of data after the header
    
    months = []
    profits = []
    monthly_profit_change = []
 
    # Iterate through the rows 
    for row in csvreader: 

        months.append(row[0])
        profits.append(int(row[1]))
    total_profit=sum(profits)
    for i in range(len(profits)-1):
        monthly_profit_change.append(profits[i+1]-profits[i])
        
# maximum and minimum value
maximum_value_increase = max(monthly_profit_change)
minimum_value_decrease = min(monthly_profit_change)


greatest_increase_Month = monthly_profit_change.index(max(monthly_profit_change)) + 1
greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total_profit}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[greatest_increase_Month]} $({maximum_value_increase})")
print(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} $({minimum_value_decrease})")


#Exporting

output_file = open("Financial_Analysis.txt", "w")
output_file.write("Financial Analysis\n")
output_file.write("----------------------------\n")
output_file.write(f"Total Months: {len(months)}\n")
output_file.write(f"Total: ${total_profit}\n")
output_file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
output_file.write(f"Greatest Increase in Profits: {months[greatest_increase_Month]} $({maximum_value_increase})\n")
output_file.write(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} $({minimum_value_decrease})\n")