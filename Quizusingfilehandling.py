print("-" * 40)
print("WELCOME TO QUIZ".center(40))
print("-" * 40)
import os

USER_FILE = "users.txt"
SCORE_FILE = "scores.txt"

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    return users

def load_scores():
    scores = {}
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as file:
            for line in file:
                username, score = line.strip().split(',')
                scores[username] = int(score)
    return scores

def save_user(u_name, pwd):
    with open(USER_FILE, 'a') as file:
        file.write(f"{u_name},{pwd}\n")

def save_score(u_name, score):
    with open(SCORE_FILE, 'a') as file:
        file.write(f"{u_name},{score}\n")

def registration(users):
    u_name = input("Enter a username: ")
    if u_name in users:
        print("Username already exists. Please try a different one!")
        return False
    pwd = input("Enter the password: ")
    users[u_name] = pwd
    save_user(u_name, pwd)
    print("Registration Successful")
    return True

def login(users):
    u_name = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if u_name in users and users[u_name] == pwd:
        print(f"Welcome {u_name}, Login Successful")
        return True
    print('Invalid username or password')
    return False

def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    user_answer = input("Your answer (a/b/c): ").lower()
    return user_answer == correct_answer

def quiz(users):
    questions = [
        {
            'question': "What is the capital of France?",
            'options': ['(a) Paris', '(b) London', '(c) Brazil'],
            'answer': 'a'
        },
        {
            'question': "What is the short form of Data Structure and Algorithms?",
            'options': ['(a) DBMS', '(b) DSA', '(c) BI'],
            'answer': 'b'
        },
        {
            'question': "What is the color of the sky?",
            'options': ['(a) Green', '(b) Yellow', '(c) Blue'],
            'answer': 'c'
        },
        {
            'question': "What is the keyword used for defining a Function in Python?",
            'options': ['(a) for', '(b) def', '(c) if'],
            'answer': 'b'
        },
        {
            'question': "Which keyword is used for iterating over a sequence in Python?",
            'options': ['(a) for', '(b) while', '(c) if'],
            'answer': 'a'
        }
    ]
    score = 0
    for q in questions:
        if ask_question(q['question'], q['options'], q['answer']):
            print("Correct")
            score += 1
        else:
            print("Wrong! The correct answer is", q['answer'])
    print(f"You scored {score} out of {len(questions)}")
    
    save_score(users, score)
    return score

def main():
    users = load_users()
    
    while True:
        action = input("Do you want to (r)register, (l)ogin, or (q)uit? ").lower()
        if action == 'r':
            registration(users)
        elif action == 'l':
            if login(users):
                score = quiz(users)
                print(f"Your score has been saved: {score}")
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
