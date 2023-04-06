#import libraries
import time
import calendar

#program that print 1 -500 seprated by comma. Track time taken by program, round of to 1dp
start_time = time.time() #start counting
counter = 0

for i in range(500):
    print(i, end=" , ")
    
end_time = time.time() #end counting
print()
#time taken
print(f"Program to {round(end_time-start_time, 1)}")
print()

#program that prints NON_LEAP YEARS since 2000

for i in range(2000, 2023):
    if calendar.isleap(i) == True:
        print(i)