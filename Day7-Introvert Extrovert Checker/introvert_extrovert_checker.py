class PersonalityQuiz:
    def __init__(self):
        self.questions=["When a stranger talks to me, I consider it an opportunity to make a connection.",
                        "Being out with a big group of friends all night can be exhausting",
                        " I consider myself to be an assertive person",
                        "It’s not unusual for me to get lost in thought around other people",
                        "I think that being on a reality show would be a nightmare.",
                        "I don’t mind talking about anything, even if I’m not that knowledgeable about it.",
                        "I'd rather spend one-on-one time with a close friend than get together with a friend group.",
                        "It’s better to have a roommate than to live alone.",
                        "It's disappointing to review my weekly schedule and see that it includes no social plans.",
                        "At work meetings, I think it’s important to speak up often",
                        "I have a lot of fun playing tricks on my friends and family",
                        "I like to get my friends and co-workers excited about our plans.",
                        "I don’t like to feel pushed into dancing at parties.",
                        "When I'm in charge, I prefer meeting with people one-on-one to holding large brainstorming sessions.",
                        "When I go to a party, I often think about how early it would be appropriate to leave.",
                        "If someone is interesting enough, I could happily spend an evening just listening to their stories",
                        "In work or in life, I’d rather take some time to consider the next steps even if others are eager to rush ahead.",
                        "As a kid, I was always the first to volunteer to read aloud",
                        "One of the great attractions of travel is the opportunity to meet new people",
                        "A day spent alone working on my hobbies sounds perfect."]

        #For questions used this website "https://www.psychologytoday.com/us/tests/personality/extroversion-introversion-test"
        self.score=0
    def take_quiz(self):
        for question in self.questions:
            print()
            print(question)
            answer=input("1. Agree 2. Disagree").strip()
            while answer != "1" and answer != "2":
                print ("Please enter 1 or 2")
                answer=input("1. Agree 2. Disagree").strip()
                     
            if answer=="1": 
                self.score+=1
            else:
                self.score-=1

                                                  
    def get_result(self):
        if self.score>0:
            print(f"Your Personality Type is Extrovert and Your Score is {self.score}")
        elif self.score<0:
            print(f"Your Personality Type is Introvert and Your Score is {self.score}") 
        else:
            print(f"Your Personality Type is Ambivert and Your Score is {self.score}")

quiz = PersonalityQuiz()
quiz.take_quiz()
quiz.get_result()

              