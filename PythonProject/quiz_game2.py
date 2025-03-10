import random
import time

# Question bank (could be loaded from a file like JSON/CSV in a larger project)
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"],
     "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Whale", "Giraffe", "Shark"],
     "answer": "Whale"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"],
     "answer": "Shakespeare"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"}
]


def display_question(question_data):
    """Display the question and options."""
    print("\nQuestion: " + question_data['question'])
    for idx, option in enumerate(question_data['options'], 1):
        print(f"{idx}. {option}")


def ask_question(question_data):
    """Ask the question and get the user's answer."""
    display_question(question_data)
    try:
        answer_index = int(input("Enter the number of your answer: "))
        if question_data['options'][answer_index - 1] == question_data['answer']:
            return True
        else:
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid option number.")
        return False


def start_quiz():
    """Start the quiz game."""
    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")
    name = input("Enter your name: ")

    # Shuffle the questions to randomize order
    random.shuffle(questions)

    for i, question_data in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total_questions}")

        # Timer for each question
        start_time = time.time()
        correct = ask_question(question_data)
        end_time = time.time()

        # Time taken for the answer
        time_taken = end_time - start_time
        print(f"You took {time_taken:.2f} seconds to answer.")

        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['answer']}")

        print(f"Your current score is: {score}/{i}")

    # Final result
    print("\nQuiz Over!")
    print(f"Your final score: {score}/{total_questions}")
    print(f"Thank you for playing, {name}!")


if __name__ == "__main__":
    start_quiz()
