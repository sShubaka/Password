import random
import string

def fun():
    numberofcharacters = int(input("How many characters do you want in your password?(Enter a number) "))

    def passwordmaker():
        password = print(''.join(random.sample(string.ascii_letters + string.punctuation + string.digits, numberofcharacters)))

    if numberofcharacters <= 6:
        print("The password length is too short. Are you sure you want your password to be", numberofcharacters ,"characthers long.\nThe minimum length should be at least 7 charachters.")
        yesorno = input("Your password will be the number of characters long as you chose before.\nType 'Yes' or 'No' if you want your password to be 6 characters long or shorter. ")
        if yesorno == "Yes":
            print("Here is your generated password:")
            passwordmaker()
        elif yesorno == "No":
            quit()
        else:
            print("Wrong input.")
            print("Lets try again.\n\n\n")
            fun()
    else:
        print("Here is your generated password:")
        passwordmaker()
    def anotherpass():
        anotherpass = input("Would like to make a another password?\nType 'Yes' or 'No'. ")
        if anotherpass == "Yes":
            print("Starting again.\n\n\n")
            samenumberofcharacters = input("Would you like to have to same number of characters in this new password?\nType'Yes' or 'No'. ")
            if samenumberofcharacters == "Yes":
                print("Here is your generated password:")
                passwordmaker()
            elif samenumberofcharacters == "No":
                fun()
            else:
                print("Wrong input.")
                print("Let's try again.\n\n\n")
                fun()
        elif anotherpass == "No":
            print("Thank for making a password with us!")
            quit()
        else:
            print("Wrong input.")
            print("Let's try again.\n\n\n")
            fun()
    anotherpass()
fun()