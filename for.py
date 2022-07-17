expense=[25000,30000,28000,35000,40000]
total = 0
for item in expense:
    total = total + item

for i in range(len(expense)):
    print("Month ",i+1," Expense ",expense[i])
    total = total + expense[i]

print("Your Expence till May Month is ",total)

for i in range(1,11):
    print(i*i)