#It is important to know that to import things from other files
#The file must be in the same folder
import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 7, 26)

days_away = next_birthday - today

#In here I imported a variable from another file!
if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is in {days_away.days} days away!")

print("\n")

relevant_date = datetime.date(2005, 7, 26)

days_passed = today - relevant_date

print(f"The amount of days that has passed is of: {days_passed.days} days")
