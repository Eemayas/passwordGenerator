import string
import random


print("Enter password length: ")
Digit = int(input("Number of Digits:  "))
Letters = int(input("Number of letters: "))
Specialcharacters = int(input("Number of Special characters:  ")) 


characterList = []
entry=""
i=0
j=0
length=Specialcharacters+Letters+Digit
for i in range(length):
    for j in range(Letters):
        characterList.append(string.ascii_letters)
    j=0
    for j in range(Digit):
        characterList.append(string.digits)
    j=0
    for j in range(Specialcharacters):
        characterList.append(string.punctuation) 


GroupPassword=[]
i=0
j=0
for i in range(10):
    password =""
    for j in range(length):
        randomchar = random.choice(characterList[j])
        password+=randomchar
        password=list(password)
        random.shuffle(password)
        password=''.join(password)
    GroupPassword.append(password)

print("The 10 random password are")

for i in range(10):
    print("\n")
    print(GroupPassword[i])
