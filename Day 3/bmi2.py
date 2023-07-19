weight = int(input("Enter your weight here: "))
height = float(input("Enter your height here:  "))

bmi = weight / (height * height)

if (bmi < 18.5):
    print("Underweight")
elif (bmi > 18.5 and bmi < 25):
    print("Normal Weight")
elif (bmi > 25 and bmi < 30):
    print("Overweight")
elif (bmi > 30 and bmi < 35):
    print("Obese")
else:
    print("Clinically Obese")
    