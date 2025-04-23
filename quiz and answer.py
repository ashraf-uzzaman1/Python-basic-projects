questions = [
    "What is the capital of Bangladesh?",
    "What is 5 + 7?",
    "Which planet is known as the Red Planet?",
    "Who wrote 'Hamlet'?"
]

choices = [
    ["A) Khulna", "B) Sylhet", "C) Dhaka", "D) Chittagong"],
    ["A) 10", "B) 11", "C) 12", "D) 13"],
    ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
    ["A) Charles Dickens", "B) Leo Tolstoy", "C) William Shakespeare", "D) Mark Twain"]
]

answers = ["C", "C", "B", "C"]

# Function to run the quiz
def run_quiz():
    score = 0
    for i in range(len(questions)):
        print(f"\n{questions[i]}")
        for choice in choices[i]:
            print(choice)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        if answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answers[i]}.")
    
    print(f"\nYour final score is: {score}/{len(questions)}")

# Start the quiz
run_quiz()
