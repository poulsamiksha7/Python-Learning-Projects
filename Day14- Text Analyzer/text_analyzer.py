user_input=input("Enter your Paragraph... ")

print(f"Total characters with space:  {len(user_input)}")

print(f"Total characters without space: {len(user_input.replace(" ",""))}")

print(f"Total Words: {len(user_input.split(""))}")

most_repeated_word=user_input.lower().split("")

word_list = []

wordfreq = []

for i in most_repeated_word:
    word_list.append(i)

print(f"Most repeated word is: {max(word_list, key=word_list.count)}")

print(f"Number of sentences: {user_input.count(".")}")

search_word=input("Search for a word? ")

if search_word.lower() in user_input.lower():
    print(f"{user_input.find(search_word)}")
else:
    print("Sorry Could not fin Matching word.")


# Make this AS AI TEXT ANALYZER on 14-05-2026