x1 = 10 # t = 10 min
y1 = 2028 # at t = 10 min, distance is 2,028 km

x2 = 45 # t = 45 min
y2 = 23028 # at t = 45 min, distance is 23,028 km

chosen_x = 25

interp = ((y2 - y1) / (x2 - x1)) * (chosen_x - x1) + y1

print(interp)