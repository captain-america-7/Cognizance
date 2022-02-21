#Created and Developed by Aruntej
#Program to check if the given number is a palindrome number
num=int( input("Enter the number:-") )
temp=num
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if(temp==reverse):
    print("The number is palindrome")
else:
    print("Not a palindrome")