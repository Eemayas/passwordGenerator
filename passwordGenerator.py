import string
import random


print("Enter password length: ")
Digit = int(input("Number of Digits:  "))
Letters = int(input("Number of letters: "))
Specialcharacters = int(input("Number of Special characters:  ")) 


characterList = ""
i=0
j=0
length=Specialcharacters+Letters+Digit
for i in range(length):

    for j in range(Letters):
        characterList += string.ascii_letters
    j=0
    for j in range(Digit):
        characterList += string.digits
    j=0
    for j in range(Digit):
        characterList += string.punctuation


GroupPassword=[]
i=0
j=0
for i in range(10):
    password =""
    for j in range(length):
       
        randomchar = random.choice(characterList)
        password+=randomchar
    GroupPassword.append(password)

print("The 10 random password are")

for i in range(10):
    print("\n")
    print(GroupPassword[i])
