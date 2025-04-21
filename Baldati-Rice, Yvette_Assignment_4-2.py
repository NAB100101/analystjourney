# This program calculates an employee’s productivity bonus and prints the employee’s name and bonus.

employee_name = input("Employee's name: ")
num_shifts = int(input("Number of shifts: "))
num_transactions = int(input("Number of transactions: "))
transaction_value = float(input("Transaction dollar value: "))

productivity_score = transaction_value / num_transactions / num_shifts

if productivity_score <= 30:
    bonus=50
elif productivity_score <= 60:
    bonus = 75
elif productivity_score <= 199:
    bonus = 100
else:
    bonus =200

print(f"Employee Name: {employee_name}")
print(f"Employee bonus: ${bonus: }")