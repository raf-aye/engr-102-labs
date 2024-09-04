# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rafay Bhatti
# Allen Parrin Grabowski
# Aidan Iao
# Omar Hinojosa
# Section: 505
# Assignment: 1
# Date: 09/04/2024

pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

change = (pay - cost) 


print(f"You received ${change:.2f} in change. That is...")

change = round(change * 100,2) # Make it a much easier number to work with, dont deal with floating point error!! yay!!!

quarters = change // 25

if quarters > 0:
    if quarters == 1:
        print(f"{int(quarters)} quarter")
    else:
        print(f"{int(quarters)} quarters")
    change = change % 25
    
dimes = change // 10

if dimes > 0:
    if dimes == 1:
        print(f"{int(dimes)} dime")
    else:
        print(f"{int(dimes)} dimes")
    change = change % 10
    
    
nickels = change // 5

if nickels > 0:
    if nickels == 1:
        print(f"{int(nickels)} nickel")
    else:
        print(f"{int(nickels)} nickels")
    change = change % 5


pennies = change // 1
if pennies > 0:
    if pennies == 1:
        print(f"{int(pennies)} penny")
    else:
        print(f"{int(pennies)} pennies")
    change = change % 1