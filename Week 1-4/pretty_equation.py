# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rafay Bhatti
# Allen Parrin Grabowski
# Aidan Iao
# Omar Hinojosa
# Section: 505
# Assignment: 4.16 Lab
# Date: 04 09 2024
import math

# Ax^2+Bx+C = 0

#PreRec:
#       should not print the coefficient “1”
#       should not print a term with a coefficient “0”
#       should replace plus signs (+) with minus signs (-) for negative coefficients.
#       include one space around the sign and the term.


A = input('Please enter the coefficient A: ')
B = input('Please enter the coefficient B: ')
C = input('Please enter the coefficient C: ')

if A == "1":
    A = ""

if B == "1":
    B = ""


    
equation = ""

if A != "0":
    if A.startswith("-"):
        if A == "-1":
            equation += "- x^2 "
        else:
            equation += f"- {int(math.fabs(int(A)))}x^2 "
    else:
        equation += f"{A}x^2 "    
if B != "0":
    if B.startswith("-"):
        if B == "-1":
            equation += "- x "
        else:
            equation += f"- {int(math.fabs(int(B)))}x "
    else:
        if equation == "":
            equation += f"{B}x "
        else:
            equation += f"+ {B}x "    
        
if C != "0":
    if C.startswith("-"):
        if C == "-1":
            equation += "- 1 "
        else:
            equation += f"- {int(math.fabs(int(C)))} "
    else:
        if equation == "":
            equation += f"{C} "
        else:
            equation += f"+ {C} "       

equation += "= 0"


print("The quadratic equation is " + equation)
