rent= int(input("Enter your Room rate= "))
food= int(input("Enter the amount of food order= "))
electricity_spend= int(input("Enter the total of electricity spend= "))
charger_per_unit= int(input("Enter the charge per unit= "))
persons=int(input("Enter the number of persons living in room= "))

total_bill=electricity_spend * charger_per_unit

output= (food + rent + total_bill) // persons

print("Each person will pay =", output)