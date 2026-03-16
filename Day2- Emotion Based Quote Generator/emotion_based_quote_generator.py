from datetime import datetime
import random

user_input=input("How are you feeling Today?\n Happy/Sad/Tired/Anxious \n  Choose any 1 from Above ").strip().lower()

happy=["Choose joy today","Smile: it's free therapy","Chase sunsets, not storms","Today is a good day for a good day"]
sad=["Grief is the price we pay for love","And thus the heart will break, yet brokenly live on","The silence in this room screams your name","Sometimes, when one person is missing, the whole world seems depopulated"]
tired=["On a scale of 1–tired, today I’m Sleeping Beauty","I’m so tired, even my tiredness is tired","I’m so tired, even my tiredness is tired","Laziness is nothing more than the habit of resting before you get tired"]
anxious=["Breathe in courage, exhale fear","Don't believe every worried thought","Nothing diminishes anxiety faster than action","Trust yourself. You've survived a lot, and you'll survive whatever is coming"]

entry=input("Write down Your Mood (Press 'Enter' to Save)")

if 'happy' in user_input:
    print(random.choice(happy))
elif 'sad' in user_input:
    print(random.choice(sad))
elif 'tired' in user_input:
    print(random.choice(tired))
elif 'anxious' in user_input:
    print(random.choice(anxious))
else:
    print("I don't know what this feeling is called, but everything works according to time. Wait for your time")

current_time=datetime.now().strftime("%Y-%m-%d %H-%M-%S")

with open("journal.txt","a") as file:
    file.write(f"Current date {current_time}\n")
    file.write(f"Mood: {user_input}\n")
    file.write(f"Thoughts: {entry}\n")
    file.write(f"-"*30+"\n")
print("Your entry has been saved to journal.txt")

date_only=datetime.now().strftime("%Y-%m-%d")
with open("mood.csv","a") as csv_file:
    csv_file.write(f"{date_only},{user_input},{entry}\n")

print("Your data has been saved to mood.csv")
