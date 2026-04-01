def stress_level_management():
    stress_level_habits = input("What are your common habits when you feel stressed? (separate them with commas)").strip().lower().split(",")

    habits_score = {
        "coffee": 2,
        "sleep": -3,
        "scrolling": 4,
        "gym": -4,
        "work": 3,
        "read": -2,
        "cook": -1,
        "clean": -1
    }

    stress_level_habits = list(map(str.strip, stress_level_habits))

    habit_score = list(map(lambda habit: habits_score.get(habit, 0), stress_level_habits))

    positive_habits = list(filter(lambda pair: pair[1] > 0, zip(stress_level_habits, habit_score)))
    negative_habits = list(filter(lambda pair: pair[1] < 0, zip(stress_level_habits, habit_score)))

    total_stress = sum(habit_score)

    print("Your Stress Score is:", total_stress)

    if total_stress > 5:
        print("You have High Stress due to:", [habit for habit,_ in positive_habits])
        print("Try replacing them with healthier habits like: gym, read, cook.")
    elif total_stress >= 1:
        print("You have Moderate Stress due to:", [habit for habit,_ in positive_habits])
    elif total_stress <= 0:
        print("You are Relaxed/Balanced")
    else:
        print("Error!")

    print("Habits reducing stress:", [habit for habit,_ in negative_habits])
    print("Habits increasing stress:", [habit for habit,_ in positive_habits])


stress_level_management()