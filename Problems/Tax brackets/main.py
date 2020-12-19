def tax_calculation():
    income = int(input())
    tax = 0
    if 15527 < income < 42708:
        tax = 15
    elif 42707 < income < 132407:
        tax = 25
    elif income >= 132407:
        tax = 28
    calculated_tax = int(round(income * (tax / 100)))
    print(f"The tax for {income} is {tax}%. That is {calculated_tax} dollars!")


tax_calculation()
