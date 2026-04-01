def predict_milestone(age,**kwargs):
    print(f"Your current age is {age}")
    senior_role_age=age+5
    financial_independent_age=age+10
    leadership_age=age+15
    # print(f"Age {senior_role_age} -> Senior Role \n Age {financial_independent_age} -> financial Independent \n {leadership_age}-> Leadership")
    print(f"Age {senior_role_age} -> Senior Role")
    print(f"Age {financial_independent_age} -> Financial Independent")
    print(f"Age {leadership_age} -> Leadership")
    print("\n Custom Goals")
    step=3
    for i, (key,goal) in enumerate(kwargs.items(), start=1):
        predict_age=age+step*i
        print(f"Age {predict_age} -> {goal}")
              
user_input=int(input("Enter your current age"))
predict_milestone(
    user_input,
    goal1="Buy a House",
    goal2="Buy a Car",
    goal3="Travel a Country"

)