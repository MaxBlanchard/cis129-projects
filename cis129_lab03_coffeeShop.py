#price coffee is 5$
priceCoffee = 5
#price for muffin is 4$
priceMuffin = 4
#6% tax
tax = .06
#For formating the reciept
print('****************************')

#gets the data from the user to use in calculations
print("Max's Coffee Shop")
coffeeBought = int(input("How Many Coffees did you buy? "))
muffinBought = int(input("How Many Muffins did you buy? "))

#Gives spacing on the Reciept
print('****************************')
print(" ")
print('****************************')

#Creates totals based on the prices beofor
totalCoffee = coffeeBought * priceCoffee
totalMuffin = muffinBought * priceMuffin

#Gets the amount of tax owed from the previous totals
totalTax = float(totalMuffin * tax) + float(totalCoffee * tax)

#Returns the previous totals 
print("Max's Coffee Shop Receipt")
print('1 Coffee at 5$ each: $', totalCoffee)
print('1 Muffin at 4$ each: $', totalMuffin)
print('6% tax: ',totalTax)
print('----------')

#adds all the different costs together to give the total
taxCoffee = (totalTax + totalCoffee)
totalTota1 = totalMuffin + taxCoffee

print('Total: $', str(totalTota1))
print('****************************')
