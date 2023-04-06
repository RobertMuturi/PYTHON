#Definite loops - Defined set of items (items in a list, tuple, dict, set-- str characters
#for loop
'''
for number in [1,2,3,4,5]:
    print("Number: ", number)
print("End of the program")

#Iterate a list
my_contacts = ["Robin", "Robert", "Priscah", "Adrian", "Tyson"]
for every_contact in my_contacts:
    print("Hey --{}--, let's meet at 6pm.".format(every_contact))
print("Message sent!")

#Check the largest number
largest_number = -1
list_of_numbers = [12, 2, 45, 4, 9, 66, 13, 101]

for number in list_of_numbers:
    if number > largest_number:
        largest_number = number
    print("Largest number: ", largest_number)
print()
print("Largest number: ", largest_number)

#counting in a loop
#Count number of executions
coin_tosses = ["Tail", "Head", "Head", "Head", "Tail", "Tail", "Head","Tail", "Tail"]
counter_tail = 0
counter_head = 0

for toss in coin_tosses:
    if toss == "Tail":
        counter_tail = counter_tail + 1
        print("Count Tails {} : {} ".format(counter_tail, toss))
    else:
        counter_head = counter_head + 1
        print("Count Heads {} : {} ".format(counter_head, toss))
print()
print("Total Head Tosses: ", counter_head)
print("Total Tail Tosses: ", counter_tail)

#Customer sales -- amount
sales_amount = [200, 1300, 100, 450, 1200, 900]
total_sales = 0
#count = 0

for amount in sales_amount:
    total_sales = total_sales + amount
    print("Total: ", total_sales)
    #count  = count + 1
    
print()
print("Total sales: ", total_sales)
print("Average sales: ", total_sales/len(sales_amount

#Search an item
names = ["Adrian", "Robin", "Tyson", "Priscah", "Robert"]
found = False
                                         
for name in names:
    if name == "Tyson":
        found = True
        print("Name found!")
        break #If searching only one entry
    print(found, name)
print("Search status: ", found)
'''
#Check the Smallest number
smallest_number = None
list_of_numbers = [12, 2, 45, 4, 9, 66, 13, 101]

for number in list_of_numbers:
    if smallest_number is None:
        smallest_number = number
    elif number < smallest_number:
        smallest_number = number
    print("Smallest number: ", smallest_number)
print()
print("Smallest number: ", smallest_number)

#Nested for loop
                                           
