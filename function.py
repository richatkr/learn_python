def calculate_expense(exp):
    total = 0
    for item in exp:
        total= total + item
    return total
nehas_expenses=[5000,4000,5500,5000]
richas_expenses=[15000,16000,22000,15000]

nehas_total=calculate_expense(nehas_expenses)
richs_total=calculate_expense(richas_expenses)

print("Total of Neha's Expenses till April is : ",nehas_total)
print("Total of Richa;s Expenses till April Month is : ",richs_total)

def add(a,b):
    total=a+b
    return total
n=add(5,6) 
print("Addition of 5 and 6 is : ",n)   