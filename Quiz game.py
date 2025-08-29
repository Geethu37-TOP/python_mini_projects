print("Welcome to the Quiz! 🎉")
score = 0

answer = input("Q1. What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

answer = input("Q2. 5 + 7 = ? ")
if answer == "12":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

print(f"Your final score is {score}/2")
