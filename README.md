# AUTOMATIC BIRTHDAY EMAILER  

Automatically send a happy birthday email to family and friends.

## Description

This automatic email sending program built with PyCharm uses a service like https://www.pythonanywhere.com/ which allows automatic execution of a program with a chosen cadence (e.g. daily).
The program references a `birthdays.csv` file and if a birthday matches the current date, an email will automatically be sent to the individual with contents of one of the letters in `letter_templates` folder.

## Getting Started

* Download the zip and unpack.
* Open the project in your Python IDE.
* Open `main.py` and edit the four variables near the top of the file.
  * Example (note that if you are not using GMAIL as your email provider, then the PORT and EMAIL_SMTP will be different):
  ```sh
    MY_EMAIL = "my_email@gmail.com"
    MY_PASSWORD = "my_password"
    PORT = 587
    EMAIL_SMTP = "smtp.gmail.com"
  ```
* Edit `birthdays.csv` with the name, email, year(2022), month(3), and day(31) of each individual's birthday.

### Executing the program

* Running `main.py` will only cross-reference the `birthdays.csv` list for today's date.
* To automatically execute the program on a daily basis without having to open and run the project each day, create an account on https://www.pythonanywhere.com/ and have the program execute `main.py` daily.

## Authors

* Godman Tan
  * gtprogramming1@gmail.com
