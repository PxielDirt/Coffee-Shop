#tutorial on how to make a coffee shop
import time
print("Welcome to my coffee shop")
time.sleep(2)
name = input("What is your name?\n: ")

print("Hello " +name+ ", Thank you for coming in today")
time.sleep(4)
print("Here is our menu " +name+ ", tell me when you found what you would like")
time.sleep(2)
menu = "espresso , coffee , black coffee , tea , cappucino , latte"
print(name+ " this is the list of everything that is being served today. Take your pick!\n" +menu)

order = input()

price = 8

amount = input("How many " +order+ " do you want?\n")

total = price * int(amount) 
print("Thank you for choosing " +order+ " Your total will add up to " +str(total)+ " pounds.")
time.sleep(2)
print("Now we will go and get your " +order+ " ready. Please stay here for a second while we make your " +order)
time.sleep(10)
print("Your " +order+ " is now ready. Your total is " +str(total)+ " pounds. How would you like to pay?\n Cash or card?")
payment = input()
print("Your payment via " +payment+ " has been recieved. Go and enjoy your coffee.")
