import random

def randid(n):
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  number = "1234567890"
  special = "`~!@#$%^*&()_-+={}[]:;,.<>/?"
  all = lower + upper + number + special
  return("".join(random.sample(all, n)))

print("How you want your password to look like?")
choice = input("'1: start with your initials' or '2: a random password'? \n").lower()

if choice in ['1', '1:', '1: start with initials', 'initials']:
    initials = input("type your initials : \n").lower() 
    n = input("Give your password length : \n")
    num = input("How many passwords you want? \n")
    for i in range(int(num)):
      psw = initials + randid(int(n)-len(initials))
      print(psw)
elif choice in ['2', '2:', '2: a random password', 'random']:
    n = input("Give your password length : \n")
    num  = input("How many passwords you want? \n")
    for i in range(int(num)):
      psw = randid(int(n))
      print(psw)
else:
    print("Please re-run the app and select from given options.")