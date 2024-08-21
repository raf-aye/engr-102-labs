# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rafay Bhatti
# Allen Parrin Grabowski
# Aidan Iao
# Omar Hinojosa
# Section 505
# Assignment: 1
# Date: 08/19/2024

x1 = 10 # t = 10 min
y1 = 2028 # at t = 10 min, distance is 2,028 km

x2 = 45 # t = 45 min
y2 = 23028 # at t = 45 min, distance is 23,028 km

chosen_x = 25

interp = ((y2 - y1) / (x2 - x1)) * (chosen_x - x1) + y1

#hi

print(interp)