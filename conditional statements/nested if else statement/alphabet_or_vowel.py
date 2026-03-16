#Write a Python program that accepts a single character and checks whether it is an alphabet and also a vowel.
a=input("Enter a character")
ch="abcdefghijklmnopqrstuvwxyz"
vo="aeiou"
if a in ch:
    if a in vo:
        print("its a alphabet as well a vowel also")
    else:
        print("its a alphabet")