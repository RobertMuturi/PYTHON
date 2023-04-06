#Date and Time Library in Python 
import time
import calendar
'''
ticks = time.time() #Number of seconds
print("Number of ticks since 12:00am, January 1, 1970: ", ticks)

#Get current time
curr_time = time.localtime(time.time())
print("Current Time: ", curr_time)
print()

#Formatted time
curr_time_formatted = time.asctime(curr_time)
print("Current Time: ", curr_time_formatted)
print()
march_2023 = calendar.month(2023,3)
print("March 2023: ", march_2023)

print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())


#using string formatted time (define your format) strftime()
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

#More calendar
print(calendar.firstweekday())

#Leap year
for i in range(10):
    check_leap_year = int(input("Enter year to check if it's leap: "))
    if calendar.isleap(check_leap_year) == True:
        print("The year {} is a leap year.".format(check_leap_year))
        print("--------------------------------")
    else:
        print("The year {} is NOT a leap year.".format(check_leap_year))
        print("--------------------------------")


print("Check leap days between 2018 and 2023: ", calendar.leapdays(2010, 2023))
print("Month calendar: ", calendar.monthcalendar(2023,3))
print("Month range: ", calendar.monthrange(2023,3))

print()
#print("2023 Calendar", calendar.prcal(2023))
print("March 2023 Calendar", calendar.prmonth(2023,3))


#Set first day of the week as Tuesday
first_day = calendar.setfirstweekday(calendar.TUESDAY)

#Return index of weekday (0-6) Monday=0, Tues=1,and so on
print(calendar.weekday(2023, 3, 5))
'''

#Application of start and end time (time taken)
#Show how long one takes to win a game
#Guessing game - Guess -- Lottery -- random 
print(" ---Welcome to a Guessing game----")
print(" #################################")
print("You are allowed enter any number")
print("The game ends when your entry matches the number in the draw")
print()
start_time = time.time() #Start counting time (in seconds)
counter = 0
while True:
    number = int(input('Enter a number: '))
    counter = counter + 1
    if number  == 5:
        break #Note the use of break
    print(number)
    print()
end_time = time.time() #Stop counting after the game ends
time_taken = end_time-start_time
print("You made {} attempts".format(counter))
print("You took {} seconds to win!".format(round(time_taken, 2)))
print("--------------------------------")
print("End of the Game!")

