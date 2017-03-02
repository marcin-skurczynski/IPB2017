cardPin = 3471
balance = 143.43

pin = int(input("Enter your PIN: "))
while pin != cardPin:
	print ("Wrong PIN. Try again.")
	pin = int(input("Enter your PIN: "))

amount = float(input("How much money would you like to withdraw? "))
while amount > balance:
	print ("There is not enough money to withdraw. Try again.")
	amount = float(input("How much money would you like to withdraw? "))

balance -= amount
print ("You have successfully withdrawn", amount, "zł. You current balance is", balance, "zł")
