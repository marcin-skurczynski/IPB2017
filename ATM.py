cardPin = 3471
balance = 143.43

pin = int(input("Enter your PIN: "))
counter = 1

while pin != cardPin:
	if (counter >= 3):
		print("Wrong PIN. You have run out of attempts. ")
		exit()

	counter += 1
	print ("Wrong PIN. Try again.")
	pin = int(input("Enter your PIN: "))

amount = float(input("How much money would you like to withdraw? "))
while amount > balance:
	print ("There is not enough money to withdraw. Try again.")
	amount = float(input("How much money would you like to withdraw? "))

balance -= amount
print ("You have successfully withdrawn %.2f zł. Your current balance is %.2f zł." % (amount, balance))
