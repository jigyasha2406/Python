#1. Split the string "apple,banana,grapes" into a list using comma.
s="apple,banana,grapes".split(",")
print(s)
#Split the string "Python is powerful" into words.
str="Python is powerful".split(" ")
print(str)
#Split the string "Python is powerful" into words.
st="2026-01-21".split("-")
print(st)
#Join the list ["I", "love", "Python"] into a single sentence with spaces.
print(" ".join(["I","Love","python"]))
#print(" ".join(sr))
#Join ["a", "b", "c"] using - between them.'
print("-".join(["a","b","c"]))
#6. Split "one|two|three|four" using |.
s="one|two|three|four".split("|")
print(s)
#7. Convert "red blue green yellow" into a list of words.
list="red blue green yellow".split(" ")
print(list)
#8. Join ["10", "20", "30"] using , to form a string.
print(" ".join(["10","20","30"]))
#9. Split "user@gmail.com" to separate username and domain.
user="user@gmail.com".split("@")
print(user)
#10. Join ["2026", "01", "21"] into a date format 2026/01/21.
print("/".join(["2026","01","21"]))