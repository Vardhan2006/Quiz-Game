import random

print("--------------------------------------------------------------------------")
print("Welcome to Cricket Stars by Number: The Jersey Mastermind Challenge (CJC)")
print("--------------------------------------------------------------------------")

questions = [
    {"question": "What is the jersey no of Virat Kohli?", "answer": "18"},
    {"question": "What is the jersey no of Rohit Sharma?", "answer": "45"},
    {"question": "What is the jersey no of MS Dhoni?", "answer": "7"},
    {"question": "What is the jersey no of KL Rahul?", "answer": "1"},
    {"question": "What is the jersey no of AB de Villiers?", "answer": "17"}
]

def random_questions(questions, num_questions):
    random.shuffle(questions)
    return questions[:num_questions]

def kbc():
    score = 0
    num_questions = 3  

    selected_questions = random_questions(questions, num_questions)

    for question in selected_questions:
        print(question["question"])
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == question["answer"].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question['answer']}.")

    print(f"Your final score is {score} out of {num_questions}.")

kbc()
