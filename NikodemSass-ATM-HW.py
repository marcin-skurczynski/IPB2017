balance=2525.25
print("*********EUROCASH*********")
for i in range (1,4):
 PIN=int(input('Please enter your 4 Digit pin '))
 if PIN == (2525):
   print('You entered you pin correctly\n')
   print("""
   1)        Balance
   2)        Withdraw
   3)        Deposit
   4)        Finish operation
   """)
   Option=int(input("Enter Option: "))
   if Option==1:
     print("Balance  PLN ",balance)
     print('Thank You for using EUROCASH')
     exit()
  
   if Option==2:
     print("Balance  PLN  ",balance)
     Withdraw=float(input("Enter Withdraw amount  PLN "))
     if Withdraw>0:
       if Withdraw<balance:
         forewardbalance=(balance-Withdraw)
         print('You have withdrawn ',Withdraw)
         print("Foreward Balance  PLN " ,forewardbalance)
         receipt=input('Would you like to print a receipt?\n Please choose:\n y for Yes\n n for No\n')
        
         if receipt == 'y':
           print('Printing Your receipt...\n')
           print('PLEASE TAKE OUT YOUR CARD')
           exit()
           
         elif receipt == 'n':
           print('PLEASE TAKE OUT YOUR CARD')
           print('Thank You for using EUROCASH')
           exit()
          
       elif Withdraw>balance:
         print("No funds in account")
         exit()
       else:
         print("None withdraw made")
         exit()
     else: print('You cannot withdraw negative  values')
     exit()
  
   if Option==3:
     print("Balance  PLN ",balance)
     Deposit=float(input("Enter deposit amount  PLN "))
     if Deposit>0:
         forewardbalance=(balance+Deposit)
         print("Forewardbalance  PLN " ,forewardbalance)
         receipt=input('Would you like to print  a receipt?\n Please choose:\n y for  Yes\n n for No\n')
        
         if receipt == 'y':
           print('Printing Your receipt...\n')
           print('PLEASE TAKE OUT YOUR CARD')
           exit()
          
         elif receipt == 'n':
           print('PLEASE TAKE OUT YOUR CARD')
           print('Thank You for using EUROCASH')
           exit()
          
     else:
          print("None deposit made\n PLEASE TAKE  OUT YOUR CARD")
          exit()
  
   if Option==4:
     print('Thank You for using EUROCASH\n')
     print("PLEASE DO NOT FORGET YOUR CARD")
     exit()

 else: 
   if i==3:
     print("You reached the maximum number of attempts.\n We are sorry.")
   
   else: 
     print('ERROR \n Incorrect PIN number. \n \n Please try again')