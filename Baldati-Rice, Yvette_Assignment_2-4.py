salary = float(input("Enter salary: "))
numDependents = int(input("Enter number of dependents: "))
stateTax = (6.5/100) * salary
federalTax = (28/100) * salary
dependentDeduction = ((salary * (2.5/100)) * (numDependents))
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
print("stateTax: $" + str(stateTax))
print("federalTax: $" + str(federalTax))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))