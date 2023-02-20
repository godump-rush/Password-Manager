import os.path

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

def appendNew():
    # This function will append new new password in the text file
    file = open("info.txt", 'a')

    print()
    print()

    username = input("Please enter the Username: ")
    password = input("Please Enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "Username: " + username + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("------------------------------\n")
    file.write("\n")
    file.close()

def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)

# Call checkExistence to make sure the file exists
checkExistence()

# Call appendNew to append new password to the file
appendNew()

# Call readPasswords to read and print the content of the file
readPasswords()


