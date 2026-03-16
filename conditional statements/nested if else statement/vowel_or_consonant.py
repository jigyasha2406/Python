#Write a program using nested if to check whether a character is an alphabet, and if it is an alphabet, check whether it is a vowel or consonant.
a=input("enter an alphabet:")
alpha="abcdefghijklmnopqrstuvwxyz"
vowels="adieu"
if a in alpha:
  if a in vowels:
    print("it is a vowels")
  else:
    print("it is a consonant")
else:
  print("it is not a alphabet")