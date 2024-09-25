cartcost = int(input("Enter your cart cost: "))
cash = int(input("Enter your cash: "))
if cash > cartcost:
    print("you can afford this cart")
else:
    print("you cannot afford this cart")
