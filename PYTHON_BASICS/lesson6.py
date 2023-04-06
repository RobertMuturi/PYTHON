#Iterate or loop through list
countries = ["Kenya", "Tanzania", "South Africa", "Uganda"]
#use for loop to print each item --
'''
for country in countries:
    print("Country Name: ", country)
    
#Also we can loop using index
for index in range(len(countries)): #count = 4
    #countries[0]
    #countries[1]
    #countries[2]
    #countries[3]
    print("Country Name: ", countries[index])
    
#Loop using while loop
i = 0
while i<len(countries):
    print(countries[i])
    i=i+1
   
#List comprehension - shorten the for loop
[print(country) for country in countries]


#List of people/contacts
phone_book = ["Robert", "eliud", "Ann", "Priscah", "Tyson", "adrian", "Elizabeth"]
person_name_a = []
for person_name in phone_book:
    if "a" in person_name:
        person_name_a.append(person_name)
        print("Names with 'a':", person_name)

#Shorten the above code
person_name_a = [person_name for person_name in phone_book if "a" in person_name]
print(person_name_a)
print()
#sort list
phone_book.sort(key = str.lower)
print("Sorted Phonebook: \n", phone_book)
print()
phone_book.reverse()
print("Reversed Sort Order of Phonebook: \n", phone_book)

#Copy a list
new_phone_book = phone_book.copy()
print("New Phone Book: ", new_phone_book)
#Or copy also using
new_phone_book = list(phone_book)

#JOIN LISTS
## Use + operator
numbers = [12, 23, 45, 56]
pbook = phone_book + numbers
print(pbook)
print()
## Also can use for loop to join list
for number in numbers:
    phone_book.append(number)
    print(phone_book)
'''

### TUPLES
tuple_1 = ("Alfred", 2023, True, "Kenya")
#Using a constructor
tuple_2 = tuple(("Alfred", 2023, True, "Kenya"))
print(type(tuple_1))

#Indexing - just as in list
tuple_1[0]
tuple_1[2:4] #0,1,2,3,4,5

#Check if items exists
if 2023 in tuple_1:
    print("Item Exists")
else:
    print("Item does not exist")

#Update tuple - first convert to list, update, convert back to tuple
list_tuple_1 = list(tuple_1)
list_tuple_1[2] = "New Item"
tuple_1 = tuple(list_tuple_1)
print(tuple_1)
