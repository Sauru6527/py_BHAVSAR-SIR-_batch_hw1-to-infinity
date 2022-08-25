#HOMEWORK_15
"""

Write a function which accept a list and one integer number... 

If we get 1 as a second parameter sort list in ascending order. 

If we get 2 as a second parameter sort list in descending order. 

Example - 
List [19,5,35] 
Function Call
fun(list, 1)

Output - [5,19,35] 

Function Call
fun(list, 2)

Output - [35,19,5] 

Note - Value should be same of original list after function call

Function call chya aadhi ani nantr list madhil value same print zalya pahije.
Output Function madhe print kele tri chalel

"""
list = []                 #ORIGINAL LIST
list_temp = []            #TEMPERORAY LIST WITH COPY OF ORIGINAL
print("BEFORE:>",list)

def func1(list_temp,press):
    print("\n")
    if(press==1):
            list_temp.sort(reverse=False)     #LIST WILL BE IN ASCENDING.12345
            print(f"Ascending,list after sort:> {list_temp}")

    elif(press==2):
            list_temp.sort(reverse=True)      #LIST WILL BE IN DESCENDING.54321
            print(f"Descending,list after sort:> {list_temp}")                 


NUM = int(input("Enter how many number you want to insert in list:>"))


for i in range(0,NUM):     #NUM IS TOTAL NUMBER TO INSERT IN LIST
        enter = int(input("Enter number:> "))      #USER CHOICE NUMBER 
        list.append(enter)                         #APPEND TO ORIGINAL LIST
print("ORIGINAL LIST => ",list)                    #PRINT ORIGINAL LIST

list_temp = list.copy()                            #CREATES DUPLICATE COPY OF ORIGINAl list

#asc_desc 
print("PRESS>>>>>>>>\n1:Ascending\n2:Descending") 
press = int(input("1/2 => "))             #MENU

func1(list_temp,press)                   #FUNCTION Call



print("Last final list=> ",list)    #TO CHECK ORIGINAL LIST IS CHNAGE OR NOT 