# NAME       - RAJEEV KUMAR
# ENROLLMENT - 0157AL231167
# BATCH      - 5(MTF)
# BATCH TIME - 10:30 - 12:10


import random
import json

USER_FILE = "users.json"
LEADERBOARD_FILE = "leaderboard.json"

# -------------------- Load and Save Functions --------------------
def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

# -------------------- Signup and Login --------------------
def signup():
    users = load_data(USER_FILE)
    username = input("Enter new username: ")
    if username in users:
        print("❌ Username already exists! Try login instead.")
        return None
    password = input("Enter password: ")
    users[username] = password
    save_data(USER_FILE, users)
    print("✅ Signup successful! Please login now.")
    return None

def login():
    users = load_data(USER_FILE)
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(f"\n✅ Welcome {username}!\n")
        return username
    else:
        print("❌ Invalid username or password.")
        return None

# -------------------- Coding Questions (30) --------------------
questions = [
    {"question": "What will be the output of print(2 ** 3 ** 2)?", "options": ["64", "512", "256", "8"], "answer": "512"},
    {"question": "Which of the following is immutable in Python?", "options": ["List", "Dictionary", "Set", "Tuple"], "answer": "Tuple"},
    {"question": "Which keyword is used to create a function in Python?", "options": ["func", "def", "function", "lambda"], "answer": "def"},
    {"question": "What is the output of print('Hello'[::-1])?", "options": ["olleH", "Hello", "error", "None"], "answer": "olleH"},
    {"question": "Which method adds an item at the end of a list?", "options": ["add()", "append()", "insert()", "extend()"], "answer": "append()"},
    {"question": "What is the output of print(bool(0))?", "options": ["True", "False", "0", "None"], "answer": "False"},
    {"question": "In Python, which of the following is used for comments?", "options": ["//", "#", "/* */", "<!-- -->"], "answer": "#"},
    {"question": "What is the output of print(10//3)?", "options": ["3.33", "3", "4", "Error"], "answer": "3"},
    {"question": "What is the output of print(3 * 'ab')?", "options": ["ababab", "ab3", "error", "3ab"], "answer": "ababab"},
    {"question": "What is the output of print(len('Python'))?", "options": ["5", "6", "7", "error"], "answer": "6"},
    {"question": "Which of the following is not a Python keyword?", "options": ["pass", "eval", "assert", "nonlocal"], "answer": "eval"},
    {"question": "Which data structure does LIFO represent?", "options": ["Queue", "Stack", "List", "Tuple"], "answer": "Stack"},
    {"question": "What is the output of print(5 != 3)?", "options": ["True", "False", "Error", "None"], "answer": "True"},
    {"question": "Which operator is used for exponent in Python?", "options": ["^", "**", "exp", "//"], "answer": "**"},
    {"question": "Which of these will raise an error: print(5 + '5')?", "options": ["Yes", "No", "Depends", "None"], "answer": "Yes"},
    {"question": "Which method is used to convert string to lowercase?", "options": ["lower()", "down()", "toLower()", "str.lowercase()"], "answer": "lower()"},
    {"question": "Which function returns the type of an object?", "options": ["id()", "type()", "class()", "dir()"], "answer": "type()"},
    {"question": "Which function is used to read a line from a file?", "options": ["read()", "readline()", "readlines()", "input()"], "answer": "readline()"},
    {"question": "What is the output of print([i for i in range(3)])?", "options": ["[0,1,2]", "[1,2,3]", "[0,1,2,3]", "error"], "answer": "[0,1,2]"},
    {"question": "What is the output of print(bool('False'))?", "options": ["False", "True", "None", "Error"], "answer": "True"},
    {"question": "Which of the following is not used for looping?", "options": ["for", "while", "repeat", "None"], "answer": "repeat"},
    {"question": "What is the output of print(type([]))?", "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"], "answer": "<class 'list'>"},
    {"question": "Which keyword is used for exception handling?", "options": ["catch", "try", "throw", "except"], "answer": "try"},
    {"question": "Which function is used to take input from user?", "options": ["input()", "get()", "scan()", "read()"], "answer": "input()"},
    {"question": "Which module is used for random numbers in Python?", "options": ["math", "random", "numbers", "rand"], "answer": "random"},
    {"question": "What is the output of print('A' < 'a')?", "options": ["True", "False", "Error", "None"], "answer": "True"},
    {"question": "What is the output of print(3 == 3.0)?", "options": ["True", "False", "Error", "None"], "answer": "True"},
    {"question": "Which of the following defines a dictionary?", "options": ["{}", "[]", "()", "None"], "answer": "{}"},
    {"question": "Which keyword is used to create a class?", "options": ["class", "def", "create", "function"], "answer": "class"},
    {"question": "Which of these is used to import modules?", "options": ["package", "import", "include", "library"], "answer": "import"}
]

# -------------------- Leaderboard Functions --------------------
def update_leaderboard(username, score):
    leaderboard = load_data(LEADERBOARD_FILE)
    if username not in leaderboard or score > leaderboard[username]:
        leaderboard[username] = score
        save_data(LEADERBOARD_FILE, leaderboard)

def show_leaderboard():
    leaderboard = load_data(LEADERBOARD_FILE)
    if not leaderboard:
        print("\nNo records found yet.\n")
        return

    sorted_lb = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    print("\n🏆 Leaderboard - Top Performers 🏆")
    print("-----------------------------------")
    for i, (user, score) in enumerate(sorted_lb[:10], start=1):
        print(f"{i}. {user} - {score}/30")
    print("-----------------------------------\n")

# -------------------- Quiz Function --------------------
def start_quiz(username):
    print("\n🎯 Starting your coding quiz...\n")
    random.shuffle(questions)
    score = 0

    for i, q in enumerate(questions[:30], start=1):
        print(f"{i}. {q['question']}")
        for j, opt in enumerate(q["options"], start=1):
            print(f"   {j}. {opt}")
        try:
            ans = int(input("Enter your answer (1-4): "))
            if q["options"][ans - 1] == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")
        except:
            print("Invalid input! Skipping question.\n")

    percent = (score / 30) * 100
    print(f"Quiz Finished! {username}, Your Score: {score}/30 ({percent:.2f}%)")
    update_leaderboard(username, score)

    if percent >= 80:
        print("🎉 Excellent Work!")
    elif percent >= 50:
        print("👍 Good Effort, keep practicing!")
    else:
        print("😅 Needs improvement, study more coding concepts!")

# -------------------- Main Program --------------------
def main():
    print("=== 🔥 Coding Quiz Application ===")
    while True:
        print("\n1. Login")
        print("2. Signup")
        print("3. View Leaderboard")
        print("4. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            user = login()
            if user:
                start_quiz(user)
        elif ch == "2":
            signup()
        elif ch == "3":
            show_leaderboard()
        elif ch == "4":
            print("👋 Thank you for using Coding Quiz App!")
            break
        else:
            print("Invalid choice, try again!")

# -------------------- Correct main entry point --------------------
if __name__ == "__main__":
    main()
