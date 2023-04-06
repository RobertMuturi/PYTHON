#Conditional statements
#Checking weather and recommended cloth to be worn

#weather_condition = ["cold", "hot", "warm"] #Control flow of program

print("How is the weather today?")
print("------------------------")
print("1. Cold")
print("2. Hot")
print("3. Warm")
print("------------------------")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Wear heavy clothing")
elif choice == 2:
    print("Wear light clothing")
elif choice == 3:
    print("Minimal clothing")
else:
    print("Sorry you have entered a wrong choice"
    
#Nested conditionals statements = if(if-- if) else
#If a person is 18 and if they are male or female and live in a certain city
#Customers == 'Working', 'Nairobi' == Get discount
          
age = 20
gender = 'Female'
city = 'Msa'

if age > 18:
    if gender == 'Male':
        if city == 'Nairobi':
            print("This is a male adult living in Nairobi ")
        else:
            print("The male adult does not live in Nairobi")
    else:
        print("The person is above 18 but not male")
else:
    print("The person is not above 18 years")

  # --- TAKEAWAY TASK ---- #
# If a student comes from JKUAT Main --- Dept. Eng --- Learn a particular unit (Robert)
# If patient_temp > 37 --- coughing --- no_headache (cold) -- Eddy
# If safaricom_user -- mshwari_limit(0)-- does not qualify for Mshwari -- (Priscah)
# If kenyan -- has_masters_finance -- 5_years exp can apply to be CEO -- Elizabeth
# If kenyan -- above_18 -- quality for national_id -- Adrian

#Those who are absent create a case where you can use a nested loop and write the code
