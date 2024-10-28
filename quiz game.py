questions = ("What is the capital of India? ",
                       "How many continents are there in the world?: ",
                       "How many members are there in BTS?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the smallest?: ")

options = (("A. Haryana", "B. New Delhi", "C. Karnataka", "D. Goa"),
                   ("A. 4", "B. 5", "C. 7", "D. 6"),
                   ("A. 7", "B. 8", "C. 9", "D. 5"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mars", "B. Venus", "C. Earth", "D. Mercury"))

answers = ("B", "C", "A", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")