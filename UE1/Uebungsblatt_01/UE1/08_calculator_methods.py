#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
from calc_functions import add, subtract, divide, multiply

def calculate():
    while True:   
        try:
            print("""
                  ====================================================
                  ==                 CALCULES 2000                  ==
                  ====================================================
                  """)

            num1 = float(input("Enter a number: "))
            oper = input("Choose the operator:")
            num2 = float(input("Enter a second number: "))

            #num1 = float(num1)
            #num2 = float(num2)


            if (oper == "+"):
                print("Your calculation: ",

                      num1, " + ", num2)
                print("Result: ", add(num1, num2))

            elif (oper == "-"):
                print("Your calculation: ",
                      num1, " - ", num2)
                print("Result: ", subtract(num1, num2))

            elif (oper == "/"):
                print("Your calculation: ",
                      num1, " / ", num2)
                print("Result: ",divide(num1, num2))

            elif (oper == "*"):
                print("Your calculation: ",
                      num1, " * ", num2)
                print("Result: ",
                      multiply(num1, num2))

            else:
                print("Please choose a valid operator!")
                calculate()

            calculate()

        except ValueError as err:
            print("Please only put in numbers!")
            calculate()
        except KeyboardInterrupt:
            print('Program interrupted!')
            input('Press ENTER to exit')
            sys.exit()

calculate()
            
