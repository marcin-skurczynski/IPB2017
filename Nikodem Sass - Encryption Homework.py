import string
alfa = string.ascii_letters
choice = 0
while choice != '3':
  print ('\n --- --- --- \n\nChoose to encrypt or decrypt Your message: \n')
  print ('1 - Encryption \n')
  print ('2 - Decryption \n')
  print ('3 - Exit \n')
  choice = input('Your Choice ')

  if choice == '1':
    name = input('What is Your message? \n')
    shift = int(input('Input desired shift \n'))
    print('\nLength of the string is', len(name),'\n')

    for i in range (len(name)):
      counter = 0
      if name[i].isalpha() :
        while alfa[counter] != name[i]:
          counter = counter + 1
        print(alfa[(counter+shift)%52], end='')
      else:
        print(name[i], end='')
        counter = counter + 1
    print('\nThis is Your encrypted message\n')
      
  if choice == '2':
    name = input('What is Your message? \n')
    shift = int(input('Input desired shift \n'))
    print('\nLength of the string is', len(name),'\n')

    for i in range (len(name)):
      counter = 0
      if name[i].isalpha():
        while alfa[counter] != name[i]:
          counter = counter + 1
        print(alfa[(counter-shift)%52], end='')
      else:
        print (name[i], end='')
        counter = counter + 1
    print('\nThis is Your decrypted message\n')

print ('Thank You for using my program ! :)')
exit()