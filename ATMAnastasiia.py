# try and write a python program that will:
# 1. DONE! Work in loop
# 2. DONE! Will ask for your pin 
# 3. DONE! Will check the pin vs. provided "hard-coded" value
# 4. DONE! Will ask for amount of money to withdraw and check if it is available (again - hard-coded value)




pin=4444
balance=11049.62
access=False

print("Insert your card")
for i in range (1,4):
  pinInserted=int(input("Input your PIN-code "))
  if pinInserted==pin:
    print("Welcome, Anastasia!")
    access=True
    break
  else:
    if i==3:
      print("The number of attempts has expired.")
    else:
      print("Your PIN-code is incorrect. Try again.")

if access==True:
  moneyNeeded=float(input("What amount of money would you like to withdraw? "))
  while moneyNeeded>balance:
    print("Sorry, you have not enough money on your account. Try to withdraw another sum.")
    moneyNeeded=float(input("What amount of money would you like to withdraw? "))
  print("Here is your money. You have withdrawn %.2f RUB. Your balance now is %.2f RUB. Thank you." % (moneyNeeded, balance-moneyNeeded))
    
print("Take your card back. Thank you for choosing Sberbank.")
  
  
