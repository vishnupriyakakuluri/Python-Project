# Simple Quiz Game in Python

# List of questions and their corresponding options and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 8", "C. 10", "D. 12"],
        "answer": "B"
    }
]


# Function to run the quiz
def run_quiz():
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

        # Get user's answer
        user_answer = input("Please select the correct answer (A/B/C/D): ").upper()

        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")

    # Display the final score
    print(f"Your final score is {score}/{len(questions)}")


# Main function to start the quiz
if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    run_quiz()
