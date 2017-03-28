import string 
alfa = string.ascii_letters
print ('Choose to encrypt or decrytp your message: \n')
print ('1 - Encryption \n')
print ('2 - Decryption \n')
choice = input('Define your choice \n')

if choice == '1':
  
 name = input('What is your Name?\n')
 shift = int(input('Input your disired shift\n'))
 print ('Lenght of the string is', len(name))

 for i in range (len(name)):
   counter = 0
   while alfa[counter] != name[i]:
     counter = counter + 1
   print (alfa[counter+shift], end='')
   
if choice == '2':
  name = input('What is your Name?\n')
  shift = int(input('Input your disired shift\n'))
  print ('Lenght of the string is', len(name))

  for i in range (len(name)):
   counter = 0
   while alfa[counter] != name[i]:
     counter = counter + 1
   print (alfa[counter-shift], end='')
