income = float(input("Enter the annual income: "))
tax_relief = 0

# code
if income < 85528:
    tax_relief = (0.18 * income) - 556.02
else:
    tax_relief = 14829.02 + (0.32 * (income - 85528))


tax = round(tax_relief, 0)
print("The tax is:", tax, "thalers")
