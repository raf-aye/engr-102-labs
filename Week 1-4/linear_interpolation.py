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

import math
# ============================ PART 1 ============================

x1 = 10  # t = 10 min
y1 = 2028  # at t = 10 min, distance is 2,028 km

x2 = 55  # t = 55 min
y2 = 23028  # at t = 55 min, distance is 23,028 km

chosen_x = 25

interp = ((y2 - y1) / (x2 - x1)) * (chosen_x - x1) + y1

print("Part 1:")
print("For t = 25 minutes, the position p = " + str(interp) + " kilometers")

# ============================ PART 2 ============================

radius = 6745

chosen_x = 300  # Changes from 25 mins to 5 hours (300 min)
circumference = 2 * math.pi * radius

interp = ((y2 - y1) / (x2 - x1)) * (chosen_x - x1) + y1

interp = interp % circumference
print("Part 2:")
print("For t = 300 minutes, the position p = " + str(interp) + " kilometers")
