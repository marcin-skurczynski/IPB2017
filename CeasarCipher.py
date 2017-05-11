import string

def charIsThere(char, _chars):
  try:
    indexValue=_chars.index(char)
  except ValueError:
    return False
  return True

def encode(w, shift):
  x=string.ascii_letters  
  chars="0123456789.,!? @#$%^&*()_]\|/"
  #print (len(x))
  
  q=len(w)
  # print (w)
  
  encryptedString=""
  for i in range (q):
    if charIsThere(w[i], chars):
      encryptedString+=w[i]
    else:
      newIndex=x.index(w[i])+shift
      if newIndex>51:
        newIndex=newIndex%52
      elif newIndex<-52:
        newIndex=newIndex%(-52)+52
      elif newIndex<0:
        newIndex=newIndex+52
      encryptedString+=x[newIndex]
  return encryptedString
  
def decode(w, shift):
  x=string.ascii_letters  
  chars="0123456789.,!? @#$%^&*()_]\|/"
  #print (len(x))
  
  q=len(w)
  # print (w)
  
  decryptedString=""
  for i in range (q):
    if charIsThere(w[i], chars):
      decryptedString+=w[i]
    else:
      newIndex=x.index(w[i])-shift
      if newIndex>51:
        newIndex=newIndex%52
      elif newIndex<-52:
        newIndex=newIndex%(-52)+52
        if newIndex==52:
          newIndex=0
      elif newIndex<0:
        newIndex=newIndex+52
      decryptedString+=x[newIndex]
  return decryptedString

answer=int(input("Please, choose whether to encode or decode:\n 1 - encode \n 2 - decode\n"))

w=input('Enter the sentense: ')
shift=int(input('Please, enter shift :'))  

if answer==1:
  print (encode(w, shift))
else:
  print (decode(w, shift))
  
    
# for i in range (q):
  
#   if w[i]==" ":
#     print (" ")
#   else:
#     newIndex=x.index(w[i])+shift
#     if newIndex>51:
#       newIndex=newIndex%52
#     print (w[i], x.index(w[i]), x[newIndex])
    
    
    
  
