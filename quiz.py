def run_quiz():
    questions = {
        "Python": "What language is widely used for AI and web development?",
        "JavaScript": "What language is essential for front-end web development?",
        "Docker": "What tool is commonly used for containerization?",
        "AI": "What field involves creating machines with human-like intelligence?",
        "HTTPS": "Which protocol is used for secure data transfer over the web?",
        "Binary" : "Which search algorithm is used in balanced binary trees with time complexity O(log n)?",
        "Bash" : "What is the default shell for most Linux distributions?",
        "Hashmap" :"What is the data structure where elements are stored in key-value pairs?",

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
