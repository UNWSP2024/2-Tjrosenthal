def calculate_total_purchase():
 #Tanner Rosenthal
#1/24/2025

#A customer purchases 5 items and the program asks for the prices
item1 = float(input("What is the price of the first item?"))
item2 = float(input("What is the price of the second item?"))
item3 = float(input("What is the price of the third item?"))
item4 = float(input("What is the price of the fourth item?"))
item5 = float(input("What is the price of the fith item?"))

#Calulates the combines cost
totalCost = item1 + item2 + item3 + item4 + item5

#Calculates the tax amount
taxAmount = totalCost * 0.07

#Rounds both the combines amount and the tax amount
roundedTotal = round(totalCost, 2)
roundedTax = round(taxAmount, 2)

#Calculates total cost
finalCost = roundedTotal + roundedTax

#Prints the cost, the tax, and the final total
print("Cost:", roundedTotal)
print("Tax:", roundedTax)
print("Final Cost:", finalCost)

calculate_total_purchase()
