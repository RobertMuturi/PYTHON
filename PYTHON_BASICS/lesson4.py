##########  STRING OPERATIONS   ###########

#Indexing
#variable_name[position]
#Positive Indexing - Index from the start to end
char_at_pos_0 = string_one[0]
char_at_pos_1 = string_one[1]
char_at_pos_2 = string_one[2]

print("First character: ", char_at_pos_0)
print("Second character: ", char_at_pos_1)
print("Third character: ", char_at_pos_2)
print()
#Positive indexing to slice a String (extract part of string)
#variable_name[start:end] #NB- end is the character just before the value 
read_first_word = string_one[0:3]
print("First word in string_one: ", read_first_word)
read_second_word =string_one[5:9]
print("Second word in string_one: ",read_second_word)

#from a specific position to the end
string_one = "Some text is called a string"
pos_2_to_end = string_one[2:]

##################################################################

#Negative Indexing - Index from end to start -- Reverse a word(hide a meaning)
last_character = string_one[-1]
second_last_character = string_one[-2]
print("Last Character: ", last_character)

#Negative indexing to slice a String (extract part of string) - end to the beginning
#variable_name[start:end] #NB- end is the character just before the value 
last_word = string_one[-6:-1]
print("Last word using negative index: ", last_word)

string_one = "Some text is called a string"
#Index out of range error
#print(string_one[100])

string_one = 'This is the new version of string one'
print("Replaced string one: ", string_one)

#Multiple line string
string_with_multiple_lines = """
Line one of string
Line two of string
line three of string
"""
print(string_with_multiple_lines)

#Compare strings
string_two = "We are writing strings"
string_three = "We are coding"
string_four = "We are writing strings"

print(string_two == string_three) #False
print(string_two == string_four) #True

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
print("Hello", first_name +" "+ last_name )
print("Your username is:  ", first_name+last_name +"2023")


string_five = "CODING"
#Iterate (loop through a string) - Extra characters and print each line by line   -- user for loop
for character in string_five:
    print(character)

#Length of string
print("Length of String Five: ", len(string_five))


#Example Post character count: 10
post = input("Write something: ")
if len(post)> 10:
    print("Exceeded max character limit")
else:
    print("Post character is on the correct limit")

        
        


