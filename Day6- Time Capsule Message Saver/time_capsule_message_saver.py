import json
from datetime import datetime 
message=input("What message you want for your Future Self? ").lower().strip()
unlock_date=input("When do you want to see this message?(YYYY-MM-DD)").strip()

current_time=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
data={
    "created_at":current_time,
    "unlock_date":unlock_date,
    "message":message
}
with open("future_message.json","a") as file:
   json.dump(data,file)
   file.write("\n")
print("Your entry has been saved to future_message.json")
date_only=datetime.now().strftime("%Y-%m-%d")
with open("future_message.csv","a") as csv_file:
    csv_file.write(f"{date_only},{unlock_date},{message}\n")

print("Your data has been saved to future_message.csv")
