# Input: Employee's name, number of shifts, number of transactions, and transaction dollar value

# Employee's name
employee_name = input("Enter Employee Name: ")
# Number of shifts
num_shifts = int(input("Enter number of shifts: "))
# Number of transactions
num_transactions = int(input("Enter number of transactions: "))
# Dollar value of transactions
transaction_value = float(input("Enter transactions dollar value: "))


# Calculate the productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

# Determine the bonus using a nested if statement
if productivity_score <= 30:
  bonus = 50.00
elif 31 <= productivity_score <= 69:
  bonus = 75.00
elif 70 <= productivity_score <= 199:
  bonus = 100.00
else:
  bonus = 200.00

# Output: Employee's name and bonus
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:}")