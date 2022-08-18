#Armstrong Number===> 153 = 1*1*1 + 5*5*5 + 3*3*3* => 153

# Took the Input from User..
NUM = int(input("Enter the Number ==> "))

#this is temporary variable....
reserved_NUM = NUM

#We are counting digits of number from user and return count of digits which we required in for loop....
def digit_counter(give_number):
                 count = 0
                 while(give_number != 0):
                          give_number = give_number // 10
                          count = count+1
                 return count

counts = digit_counter(NUM)
#print(f"Total Digits in given Number:::> {counts}")




sum= 0
count_digits = 0
count = 0




#for loop

for i in range(0,counts):
    count = count+1
    mod = NUM%10
    NUM = NUM//10
    sum  = sum +mod*mod*mod

#print(f"TOTAL====>> {sum}")


#actual logic to check number is armstrong
def check_armstrong(sum,reserved_NUM):
    #print(f"SUM ===> {reserved_NUM}")
    #print(f"reserved_NUM ===> {sum}")

    if(sum == reserved_NUM):
        print(f"Yes It's Armstrong Number")
    else:
        print(f"Its Not an Armstrong!")


check_armstrong(sum,reserved_NUM)