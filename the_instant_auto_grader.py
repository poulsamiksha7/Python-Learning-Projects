import numpy as np
class Classroom:
    def __init__(self):
        scores = np.array([55, 82, 91, 64, 77,44,55,76,34,89])
        self.curved_scores = scores + 5
        self.class_avg=np.mean(self.curved_scores)
        self.highest_score=np.max(self.curved_scores)
    def __str__(self):
        return f"Instant Auto Grader \n Class Average: {round(self.class_avg,2)} \n Highest Score:  {self.highest_score}\n Curved Scores: {self.curved_scores}"
myclassroom=Classroom()
print(myclassroom)
    
