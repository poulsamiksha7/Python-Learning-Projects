from datetime import datetime
mood=input("How are you feeling today?").lower()
if "happy"in mood:
    print("It's good you're feeling happy.")
elif "sad" in mood:
    print("Some days are good some days are bad. It's okay take care of yourself.")
elif "anxious" in mood:
    print("Do deep breathing.")
elif "tired" in mood:
    print("It's okay to feel tired.")
else:
    print("I don't know about this feeling but Take care of yourself.")

entry=input("Expand your thoughts (Press 'Enter' to Save)")

current_time=datetime.now().strftime("%Y-%m-%d %H-%M-%S")

with open("journal.txt","a") as file:
    file.write(f"Current date {current_time}\n")
    file.write(f"Mood {mood}\n")
    file.write(f"Thoughts {entry}\n")
    file.write(f"-"*30+"\n")
print("Your entry has been saved to journal.txt")

date_only=datetime.now().strftime("%Y-%m-%d")
with open("mood.csv","a") as csv_file:
    csv_file.write(f"\n{date_only},\n{mood},\n{entry}\n")

print("Your data has been saved to mood.csv")