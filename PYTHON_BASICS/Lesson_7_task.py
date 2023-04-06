
#Create a tuple called ‘customers’ with name of 5 customers
customers = ("Mary", "John", "Faith", "Mike", "Eve")

#Unpack the tuple with ids of the customers 
(A15, B20, C3, D36, E23) = customers 

#Print the values of the tuple using the customer ids
print(A15)
print(B20)
print(C3)
print(D36)
print(E23)

#Create an empty set
phones = set()

#Add 5 items in the empty set from user input
for phone in range(5):
    phone = input("Enter phone brands: ")
    phones.add(phone)
print(phones)

#Remove the 3rd item in the set
phones.discard("sony")
print(phones)

#Delete the set
del(phones)
print(phones)


#Create 2 sets:
nairobi  = {"Kenyatta avenue", "Moi avenue", "Kimathi street"}
mombasa = {"Mtwapa street", "Kenyatta avenue", "Kisaju"}

#Create and print set union, intersection, difference, and symmetric difference for the given sets.
print("Total number of streets in both Nairobi and Mombasa are: ", nairobi.union(mombasa))

#set intersection
print("Streets found in both Nairobi and Mombasa are: ", nairobi.intersection(mombasa))

#set difference
print("Streets only found in Nairobi: ", nairobi.difference(mombasa))

#symmetric difference 
print("Streets unique only to Nairobi or Mombasa: ", nairobi.symmetric_difference(mombasa))
