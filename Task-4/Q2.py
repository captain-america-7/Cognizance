#Created and Developed by Aruntej
#Program to accept a string from the user and display characters
#that are present at an even index number
string=str( input("Enter the string:-") )
even_letters=""
for i in range(len(string)):
    if i%2==0:
        even_letters= even_letters +string[i]
print(even_letters)

  