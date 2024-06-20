'''Akshay has a number of toys and he decided to donate some of them to an NGO. After 
the donation, he still has some toys left. Write a program to help Akshay to determine 
the number of remaining toys.
Example:
Input: 50 45
Output: The remaining number of toys = 5
Input: 60 6
Output: The remaining number of toys = 54.'''
t_toys=int(input("enter the number of toys Akshay has: "))
d_toys=int(input("Enter the toys donated: "))
r_toys=t_toys-d_toys
print("the remaining toys are: ",r_toys)