import random

num1 = 0
number = int(input("How many characters do you want in your password?(Enter a number) "))

def passwordmaker():
    characters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                  'A','B','C','D','E','F','G','H',"I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                  "1","2","3","4","5","6","7","8","9","0","`","~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{",
                  "}","[","]","|",":",";","'",'"',",","<",">",".","?","/")

    print(random.choice(characters))

if number <= 6:
    print("The password length is too short. Are you sure you want your password to be", number ,"characthers long.\nThe minimum length should be at least 7 charachters.")
else:
    while num1 < number:
        passwordmaker()
        num1 += 1