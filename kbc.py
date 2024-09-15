def kbc(questions, answers):
    count = 0
    wrong = 3
    reward = 1

    i = 0
    while i < len(questions) and wrong > 0:
        print(questions[i])
        ans = input("Enter the Answer: ")
        
        if ans == answers[i]:
            print("**Answer is Correct**")
            count += 1
            reward *= 50
            i += 1  
        else:
            print("**Answer is Wrong**")
            wrong -= 1
            print(f"You have {wrong} attempts left.")

    print("Your Total Price is: ", reward)


questions = (
    "How many continents are there in the world?", 
    "Where is Pakistan located?", 
    "South of Pakistan?", 
    "What does LOC stand for?",
    "What is the capital of France?", 
    "What is 5 + 7?", 
    "Who wrote 'To Kill a Mockingbird'?", 
    "What is the chemical symbol for water?",
    "Which planet is known as the Red Planet?", 
    "What is the largest ocean on Earth?", 
    "Who is known as the Father of Computers?", 
    "In which year did the Titanic sink?"
)

answers = (
    "7", 
    "Asia", 
    "China", 
    "Line Of Control",
    "Paris", 
    "12", 
    "Harper Lee", 
    "H2O",
    "Mars", 
    "Pacific", 
    "Charles Babbage", 
    "1912"
)

kbc(questions, answers)
