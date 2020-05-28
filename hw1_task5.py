income = int(input("Enter income:"))
cost = int(input("Enter costs:"))
if income < cost:
    print("You worked negatively, you need to work more efficiently!")
elif income == cost:
    print("You have lost nothing, but also have not earned money.")
else:
    profit = ((income - cost) / income) * 100
    print(f"You profitability was {profit: .1f} %!")
    empl = int(input("Hoy many employees do you have?"))
    print(f"You profit was {((income - cost) / empl):.1f} per employee.")
