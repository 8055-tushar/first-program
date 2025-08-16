#spy number is digits of number are equal to digits of sum
n=int(input("Enter any number"))
pro=1
add=0
while(n>=1):
    rem=n%10
    add=add+rem
    pro=pro*rem
    n=n//10
if(pro==add):
    print("It's spy number")
else:
    print("It's not spy number")
    
