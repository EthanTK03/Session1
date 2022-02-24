bill = int(input('What is your bill? Type here: $'))
print("Your price comes out to $" + str(bill) + ". If you would like to tip, here is a tip guide: ")


print("The 10% tip is $" + str(bill*.10) + " for a total of $" + str(bill+(bill*.10)))

print("The 15% tip is $" + str(bill*.15) + " for a total bill of $" + str(bill+(bill*.15)))

print("The 20% tip is $" + str(bill*.20) + " for a total of $" + str(bill+(bill*.20)))

print("And finally the 25% bill is $" + str(bill*.25) + " for a total bill of $" + str(bill+(bill*.25)))

tip = int(input("What tip percentage would you like to give?: "))
print("Your tip percentage is " + str(tip), "a total of $" + str(((bill)/(tip))+bill))