'''Idea: BMI Calculator
Project Description:
For Beginners: Create a command-line BMI calculator in Python. Prompt users for their weight (in kilograms) 
and height (in meters). Calculate the BMI and classify it into categories (e.g., underweight, normal, overweight) 
based on predefined ranges. Display the BMI result and category to the user.'''
'''FORMULA -- BMI = WEIGHT(kg)/(height*height(m))
   1. BMI < 18.5 : UNDERWEIGHT
   2. BMI 18.5 - 24.9 : NORMAL
   3. BMI 25.0 - 29.9 :OVERWEIGHT
   4. BMI >= 30.0 : OBESE'''


def bmi(BMI):
    print(f"You have BMI of {BMI}")
    if BMI <= 18.5:
        print("You are underweight!!Please gain your weight to be healthy.")
    elif BMI>18.5 and BMI<=24.9:
         print("GOOD!!You have normal BMI.")
    elif BMI>=25.0 and BMI <=29.9:
        print("OHH!! You are overweight.Please reduce it to be healthy.")
    elif BMI>=30.0:
        print("OBESE Condition!! Need to take care.")


import math
stop=False
while(stop!=True):
    print("STARTING THE BMI CALCULATOR :)")
    weight=float(input("Please enter the weight in kilograms (kg):"))
    height=float(input("Please enter the height in meters (m):"))
    BMI=weight/(height*height)
    bmi(BMI)
    again=input("Do you want to calculate again?Type 'yes' or 'no':")
    if again.lower()=='yes':
        print("OK")
    else:
        print("THANK YOU !!")
        stop=True


