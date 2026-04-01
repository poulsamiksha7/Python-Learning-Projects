from datetime import datetime
life_map={
    "lazy": "Discipline",
    "gym": "Health",
    "broke": "Career",
    "tired": "Rest",
    "study": "Wisdom",
    "silence": "Expression",    
    "closed": "Boldness",      
    "drift": "Connection",     
    "deceit": "Integrity",      
    "neglect": "Foundation"
}
history=set()

print("Type your regrets (Type 'exit' to Stop )")

while True:
    regret=input("Enter a regret: ").lower().strip()
    if regret=="exit":
        print("Good job reflecting today. See you!")
        break
    if regret in history:
        print("You already Said that. Thank you !")
        continue

    history.add(regret)

    if regret in life_map:
        category=life_map[regret]
        print(f"This regret relates to {category}")
    else:
        category="Uncategorized"
        print("This regret is not categorized yet.")

    current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open("regret_categorizer.txt", "a") as file:
        file.write(f"Date: {current_time}\n")
        file.write(f"Regret: {regret}\n")
        file.write(f"Life area : {category}\n")
        file.write("-" * 30 + "\n")

    print("Your entry has been saved to regret_categorizer")

    date_only = datetime.now().strftime("%Y-%m-%d")
    with open("regret_categorizer.csv", "a") as csv_file:
        csv_file.write(f"{date_only},{regret},{category}\n")

    print("Your data has been saved to regret_categorizer.csv")
