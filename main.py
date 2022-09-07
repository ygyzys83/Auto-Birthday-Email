import datetime as dt
import pandas as pd
import random
import smtplib, ssl
port = 587
context = ssl.create_default_context()

MY_EMAIL = ""
# if gmail, generate a password through gmail's app password generator in account security
MY_PASSWORD = ""

#  Create a tuple from today's month and day using datetime
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# create a pandas dataframe out of birthdays.csv
data = pd.read_csv("birthdays.csv")
# print(data)

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

#  Compare and see if today's month/day tuple matches one of the keys in birthday_dict
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.starttls(context=context)
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )




