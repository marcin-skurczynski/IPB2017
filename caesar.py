import string

def selectMode():
  mode = input("What would you like to do?\n\
  e – encrypt\n\
  d – decrypt\n")
  
  if (mode != 'e' and mode != 'd'):
    print ("Please choose either 'e' or 'd'.")
    selectMode()
    
  return mode

def isChar(char, chars):
  try:
    char_index = chars.index(char)
  except ValueError:
    return False
  return True

def crypt(encrypt, text, shift):
  letters = string.ascii_letters
  chars = ' .,!?'
    
  length = len(text)
  letters_length = len(letters)

  crypted_text = ''

  for i in range(length):
    if isChar(text[i], chars):
      crypted_text += text[i]
    else:
      letter_index = letters.index(text[i])
      
      if encrypt == True:
         new_index = letter_index + shift
      else:
        new_index = letter_index - shift

      if (new_index > letters_length-1):
        new_index = new_index % letters_length
      elif (new_index < -letters_length):
        new_index = 52 + (new_index % -52)
        if (new_index == 52):
          new_index = 0
      elif (new_index < 0):
        new_index = 52 + new_index

      crypted_text += letters[new_index]
      
  return crypted_text

mode = selectMode()
text = input("Please enter text: ")
shift = int(input("Please enter shift: "))

if mode == 'e':
  print(text)
  print(crypt(True, text, shift))
else:
  print(text)
  print(crypt(False, text, shift))
