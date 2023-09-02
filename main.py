import datetime as dt
import smtplib
import pandas as pd
import random

my_email = "buggyclowndummy@gmail.com"
pssword = "qqjuiuxbkfvrvyej"

choices = [1,2,3]


birthday_data = pd.read_csv("bwish/birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")



now = dt.datetime.now()
current_date = now.day
current_month = now.month


for row in birthday_dict:
    if row["month"] == current_month and row["day"] == current_date:
        name = row["name"]
        address = row["email"]
        print("Found")
        num  =random.choice(choices)
        with open(f"bwish/letter_templates/letter_{num}.txt") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]",name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=pssword)
            connection.sendmail(from_addr=my_email,to_addrs=address,msg=f"Subject:Testing\n\n{letter}")
            connection.close()







    