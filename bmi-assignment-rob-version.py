## FOP Assignment 6.01 ##
## by Mu'aadh Muhammad
## 8/7/2025 ##

from math import *
from re import match

def calculateBMI_BMR():

    userWeight = int(input("Please enter your weight. (LBS)"))
    userAge = int(input("Please enter your age."))

    while True:
        userHeightMatches = match(r"\s*(\d+)\s*'\s*(\d+)\s*\"?", input("Please enter your height in feet. (ex: 5'7)"))

        if not userHeightMatches:
            print("Invalid input. Please enter your height in foot, inch format.")
            continue

        userHeight = (int(userHeightMatches.group(1)) * 12) + int(userHeightMatches.group(2))
        break

    kilogram = float(0.4535)
    meter = float(0.0254)
    userKG = userWeight * kilogram
    userMTR = pow((userHeight * meter), 2) 
    userCentimeter = (userHeight * meter) * 100

    userBMI = str(userKG / userMTR)

    userBMR = str((10 * userKG) + (6.25 * userCentimeter) - (5 * userAge) + 5)

    print("\\\\\\\\RESULTS////")
    print("=====================")
    print(f"Your BMI is: {userBMI[0:4]}")
    print(f"Your BMR is: {userBMR[0:4]}")
    

    
def main():
    calculateBMI_BMR()
	
main()