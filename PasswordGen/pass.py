import string
import random
import sys

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    #print(s1)
    s2 = string.ascii_lowercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
    s5 = string.whitespace
    #print(s5)
    try:                                                    #use this to handle gibberish
     plen = int(input("Enter the password length:\n"))
    except:
     sys.exit("Invalid Length")

    s=[]
    s.extend(list(s1))
    s.extend(list(s2)) 
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your password is:")
    print("".join(s[0:plen]))