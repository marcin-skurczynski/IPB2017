balance=2475.11
print(" > > > >  eCard  < < < <  ")
for i in range (1,4):
 PIN = int(input('Please Enter You 4 Digit Pin: '))
 if PIN == (7546):
   print('Your PIN Is Correct\n')
   print("""
   1)        Balance
   2)        Withdraw
   3)        Deposit
   4)        Return Card
   """)
   Option=int(input("Enter Option: "))
  
   if Option==1:
     print("Balance  $ ",balance)
     print('Thank You For Using eCard')
     exit()
   
   if Option==2:
     print("Balance  $  ",balance)
     Withdraw=float(input("Enter Withdraw amount $ "))
     if Withdraw>0:
       if Withdraw<balance:
         forewardbalance=(balance-Withdraw)
         print('You Have Withdrawn ',Withdraw)
         print("Foreward Balance  $ ",forewardbalance)
         receipt=input('Would You Like To Print Receipt?\n Please Choose:\n y for YES\n n for NO')
      
         if receipt=='y':
           print('Printing Your Receipt\n')
           print('PLEASE TAKE OUT YOUR CARD')
           exit()
         elif receipt=='n':
           print('PLEASE TAKE OUT YOUR CARD\n')
           print('THANK YOU FOR USING eCARD')
           exit()
       elif Withdraw>balance:
         print("No Money No Honey")
         exit()
       else:
         print("None withdraw made")
         exit()
     else: print('Negative Values are Impossible To Withdraw')
     exit()
        
   if Option==3:
     print("Balance  $ ",balance)
     Deposit=float(input("Enter deposit amount $ "))
     if Deposit>0:
         forewardbalance=(balance+Deposit)
         print("Forewardbalance   ",forewardbalance)
         receipt=input('Would You Like To Print Receipt?\n Please Choose:\n y for YES\n n for NO')
      
         if receipt=='y':
           print('Printing Your Receipt\n')
           print('PLEASE TAKE OUT YOUR CARD')
           exit()
         elif receipt=='n':
           print('PLEASE TAKE OUT YOUR CARD\n')
           print('THANK YOU FOR USING eCARD')
           exit()
     else:
         print("None deposit made\n PLEASE TAKE OUT YOUR CARD")
         exit()
        
   if Option==4:
     print('THANK YOU FOR CHOOSING eCard\n ')
     print('TAKE OUT YOUR CARD')
     exit()
     
 else:
   if i==3:
     print("You Have Reached The Limit Of Transactions Possible")
   
   else: 
     print('Error Incorrect PIN Number\n \n PLEASE TRY AGAIN ')
