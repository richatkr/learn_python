# JSON : JAVA SCRIPT OBJECT NOTATION
# Here we write two program
# 1)to create address book and write some record in it
# 2)Read this address book
# JSON is not any data type, it is a way of arranging data in a specific format supportted by various programmimg language C++, java Script
# Only python has Dictionary to store data
address_book={}
address_book["Tom"]={
    "name":"Tom",
    "address" : "1 red Street, Newyork",
    "phone":5454543412
}

address_book["Joe"]={
    "name":"Joe",
    "address" : "2 red Street, Newyork",
    "phone":5876453419
}

# Above we created a address_book dictionary, for converting this dictionary into JSON object

import json
s=json.dumps(address_book)
print(s);

with open("/Users/richa/Desktop/python/address_book.txt","w") as f:
    f.write(s)

f=open("/Users/richa/Desktop/python/address_book.txt","r")
s=f.read()
print(s)

book=json.loads(s)

print(type(book))

print(book['Tom'])
print(book['Tom']['phone'])

for person in book:
    print(book[person]['name']," lives at ",book[person]['address'])






