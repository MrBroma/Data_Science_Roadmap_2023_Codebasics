# 1 Write a program that can tell you your BMI Category.
print("Welcome in the BMI calculator\n")
height = float(input("Enter your height (m): "))
weight = int(input("Enter your weight (kg): "))

bmi = weight / (height ** 2)
print(round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif 29 >= bmi >= 25:
    print("Overweight")
elif 25 > bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
