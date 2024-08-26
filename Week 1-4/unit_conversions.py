# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rafay Bhatti
# Shane McCollam
# Aidan Iao
# Omar Hinojosa
# Section: 505
# Assignment: Lab 3.17
# Date: 08/26/2024

num = float(input("Please enter the quantity to be converted: "))


newtons = num * 4.44822
feet = num *3.28084
kpa = num * 101.325
btu = num * 3.41214163
gal = num * 0.264172052 * 60
far = num * (9/5) + 32 # Celcius to Farenheight

print(f'\n{num:.2f} pounds force is equivalent to {newtons:.2f} newtons')
print(f'{num:.2f} meters is equivalent to {feet:.2f} feet')
print(f'{num:.2f} atmospheres is equivalent to {kpa:.2f} kilopascals')
print(f'{num:.2f} watts is equivalent to {btu:.2f} BTU per hour')
print(f'{num:.2f} liters per second is equivalent to {gal:.2f} US gallons per minute')
print(f'{num:.2f} degrees Celsius is equivalent to {far:.2f} degrees Fahrenheit')
