# Dictionary is the collection of Key and Value pair of element, key can be anything string,number
telephone_dairy={"Neha":888676765,"Aditya":9031285927,"Mamma":9931125932,"Papa":9234450262,"Richa":8789252848}
print(telephone_dairy)

# to get one element from list, acceess through the key value
print(telephone_dairy["Neha"])

# to add new element in dictionary
telephone_dairy["Sanny"]=7788556677
print(telephone_dairy)

#to delete any element from the dictionary
del(telephone_dairy["Sanny"])
print(telephone_dairy)

# to get all the elements from the dictionary one by one
#Method 1
for key in telephone_dairy:
    print("Key :",key,"   ,    Value :",telephone_dairy[key])
print("\n")

#Method 2
for k,v in telephone_dairy.items():
    print("Key : ",k,",Value : ",v)

#to search any element in dictionary
input_key=input("Enter the People you want to search in Dictionary : ")
if input_key in telephone_dairy :
    print('True')
else:
    print("False")

# to delete all the elements from the dictionary
telephone_dairy.clear()

print(telephone_dairy)
