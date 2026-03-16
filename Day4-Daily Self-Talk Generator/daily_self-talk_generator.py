import random
from datetime import datetime


user_input = input("What part of the day is it? (morning / evening / night): ").lower().strip()


morning = [
    "Rise and shine – may your day be as bright as the morning sun!",
    "Wishing you a day filled with sunny smiles and happy thoughts!",
    "Good morning! Embrace the new day with hope and a positive spirit.",
    "May your coffee be strong and your Monday be short. Good morning!"
]

evening = [
    "This is an evening of wonders, indeed!",
    "Every sunset is an opportunity to reset.",
    "The evening has turned sweet and blue.",
    "The evening's glow is the day's gentle farewell."
]

night = [
    "The day is done, and the darkness falls from the wings of night.",
    "Night is the mother of thoughts.",
    "The night is more alive and more richly colored than the day.",
    "Sleep is that golden chain that ties health and our bodies together."
]

match user_input:
    case "morning":
        print("Good Morning! ☀️")
        affirmation = random.choice(morning)
    case "evening":
        print("Good Evening! 🌆")
        affirmation = random.choice(evening)
    case "night":
        print("Good Night! 🌙")
        affirmation = random.choice(night)
    case _:
        affirmation = "No matter the time, you are doing your best. Keep going. 💛"

print("💬 Affirmation for you:")
print(affirmation)


energy_level = int(input("What is your Energy Level today? (1-10): "))
sleep_level = int(input("What is your Sleep Level today? (1-10): "))

daily_power_level = (energy_level + sleep_level) * 5

print("⚡ Your Power Level for today is:", daily_power_level)

current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

with open("daily_self_talk.txt", "a") as file:
    file.write(f"Date: {current_time}\n")
    file.write(f"Time of Day: {user_input}\n")
    file.write(f"Affirmation: {affirmation}\n")
    file.write(f"Power Level: {daily_power_level}\n")
    file.write("-" * 30 + "\n")

print("Your entry has been saved to daily_self_talk")

date_only = datetime.now().strftime("%Y-%m-%d")
with open("daily_self_talk.csv", "a") as csv_file:
    csv_file.write(f"{date_only},{user_input},{daily_power_level}\n")

print("Your data has been saved to daily_self_talk.csv")
