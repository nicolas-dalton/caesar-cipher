# Name: Nicolas Dalton
# Date: 9-3-2020
# Course: COSC 4343 Fall 2020 (Dr. Shebaro)
# Program Description: A python program that encrypts and decrypts a text file using a modified version of
                    # Caesar cipher by shifting each letter in the plaintext by a given shift value n
import string
#Function description: opens a text file and converts it to an array of characters
#precondition: Receives textfile string name
#postcondition:  array of characters from the text file
def open_file_and_convert_to_list(file_name):
    input = open(file_name, "r+")
    text = input.read()
    input.close()
    text = text.upper()
    text_list = list(text)
    return text_list

#Function description: writes on text file
#precondition: Receives textfile name and the written text
#postcondition:  writes on the text file
def write_file(file_name,text):
    output = open(file_name, "w")
    output.write(text)
    output.close()
#Function description: converts plain text to cipher text using caesar's cipher algorithim
#precondition: Receives n, the key value, or the shift value between 1 to 25
#postcondition:  writes encrypted cipher text on the cipher text file
def encrypt(n):
    plain_text_list = open_file_and_convert_to_list("plaintext.txt")
    alphabet_list = list(string.ascii_uppercase)
    cipher_text_list = []
    for i in plain_text_list:
        if i not in alphabet_list:
            cipher_text_list.append(i)
        for j in alphabet_list:
            if i == j:
                index = alphabet_list.index(j)
                if index+n > (len(alphabet_list)-1):
                        updated_n = (len(alphabet_list))- index
                        updated_index = n - updated_n
                        cipher_text_list.append(alphabet_list[updated_index])
                if index+n <= (len(alphabet_list)-1):
                    cipher_text_list.append(alphabet_list[index+n])
    cipher_text = ""
    for i in cipher_text_list:
        cipher_text += i
    write_file("ciphertext.txt",cipher_text)

#Function description: converts cipher text to plain text using caesar's cipher algorithim
#precondition: Receives n, the key value, or the shift value between 1 to 25
#postcondition:  returns the plain text in a string
def decrypt(n):
    cipher_text_list = open_file_and_convert_to_list("ciphertext.txt")
    alphabet_list = list(string.ascii_uppercase)
    plain_text_list = []
    for i in cipher_text_list:
        if i not in alphabet_list:
            plain_text_list.append(i)
        for j in alphabet_list:
            if i==j:
                index = alphabet_list.index(j)
                updated_index = index - n
                plain_text_list.append(alphabet_list[updated_index])
    plain_text = ""
    for i in plain_text_list:
        plain_text+=i
    return(plain_text)

#Function description: Writes the decrypted plain text on the plain text file
#precondition: Receives n, the key value, or the shift value between 1 to 25
#postcondition:  writes on the plain text file
def write_to_decrypt_file(n):
    plain_text = decrypt(n)
    write_file("plaintext.txt", plain_text)

#Function description: Decrypts plain text file to the user and asking user if it correct and will display the key value
#precondition: nothing
#postcondition:  returns the key value n
def break_for_trudy():
    print("Here is a possiblity")
    n=0
    for i in range(26):
        n+=1
        print(decrypt(n))
        answer = input("Does this look correct? Please type Yes or No : ")
        answer = answer.lower()
        if answer == "yes":
            break
    print("You key value for this decrpytion is : " + str(n))

#Function description: Displays the menu of options
#precondition: nothing
#postcondition:  Displays the menu of options
def menu():
    option = 1
    while option != 4:
        option = int(input("Choose the following the options: \n 1 - Encrypt \n 2 - Decrypt \n 3 - Break \n 4 - Exit : "))
        if option == 1:
            key = int(input("What is the key value n to encyrpt? : "))
            encrypt(key)
        elif option == 2:
            key = int(input("What is the key value n to decrypt? : "))
            write_to_decrypt_file(key)
        elif option == 3:
            print("We will display you different possibilites to decrypt. \n Please type Yes if the decrypt looks correct ")
            break_for_trudy()
        elif option > 4 or option < 1:
            print("That option is not available! Try again!")

menu()

