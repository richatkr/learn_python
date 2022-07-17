num=input("Enter a Number : ")
num=int(num)
if num%2==0:
    print("Number is even")
else :
    print("Number is odd")

indian=["Somasa","Jalebi","Daal","Naan"]
chinese=["Egg role","Fried Rice","Pot Striker"]
italian=["Pasta","Pizza","Risotto"]

dish=input("Enter your dish : ");
if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chanese")
elif dish in italian:
    print("Italian")
else:
    print("Based on little Knowledge I have I donot know which cuisine is ",dish)

