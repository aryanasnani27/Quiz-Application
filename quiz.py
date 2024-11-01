print("-"*40)
print("WELCOME TO QUIZ".center(40)
print("-"*40)

users={}

def registration():
    u_name=input("Enter a username: ")
    if u_name in users:
        print("Username already exists.Please try a different one!")
        return False
    pwd=input("Enter the password: ")
    users[u_name]=pwd
    print("Registration Successful")
    return True
def login():
    u_name=input("Enter your username: ")
    pwd=input("Enter your password: ")
    if u_name in users and users[u_name]==pwd:
        print(f"Welcome {u_name} Login Successful")
        return True
    print('Invalid username or password')
    return False
def ask_question(question,options,correct_answer):
    print(question)
    for option in options:
        print(option)
    user_answer=input("Your answer (a/b/c): ").lower()
    return user_answer==correct_answer
def quiz():
    questions=[
        {
            'question':"What is capital of France?",
            'options':['(a) Paris','(b) London','(c) Brazil'],
            'answer':'a'
        },
        {
            'question':"What is short form of Data structure and Algorithms?",
            'options':['(a) Dbms','(b) Dsa','(c) BI'],
            'answer':'b'
        },
        {
            'question':"What is colur of sky?",
            'options':['(a) Green','(b) Yellow','(c) Blue'],
            'answer':'c'
        },
        {
            'question':"What is the keyword used for defining a Function in Pyhon?",
            'options':['(a) for','(b) def','(c) if'],
            'answer':'b'
        },
        {
            'question':"Which keyword is used for iterating over a sequence in Python?",
            'options':['(a) for','(b) while','(c) if'],
            'answer':'a'
        }
    ]
    score=0
    for q in questions:
        if ask_question(q['question'],q['options'],q['answer']):
            print("Correct")
            score+=1
        else:
            print("wrong! The correct answer is",q['answer'])
    print(f"You scored {score} out of {len(questions)}")

def main():
    while True:
        action=input("Do you want to (r)register,l(login) or q(quit?)").lower()
        if action=='r':
            registration()
        elif action=='l':
            if login():
                quiz()
        elif action=='q':
            print("Goodbye!")
            break
        else:
            print("Invalid option,please try again")
if __name__=="__main__":
    main()
