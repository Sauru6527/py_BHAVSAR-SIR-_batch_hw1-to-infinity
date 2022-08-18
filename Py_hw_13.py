#Program that returns true or false
import time
def fun(input):
    if(input%2==0):
        return True
    else:
        return False

input = int(input("ENTER THE NUMBER => "))

print("Processing...........")
time.sleep(3)
catches = fun(input)

if(catches==True):
    print("This Is Even Number")

else:
    print("Its ODD Number")