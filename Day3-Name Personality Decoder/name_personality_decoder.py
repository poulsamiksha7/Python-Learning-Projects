from datetime import datetime
user_input = input("Enter your name... ").lower()
no_spaces_input = user_input.replace(" ", "")

first_char = no_spaces_input[0].upper()

match first_char:
    case 'A':
        trait = "Ambitious"
    case 'B':
        trait = "Brave"
    case 'C':
        trait = "Creative"
    case 'D':
        trait = "Dashing"
    case 'E':
        trait = "Energetic"
    case 'F':
        trait = "Focused"
    case 'G':
        trait = "Generous"
    case 'H':
        trait = "Hardworking"
    case 'I':
        trait = "Intelligent"
    case 'J':
        trait = "Joyful"
    case 'K':
        trait = "Kind"
    case 'L':
        trait = "Loyal"
    case 'M':
        trait = "Motivated"
    case 'N':
        trait = "Nurturing"
    case 'O':
        trait = "Optimistic"
    case 'P':
        trait = "Passionate"
    case 'Q':
        trait = "Quick-witted"
    case 'R':
        trait = "Resilient"
    case 'S':
        trait = "Smart"
    case 'T':
        trait = "Thoughtful"
    case 'U':
        trait = "Unique"
    case 'V':
        trait = "Visionary"
    case 'W':
        trait = "Wise"
    case 'X':
        trait = "X-factor personality"
    case 'Y':
        trait = "Youthful"
    case 'Z':
        trait = "Zealous"
    case _:
        trait = "Mysterious"

name_length = len(no_spaces_input)

if name_length < 5:
    vibe = "Short & Sharp ⚡"
elif 5 <= name_length <= 8:
    vibe = "Balanced & Cool 😎"
else:
    vibe = "Grand & Royal 👑"

print(f"✨ Name Decode Result ✨")
print(f"Name: {user_input.title()}")
print(f"Starts with: {first_char}")
print(f"Personality Trait: {trait}")
print(f"Vibe Check: {vibe}")

