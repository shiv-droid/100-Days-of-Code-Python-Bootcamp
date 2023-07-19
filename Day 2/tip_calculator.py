bill_amount = float(input("Enter the bill amount:  "))
number = int(input("How many people will split this?: "))

#tip is 12% 
to_pay = (bill_amount/number) * 1.12

print(f"The amount to pay by each person is {round(to_pay , 2)}")