from art import logo
import os

print(logo)

switch = True

# bucle: mientras quiera otra operacion
def switch_other_operation():
    desition = ""
    while desition != "Y" or desition != "N":
        desition = input("Do you want to do other operation? (Y) or (N): ").upper()
        if desition == "Y":
            return True
        elif desition == "N":
            return False
        else:
            print("Wrong answer? choose Y or N")

while switch:

    #Si quiere encriptar o descibrar
    encript_decript = input("Do you want encrypt (E) or decript (D)? ").upper()
    
    if encript_decript == "E":
    
        # si quiere encriptar
        text = input("What do you want to encript?\n")
        code = int(input("Set level of ecryptation? Must be a number: \n "))
        coded_text = []
        for char in text:
            coded_text.append(chr(ord(char) + code))
            
        os.system("clear")
        stringify_text = "".join(coded_text) 
        print(f"Your coded word:\n {stringify_text}")
        
    if encript_decript == "D":
        text = input("What do you want to decript?\n")
        code = int(input("what level of ecryptation you used? Must be a number: \n "))
        decoded_text = []
        for char in text:
            decoded_text.append(chr(ord(char) - code))
        
        os.system("clear")
        stringify_text = "".join(decoded_text) 
        print(f"Your decoded word:\n {stringify_text}")
        
    switch = switch_other_operation()