from datetime import datetime
import json
user_mood=input("What is your Mood?").strip().lower()
books={"happy":"Feel-Good Fiction",
       "sad":"Inspirational",
       "anxious":"Psychology",
       "tired":"Light Reading",
       "dreamy":"Fantasy",
       "romantic":"Romance",
       "lost":"Self-help"}
if user_mood in books:
    book_to_read=books[user_mood]
    print(f"You can read from this {book_to_read} genre")
else:
    print("I don't have a book for that mood, but I recommend reading Fantasy today!")

log_input=input("Do you want to log a book you are reading ?(Yes/No)").strip().lower()
if log_input == "yes":
    book_name=input("Which book you're reading? ")
    genre=input("Which book genre you're reading? ")
    print("Please enter the date in YYYY-MM-DD format.")
    start_date=input("When you're starting date ? (%Y-%m-%d)")
    end_date=input("When you're ending date ? (%Y-%m-%d)")
    format_pattern = "%Y-%m-%d"
    created_at = datetime.now().strftime("%Y-%m-%d")
    start_datetime_object = datetime.strptime(start_date, format_pattern)
    end_datetime_object=datetime.strptime(end_date,format_pattern)
    reading_time =  end_datetime_object - start_datetime_object 
    print(f"Estimated reading duration: {reading_time.days} days")
    record={
        "created_at":created_at,
        "book_name": book_name,
        "genre": genre,
        "start_date": start_date,
        "end_date": end_date,
        "reading_days": reading_time.days
        }
    try:
        with open("book_tracker.json","r") as file:
            data=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data=[]
    data.append(record)
    with open("book_tracker.json","w") as file:
            json.dump(data,file,indent=4) 
    print("Book logged successfully!")
