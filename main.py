import datetime as dt
import random
import smtplib
import pandas

# Use your email and password
MY_EMAIL = "email@example.com"
MY_PASSWORD = "password123"

now = dt.datetime.now()
todays_month = now.month
todays_day = now.day

# Read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Check if today matches a birthday in the birthdays.csv
for index, person in data.iterrows():
    if person["day"] == todays_day and person["month"] == todays_month:
        persons_name = person["name"]

        # Pick a random letter, replace the [NAME] with the person's name
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            letter_content = letter.read()
            modified_letter = letter_content.replace("[NAME]", persons_name)

            # Send a letter to person's email
            with smtplib.SMTP("smtp.example.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=person["email"],
                    msg=f"Subject:Happy Birthday, {person['name']}\n\n{modified_letter}"
                )



