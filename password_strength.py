# code to check password strength

import re

def check_password(pw):
    # check password length
    if len(pw) < 8:
        print("Password length less than 8 characters.\nPassword must be atleast 8 characters long.\n")
        return False
    
    # check for UC letter
    if not re.search(r'[A-Z]', pw):
        print("No uppercase character found.\nPassword must include atleast 1 uppercase character.\n")
        return False
    
    # check for LC letter
    if not re.search(r'[a-z]', pw):
        print("No lowercase character found.\nPassword must include atleast 1 lowercase character.\n")
        return False
    
    # check for digit
    if not re.search(r'\d', pw):
        print("No digits found.\nPassword must contain atleast 1 digit.\n")
        return False
    
    # check for speacial character
    if not re.search(r'[!@#$[\]%\\^&*()\/,.?":{}|<>]', pw):
        print("No special charcter found.\nPassword must contain atleast 1 special character.\n")
        return False
    
    return True
    

pw = input("Enter your password: ")
res = check_password(pw)

if res:
    print("VALID PASSWORD\n")
else:
    print("INVALID PASSWORD")