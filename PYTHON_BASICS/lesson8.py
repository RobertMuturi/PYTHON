##DICTIONARY## use key-value pair - Key is a unique identifier
#dict_format = {key:value, key:value, key:value}
countries = {"Kenya":"Nairobi", "Uganda":"Kampala", "Tanzania":"Dar es salaam"}
print(countries)
print()
print("Capital city of Kenya: ", countries["Kenya"])
print("Capital city of Uganda: ", countries["Uganda"])
print("Capital city of Tanzania: ", countries["Tanzania"])
print()
#Add an item to a dictionary
countries["Ethiopia"] = "Addis Ababa"
print(countries)
print()
countries["Kenya"] = "Mombasa"

#Delete a item in dictionary --- use del dict_name[key]
del countries["Uganda"]
print(countries)

#del countries
#print(countries)

#Membership test in dictionary -- check if an entry exists

print("Kenya" in countries)
print("Kenya" not in countries)
print("Burundi" in countries)
print()

#Iterate through  dictionary -- for loop
for i in countries:
    print(countries[i])

#Number of items in a dictionary
print(len(countries))

#Empty-- clear a dictionary    empty_dictionary = {}
#countries.clear()
print(countries)

#Print keys and values
print(countries.keys())
print(countries.values())

#Sort a dictionary
print(sorted(countries.items()))


