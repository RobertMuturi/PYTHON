###String formating###

# % operator
string_1 = "Hello everyone, we are %s programming"
print(string_1 %'learning')

# format() function
string2 = "hello  how are you"
first_name = "Robert"
second_name = "John"
age = 40
print("Hello {1}. Your first name is {0}. You are {2} years old".format(first_name, second_name, age))

number = 3.12454564667
print("Round to 4 d.p: ", round(number,4))
print('The value of pi is: {0:1.5f}'.format(3.141592))

#Change case
string_3 = "Today is on Tuesday"
print("Lower case:", string_3.lower())
print("Upper case: ", string_3.upper())
print("Title case: ", string_3.title())

#lstrip() and rstrip()
string_with_whitespace= "         Good evening. We are coding              "
print(string_with_whitespace)
left = string_with_whitespace.lstrip()
print(left)
print(left.rstrip())
'''


##COLLECTION DATA TYPES
'''
#List
robin = ["Ochola", 2023]
print(type(robin))
print(robin)
'''
#List constructor
fruits = list(("Bananas", "Berries", "Oranges", "Lemon"))
'''
print(fruits)
#Indexing - Positive and negative
print(fruits[0])
print(fruits[-1])

#Slicing
print(fruits[0:2])

#Change/replace items in a list ---- by index
fruits[1] = "Apple"
print(fruits)

fruits[0:2] = ["Lime", "Pineapple","Passion", "Mango"]
print(fruits)

fruits = list(("Bananas", "Berries", "Oranges", "Lemon"))

#Append an item to a list - to the end of the list
fruits.append("Kiwi")
#Insert to a specific position in a list
fruits.insert(2, "New fruit")
print(fruits)
vegetables = ["Spinach", "Kale"]

#Extend a list
fruits.extend(vegetables)
print(fruits)


#Remove item
fruits.remove("Kale")
print(fruits)

#Pop() removing item at a given index
fruits.pop(2)
fruits.pop() #Remove the last item by default

#Delete at a given index
del fruits[3]

#Delete entire list
del fruits

#Clear function to clear list items
fruits = list(("Bananas", "Berries", "Oranges", "Lemon"))
fruits.clear()
print(fruits)

#Application of append() in list
customers = []
for customer in range(6):
    customer = input("Customer Name: ")
    customers.append(customer)
print("Customer names: ", customers)
 
