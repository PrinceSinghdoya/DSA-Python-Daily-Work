#  Extraction of Digits

#  Interviewer Give a Input 
n = 5873

# let's create a variable for storing value of n
num = n
while num>0:
    lastDigit = num%10 #for taking out the last digit
    print(lastDigit)
    num=num//10 #for converting 5873 into 5873 by floating means it convert 587.3 into 587

