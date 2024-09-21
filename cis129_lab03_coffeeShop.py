#price coffee is 5$
priceCoffee = 5
#price for muffin is 4$
priceMuffin = 4
#price for a Donut is 4$
priceDonut = 4
#price for a Soda is 3$
priceSoda = 3
#6% tax
tax = .06

#For formating the reciept
print('****************************')

#gets the data from the user to use in calculations
print("Max's Coffee Shop")
coffeeBought = int(input("How Many Coffees did you buy? "))
muffinBought = int(input("How Many Muffins did you buy? "))
donutBought = int(input("How Many Donuts did you buy? "))
sodaBought = int(input("How Many Sodas did you buy? "))

#Gives spacing on the Reciept
print('****************************')
print(" ")
print('****************************')

#Creates totals based on the prices beofor
totalCoffee = coffeeBought * priceCoffee
totalMuffin = muffinBought * priceMuffin
totalDonut = donutBought * priceDonut
totalSoda = sodaBought * priceSoda

#Gets the amount of tax owed from the previous totals
totalTax = float(totalMuffin * tax) + float(totalCoffee * tax) + float(totalDonut * tax) + float(totalSoda * tax)

#Returns the previous totals 
print("Max's Coffee Shop Receipt")
print('1 Coffee at 5$ each: $', totalCoffee)
print('1 Muffin at 4$ each: $', totalMuffin)
print('1 Donut at 4$ each: $', totalDonut)
print('1 Soda at 3$ each: $', totalSoda)
print('6% tax: ',totalTax)
print('----------')

#adds all the different costs together to give the total
totalTotal = totalTax + totalCoffee + totalMuffin + totalDonut + totalSoda

#prints the total and gives and ending line
print('Total: $', str(totalTotal))
print('****************************')
