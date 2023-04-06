#create a list with 5 items
fruits = ["Mangoes", "Oranges", "Apples", "Bananas", "Passion"]

#Access and print each item using for loop
for fruit in fruits:
    print(fruit)
    
#Access and print each item using for loop and list comprehension
[print(fruit) for fruit in fruits]

#Sort this list below in descending order
counties = ["Mombasa", "kirinyaga", "embu", "Nairobi", "Kisumu"]
counties.sort(key = str.lower)
counties.reverse()
print("Counties sorted: ", counties)

#Get user input for five items and add them to an empty tuple. Print output

veg_list = []

for veg in range(5):
    veg  = input("Enter vegetables: ")
    veg_list.append(veg)

veg_tuple = tuple(veg_list)
print(veg_tuple)

#Add new item to the tuple created in Question 3. Print output.
veg_list = list(veg_tuple)
veg_list.append("onions")
veg_tuple = tuple(veg_list)
print(veg_tuple)

#Delete the tuple created. Print output.
del veg_tuple
print(veg_tuple)
