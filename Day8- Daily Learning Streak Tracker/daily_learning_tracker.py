from datetime import datetime
import json
import matplotlib.pyplot as plt
class StreakTracker:
    def __init__(self):
        self.streak=0
        self.file="streak.json"
        self.history={}
        self.load_data()
    def load_data(self):
        try:
            with open(self.file,"r") as file:
                 data=json.load(file)
                 self.streak=data["streak"]
                 self.history=data["history"]
        except:
            self.streak=0
            self.history={}
    def save_data(self):
        data={
            "streak": self.streak,
            "history": self.history
        }
        with open(self.file,"w") as file:
            json.dump(data,file,indent=4)
    def log_day(self,studied_today):
        today=datetime.now().strftime("%Y-%m-%d")
        if studied_today.strip().lower()=="yes":
            self.streak+=1
            self.history[today]=1
        else:
            self.streak=0
            self.history[today]=0
        self.save_data()
        total_days = len(self.history)
        studied_days = sum(self.history.values())

        consistency = (studied_days / total_days) * 100
        print(f"Your Current Streak is {self.streak}")
        print(f"📊 Study Consistency: {consistency:.1f}%")
    def show_graph(self):

        sorted_history = dict(sorted(self.history.items()))

        dates = list(sorted_history.keys())
        values = list(sorted_history.values())
        colors = ["green" if v == 1 else "red" for v in values]

        plt.bar(dates, values, color=colors)
        plt.style.use("seaborn-v0_8")
        plt.title("Study Consistency Tracker")
        plt.xlabel("Date")
        plt.ylabel("Study Activity")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.yticks([0,1], ["Missed","Studied"])
        plt.xticks(rotation=45)
        plt.figure(figsize=(10,5))
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()

        plt.show()
tracker=StreakTracker()
answer = input("Did you study today? (yes/no): ")
tracker.log_day(answer)
tracker.show_graph()
