def run_quiz():
    questions = {
        "Python": "What language is widely used for AI and web development?",
        "JavaScript": "What language is essential for front-end web development?",
        "Docker": "What tool is commonly used for containerization?",
        "AI": "What field involves creating machines with human-like intelligence?"
    }
    
    correct_count = 0
    for column, question in questions.items():
        while True:
            answer = input(f"{question} ").strip()
            if answer.lower() == column.lower():
                print("Correct!")
                correct_count += 1
                break
            else:
                print("Try again!")

    return correct_count == len(questions)
