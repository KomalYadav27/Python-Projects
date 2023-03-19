# # BMI Calculator
# Referance: https://www.calculator.net/bmi-calculator.html
weight = int((input("Enter your weight in kg:")))
height = float((input("Enter your height in meters:")))
BMI = weight/(height*height)
print(BMI)
if BMI>0:
    if BMI<16:
        print("You have severe thinness")
    elif BMI<=17:
        print("You have moderate thinness")
    elif BMI<=18.5:
        print("You have mild thinness")
    elif BMI<=25:
        print("You have normal weight")
    elif BMI<=30:
        print("You are overweight")
    elif BMI<=35:
        print("You are obese class 1")
    elif BMI<=40:
        print("You are obese class 2")
    elif BMI>40:
        print("You are obese class 3")
    else:
        print("Enter correct values of weight and height")




