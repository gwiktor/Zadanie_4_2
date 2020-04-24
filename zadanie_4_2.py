#Zadanie 4_2
def palindrom(slowo):
  if slowo[::-1] == slowo:
    print(slowo, slowo[::-1])
    return True
  else:
    print("To nie palindrom")
    return False
    
palindrom("oko")
palindrom("słoń")