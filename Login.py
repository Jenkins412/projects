def sign_up_or_login(usernames,passwords):
    print("\nPlease choose one of the following: (Type 'a','b',or 'c')")
    print("a) Sign-up")
    print("b) Login")
    a = input("c) Quit program\n")
    if str(a) == 'b' or str(a) == 'B':
        login_main(usernames,passwords)
    elif str(a) == 'a' or str(a) == 'A':
        sign_up(usernames,passwords)
    elif str(a) == 'c' or str(a) == 'C':
        return False
    else:
        print("\nUser's input unable to be understood. Please try again.")
        sign_up_or_login(usernames,passwords)


def login_main(usernames,passwords):
    user = input("\nUsername:\t") 
    password = input("Password:\t")
    for e in range(0, len(usernames)):
        if usernames[e] == user and passwords[e] == password:
            print("Sign in successful. Thank you for using my program.")
            sign_up_or_login(usernames,passwords)
        elif user not in usernames:
            print("Username does not exist. Please try again. Press 's' to sign up for a new account.")
            login_main2(usernames,passwords)
    else:
        print("Username and password do not match. Please try again. Press 's' to sign up for a new account.")
        login_main2(usernames,passwords)

                
def login_main2(usernames,passwords):
    user = input("\nUsername:\t")
    if user == str('s') or user == str('S'):
        sign_up(usernames,passwords)
    password = input("Password:\t")
    for e in range(0, len(usernames)):
        if usernames[e] == user and passwords[e] == password:
            print("Sign in successful. Thank you for using my program.")
            sign_up_or_login(usernames,passwords)
        elif user not in usernames:
            print("Username does not exist. Please try again. Press 's' to sign up for a new account.")
            login_main2(usernames,passwords)
    else:
        print("Username and password do not match. Please try again. Press 's' to sign up for a new account.")
        login_main2(usernames,passwords)
    

def sign_up(usernames,passwords):
    x = input("\nChoose your username:\t")
    for e in usernames:
        if str(e) == str(x):
            print("That username is already taken.")
            sign_up(usernames,passwords)
    if len(x) < 8:
        print("\nLength of username must be at least 8 characters.")
        sign_up(usernames,passwords)
    else:
        with open('user_data.csv','w') as file:
            data = file.write(str(x))
    usernames.append(x)
    create_password(usernames,passwords)
    
def existing_sign_up(usernames,passwords):
    a = input("Create your username:")
    for e in usernames:
        if str(e) == str(a):
            print("That username is already taken.")
            existing_sign_up(usernames,passwords)
        else:
            create_password(usernames,passwords)
    

def create_password(usernames,passwords):
    y = input("Create your password:\t")
    if len(y) < 8:
        print("\nYour password must be at least 8 characters long and contain one number.")
        create_password(usernames,passwords)
    for e in str(y):
        if str(e) == str(1):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(2):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(3):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(4):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(5):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(6):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(7):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(8):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
        elif str(e) == str(9):
            z = input("Confirm your password:\t")
            if str(y) == str(z):
                with open('user_data.csv','a') as file:
                    data = file.write(str(z))
                print("\nYour account has been created.")
                passwords.append(z)
                sign_in(usernames,passwords)
            else:
                print("\nYour passwords do not match. Please try again.")
                create_password(usernames,passwords)
    else:
        print("\nYour password must be at least 8 characters long and contain one number.")
        create_password(usernames,passwords)



def sign_in(usernames,passwords):
    sign_in = input("\nWould you like to sign in? Please reply 'Yes' or 'No'.\n")
    if sign_in == 'Yes' or sign_in == 'yes':
        user = input("\nUsername:\t") 
        password = input("Password:\t")
        for e in range(0, len(usernames)):
            if usernames[e] == user and passwords[e] == password:
                print("Sign in successful. Thank you for using my program.")
                sign_up_or_login(usernames,passwords)
            elif user not in usernames:
                print("Username or password is incorrect.")
                sign_in(usernames,passwords)
        else:
            print("Username and password do not match. Please try again. Press 's' to sign up for a new account.")
            login_main2(usernames,passwords)
        
    elif sign_in == 'No' or sign_in == 'no':
        newaccount = input("Would you like to sign up for another account? Please reply 'Yes' or 'No'.\n")
        if str(newaccount) == 'Yes' or str(newaccount) == 'yes':
            sign_up(usernames,passwords)
        elif str(newaccount) == 'No' or str(newaccount) == 'no':
            a = input("Would you like to login to an existing account? Please reply 'Yes' or 'No'.\n")
            if str(a) == 'no' or str(a) == 'No':
                sign_up_or_login(usernames,passwords)
            elif str(a) == 'yes' or str(a) == 'Yes':
                login_main(usernames_passwords)
            else:
                print("Unable to process user's input. Please try again.")
                sign_up_or_login(usernames,passwords)
        else:
            print("Unable to process user's input. Please try again.")
            sign_in(usernames,passwords)
    else:
        print("Unable to process the user's input. Please try again.\n")
        sign_up_or_login(usernames,passwords)

def makenewaccount(usernames,passwords):
    newaccount = input("Would you like to sign up for another account? Please reply 'Yes' or 'No'.\n")
    if str(newaccount) == 'Yes' or str(newaccount) == 'yes':
        sign_up(usernames,passwords)
    elif str(newaccount) == 'No' or str(newaccount) == 'no':
        a = input("Would you like to  Please reply 'Yes' or 'No'.\n")
    else:
        print("Unable to process user's input. Please try again.")
        makenewaccount(usernames,passwords)
    
def main():
    usernames = []
    passwords = []
    sign_up_or_login(usernames,passwords)

main()
