import string
alfa = string.ascii_letters
choice = 0
while choice != '3':
  print ('\n --- --- --- \n\nChoose to Encrypt or Decrypt Your Message: \n')
  print ('1 - Encryption \n')
  print ('2 - Decryption \n')
  print ('3 - Exit \n')
  choice = input('Your Choice ')

  if choice == '1':
    name = input('What is Your Message? \n')
    shift = int(input('Input Desired Shift \n'))
    print('\nLength of The String is', len(name),'\n')

    for i in range (len(name)):
      counter = 0
      if name[i].isalpha() :
        while alfa[counter] != name[i]:
          counter = counter + 1
        print(alfa[(counter+shift)%52], end='')
      else:
        print(name[i], end='')
        counter = counter + 1
    print('\nThis is Your Encrypted Message\n')
      
  if choice == '2':
    name = input('What is Your Message? \n')
    shift = int(input('Input Desired Shift \n'))
    print('\nLength of The String is', len(name),'\n')

    for i in range (len(name)):
      counter = 0
      if name[i].isalpha():
        while alfa[counter] != name[i]:
          counter = counter + 1
        print(alfa[(counter-shift)%52], end='')
      else:
        print (name[i], end='')
        counter = counter + 1
    print('\nThis is Your Decrypted Message\n')

print ('Thank You for using my application!!!')
exit()
