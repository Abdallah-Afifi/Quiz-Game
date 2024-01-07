def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    return int(input("Enter the number of your answer: "))

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def quiz():
    print("Welcome to the Quiz Game!")

    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Paris', 'Rome', 'Madrid'],
            'correct_answer': 2
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 1
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 2
        }
        # Add more questions as needed
    ]

    score = 0

    for question_data in questions:
        user_answer = display_question(question_data['question'], question_data['options'])
        if check_answer(user_answer, question_data['correct_answer']):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['correct_answer']}\n")

    print(f"You scored {score}/{len(questions)}.")

if __name__ == "__main__":
    quiz()
