import random as r
import string as s
x = s.ascii_letters

def random_password_generator():
    password = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x = s.ascii_letters
    y = s.digits
    for e in range(0,13):
        password[e] = r.choice(x)
    for e in range(13,15):
        password[e] = r.randint(0,10)
    for e in range(15,19):
        password[e] = r.choice(x+y)
    newpassword = ''
    for e in password:
        newpassword = newpassword + str(e) 
    print(newpassword) 


def listToString(s): 
    string = ''
    for e in s:
        string = string + str(e) 
    print(string) 

random_password_generator()

