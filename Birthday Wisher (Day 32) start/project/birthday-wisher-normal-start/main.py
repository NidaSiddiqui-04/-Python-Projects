##################### Normal Starting Project ######################
import datetime as dt
import random
import smtplib


import pandas
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
current_date=dt.datetime.now()
today=(current_date.month,current_date.day)
print(today)
# HINT 2: Use pandas to read the birthdays.csv
data=pandas.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthday_dict={(row.month,row.day):f"{row[0],row.email,row.year,row.month,row.day}" for (index,row) in data.iterrows()}
name=birthday_dict[today][0]


#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
def mail(letter):
    my_email="rubarumi.____@gmail.com"
    password="vhrllfntnfgexoan"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(from_addr=my_email,to_addrs="ni______i.0404@gmail.com",msg=f"Subject:Happy Birthday\n\n{letter}")
if today in birthday_dict:
           print("yesss")
           value = birthday_dict[today][2:6]
           randomno = random.randint(1, 3)
           print(randomno)
           if randomno == 1:
               with  open("letter_templates/letter_1.txt") as f1:
                   firead = f1.read()
                   personalized_letter = firead.replace("[NAME]", value)
                   mail(personalized_letter)





           elif randomno == 2:
               with open("letter_templates/letter_2.txt") as f2:
                   f2read = f2.read()
                   personalized_letter = f2read.replace("[NAME]", value)
                   mail(personalized_letter)


           elif randomno==3:
               with open("letter_templates/letter_3 .txt") as f3:
                   f3read = f3.read()
                   personalized_letter = f3read.replace("[NAME]", value)
                   mail(personalized_letter)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



