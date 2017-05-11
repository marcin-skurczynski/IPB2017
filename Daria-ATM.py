balance = 542.31
pin = "1423"

inputPin = input("Please input your pin: ") 
while pin != inputPin:
  print ("Wrong password. Please try again.")
  inputPin = input("Please input your pin: ")
  
withdrawSum = float(input("How much money do you need? "))
while withdrawSum > balance:
  print ("The sum you are trying to withdraw exceeds your balance. Try again.")
  withdrawSum = float(input("How much money do you need? "))

print ("You have successfully withdrawn " + str(withdrawSum) + "PLN. Your current balance is " + str(round((balance-withdrawSum), 2)) + "PLN.")
