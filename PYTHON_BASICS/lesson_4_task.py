#String Variable
string_one = "Today is on Tuesday in month of February"

#counting characters from position 5
print("The number of characters is", len(string_one[5:]))

#First name and birth year input
first_name = input("Enter your first name: ")
yob = input("Enter the year you were born: ")

#generating username
username = (first_name + yob)
print("Hello", username.lower(), "You are", 2023 - int(yob))




