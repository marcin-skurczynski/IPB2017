import string
alfa = string.ascii_letters
print ('Choose to encrypt or decrypt Your message: \n')
print ('1 - Encryption \n')
print ('2 - Decryption \n')
choice = input('Your Choice ')

if choice == '1':
  name = input('What is Your name? \n')
  shift = int(input('Input desired shift \n'))
  print('Length of the string is', len(name))

  for i in range (len(name)):
    counter = 0
    while alfa[counter] != name[i]:
      counter = counter + 1
    print(alfa[counter+shift], end='')

if choice == '2':
  name = input('What is Your name? \n')
  shift = int(input('Input desired shift \n'))
  print('Length of the string is', len(name))

  for i in range (len(name)):
    counter = 0
    while alfa[counter] != name[i]:
      counter = counter + 1
    print(alfa[counter-shift], end='')
