# To read listOfPeople.json and create a file excatly like listOfCountries.json
import json

f=open("/Users/richa/Desktop/python/Question_on_json/listOfPeople.json","r")
file_string = f.read()
people_list_json=json.loads(file_string)
people_list = people_list_json["address_book"]
list_of_country={}
for person in people_list:
    if person['country'] in list_of_country:
        list_of_country[person["country"]].append(person)
    else:
        list_of_country[person["country"]]=[person]
list_of_country_json= json.dumps(list_of_country, indent=4)
with open("/Users/richa/Desktop/python/Question_on_json/countries_list.json","w") as f:
    f.write(list_of_country_json)


