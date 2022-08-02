
"""

HOMEWORK_5  : Pay Bill (choose the random friend)
NAME        : AHER SAURABH SANTOSH
BATCH       : PYTHON
GUIDE BY    : AMOL BHAVSAR SIR
DATE        : 2/8/2022 (5:46 PM)
DESCRIPTION : GIVE 5 credit cards to waiter he will choose any one from it he the randomly choose credit card owner will pay the bill


"""



#>>>>imported the random name module
import random
import random
import random
import random
import random
import random

#>>name1="saurabh"
#>>name2="akash"
#>>name3="sai"

#T>>>AKING INPUT FROM USERS............
name1=input("ENTER THE NAME OF PERSON :> ")
name2=input("ENTER THE NAME OF PERSON :> ")
name3=input("ENTER THE NAME OF PERSON :> ")
name4=input("ENTER THE NAME OF PERSON :> ")
name5=input("ENTER THE NAME OF PERSON :> ")

#>>>CREATED LIST AND ADDED VARIABLES IN IT......
list=[name1,name2,name3,name4,name5]

#>>>>random.choice is module of random package
choice=random.choice(list)

#>>>Printing the  Choice variable which has random string in it i.e our friend
print("\nHEY! "+choice+" Pay the Bill. ")