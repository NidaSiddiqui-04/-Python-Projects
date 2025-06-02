#Write a program that returns True or False whether if a given year is a leap year.
def is_leap_year(year):
    if year%4==0 :
         
    
        if year%100==0 :
           if year%400==0:
               return True
           else:
               return False
        else:
           return True
    
    else:
        return False# Write your code here. 
print(is_leap_year(2000))
print(is_leap_year(1700))