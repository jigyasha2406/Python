#Write a program using elif to check whether a character is a vowel, consonant,digit, or special character.
a=input("Enter a character")
ch="bcdfghjklmnpqrstvwxyx"
vo="aeiou"
sp="@!#$%^&*_-"
if(a in ch ):
    print("Its a consonant")
elif( a in vo):
    print("Its a vowel")
elif(a in sp ):
    print("Its a special character")
else:
    print("ita a number")